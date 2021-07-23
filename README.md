# text-relations

**Dependencies**
- Python >= 3.6
- matplotlib
- NumPy
- scikit-learn

**What and how**

This little program visualises the relationship between the provided text files through some basic analyses. The content of the text files gets analysed by first counting the occurrences of the words it contains and then converting these to vectors of probabilities. The vectors' feature dimension gets reduced using principal component analysis (PCA), and finally the data is visualised in a 2D scatter plot using either PCA or t-distributed stochastic neighbour embedding (t-SNE). If you choose to use t-SNE for visualisation, you should experiment a little with the perplexity parameter since it will depend on the text files and the desired visual outcome. Perhaps in the range [2.0, 10.0].

The example text files contain the two first paragraphs from Wikipedia articles about different countries.

Run _main.py_ to give it a go

![tsne](https://user-images.githubusercontent.com/42536147/126667075-6041a95d-ae82-47ff-85cf-be9e41b49b76.png)

**TODO**

[] Test the program with other texts. Preferably a mix of categories?
[] Add the possibility to ignore certain words. E.g. prepositions
[] Introduce a deep learning language model for feature extraction. BERT?
[] Find an appropriate clustering method. Not sure DBSCAN is the way to go due to highly sensitive parameter settings. 
[] If clustering: It would be nice to see e.g. the "top 3" words within each cluster.
