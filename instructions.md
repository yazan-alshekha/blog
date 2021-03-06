# Instructions (How to)

**create new empty folder and go inside it**

```
- mkdir lab31
- cd lab31
```

**initialize project**

```
- poetry init -n
```

**add django framework to our project**

```
-poetry add django==3.2
```

**switching to the shell**

```
- poetry shell
```

**create new project
add "." at the end of the command in order to create the project at the root**

```
- django-admin startproject _project_name .
```

**if you won't need to customize your models you can do migrate now**

```
 - python manage.py migrate
    
```

**then create superuser**

- python manage.py createsuperuser

**to run the server**

```
- python manage.py runserver 
```

**install djangorestframework**

```
poetry add djangorestframework
```

**add new app**

```
- python manage.py startapp _app_name
```

go to setting then INSTALLED_APPS and add the following

```
'rest_framework',
#app name
'_app_name',
```
add the following to seeting.py 

```
# Django REST framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

| Syntax | Description |
| ----------- | ----------- |
| views |  [click here](readme_pages/views) |
| serializers | [click here](readme_pages/serializers) |

