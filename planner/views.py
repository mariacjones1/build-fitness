from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required, permission_required
from .models import Workout, Category, User
from .forms import *


def homepage(request):
    workout = Workout.objects.all()[:3]
    category = Category.objects.all().order_by('id')
    return render(request, 'index.html',
                  {'Workout': workout, 'Category': category})


def category_list(request):
    category = Category.objects.all().order_by('id')
    return render(request, 'index.html',
                  {'Category': category})


class WorkoutList(generic.ListView):
    model = Workout
    category = Category.objects.all()
    queryset = Workout.objects.order_by('-created_on')
    template_name = 'workouts.html'
    paginate_by = 6


class WorkoutListByCategory(generic.ListView):
    model = Workout
    template_name = 'workouts.html'
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(
            Category, slug=self.kwargs['category_name'])
        return Workout.objects.filter(
            category=self.category).order_by('-created_on')


class SavedWorkoutsView(generic.ListView):
    model = Workout
    template_name = 'workouts.html'
    paginate_by = 6

    def get_queryset(self):
        return Workout.objects.filter(saves__id__in=[self.request.user.id])


class CompletedWorkoutsView(generic.ListView):
    model = Workout
    template_name = 'workouts.html'
    paginate_by = 6

    def get_queryset(self):
        return Workout.objects.filter(completed__id__in=[self.request.user.id])


class SearchWorkoutsView(generic.ListView):
    model = Workout
    template_name = 'workouts.html'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Workout.objects.filter(name__icontains=query)


class WorkoutDetail(View):

    def get_queryset(self):
        exercises = super().get_queryset()
        exercises = exercises.prefetch_related("exercises")
        return exercises

    def get(self, request, slug, *args, **kwargs):
        queryset = Workout.objects.all()
        workout = get_object_or_404(queryset, slug=slug)
        comments = workout.comments.filter(
            approved=True).order_by("created_on")
        saved = False
        completed = False
        if workout.saves.filter(id=self.request.user.id).exists():
            saved = True
        if workout.completed.filter(id=self.request.user.id).exists():
            completed = True

        return render(
            request,
            "workout_detail.html",
            {
                "workout": workout,
                "comments": comments,
                "commented": False,
                "saved": saved,
                "completed": completed,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Workout.objects.all()
        workout = get_object_or_404(queryset, slug=slug)
        comments = workout.comments.filter(
            approved=True).order_by("created_on")
        saved = False
        completed = False
        if workout.saves.filter(id=self.request.user.id).exists():
            saved = True
        if workout.completed.filter(id=self.request.user.id).exists():
            completed = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.workout = workout
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "workout_detail.html",
            {
                "workout": workout,
                "comments": comments,
                "commented": True,
                "saved": saved,
                "completed": completed,
            },
        )


class SaveWorkout(View):
    def post(self, request, slug):
        workout = get_object_or_404(Workout, slug=slug)
        if workout.saves.filter(id=self.request.user.id).exists():
            workout.saves.remove(request.user)
        else:
            workout.saves.add(request.user)
        return HttpResponseRedirect(reverse('workout_detail', args=[slug]))


class CompleteWorkout(View):
    def post(self, request, slug):
        workout = get_object_or_404(Workout, slug=slug)
        if workout.completed.filter(id=self.request.user.id).exists():
            workout.completed.remove(request.user)
        else:
            workout.completed.add(request.user)
        return HttpResponseRedirect(reverse('workout_detail', args=[slug]))


@login_required
@permission_required('planner.add_workout', raise_exception=True)
def create_workout(request):
    ExerciseFormSet = inlineformset_factory(
        Workout,
        Exercise,
        form=ExerciseForm,
        extra=0,
        min_num=3,
        validate_min=True,
        max_num=10,
        can_delete=False)
    workout_form = WorkoutForm()
    exercise_formset = ExerciseFormSet(instance=Workout())
    if request.method == 'POST':
        workout_form = WorkoutForm(request.POST, request.FILES)
        exercise_formset = ExerciseFormSet(request.POST, request.FILES)
        if workout_form.is_valid():
            workout_form.instance.author = request.user
            workout_form.instance.slug = slugify(workout_form.instance.name)
            workout = workout_form.save(commit=False)
            if exercise_formset.is_valid():
                workout.save()
                for exercise in exercise_formset:
                    exercise.instance.workout = workout
                    exercise.save()
                return HttpResponseRedirect(reverse('home'))

    else:
        workout_form = WorkoutForm()
        exercise_formset = ExerciseFormSet(instance=Workout())

    return render(
        request,
        "new_workout.html",
        {
            "workout_form": workout_form,
            "exercise_formset": exercise_formset,
        },
    )


@login_required
@permission_required('planner.change_workout', raise_exception=True)
def edit_workout(request, slug):
    queryset = Workout.objects.all()
    workout = get_object_or_404(queryset, slug=slug)
    ExerciseFormSet = inlineformset_factory(
        Workout,
        Exercise,
        form=ExerciseForm,
        extra=0,
        min_num=3,
        validate_min=True,
        max_num=10,
        can_delete=True)
    workout_form = WorkoutForm(instance=workout)
    exercise_formset = ExerciseFormSet(instance=workout)
    if request.method == 'POST':
        workout_form = WorkoutForm(
            request.POST, request.FILES, instance=workout)
        exercise_formset = ExerciseFormSet(
            request.POST, request.FILES, instance=workout)
        if workout_form.is_valid():
            workout_form.instance.slug = slugify(workout_form.instance.name)
            workout = workout_form.save(commit=False)
            if exercise_formset.is_valid():
                workout.save()
                exercises = exercise_formset.save(commit=False)
                for obj in exercise_formset.deleted_objects:
                    obj.delete()
                for exercise in exercises:
                    exercise.save()
                return HttpResponseRedirect(
                    reverse('workout_detail', args=[workout.slug]))

    return render(
        request,
        "edit_workout.html",
        {
            "workout_form": workout_form,
            "exercise_formset": exercise_formset,
        },
    )


@login_required
@permission_required('planner.delete_workout', raise_exception=True)
def delete_workout(request, slug):
    queryset = Workout.objects.all()
    workout = get_object_or_404(queryset, slug=slug)
    if request.method == 'GET':
        return render(request, 'confirm_delete.html', {'workout': workout})
    elif request.method == 'POST':
        workout.delete()
        return HttpResponseRedirect(reverse('home'))
