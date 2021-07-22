

import argparse
from system import TextFileVisualiser

parser = argparse.ArgumentParser()
parser.add_argument('--visualisation_method', type=str, default='tsne')
parser.add_argument('--file_directory', type=str, default='text_files')
parser.add_argument('--max_pca_components', type=int, default=100)
parser.add_argument('--tsne_perplexity', type=float, default=7.0)
args = parser.parse_args()

if __name__ == "__main__":
    tfv = TextFileVisualiser(args.max_pca_components,
        args.visualisation_method, args.tsne_perplexity)
    tfv(args.file_directory)
