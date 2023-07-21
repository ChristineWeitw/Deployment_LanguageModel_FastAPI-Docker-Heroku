# Deployment_LanguageModel_FastAPI-Docker-Heroku
Deploy an Language Detection ML model with FastAPI, Docker, and Heroku

* Model Development :
  
  'LanguageDetection.ipynb' - create a language detection model using sklearn CountVectorizer with naive_bayes, then create pipeline to wrap them together.
* FastAPI app :
  
  'main.py' - for fastapi endpoints.
  
  'model.py' - to call the pipeline models inside pkl file.
* Dockerize the app: 

  '.dockerignore' - to ignore certain files

  'Dockerfile' - build to doucker image
    * reference: https://fastapi.tiangolo.com/deployment/docker/
    * Run the command in terminal to build the image:
        "docker build -t <name> ."
    * To test and run the image to see if it works:
        "docker run -p 80:80 <name>"
* Deployment to Heroku
* Final Testing
