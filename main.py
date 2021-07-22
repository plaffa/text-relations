
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from system import TextInvestigator
from text_processing import FileRegistry

viz = 'tsne'

if __name__ == "__main__":
    fr = FileRegistry()
    fr.register_files('text_files')
    X = fr.create_matrix()

    if viz == 'pca':
        pca = PCA(n_components=2)
        X_new = pca.fit_transform(X)

        fig = plt.figure()
        plt.scatter(X_new[:, 0], X_new[:, 1], marker='*')
        for i, f in enumerate(fr.registry):
            plt.text(X_new[i, 0], X_new[i, 1], str(f.file_name[:-4]), color="red", fontsize=12)
        plt.show()

    elif viz == 'tsne':
        pca = PCA(n_components=min(X.shape))
        X_new = pca.fit_transform(X)
        X_tsne = TSNE(n_components=2, perplexity=5.0).fit_transform(X_new)
        fig = plt.figure()
        plt.title('TSNE')
        plt.scatter(X_tsne[:, 0], X_tsne[:, 1], marker='*')
        for i, f in enumerate(fr.registry):
            plt.text(X_tsne[i, 0], X_tsne[i, 1], str(f.file_name[:-4]), color="red", fontsize=12)
        plt.show()


