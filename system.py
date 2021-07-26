"""
Author: Patrick R. Gorton
Date:   July 2021
"""


from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
from text_processing import FileRegistry


class TextFileVisualiser:
    def __init__(self, max_pca_components=50, visualisation_method='tsne',
        tsne_perplexity=2.0):

        self.visualisation_method = visualisation_method
        self.max_pca_components = max_pca_components
        self.file_registry = FileRegistry()
        self.tsne_preplexity = tsne_perplexity

    def __call__(self, file_dir):
        data = self.analyse_text_files(file_dir)
        fig = self.visualise_data(data)
        return fig

    def analyse_text_files(self, file_dir):
        self.file_registry.register_files(file_dir)
        data = self.file_registry.create_data_matrix()
        return data

    def visualise_data(self, data):
        if self.visualisation_method == 'pca':
            data = PCA(n_components=2).fit_transform(data)

            fig = plt.figure()
            plt.scatter(data[:, 0], data[:, 1], marker='*')
            for i, f in enumerate(self.file_registry.registry):
                plt.text(data[i, 0], data[i, 1], str(f.file_name[:-4]), color="red", fontsize=12)
            plt.show()

        elif self.visualisation_method == 'tsne':
            data = PCA(n_components=min(data.shape[0], self.max_pca_components)).fit_transform(data)
            data = TSNE(n_components=2, perplexity=self.tsne_preplexity).fit_transform(data)
            fig = plt.figure()
            plt.title('TSNE')
            plt.scatter(data[:, 0], data[:, 1], marker='*')
            for i, f in enumerate(self.file_registry.registry):
                plt.text(data[i, 0], data[i, 1], str(f.file_name[:-4]), color="red", fontsize=12)
            plt.show()
        return fig
