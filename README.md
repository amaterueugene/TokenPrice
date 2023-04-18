# What is this project about?

TokenPrice is a pet-project that was made for practicing web-parsing connected with Django and Django REST API.

The only thing this project does is parsing information about top 50 tokens and shows it to you due to common HTML page or API.

Tokens information source: https://crypto.com/price

# Installation

First at first you gotta clone this repository to your local machine.

`$ git clone "https://github.com/amaterueugene/TokenPrice.git"`

Now get into the directory of repository you've just cloned and paste following command to the terminal in order to install all requirements you need to get ready for launching the project.

```bash
$ python -m venv venv
$ pip install -r requirements.txt 
```

But, before starting the server, create all the migrations django needs to work correctly.

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Great! Now you are ready to start. Just use default django commands for starting local server.

`python manage.py runserver`

# Usage

There are 2 options you've got:

1. Look at the information from the website
2. Get the information in JSON format through the API

For reaching the webpage that you need, just paste the following url to your browser:

> http://127.0.0.1:8000/price/

For getting information due to API you gotta send the get request to the next address:

> http://127.0.0.1:8000/price/api/v1/
