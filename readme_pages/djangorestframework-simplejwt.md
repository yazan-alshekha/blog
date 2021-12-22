[check the documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)

1. poetry add `djangorestframework-simplejwt`

2. Then, your django project must be configured to use the library. In settings.py, add rest_framework_simplejwt.authentication.JWTAuthentication to the list of authentication classes:
```
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}

```



3. add to your project -> urls.py (note that project not app)
```
from rest_framework_simplejwt import views as jwt_views

path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
```


the senario is :
- you are going to hit api token route and take the copy the token  it should be **post request**
- past it in bearer >- auth in thunder client app when you are trying to hit the others routes to get data 
