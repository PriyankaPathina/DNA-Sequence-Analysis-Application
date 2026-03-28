def run_analysis(file_path):
    """
    Executes full DNA sequence analysis workflow
    with structured error handling.
    """

    try:
        # Attempt to read FASTA file
        sequence = read_fasta(file_path)

        # Validate DNA sequence
        validate_dna_sequence(sequence)

        # Perform analysis
        length = len(sequence)
        gc = calculate_gc_content(sequence)
        motif_positions = search_motif(sequence, "TATA")

        print("\n--- DNA Sequence Analysis Results ---")
        print(f"Sequence Length: {length}")
        print(f"GC Content: {gc:.2f}%")
        print(f"Motif Positions: {motif_positions}")

    except FileNotFoundError as fnf_error:
        print(f"File Error: {fnf_error}")

    except ValueError as val_error:
        print(f"Validation Error: {val_error}")

    except Exception as unexpected_error:
        print("An unexpected error occurred.")
        print(f"Details: {unexpected_error}")

    finally:
        print("\nProgram execution completed.")