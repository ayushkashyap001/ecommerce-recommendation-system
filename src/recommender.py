from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:

    def __init__(self, df):
        self.df = df.copy()

    def build_model(self):

        self.df['TITLE'] = self.df['TITLE'].fillna('')
        self.df['BULLET_POINTS'] = self.df['BULLET_POINTS'].fillna('')
        self.df['DESCRIPTION'] = self.df['DESCRIPTION'].fillna('')

        self.df['combined'] = (
            self.df['TITLE'].astype(str) + " " +
            self.df['BULLET_POINTS'].astype(str) + " " +
            self.df['DESCRIPTION'].astype(str)
        )

        tfidf = TfidfVectorizer(stop_words='english')
        matrix = tfidf.fit_transform(self.df['combined'])

        self.similarity = cosine_similarity(matrix)

    def recommend(self, product_title, top_n=5):

        idx_list = self.df[self.df['TITLE'].str.contains(product_title, na=False)].index

        if len(idx_list) == 0:
            return self.df[['TITLE']].head(top_n)

        idx = idx_list[0]

        scores = list(enumerate(self.similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        top_products = scores[1:top_n+1]
        indices = [i[0] for i in top_products]

        return self.df.iloc[indices][['TITLE']]