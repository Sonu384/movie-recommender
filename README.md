# Movie Recommender System

This project is a movie recommendation system built using Python. It leverages content-based filtering techniques to suggest movies based on user preferences.

## Features

* *Content-Based Recommendations:* Recommends movies similar to those the user has enjoyed in the past.
* *Interactive Web Interface:* Utilizes Streamlit to provide an easy-to-use web interface.
* *TMDB Dataset:* Uses the TMDB 5000 Movies and Credits datasets for movie information.

## Files

* app1.py: The main Python script containing the Streamlit application and recommendation logic.
* tmdb_5000_credits.csv: Dataset containing movie credits (cast, crew).
* tmdb_5000_movies.csv: Dataset containing movie details (title, overview, genres, etc.).
* README.md: This file, providing project information.
* .gitignore: Specifies files to ignore when committing to Git.
* LICENSE: Specifies the project license (MIT License).

## Dependencies

* Python 3.x
* Streamlit
* Pandas
* Scikit-learn (if used for similarity calculations)

## Installation

1.  Clone the repository:

    bash
    git clone
    

2.  Navigate to the project directory:

    bash
    cd movie-recommender
    

3.  Install the required packages:

    bash
    pip install streamlit pandas scikit-learn  # Add other packages if needed
    

## Usage

1.  Run the Streamlit application:

    bash
    streamlit run app1.py
    

2.  Open your web browser and navigate to http://localhost:8501.

3.  Use the interface to get movie recommendations.

## Dataset

This project uses the TMDB 5000 Movies and Credits datasets, which contain information about 5000 movies from The Movie Database (TMDB).

* *tmdb_5000_movies.csv:* Contains movie details such as title, overview, genres, keywords, and more.
* *tmdb_5000_credits.csv:* Contains movie credits, including cast and crew information.

## License

This project is licensed under the MIT License.

## Author

[sonu cristina/Sonu384]

## Contributing

Contributions are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request.# movie-recommender
A movie recommendation system built with python 
