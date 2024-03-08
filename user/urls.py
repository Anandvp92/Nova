from django.urls import path
from .views import register,LogoutUser,indexpage
urlpatterns=[
    path("api/register/",register,name="registerpage"),
    path("api/logout/",LogoutUser,name="LogoutUser"),
    path("index/",indexpage,name="indexpage"),
]