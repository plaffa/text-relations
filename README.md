# text-relations

Dependencies:
- Python >= 3.6
- NumPy
- Scikit-Learn

**What and how**

This little program visualises the relationship between the provided text files through some basic analyses. The content of the
text files get analysed by counting the occurences of the words it contains, and then get converted to vectors of probabilites.
The feature dimension of these vectors is reduced using principal component analysis (PCA), and the data is visualised using
either PCA alone or using t-distributed stochastic neighbor embedding (t-SNE). If using t-SNE for visualisation, you should
experiment a little with the perplexity variable, since it will depend on the text files and the desired visual outcome.
