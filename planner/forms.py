from .models import Comment, Workout, Exercise
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


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


# ExerciseFormSet = forms.inlineformset_factory(
#     Workout, Exercise, form=ExerciseForm, extra=3)


# class WorkoutForm(forms.ModelForm):
#     class Meta:
#         model = Workout
#         fields = ('name', 'category', 'image',)

#     template_name = "new_workout.html"

#     def __init__(self, *args, **kwargs):
#         self.formset = ExerciseFormSet(*args, **kwargs)
#         super(WorkoutForm, self).__init__(*args, **kwargs)

#     def get_context(self):
#         context = super().get_context()
#         context['formset'] = self.formset
#         return context

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         self.formset.instance = instance
#         if self.formset.is_valid():
#             instance.save()
#             self.formset.save()
#         return instance
