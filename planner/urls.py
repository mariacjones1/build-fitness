from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.homepage, name="home"),
    path("workouts/", views.WorkoutList.as_view(), name="workouts"),
    path("workouts/<category_name>/", views.CategoryList.as_view(), name="category"),
    path("<slug:slug>/", views.WorkoutDetail.as_view(), name="workout_detail"),
    path('accounts/', include('allauth.urls')),
]
