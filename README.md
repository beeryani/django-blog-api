# BLOG PROJECT BACKEND API

## Project Requirements

The objectives of this project are to:

1. Learn more about Django Rest Framework
2. Learn how to build scalable APIs, connect external DB (e.g., Postgres) and deploy them on a cloud service.
3. Integrate React UI using this API. (TO-DO)
4. Learn Django Best Practices aligned with production deployment requirements:
   1. Pass DB credentials as env secrets.
   2. Create settings package to manage settings for development, staging and production separately.
   3. Set up GH Actions for continuous testing and CI/CD in prod.

## Functional Requirements

1.  Retrieve a list of recent blog posts
2.  Retrieve a detailed view of a blog post
3.  Create a new blog post
4.  Update an existing blog post
5.  Delete an existing blog post

## Non-Functional Requirements

1.  Ensure the API is secure and protected from unauthorized access
2.  Optimize API performance for scalability
3.  Ensure API responsiveness and reliability

## High Level Design

This Django backend API will be designed to store and retrieve blog posts from a Postgres database. The API will have several endpoints to handle CRUD (Create, Read, Update, and Delete) operations for blog posts. The API will be secured with authentication and authorization to prevent unauthorized access.

## User Stories

1.  As a blog author, I want to create a new blog post using the API.
2.  As a blog reader, I want to retrieve a list of recent blog posts from the API.
3.  As a blog reader, I want to view a detailed blog post from the API.
4.  As a blog author, I want to update an existing blog post using the API.
5.  As a blog author, I want to delete an existing blog post using the API.

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/praty-1698/django-blog-project.git
    $ cd django-blog-project

Activate the virtualenv for your project.

Install project dependencies:

    $ pip install -r requirements.txt

## API Endpoints

1. Take a look at 5 recent blogs: `blog/`
2. Detailed view of a Blog: `blog/<int:pk>`
3. Create a Blog: `createblog/`
4. Update a Blog: `updateblog/<int:pk>/`
5. Delete a Blog: `deleteblog/<int:pk>/`

## Steps for Django setup

Based on local and prod deployment, refer to `settings` folder and make changes to `manage.py`:

```python
$ os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.<settings file based on use case>") ## settings.base is default
```

Then simply apply the migrations:

    $ python manage.py migrate
