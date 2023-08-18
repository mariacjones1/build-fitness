from django.shortcuts import render
from django.views import generic
from .models import Workout


class WorkoutList(generic.ListView):
    model = Workout
    queryset = Workout.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3
