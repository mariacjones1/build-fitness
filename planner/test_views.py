from django.test import TestCase
from .models import Workout, Category, User
from django.contrib.auth.models import Permission


class TestWorkoutListViews(TestCase):
    """Tests relating to workout list views"""

    def test_get_homepage(self):
        """Tests that the homepage is rendered"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_category_list(self):
        """Tests that the categories page is rendered"""
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_workout_list(self):
        """Tests that the workouts page is rendered"""
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts.html')

    def test_get_workout_list_filtered_by_category(self):
        """
        Tests that the category-filtered workouts page is rendered
        for a selected category
        """
        category = Category.objects.create(
            name='test category', slug='test-category')
        response = self.client.get(f'/workouts/{category.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts.html')

    def test_get_saved_workout_list(self):
        """Tests that the saved workouts page is rendered"""
        response = self.client.get('/saved_workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts.html')

    def test_get_completed_workout_list(self):
        """Tests that the completed workouts page is rendered"""
        response = self.client.get('/completed_workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts.html')


class TestWorkoutDetailViews(TestCase):
    """Tests relating to workout detail views"""

    def test_view_workout(self):
        """
        Tests that the workout detail page is rendered for a
        selected workout
        """
        category = Category.objects.create(name='test category')
        user = User.objects.create(username='tester')
        workout = Workout.objects.create(
            name='test workout',
            slug='test-workout',
            category=category,
            author=user,
        )
        response = self.client.get(f'/{workout.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout_detail.html')


class TestCreateWorkoutViews(TestCase):
    """Tests relating to create workout views"""

    def test_view_create_workout(self):
        """
        Tests that the create workout view is rendered for authorised
        users
        """
        user = User.objects.create_user('tester', password='test')
        user.user_permissions.add(
            Permission.objects.get(codename='add_workout'))
        self.client.login(username='tester', password='test')
        response = self.client.get('/new_workout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_workout.html')


class TestEditWorkoutViews(TestCase):
    """Tests relating to edit workout views"""

    def test_view_edit_workout(self):
        """
        Tests that the edit workout view is rendered for authorised
        users
        """
        category = Category.objects.create(name='test category')
        user = User.objects.create_user('tester', password='test')
        workout = Workout.objects.create(
            name='test workout',
            slug='test-workout',
            category=category,
            author=user,
        )
        user.user_permissions.add(
            Permission.objects.get(codename='change_workout'))
        self.client.login(username='tester', password='test')
        response = self.client.get(f'/edit_workout/{workout.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_workout.html')


class TestDeleteWorkoutViews(TestCase):
    """Tests relating to delete workout views"""

    def test_view_delete_workout_confirmation(self):
        """
        Tests that the delete workout confirmation view is rendered for
        authorised users
        """
        category = Category.objects.create(name='test category')
        user = User.objects.create_user('tester', password='test')
        workout = Workout.objects.create(
            name='test workout',
            slug='test-workout',
            category=category,
            author=user,
        )
        user.user_permissions.add(
            Permission.objects.get(codename='delete_workout'))
        self.client.login(username='tester', password='test')
        response = self.client.get(f'/delete_workout/{workout.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete.html')

    def test_can_delete_workout(self):
        """
        Tests that workouts are deleted from the database when an
        authorised user deletes them from the site
        """
        category = Category.objects.create(name='test category')
        user = User.objects.create_user('tester', password='test')
        workout = Workout.objects.create(
            name='test workout',
            slug='test-workout',
            category=category,
            author=user,
        )
        user.user_permissions.add(
            Permission.objects.get(codename='delete_workout'))
        self.client.login(username='tester', password='test')
        response = self.client.post(f'/delete_workout/{workout.slug}')
        existing_workouts = Workout.objects.filter(id=workout.id)
        self.assertEqual(len(existing_workouts), 0)


class TestSaveWorkoutViews(TestCase):
    """Tests relating to save workout views"""

    def test_save_workout(self):
        """
        Test that a user's save is stored in a workout after they save it
        """
        category = Category.objects.create(name='test category')
        user = User.objects.create_user('tester', password='test')
        workout = Workout.objects.create(
            name='test workout',
            slug='test-workout',
            category=category,
            author=user,
        )
        self.client.login(username='tester', password='test')
        response = self.client.post(f'/save/{workout.slug}')
        self.assertRedirects(response, f'/{workout.slug}/')
        saved_item = Workout.objects.get(id=workout.id)
        self.assertTrue(workout.saves.filter(id=user.id).exists())

    def test_undo_save_workout(self):
        """
        Test that a user's save is removed from a workout after they unsave
        it
        """
        category = Category.objects.create(name='test category')
        user = User.objects.create_user('tester', password='test')
        workout = Workout.objects.create(
            name='test workout',
            slug='test-workout',
            category=category,
            author=user,
        )
        self.client.login(username='tester', password='test')
        response = self.client.post(f'/save/{workout.slug}')
        self.assertRedirects(response, f'/{workout.slug}/')
        response = self.client.post(f'/save/{workout.slug}')
        self.assertRedirects(response, f'/{workout.slug}/')
        saved_item = Workout.objects.get(id=workout.id)
        self.assertFalse(workout.saves.filter(id=user.id).exists())


class TestCompleteWorkoutViews(TestCase):
    """Tests relating to complete workout views"""

    def test_complete_workout(self):
        """
        Test that a user's complete is stored in a workout after they mark a it
        as completed
        """
        category = Category.objects.create(name='test category')
        user = User.objects.create_user('tester', password='test')
        workout = Workout.objects.create(
            name='test workout',
            slug='test-workout',
            category=category,
            author=user,
        )
        self.client.login(username='tester', password='test')
        response = self.client.post(f'/complete/{workout.slug}')
        self.assertRedirects(response, f'/{workout.slug}/')
        completed_item = Workout.objects.get(id=workout.id)
        self.assertTrue(workout.completed.filter(id=user.id).exists())

    def test_undo_complete_workout(self):
        """
        Test that a user's complete is removed from a workout after they
        unmark it as completed
        """
        category = Category.objects.create(name='test category')
        user = User.objects.create_user('tester', password='test')
        workout = Workout.objects.create(
            name='test workout',
            slug='test-workout',
            category=category,
            author=user,
        )
        self.client.login(username='tester', password='test')
        response = self.client.post(f'/complete/{workout.slug}')
        self.assertRedirects(response, f'/{workout.slug}/')
        response = self.client.post(f'/complete/{workout.slug}')
        self.assertRedirects(response, f'/{workout.slug}/')
        completed_item = Workout.objects.get(id=workout.id)
        self.assertFalse(workout.completed.filter(id=user.id).exists())
