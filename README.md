<div align="center" id="top"> 
  <img src="./cardknox_logo.jpeg" alt="Cardknox" />

  &#xa0;

  <!-- <a href="https://cardknox.netlify.app">Demo</a> -->
</div>

<h1 align="center">Cardknox</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/jordanistan/cardknox?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/jordanistan/cardknox?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jordanistan/cardknox?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/jordanistan/cardknox?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/jordanistan/cardknox?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/jordanistan/cardknox?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/jordanistan/cardknox?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Cardknox 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/jordanistan" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

This Python script creates a dashboard to display JSON data fetched from a file. It utilizes Flask, a micro web framework for Python, to create a basic web application and render a HTML template (`dashboard.html`) to display the JSON data.

## Requirements
- Python 3.x
- Flask

## :sparkles: Features ##

:heavy_check_mark: - Reads JSON data from a file (`security_data.json`).
:heavy_check_mark: - Renders a dashboard using Flask, displaying the JSON data in a user-friendly format.
:heavy_check_mark: - Provides a simple and accessible way to visualize JSON data. 

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop/)


## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Node](https://nodejs.org/en/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/jordanistan/cardknox

# Access
$ cd cardknox

# Install dependencies
$ pip install -r requirements.txt

# Run the project
$ python dashboard.py

# The server will initialize in the <http://localhost:5000>
```
## :checkered_flag: Docker ##

```bash
# Clone this project
$ git clone https://github.com/jordanistan/cardknox

# Access
$ cd cardknox

# Install dependencies
$ docker build -t cardknox-dashboard-app .

# Run the project
$ docker run -p 5000:5000 cardknox-dashboard-app

# The server will initialize in the <http://localhost:5000>
$ http://localhost:5000

# Test to see if you can connect 
$ curl -o /dev/null -w '%{http_code}\n' -s -I http://127.0.0.1:5000/ -vvvv 

# If the output was "200" this means you were successfully 
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000
> HEAD / HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.4.0
> Accept: */*
>
< HTTP/1.1 200 OK <------ AWESOME You DID IT!~
< Server: Werkzeug/3.0.2 Python/3.12.2
< Date: Wed, 10 Apr 2024 05:46:14 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 5120
< Connection: close
<
* Closing connection
200 <------ AWESOME You DID IT!~

```
## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/jordanistan" target="_blank">El Gato</a>

&#xa0;

<a href="#top">Back to top</a>
