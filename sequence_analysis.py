def calculate_gc_content(sequence):
    """
    Searches for all occurrences of a given motif in the DNA sequence.
    Returns a list of starting positions (1-based indexing).
    """
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
    frequencies = {"A": 0, "T": 0, "G": 0, "C": 0}

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

    for i in range(len(sequence) - motif_length + 1):
        if sequence[i:i + motif_length] == motif:
            positions.append(i + 1)

    return positions
