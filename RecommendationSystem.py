import pandas as pd # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.metrics.pairwise import linear_kernel # type: ignore

Films = pd.read_csv(r"C:/Users/hp/Downloads/movies.csv")

Films = Films.fillna('')
Films['features'] = Films['Genre'] + ' ' + Films['Lead Studio'] + ' ' + \
                   Films['Audience score %'].astype(str) + ' ' + Films['Profitability'].astype(str) + ' ' + \
                   Films['Rotten Tomatoes %'].astype(str) + ' ' + Films['Worldwide Gross'].astype(str) + ' ' + \
                   Films['Year'].astype(str)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(Films['features'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = Films[Films['Film'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]
    movie_indices = [i[0] for i in sim_scores]
    return Films['Film'].iloc[movie_indices]

user_preference = 'Comedy'
recommended_movies = Films[Films['Genre'].str.contains(user_preference, case=False)]['Film'].tolist()
print(f"Recommended movies in {user_preference} genre:")
for movie in recommended_movies:
    print(f"- {movie}")

movie_title = 'Shayar'
print(f"\nMovies similar to '{movie_title}':")
similar_movies = get_recommendations(movie_title)
for movie in similar_movies:
    print(f"- {movie}")