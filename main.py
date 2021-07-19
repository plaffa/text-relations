#import sklearn.cluster._dbscan as dbscan
#import sklearn.decomposition._pca as pca
#import sklearn.manifold._t_sne as tsne
import re
import os
import numpy as np


class FileRegistry:
    def __init__(self):
        self.registry = []
        self.num_files = 0
        self.unique_words = []

    def register_files(self, directory):
        for file_name in os.listdir(directory):
            self.register_file(file_name, directory)

    def register_file(self, file_name, directory=''):
        words = {}
        with open(os.path.join(directory, file_name), 'r') as f:
            for line in f:
                for word in line.split():
                    # Some simple pre-processing
                    word = word.lower()
                    word_split = re.split(r"[,.]", word)
                    word = word_split[0] if len(word_split) > 1 else word

                    try:
                        words[word] += 1
                    except KeyError:
                        words[word] = 1

                    if word not in self.unique_words:
                        self.unique_words.append(word)

        self.registry.append(TextFile(self.num_files, file_name, words))
        self.num_files += 1

    def return_vectors(self, normalise=True):
        """
        Converts each element in the file registry to a vector format and returns them
        """

        mat = np.zeros((self.num_files, len(self.unique_words))
        for i, tf in enumerate(self.registry):
            for word in list(tf.word_stat):
                val = tf.word_stat[word] / tf.num_words if normalise else tf.word_stat
                mat[i, self.unique_words.index[word]] = val

        if normalise:
            pass
        pass


class TextFile:
    def __init__(self, file_name, word_stat):
        self.id = None
        self.file_name = file_name
        self.word_stat = word_stat
        self.num_words = len(word_stat)

    def __repr__(self):
        return repr('TextFile object. Name: %s. Word Count: %s' % (self.file_name, self.num_words))


if __name__ == "__main__":
    fr = FileRegistry()
    fr.register_files('text_files')
    print(len(fr.unique_words))
