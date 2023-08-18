from django.shortcuts import render
from django.views import generic
from .models import Workout, Category


def HomepageView(request):
    workout = Workout.objects.all()[:3]
    category = Category.objects.all()
    return render(request, 'index.html',
                  {'Workout': workout, 'Category': category})


class WorkoutList(generic.ListView):
    model = Workout
    queryset = Workout.objects.order_by('-created_on')
    # template_name = 'all-workouts.html'
    paginate_by = 6
