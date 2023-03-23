# BLOG PROJECT BACKEND API

## Project Requirements

1.  Develop a Django backend API to manage a blog system
2.  Implement CRUD functionality for blog posts
3.  Use Django Rest Framework to create API endpoints for blog posts
4.  Use PostgreSQL to store blog post data
5.  Implement user authentication and authorization for API endpoints
6.  Optimize API performance for scalability
7.  Implement unit and integration tests for API endpoints
8.  Set up continuous integration and deployment with GitHub Actions
9.  Use environment variables for sensitive data (e.g., database credentials)

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
4.  Implement unit and integration tests for API endpoints

## High Level Design

The Django backend API will be designed to store and retrieve blog posts from a PostgreSQL database. The API will have several endpoints to handle CRUD operations for blog posts, which will be secured with authentication and authorization to prevent unauthorized access. The API will be optimized for performance and scalability, and unit and integration tests will be implemented to ensure API responsiveness and reliability. Continuous integration and deployment will be set up with GitHub Actions, and environment variables will be used for sensitive data such as database credentials.

## User Stories

1.  As a blog author, I want to create a new blog post using the API.
2.  As a blog reader, I want to retrieve a list of recent blog posts from the API.
3.  As a blog reader, I want to view a detailed blog post from the API.
4.  As a blog author, I want to update an existing blog post using the API.
5.  As a blog author, I want to delete an existing blog post using the API.

## Learning Objectives

The objectives of this project are to:

1. Learn more about Django Rest Framework
2. Learn how to build scalable APIs, connect external DB (e.g., Postgres) and deploy them on a cloud service.
3. Integrate React UI using this API. (TO-DO)
4. Learn Django Best Practices aligned with production deployment requirements:
   1. Pass DB credentials as env secrets.
   2. Create settings package to manage settings for development, staging and production separately.
   3. Set up GH Actions for continuous testing and CI/CD in prod.
5. Learn Docker using this as the sample.
   1. Setup for development environment.
   2. Setup for production environment with gunicorn and nginx.

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

### #To-Do

1. Add separate production settings file to avoid conflict in further development.
2. Implement user authentication and authorization for API endpoints
3. Implement unit and integration tests for API endpoints
