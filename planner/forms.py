from .models import Comment, Workout, Exercise, Save
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# class SaveForm(forms.ModelForm):
#     class Meta:
#         model = Save
#         fields = '__all__'


class NewWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('name', 'category', 'image',)


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = (
            'name',
            'sets',
            'reps',
        )
