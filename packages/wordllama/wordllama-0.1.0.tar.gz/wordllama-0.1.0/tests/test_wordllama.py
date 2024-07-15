import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from wordllama.wordllama import WordLlama
from wordllama.config import (
    WordLlamaConfig,
    WordLlamaModel,
    TokenizerConfig,
    TrainingConfig,
    MatryoshkaConfig,
    TokenizerInferenceConfig,
)


class TestWordLlama(unittest.TestCase):
    @patch("wordllama.wordllama.safe_open")
    @patch("wordllama.wordllama.Tokenizer.from_pretrained")
    def setUp(self, mock_tokenizer, mock_safe_open):
        # Mock the tokenizer
        self.mock_tokenizer = MagicMock()
        self.mock_tokenizer.encode_batch.return_value = [
            MagicMock(ids=[1, 2, 3], attention_mask=[1, 1, 1])
        ]
        mock_tokenizer.return_value = self.mock_tokenizer

        # Mock the safetensors
        self.mock_safe_open = mock_safe_open
        self.mock_safe_open().__enter__().get_tensor.return_value = np.random.rand(
            128256, 64
        )

        # Example config using Pydantic models
        self.config = WordLlamaConfig(
            model=WordLlamaModel(
                n_vocab=128256,
                dim=64,
                hf_model_id="meta-llama/Meta-Llama-3-8B",
                pad_token="",
            ),
            tokenizer=TokenizerConfig(
                return_tensors="pt",
                return_attention_mask=True,
                max_length=128,
                padding="max_length",
                truncation=True,
                add_special_tokens=True,
                inference=TokenizerInferenceConfig(
                    use_local_config=False,
                    config_filename="l2_supercat_tokenizer_config.json",
                ),
            ),
            training=TrainingConfig(
                output_dir="output/matryoshka_sts_custom",
                num_train_epochs=2,
                per_device_train_batch_size=512,
                warmup_steps=256,
                evaluation_strategy="steps",
                eval_steps=250,
                save_steps=1000,
                fp16=True,
                include_num_input_tokens_seen=False,
                learning_rate=0.01,
                multi_dataset_batch_sampler="PROPORTIONAL",
                binarizer_ste="tanh",
            ),
            matryoshka=MatryoshkaConfig(dims=[1024, 512, 256, 128, 64]),
        )

        self.model = WordLlama.build("path/to/wordllama_64.safetensors", self.config)

    def test_tokenize(self):
        self.mock_tokenizer.encode_batch.return_value = [
            MagicMock(ids=[1, 2, 3], attention_mask=[1, 1, 1])
        ]
        tokens = self.model.tokenize("test string")
        self.mock_tokenizer.encode_batch.assert_called_with(
            ["test string"], is_pretokenized=False, add_special_tokens=False
        )
        self.assertEqual(len(tokens), 1)

    def test_embed(self):
        self.mock_tokenizer.encode_batch.return_value = [
            MagicMock(ids=[1, 2, 3], attention_mask=[1, 1, 1])
        ]
        embeddings = self.model.embed("test string", return_np=True)
        self.assertEqual(embeddings.shape, (1, 64))

    def test_similarity_cosine(self):
        self.mock_tokenizer.encode_batch.return_value = [
            MagicMock(ids=[1, 2, 3], attention_mask=[1, 1, 1]),
            MagicMock(ids=[4, 5, 6], attention_mask=[1, 1, 1]),
        ]
        sim_score = self.model.similarity(
            "test string 1", "test string 2", use_hamming=False
        )
        self.assertTrue(isinstance(sim_score, float))

    def test_similarity_hamming(self):
        self.mock_tokenizer.encode_batch.return_value = [
            MagicMock(ids=[1, 2, 3], attention_mask=[1, 1, 1]),
            MagicMock(ids=[4, 5, 6], attention_mask=[1, 1, 1]),
        ]
        sim_score = self.model.similarity(
            "test string 1", "test string 2", use_hamming=True
        )
        self.assertTrue(isinstance(sim_score, float))

    def test_rank_cosine(self):
        self.mock_tokenizer.encode_batch.return_value = [
            MagicMock(ids=[1, 2, 3], attention_mask=[1, 1, 1]),
            MagicMock(ids=[4, 5, 6], attention_mask=[1, 1, 1]),
            MagicMock(ids=[7, 8, 9], attention_mask=[1, 1, 1]),
        ]
        docs = ["doc1", "doc2", "doc3"]
        ranked_docs = self.model.rank("test query", docs, use_hamming=False)
        self.assertEqual(len(ranked_docs), len(docs))
        self.assertTrue(all(isinstance(score, float) for doc, score in ranked_docs))

    def test_rank_hamming(self):
        self.mock_tokenizer.encode_batch.return_value = [
            MagicMock(ids=[1, 2, 3], attention_mask=[1, 1, 1]),
            MagicMock(ids=[4, 5, 6], attention_mask=[1, 1, 1]),
            MagicMock(ids=[7, 8, 9], attention_mask=[1, 1, 1]),
        ]
        docs = ["doc1", "doc2", "doc3"]
        ranked_docs = self.model.rank("test query", docs, use_hamming=True)
        self.assertEqual(len(ranked_docs), len(docs))
        self.assertTrue(all(isinstance(score, float) for doc, score in ranked_docs))

    @patch("wordllama.wordllama.Tokenizer.from_pretrained")
    def test_build_with_truncation(self, mock_tokenizer):
        truncated_model = WordLlama.build(
            "wordllama/weights/l2_supercat_256.safetensors", self.config, trunc_dim=32
        )
        self.assertEqual(truncated_model.embedding.shape[1], 32)

    def test_error_on_wrong_embedding_type(self):
        with self.assertRaises(AssertionError):
            self.model.embed(np.array([1, 2]))

    def test_binarization_and_packing(self):
        binary_output = self.model.embed("test string", binarize=True, pack=True)
        self.assertIsInstance(binary_output, np.ndarray)
        self.assertEqual(binary_output.dtype, np.uint32)

    def test_normalization_effect(self):
        normalized_output = self.model.embed("test string", norm=True)
        norm = np.linalg.norm(normalized_output)
        self.assertAlmostEqual(norm, 1, places=5)

    def test_cosine_similarity_direct(self):
        vec1 = np.random.rand(64)
        vec2 = np.random.rand(64)
        result = WordLlama.cosine_similarity(vec1, vec2)
        self.assertIsInstance(result.item(), float)

    def test_hamming_similarity_direct(self):
        vec1 = np.random.randint(2, size=64, dtype=np.uint32)
        vec2 = np.random.randint(2, size=64, dtype=np.uint32)
        result = WordLlama.hamming_similarity(vec1, vec2)
        self.assertIsInstance(result.item(), float)


if __name__ == "__main__":
    unittest.main()
