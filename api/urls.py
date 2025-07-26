from .import views
from django.urls import path,include
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'api'
urlpatterns = [
    path('login',views.login.as_view(),name="login"),
    
    path('snippetlist',views.snippetlist.as_view(),name="snippetlist"),
    path('snippetdetails',views.snippetdetails.as_view(),name="snippetdetails"),
    path('snippetdelete',views.snippetdelete.as_view(),name="snippetdelete"),
    
    path('tagslist',views.tagslist.as_view(),name="tagslist"),
    path('tagsdetails',views.tagsdetails.as_view(),name="tagsdetails"),




]