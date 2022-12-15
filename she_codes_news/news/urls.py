from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #bringing up the IndexView class on viewspy
    path('<int:pk>/', views.StoryView.as_view(), name='story'), #directing us to the  number of a specific story (integer primary key) AND 
    path('add-story/', views.AddStoryView.as_view(), name='newStory')
]
