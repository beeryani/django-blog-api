# Personal Blog Project

The goals of this project are to:

1.  Learn more about Django Framework
2.  Learn how React can be integrated with a Python backend framework.
3.  Use postgres as a database
4.  Deploy a fullstack application on a production environment.

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/praty-1698/django-blog-project.git
    $ cd django-blog-project
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
## Steps for Django setup

Then simply apply the migrations:

    $ python manage.py migrate

## Steps for React App

This app uses [Vite](https://vitejs.dev/) as the bundler hence the integration and configuration will vary

Use the below command after installing the requirements:
    
    $ cd django-blog-frontend
    $ yarn
    $ yarn build

Now, You can run the development server:

    $ python manage.py runserver
