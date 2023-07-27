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


* Example of how fastapi/doc page looks like, when we input a sentence in whichever langugage, and the model outputs its prediction for us.

  
In this case, we entered "hola, como estas" for model to predict what language is it.
  <img width="1106" alt="image" src="https://github.com/ChristineWeitw/Deployment_LanguageModel_FastAPI-Docker-Heroku/assets/58152741/e6b03bb3-d561-4f3a-91ec-a8f51edf8193">

And the output prediction is "Spanish":

<img width="1083" alt="image" src="https://github.com/ChristineWeitw/Deployment_LanguageModel_FastAPI-Docker-Heroku/assets/58152741/ac6d5d7c-c1ee-4b03-9988-d683d7d35f90">


  
