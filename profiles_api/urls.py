from django.urls import path
from profiles_api import views

urlpatterns = [
    # a standard function to convert api view class to be rendered
    path('hello-view', views.HelloApiView.as_view()),
]