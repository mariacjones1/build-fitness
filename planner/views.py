from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Workout, Category
# from .forms import CommentForm


def HomepageView(request):
    workout = Workout.objects.all()[:3]
    category = Category.objects.all()
    return render(request, 'index.html',
                  {'Workout': workout, 'Category': category})


class WorkoutList(generic.ListView):
    model = Workout
    queryset = Workout.objects.order_by('-created_on')
    template_name = 'workouts.html'
    paginate_by = 6

    # def get(self, request, slug, *args, **kwargs):
    #     if slug == '':
    #         return render(request, 'workouts.html')
    #     else:
    #         queryset = Workout.objects.filter(category=slug)
    #         post = get_object_or_404(queryset, slug=slug)
    #         return render(request, 'workouts.html')


class WorkoutDetail(View):

    def get_queryset(self):
        exercises = super().get_queryset()
        exercises = exercises.prefetch_related("exercises")
        return exercises

    def get(self, request, slug, *args, **kwargs):
        queryset = Workout.objects.all()
        workout = get_object_or_404(queryset, slug=slug)
        # comments = post.comments.filter(approved=True).order_by("-created_on")
        # saved = False
        # completed = False
        # if workout.saves.filter(id=self.request.user.id).exists():
        #     saved = True
        # if workout.completed.filter(id=self.request.user.id).exists():
        #     completed = True

        return render(
            request,
            "workout_detail.html",
            {
                "workout": workout,
                # "comments": comments,
                # "commented": False,
                # "saved": saved,
                # "completed": completed,
                # "comment_form": CommentForm()
            }
        )
