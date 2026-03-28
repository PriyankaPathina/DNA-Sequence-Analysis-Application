import matplotlib.pyplot as plt


def plot_nucleotide_distribution(frequencies, save_path=None):
    '''
    Creates a bar chart of nucleotide frequencies.
    Optionally saves the figure if save_path is provided.
    '''

    nucleotides = list(frequencies.keys())
    counts = list(frequencies.values())

    plt.figure()
    plt.bar(nucleotides, counts)
    plt.xlabel("Nucleotide")
    plt.ylabel("Frequency")
    plt.title("Nucleotide Distribution")

    if save_path:
        plt.savefig(save_path)

    plt.show()