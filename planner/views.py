from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.template import RequestContext
from .models import Workout, Category


def homepage(request):
    workout = Workout.objects.all()[:3]
    category = Category.objects.all()
    return render(request, 'index.html',
                  {'Workout': workout, 'Category': category})


class WorkoutList(generic.ListView):
    model = Workout
    category = Category.objects.all()
    queryset = Workout.objects.order_by('-created_on')
    template_name = 'workouts.html'
    paginate_by = 6


class CategoryList(generic.ListView):
    model = Workout
    template_name = 'workouts.html'
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(
            Category, slug=self.kwargs['category_name'])
        return Workout.objects.filter(category=self.category)


class WorkoutDetail(View):

    def get_queryset(self):
        exercises = super().get_queryset()
        exercises = exercises.prefetch_related("exercises")
        return exercises

    def get(self, request, slug, *args, **kwargs):
        queryset = Workout.objects.all()
        workout = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "workout_detail.html",
            {
                "workout": workout,
            }
        )
