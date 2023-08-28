from .models import Comment, Workout, Exercise
from django import forms


class CommentForm(forms.ModelForm):
    """Uses Comment model and displays body field to user"""
    class Meta:
        model = Comment
        fields = ['body', ]


class WorkoutForm(forms.ModelForm):
    """
    Uses Workout model and displays name, category and image
    fields to user
    """
    class Meta:
        model = Workout
        fields = [
            'name',
            'category',
            'image', ]


class ExerciseForm(forms.ModelForm):
    """
    Uses Exercise model and displays name, sets and reps
    fields to user
    """
    class Meta:
        model = Exercise
        fields = [
            'name',
            'sets',
            'reps', ]
