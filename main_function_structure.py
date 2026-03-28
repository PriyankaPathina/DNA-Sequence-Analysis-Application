import sys
from file_reading_and_validation import read_fasta, validate_dna_sequence
from sequence_analysis import calculate_gc_content, calculate_nucleotide_frequencies
from sequence_analysis import search_motif
from visualisation import plot_nucleotide_distribution


def main():
    """
    Main entry point of the DNA Sequence Analysis Application.
    Handles user input, coordinates analysis, and displays results.
    """

    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_fasta_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        # Step 1: Read sequence
        dna_sequence = read_fasta(file_path)

        # Step 2: Validate sequence
        validate_dna_sequence(dna_sequence)

        # Step 3: Basic statistics
        sequence_length = len(dna_sequence)
        gc_content = calculate_gc_content(dna_sequence)
        frequencies = calculate_nucleotide_frequencies(dna_sequence)

        # Step 4: Motif search
        motif = "TATA"
        motif_positions = search_motif(dna_sequence, motif)

        # Step 5: Display results
        print("\n--- DNA Sequence Analysis Results ---")
        print(f"Sequence Length: {sequence_length}")
        print(f"GC Content: {gc_content:.2f}%")
        print(f"Motif '{motif}' Positions: {motif_positions}")

        # Step 6: Visualisation
        plot_nucleotide_distribution(frequencies)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()