
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from system import TextInvestigator
from text_processing import FileRegistry

if __name__ == "__main__":
    fr = FileRegistry()
    fr.register_files('text_files')
    X = fr.create_matrix()

    pca = PCA(n_components=2)
    X_new = pca.fit_transform(X)

    fig = plt.figure()
    #ax = fig.add_subplot(projection='2d')
    #plt.scatter(X_new[:,0], X_new[:,1], X_new[:,2], marker='*')
    plt.scatter(X_new[:,0], X_new[:,1], marker='*')
    for i, f in enumerate(fr.registry):
        print(f.file_name[:-4])
        plt.text(X_new[i,0], X_new[i,1], str(f.file_name[:-4]), color="red", fontsize=12)
    plt.show()
