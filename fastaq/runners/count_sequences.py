import argparse
from fastaq import tasks

def run(description):
    parser = argparse.ArgumentParser(
        description = 'Counts the number of sequences in a fasta/q file',
        usage = 'fastaq count_sequences <fasta/q in>')
    parser.add_argument('infile', help='Name of input fasta/q file')
    options = parser.parse_args()
    print(tasks.count_sequences(options.infile))
