import os

def read_fasta(file_path):
    """
    Reads a FASTA file and returns the DNA sequence as a single string.
    Removes header lines and joins multi-line sequences.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

    sequence = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                continue  # Skip FASTA header
            sequence += line.upper()

    if not sequence:
        raise ValueError("No sequence data found in file.")

    return sequence


def validate_dna_sequence(sequence):
    """
    Validates that the sequence contains only valid DNA nucleotides.
    Allowed characters: A, T, G, C
    """
    valid_nucleotides = {"A", "T", "G", "C"}

    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            raise ValueError(
                f"Invalid character '{nucleotide}' found in sequence."
            )

    return True


# Example usage
if __name__ == "__main__":
    file_path = "data/sample_sequence.fasta"

    try:
        dna_sequence = read_fasta(file_path)
        validate_dna_sequence(dna_sequence)
        print("Sequence successfully loaded and validated.")
        print(f"Sequence Length: {len(dna_sequence)}")
    except Exception as e:
        print(f"Error: {e}")