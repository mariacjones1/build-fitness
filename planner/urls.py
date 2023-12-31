from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.homepage, name="home"),
    path("categories/", views.category_list, name="categories"),
    path("workouts/", views.WorkoutList.as_view(), name="workouts"),
    path("workouts/<category_name>/", views.WorkoutListByCategory.as_view(),
         name="category"),
    path("saved_workouts/", views.SavedWorkoutsView.as_view(),
         name="saved_workouts"),
    path("completed_workouts/", views.CompletedWorkoutsView.as_view(),
         name="completed_workouts"),
    path("search_workouts/", views.SearchWorkoutsView.as_view(),
         name="search_workouts"),
    path("new_workout/", views.create_workout, name="new_workout"),
    path("<slug:slug>/", views.WorkoutDetail.as_view(), name="workout_detail"),
    path("edit_workout/<slug:slug>", views.edit_workout, name="edit_workout"),
    path("delete_workout/<slug:slug>", views.delete_workout,
         name="delete_workout"),
    path("save/<slug:slug>", views.SaveWorkout.as_view(), name="workout_save"),
    path("complete/<slug:slug>", views.CompleteWorkout.as_view(),
         name="workout_complete"),
    path('accounts/', include('allauth.urls')),
]
