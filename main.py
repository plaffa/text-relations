import sklearn.cluster._dbscan as dbscan
import sklearn.decomposition._pca as pca
import sklearn.manifold._t_sne as tsne
import re
import os


class FileRegistry:
    def __init__(self):
        self.registry = []
        self.num_files = 0
        self.num_unique_words = 0

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
        self.registry.append(TextFile(file_name, words))

    def return_vectors(self, normalise=True):
        """
        Converts each element in the file registry to a vector format and returns them
        :return:
        """
        if normalise:
            pass
        pass


class TextFile:
    def __init__(self, file_name, word_stat):
        self.file_name = file_name
        self.word_stat = word_stat
        self.num_words = len(word_stat)



if __name__ == "__main__":
    pass
