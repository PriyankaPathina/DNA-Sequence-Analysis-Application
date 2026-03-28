import unittest
from sequence_analysis import calculate_gc_content, search_motif


class TestSequenceAnalysis(unittest.TestCase):

    def test_gc_content_normal_sequence(self):
        """
        Test GC content calculation with a known sequence.
        """
        sequence = "GGCCAAAT"
        # GC = 4 out of 8 bases → 50%
        expected_gc = 50.0
        result = calculate_gc_content(sequence)
        self.assertAlmostEqual(result, expected_gc, places=2)

    def test_gc_content_empty_sequence(self):
        """
        Test GC content with empty sequence (should raise error).
        """
        with self.assertRaises(ValueError):
            calculate_gc_content("")

    def test_motif_found(self):
        """
        Test motif search when motif exists in sequence.
        """
        sequence = "ATGCGTATATAAGCTTATAA"
        motif = "TATA"
        result = search_motif(sequence, motif)
        self.assertEqual(result, [6, 8, 16])

    def test_motif_not_found(self):
        """
        Test motif search when motif does not exist.
        """
        sequence = "ATGCGTATATAAGCTTATAA"
        motif = "CCCC"
        result = search_motif(sequence, motif)
        self.assertEqual(result, [])

    def test_motif_empty_input(self):
        """
        Test motif search with empty motif (should raise error).
        """
        with self.assertRaises(ValueError):
            search_motif("ATGC", "")


if __name__ == "__main__":
    unittest.main()