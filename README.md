# Food-Classification-App

This is a food classification application that uses a machine learning model trained on a dataset of food images. It uses Node.js for the back-end server, Python for the machine learning part, and Express.js as the web framework.

## Project structure

The project is structured as follows:
- 'models/': Directory containing the trained model files.
- 'src/': Contains the source code for the project.
  - 'api/': Contains the Node.js server code.
  - 'client/': Contains the front-end HTML and CSS files.
- 'Dockerfile': The Dockerfile to create a Docker image for the project.
- 'app.py': The Python script for making predictions using the trained model.
- 'requirements.txt': Contains the Python dependencies required by `app.py`.
- 'package.json': Contains the Node.js dependencies required by the server.

To build the Docker images:

docker build -t my-app .

To run the Docker container:

docker run -p 3000:3000 my-app

The application will work at http://localhost:3000
