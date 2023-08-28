from django.test import TestCase
from .forms import CommentForm, WorkoutForm, ExerciseForm


class TestCommentForm(TestCase):
    """Tests relating to CommentForm()"""

    def test_comment_body_is_required(self):
        """Tests that comments can't be submitted without a body"""
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_approved_is_not_required(self):
        """Tests that comments can be submitted without having been approved"""
        form = CommentForm({'body': 'Test comment'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """Tests that the comment body is explicit in the metaclass"""
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['body', ])


class TestWorkoutForm(TestCase):
    """Tests relating to WorkoutForm()"""

    def test_empty_form_is_invalid(self):
        """Tests that the workout form cannot be submitted if it is empty"""
        form = WorkoutForm()
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Tests that the workout name, category and image are explicit in the
        meta class
        """
        form = WorkoutForm()
        self.assertEqual(form.Meta.fields, ['name', 'category', 'image', ])


class TestExerciseForm(TestCase):
    """Tests relating to ExerciseForm()"""

    def test_empty_form_is_invalid(self):
        """Tests that the exercise form cannot be submitted if it is empty"""
        form = ExerciseForm()
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Tests that the exercise name, sets and reps are explicit in the meta
        class
        """
        form = ExerciseForm()
        self.assertEqual(form.Meta.fields, ['name', 'sets', 'reps', ])

    def test_sets_above_0(self):
        """Tests that exercises cannot be submitted with 0 sets"""
        form = ExerciseForm({
            'name': 'Test exercise',
            'sets': '0',
            'reps': '1'
            })
        self.assertFalse(form.is_valid())

    def test_sets_below_11(self):
        """Tests that exercises cannot be submitted with 11 sets"""
        form = ExerciseForm({
            'name': 'Test exercise',
            'sets': '11',
            'reps': '1'
            })
        self.assertFalse(form.is_valid())

    def test_reps_above_0(self):
        """Tests that exercises cannot be submitted with 0 reps"""
        form = ExerciseForm({
            'name': 'Test exercise',
            'sets': '1',
            'reps': '0'
            })
        self.assertFalse(form.is_valid())

    def test_reps_below_31(self):
        """Tests that exercises cannot be submitted with 31 reps"""
        form = ExerciseForm({
            'name': 'Test exercise',
            'sets': '1',
            'reps': '31'
            })
        self.assertFalse(form.is_valid())
