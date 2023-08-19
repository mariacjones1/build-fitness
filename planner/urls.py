from . import views
from django.urls import path


urlpatterns = [
    path("", views.HomepageView, name="home"),
    path("workouts/", views.WorkoutList.as_view(), name="workouts"),
    path("<slug:slug>/", views.WorkoutDetail.as_view(), name="workout_detail")
]
