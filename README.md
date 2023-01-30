# UOCIS322 - Project 2 #

This project will get you started with Docker and Flask. You need to have Docker set up on your machine to complete this project. You can alternatively use the machine we talked about in class.

## Getting started

* Read every line of the docker file.

* Go to `web/`  and read every line of the flask app.

* **Go back to the main directory**, and build the simple flask app image using

  ```
  docker build -t some-image-name .
  ```
  **Make sure to use a unique name if you're running on testium.**
* Run the container using

  ```
  docker run -d -p 5001:5000 some-image-name
  ```

* Launch `http://hostname:5001` using your web browser and check the output "UOCIS docker demo!".<br>
**Q:** What's `5001` and what's `5000`?<br>
**A:** the `-p` argument opens a container port to another on your local machine. Think of the container as its own separate machine, and assume you start a web server on port `5000` there. To access the web server from your machine, you forward container's `5000` to YOUR `5001`.<br>
To understand this better, try chaning the `5001` when starting your container, or `5000`. But remember, `5000` should be the port Flask uses (see `web/app.py`).

## Tasks Info
* Name: Tong Guan 
* Info: Project 2 of class 322
* This project is an updated version of simple web server based on the project1. In project1, we use socker to manually connect the port and listen to the port. In project2, we use Flask framework to handle the connection for us. We also utilize the Docker to better manage the whole file systems.
* The function of this simple web server is similar as project1. When you typed in an existed file, it will directly show the page; if you type something illeagel, like "~~" or "..", it will return 403; if the file name you typed does not exist, it will return 404.


## Grading Rubric

* If everything works as expected, 100 will be assigned.
* If existing pages and files are NOT handled correctly, 20 points will be docked.
* For each of the errors not handled correctly (403, and 404), 20 points will be docked.
* For each the two HTML files (`404.html` and `403.html`) not in the appropriate location, 5 points will be docked.
* If `README.md` is not updated with your name and info, 5 points will be docked.
* If `Dockerfile` doesn't contain your name and email, 5 points will be docked.
* If docker builds and runs, but does not have the expected functionalities implemented, or the server is unreachable, 20 will be assigned.
	* ⚠️ NOTE: If `app.py` does not read port number and debug mode from `credentials.ini` (or `default.ini` if not found), autograder will mark this as unreachable, as it cannot look for the correct port number.
* If docker builds, but fails to run, 15 will be assigned.
* If docker fails to build, 5 will be assigned.
* If `credentials.ini` is incorrect or not submitted, 0 will be assigned.

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
