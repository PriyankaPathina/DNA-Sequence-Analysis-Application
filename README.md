Python Version Used: Python 3.14

# DNA Sequence Analysis Application

## Project Overview

This Python-based DNA Sequence Analysis Application was developed as
part of the coursework. The application performs essential
bioinformatics tasks including reading FASTA files, validating DNA
sequences, calculating GC content, identifying motifs, and generating
graphical visualisations.

The project demonstrates modular programming, structured code
organisation, error handling, and appropriate documentation in
accordance with coursework requirements.

____________________________________________________________________________

## Implementation Details

The application follows a modular structure:
- File handling and validation are implemented in `file_reading_and_validation.py`
- Sequence analysis functions are implemented in `sequence_analysis.py`
- Visualisation is handled using the matplotlib library in `visualisation.py`
- The application entry point is `main.py`
- Unit tests are implemented using Python’s built-in `unittest` framework

This modular design ensures maintainability, readability, and testability.

------------------------------------------------------------------------

## Intended Purpose

The purpose of this application is to provide a lightweight and
self-contained tool for analysing DNA sequences. The application allows
users to:

-   Read DNA sequences from FASTA files\
-   Validate nucleotide characters\
-   Calculate sequence length\
-   Compute GC content percentage\
-   Determine nucleotide frequency distribution\
-   Search for specific motifs (e.g., TATA box)\
-   Generate graphical visualisations of nucleotide composition

This tool is suitable for educational purposes and small-scale
biological analysis.

------------------------------------------------------------------------

## System Requirements
-   current used Python version 3.14
-   Python 3.8 or higher\
-   Windows, macOS, or Linux operating system

------------------------------------------------------------------------

## Installation

1.  Download or clone the project repository.

2.  Navigate to the project directory:

    cd dna_sequence_analysis_project

3.  Install required dependencies:

    pip install -r requirements.txt

If the requirements file is not provided, manually install:

pip install matplotlib

------------------------------------------------------------------------

## Project Structure

DNA-Sequence-Analysis/
│
├── main.py
├── file_reading_and_validation.py
├── sequence_analysis.py
├── visualisation.py
├── test_analysis.py
├── unit_test_code.py
├── data/
│   └── sample_sequence.fasta
└── README.md

------------------------------------------------------------------------

## How to Run the Application

Open a terminal in the project directory and run:

python main.py data/sample_sequence.fasta

Ensure you are inside the main project folder before running the command.

The application will:
1. Read the FASTA file
2. Validate the DNA sequence
3. Calculate sequence length and GC content
4. Search for the motif "TATA"
5. Display results in the terminal
6. Generate a nucleotide frequency bar chart

------------------------------------------------------------------------

## Example Use Case

Input FASTA file:

>Example_Sequence
ATGCGTATATAAGCTTATAA

Output:
- Sequence Length: 20
- GC Content: 40.00%
- Motif "TATA" found at positions: [6, 8, 16]

A bar chart is displayed showing nucleotide distribution.

------------------------------------------------------------------------

## Unit Testing

Unit tests are included in the tests directory. To run tests:

python -m unittest discover tests

The tests verify GC content calculation, motif detection accuracy, and
error handling for invalid inputs.

------------------------------------------------------------------------

## Version Control

The project is maintained using Git and hosted privately on GitHub.
Commits document incremental development stages, feature additions, and
bug fixes. SSH authentication is configured to ensure secure repository
access.

------------------------------------------------------------------------

## Ethical Considerations

Although this application does not process personal data, responsible
data handling and accurate reporting of computational results are
essential. Future extensions involving clinical or genomic datasets
would require adherence to data protection regulations and ethical
approval procedures.

------------------------------------------------------------------------

## Future Improvements

Future enhancements may include the development of a graphical user
interface, support for batch processing of multiple sequences,
implementation of open reading frame detection, translation of DNA to
protein sequences, and integration with biological databases.

------------------------------------------------------------------------

## Author

Priyanka Pathina
Module : Coursework
Github: PriyankaPathina
Github SSH link: git@github.com:PriyankaPathina/DNA-Sequence-Analysis-Application.git
Github HTTPS link: https://github.com/PriyankaPathina/DNA-Sequence-Analysis-Application.git
Newcastle University
