# PGN to Opening
A Flask web application that classifies chess openings based on PGN input. It uses a simplified ECO code and opening name classifier to identify the opening from the first few moves.

## Features:

Input a PGN string via a web form.

The app classifies the chess opening and displays the ECO code and opening name.

Uses SQLite for a simple TODO list feature (from the original template).

Dockerized environment for easy development and testing.

Unit tests included for the original TODO features.

## How to Run:

Build the Docker image:

./build_docker.sh chess-opening-classifier

Initialize the database (creates SQLite tables):

docker run --network=host -v $(pwd):/app -t chess-opening-classifier flask init_db

Run the Flask development server:

docker run --network=host -v $(pwd):/app -t chess-opening-classifier flask run

Open your browser and go to:

http://localhost:5000/

## Using the App:

On the home page, enter a PGN string representing a chess game’s opening moves.

Submit the form to see the detected ECO code and opening name.

You can still add, update, and delete TODO items as per the original template.

## Running Tests:

To run the unit tests inside the Docker container:

bash
Copy
Edit
./build_docker.sh chess-opening-classifier
docker run -t chess-opening-classifier ./run_tests.sh
To run a specific test (e.g., test_home):

arduino
Copy
Edit
docker run -t chess-opening-classifier ./run_tests.sh TodoTestCase.test_home
Project Structure:

app.py - Main Flask application with routes and chess opening classification logic.

templates/base.html - HTML template for the UI.

Dockerfile - Docker build file.

requirements.txt - Python dependencies.

unit_tests.py - Unit tests for the app.

run_tests.sh - Shell script to run tests.

build_docker.sh - Shell script to build the Docker image.

.dockerignore & .gitignore - Ignore files for Docker and git.

## Notes:

This project builds on an existing Flask TODO app template.

Chess opening classification uses a simple static dictionary for demo purposes.

The Docker image uses Python 3.13 Alpine for a lightweight container.

