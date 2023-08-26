from django.test import TestCase
from .models import Category, Workout, User, Exercise, Comment


class TestCategoryModel(TestCase):

    def test_category_string_returns_name(self):
        category = Category.objects.create(name='test category')
        self.assertEqual(Category.__str__(category), 'test category')


class TestWorkoutModel(TestCase):

    def test_workout_string_returns_name(self):
        category = Category.objects.create(name='test category')
        user = User.objects.create(username='tester')
        workout = Workout.objects.create(
            name='test workout',
            category=category,
            author=user,
            slug='test-slug'
        )
        self.assertEqual(Workout.__str__(workout), 'test workout')

    def test_workout_number_of_saves(self):
        category = Category.objects.create(name='test category')
        user = User.objects.create(username='tester')
        workout = Workout.objects.create(
            name='test workout',
            category=category,
            author=user,
            slug='test-slug',
        )
        workout.saves.add(user)
        self.assertEqual(Workout.number_of_saves(workout), 1)

    def test_workout_number_of_completed(self):
        category = Category.objects.create(name='test category')
        user = User.objects.create(username='tester')
        workout = Workout.objects.create(
            name='test workout',
            category=category,
            author=user,
            slug='test-slug',
        )
        workout.completed.add(user)
        self.assertEqual(Workout.number_of_completed(workout), 1)


class TestExerciseModel(TestCase):
    def test_exercise_string_returns_name(self):
        category = Category.objects.create(name='test category')
        user = User.objects.create(username='tester')
        workout = Workout.objects.create(
            name='test workout',
            category=category,
            author=user,
            slug='test-slug',
        )
        exercise = Exercise.objects.create(
            name='test exercise',
            sets=1,
            reps=1,
            workout=workout
        )
        self.assertEqual(Exercise.__str__(exercise), 'test exercise')


class TestCommentModel(TestCase):

    def test_comment_string_returns_body_and_username(self):
        category = Category.objects.create(name='test category')
        user = User.objects.create(username='tester')
        workout = Workout.objects.create(
            name='test workout',
            category=category,
            author=user,
            slug='test-slug',
        )
        comment = Comment.objects.create(
            body='test comment',
            user=user,
            workout=workout
            )
        self.assertEqual(
            Comment.__str__(comment), 'Comment test comment by tester')
