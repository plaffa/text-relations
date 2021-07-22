# text-relations

**Dependencies**
- Python >= 3.6
- matplotlib
- NumPy
- Scikit-Learn

**What and how**

This little program visualises the relationship between the provided text files through some basic analyses. The content of the
text files get analysed by counting the occurences of the words it contains, and then get converted to vectors of probabilites.
The feature dimension of these vectors is reduced using principal component analysis (PCA), and the data is visualised using
either PCA alone or using t-distributed stochastic neighbor embedding (t-SNE). If using t-SNE for visualisation, you should
experiment a little with the perplexity variable, since it will depend on the text files and the desired visual outcome.
Perhaps in the range [2.0, 10.0].

The example text files contain the two first paragraphs from Wikipedia articles about different countries.

![tsne](https://user-images.githubusercontent.com/42536147/126667075-6041a95d-ae82-47ff-85cf-be9e41b49b76.png)
