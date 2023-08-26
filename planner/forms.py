from .models import Comment, Workout, Exercise
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = [
            'name',
            'category',
            'image',]


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            'name',
            'sets',
            'reps',]
