from .import views
from django.urls import path,include
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'api'
urlpatterns = [
     path('login',views.login.as_view(),name="login"),

]