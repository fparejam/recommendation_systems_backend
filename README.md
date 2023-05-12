# Movie Recommendation API

This project provides a Flask-based backend API for movie recommendations. It utilizes cosine similarity to recommend similar movies based on their plot summaries. The recommendations can be generated for individual movies or a combination of movies.

## Prerequisites

Make sure you have the following dependencies installed:

- Flask
- Flask-CORS
- pandas
- numpy
- scikit-learn

## Getting Started

1. Clone the repository from GitHub:

```
git clone https://github.com/fparejam/movie_recommender_backend.git
```


2. Install the required dependencies. You can use pip:

```
pip install requirements.txt
```


3. Prepare the movie data:
   - Place a CSV file containing movie data named `movies.csv` in the `data` directory.
   - Ensure the CSV file has the following columns: `Title`, `Director`, `Genre`, `Plot`, `imdbRating`, `Poster`.
   - The `Plot` column should contain the plot summaries for each movie.
   - Remove any rows with missing plot summaries (`NaN`) to ensure accurate recommendations.

4. Start the server:
   - Navigate to the project directory: `cd movie_recommender_backend`
   - Run the Flask application:

```
flask run
```

The server will start running on `http://localhost:5000`.

## API Endpoints

### `GET /`

Returns a simple message indicating that the Movie Recommendation API is running.

### `POST /recommend`

Generates movie recommendations based on the provided movie data.

#### Request Format

The request should be a JSON object containing an array of movies.

- For individual movie recommendation:

```json
[
{
 "Title": "Movie Title"
}
]
```

* For combined movie recommendation:

```json
[
  {
    "Title": "Movie Title 1"
  },
  {
    "Title": "Movie Title 2"
  },
  {
    "Title": "Movie Title 3"
  }
]
```

Response Format
The response will be a JSON object containing an array of recommended movies.

```
[
  "Recommended Movie 1",
  "Recommended Movie 2",
  "Recommended Movie 3"
]

```
## Example Usage

Make a POST request to `http://localhost:5000/recommend` with the appropriate request format to get movie recommendations based on the provided movie data. The app is currently being hosted on railway [https://recommendationsystemsbackend-production.up.railway.app/](movies_backend), although the server might not be running continuously.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## Contact:
fparejamayo@gmail.com
