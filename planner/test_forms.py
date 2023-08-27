from django.test import TestCase
from .forms import CommentForm, WorkoutForm, ExerciseForm


class TestCommentForm(TestCase):

    def test_comment_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_approved_is_not_required(self):
        form = CommentForm({'body': 'Test comment'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['body', ])


class TestWorkoutForm(TestCase):

    def test_empty_form_is_invalid(self):
        form = WorkoutForm()
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = WorkoutForm()
        self.assertEqual(form.Meta.fields, ['name', 'category', 'image', ])


class TestExerciseForm(TestCase):

    def test_empty_form_is_invalid(self):
        form = ExerciseForm()
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ExerciseForm()
        self.assertEqual(form.Meta.fields, ['name', 'sets', 'reps', ])

    def test_sets_above_0(self):
        form = ExerciseForm({
            'name': 'Test exercise',
            'sets': '0',
            'reps': '1'
            })
        self.assertFalse(form.is_valid())

    def test_sets_below_6(self):
        form = ExerciseForm({
            'name': 'Test exercise',
            'sets': '6',
            'reps': '1'
            })
        self.assertFalse(form.is_valid())

    def test_reps_above_0(self):
        form = ExerciseForm({
            'name': 'Test exercise',
            'sets': '1',
            'reps': '0'
            })
        self.assertFalse(form.is_valid())

    def test_reps_below_16(self):
        form = ExerciseForm({
            'name': 'Test exercise',
            'sets': '1',
            'reps': '16'
            })
        self.assertFalse(form.is_valid())
