from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

# a standard way for viewset
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    # a standard function to convert api view class to be rendered
    path('hello-view', views.HelloApiView.as_view()),
    path('', include(router.urls))
]