# Anime Detector


## What it is
A web server that exposes [a face detector for anime/manga](https://github.com/nagadomi/lbpcascade_animeface) as a service. 


## Setup

### Without Docker

Install dependencies

    pip install -r requirements.txt

Start the web server

    python main.py


### With Docker

Build the image

    docker build . -t anime-detector

Start the container

    docker run -p 8080:80 anime-detector


## Usage

Upload the provided test image with cURL

    curl -X POST "http://localhost:8080/" \
         -H "accept: application/json" \
         -H "Content-Type: multipart/form-data" \
         -F "file=@test.jpg;type=image/jpg"

The response should be

    {
        "is_anime": true,
        "time_elapsed": 0.6407011000000011
    }

[FastAPI](https://fastapi.tiangolo.com/) web framework also provides automatic interactive documentation that you can access from `http://localhost:8080/docs`.
