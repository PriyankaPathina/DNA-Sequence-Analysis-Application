import sys
import os
import matplotlib.pyplot as plt


# -----------------------------
# FILE READING AND VALIDATION
# -----------------------------

def read_fasta(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Input file does not exist.")

    sequence = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                continue
            sequence += line

    if not sequence:
        raise ValueError("FASTA file contains no sequence data.")

    return sequence.upper()


def validate_sequence(sequence):
    if not sequence:
        raise ValueError("Sequence is empty.")

    valid_nucleotides = set("ATGC")

    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotide found: {nucleotide}")

    return True


# -----------------------------
# SEQUENCE ANALYSIS FUNCTIONS
# -----------------------------

def calculate_gc_content(sequence):
    if not sequence:
        raise ValueError("Sequence is empty.")

    gc_count = 0
    total_length = len(sequence)

    for nucleotide in sequence:
        if nucleotide == "G" or nucleotide == "C":
            gc_count += 1

    gc_percentage = (gc_count / total_length) * 100
    return round(gc_percentage, 2)


def calculate_nucleotide_frequencies(sequence):
    frequencies = {
        "A": 0,
        "T": 0,
        "G": 0,
        "C": 0
    }

    for nucleotide in sequence:
        frequencies[nucleotide] += 1

    return frequencies


def search_motif(sequence, motif):
    if not sequence:
        raise ValueError("Sequence is empty.")

    if not motif:
        raise ValueError("Motif is empty.")

    sequence = sequence.upper()
    motif = motif.upper()

    positions = []

    motif_length = len(motif)
    sequence_length = len(sequence)

    for index in range(sequence_length - motif_length + 1):
        substring = sequence[index:index + motif_length]

        if substring == motif:
            positions.append(index + 1)  # 1-based indexing

    return positions


# -----------------------------
# VISUALISATION
# -----------------------------

def plot_nucleotide_distribution(frequencies):
    nucleotides = list(frequencies.keys())
    counts = list(frequencies.values())

    plt.figure()
    plt.bar(nucleotides, counts)
    plt.xlabel("Nucleotide")
    plt.ylabel("Frequency")
    plt.title("Nucleotide Distribution")
    plt.show()


# -----------------------------
# MAIN FUNCTION
# -----------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <fasta_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        sequence = read_fasta(file_path)
        validate_sequence(sequence)

        sequence_length = len(sequence)
        gc_content = calculate_gc_content(sequence)
        frequencies = calculate_nucleotide_frequencies(sequence)

        motif = "TATA"
        motif_positions = search_motif(sequence, motif)

        print("\n--- DNA Sequence Analysis Results ---\n")
        print(f"Sequence Length: {sequence_length}")
        print(f"GC Content: {gc_content}%\n")

        print("Nucleotide Frequencies:")
        for nucleotide, count in frequencies.items():
            print(f"{nucleotide}: {count}")

        print(f"\nMotif '{motif}' Positions:")
        print(motif_positions)

        plot_nucleotide_distribution(frequencies)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()