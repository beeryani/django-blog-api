# BLOG PROJECT BACKEND API

The objectives of this project are to:

1.  Learn more about Django Rest Framework
2.  Learn how to build scalable APIs, connect external DB (eg: Postgres) and deploy them on a PaaS.
3.  Integrate React UI using this API.
4.  Learn Django Best Practices aligned with production deployment requirements.
    1. Pass DB credentials as env secrets.
    2. Creating settings package to manage settings for development, staging and production separately.
    3. Setting up GH Actions for continuous testing and CI/CD in prod.

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
