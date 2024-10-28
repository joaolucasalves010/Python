from django.contrib import admin
from django.urls import path
from app import views


app_name = 'app'
urlpatterns = [
  path("", views.index, name="index"),
  path("<int:question_id>/", views.detail, name="detail"), # >> app/5 
  path("<int:question_id>/results/", views.results, name="results"), # >> app/5/results/
  path("<int:question_id>/vote/", views.vote, name="vote")
]