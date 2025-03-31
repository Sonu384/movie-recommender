import requests
from flask import Flask, render_template, request
import pandas as pd
import urllib.parse

app = Flask(__name__)

# Load the TMDb 5000 Movies dataset (make sure it's in your project folder)

# Your OMDb API Key
OMDB_API_KEY = 'http://www.omdbapi.com/?i=tt3896198&apikey=e0cba98e'

def fetch_movie_details(title):
    """
    Fetch movie poster and plot from OMDb API using the movie title.
    """
    # URL-encode the title to safely include it in the URL
    encoded_title = urllib.parse.quote(title)
    url = f"http://www.omdbapi.com/?t={encoded_title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Get the poster URL and plot. Fallback if not found.
        poster = data.get("Poster", "")
        plot = data.get("Plot", "No description available.")
        return poster, plot
    else:
        return "", "No description available."

def recommend_movies(movie_name):
    """
    Given a movie name from the search form, this function finds a matching movie
    and then randomly selects 12 movies from the dataset. For each movie, it fetches
    the poster and description using the OMDb API.
    """
    # Find a movie in the dataset by title (case-insensitive)
    movie = movies_df[movies_df['title'].str.contains(movie_name, case=False)]
    if movie.empty:
        return []  # Return empty list if no matching movie is found

    # For demonstration, pick 12 random movies from the dataset
    similar_movies = movies_df.sample(12)
    recommended_movies = []
    for i in range(len(similar_movies)):
        title = similar_movies.iloc[i]['title']
        poster, plot = fetch_movie_details(title)
        recommended_movies.append((title, plot, poster))
    return recommended_movies

@app.route("/", methods=["GET", "POST"])
def index():
    # Get a list of movie titles for potential search suggestions (if needed)
    movie_titles = movies_df["title"].tolist()

    if request.method == "POST":
        movie_name = request.form["movie_name"]
        recommended_movies = recommend_movies(movie_name)
        return render_template("index.html", movies=recommended_movies, movie_titles=movie_titles)
    
    return render_template("index.html", movies=[], movie_titles=movie_titles)

if __name__ == "_main_":
    app .run(debug=True)