from flask import Flask, request, jsonify
import logging
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# load movie data
df = pd.read_csv('data/movies.csv')
#df = pd.read_csv('movies.csv')
df = df[df['Plot'].notna()]

# calculate cosine similarity matrix
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['Plot'])

cosine_sim = cosine_similarity(tfidf_matrix)

# create a Series of movie titles with their corresponding index
indices = pd.Series(df.index, index=df['Title']).drop_duplicates()

app = Flask(__name__)

# define recommendation functions
def get_recommendations(title, cosine_sim=cosine_sim, num_recommend=10):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_similar = sim_scores[1:num_recommend+1]
    movie_indices = [i[0] for i in top_similar]
    final_recommendation = df.iloc[movie_indices][['Title', 'Director', 'Genre', 'Plot', 'imdbRating', 'Poster']].to_dict('records')
    return final_recommendation

def get_combined_recommendations(movie_list, num_recommend=10):
    combined_sim_scores = np.zeros(cosine_sim.shape[0])

    for movie_title in movie_list:
        idx = df[df['Title'] == movie_title].index[0]
        sim_scores = cosine_sim[idx]
        combined_sim_scores += sim_scores

    sim_scores = list(enumerate(combined_sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in sim_scores[1:num_recommend+len(movie_list)]]

    recommended_movies = []
    for i in movie_indices:
        if df['Title'].iloc[i] not in movie_list:
            recommended_movies.append(df['Title'].iloc[i])

    return recommended_movies

@app.route('/')
def home():
    return 'Movie Recommendation API'

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    title = data.get('title', None)
    logging.debug(title)
    if title:
        recommendations = get_recommendations(title)
    else:
        movie_list = data.get("movie_list", [])
        recommendations = get_combined_recommendations(movie_list)

    return jsonify(recommendations)

if __name__ == "__main__":
    app.run()
