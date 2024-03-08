from django.urls import path
from .views import register,LogoutUser,createUser
urlpatterns=[
    path("api/register/",register,name="registerpage"),
    path("api/logout/",LogoutUser,name="LogoutUser"),
    path("api/createuser/",createUser,name="indexpage"),
]