# Inhouse Project.

## _La Ropa_ - an E-commerce Website

[<img src="https://static.djangoproject.com/img/logos/django-logo-negative.png" height="75" alt="Django">](https://www.djangoproject.com)
[<img src="https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg" width="75" alt="Bootstrap">](https://getbootstrap.com)

A dynamic e-commerce website designed while keeping the mobile first design approach as the primary focus. A responsive website made using [Django](https://djangoproject.com), as the templating engine and back-end, and [Bootstrap 5.0](https://getbootstrap.com/), for front-end, along with HTML, CSS and JavaScript.

## Installation

[Python 3.6 or later](https://www.python.org/downloads/) is required to run the project

### Cloning the repository

Download directly via GitHub or by using Git:

```sh 
git clone https://github.com/vishnuz1611/Inhouse-project.git
```

### Install the dependencies

Install **pip**
```sh
python -m ensurepip --upgrade
```

Install **virtualenv**
```sh
pip install virtualenv
```

#### Create a virtual environment
```sh
virtual env
```

#### Activate the virtual environment
From the project's root directory:
```sh
cd venv/Scripts
activate
```

### Install dependencies from `requirements.txt`
```sh
pip install -r requirements.txt
```

## Start the project
From the project's root directory
```sh
cd core
python manage.py runserver
```

To stop the server press `Ctrl + C`

### Deactivate the virtual environment
To stop the server 
```sh
cd venv/Scripts
deactivate
```

