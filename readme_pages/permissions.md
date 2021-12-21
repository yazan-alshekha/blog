
1. go to setting.py and edit REST_FRAMEWORK list and change it from **AllowAny** to **IsAuthenticated**
2. add new file to your app **"permissions.py"*
3. import permissions from rest_framework

```
from rest_framework import permissions

class testAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user==obj.author   

```
import  testAuthenticated class you made to views.py  

`from .permissions import testAuthenticated`

add this line to the view:

`permission_classes=(testAuthenticated,)`