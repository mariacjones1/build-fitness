from django.test import TestCase
from .models import Workout, Category, User
from django.contrib.auth.models import Permission


class TestWorkoutListViews(TestCase):

    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_category_list(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_workout_list(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts.html')

    def test_get_workout_list_filtered_by_category(self):
        category = Category.objects.create(
            name='test category', slug='test-category')
        response = self.client.get(f'/workouts/{category.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts.html')

    def test_get_saved_workout_list(self):
        response = self.client.get('/saved_workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts.html')

    def test_get_completed_workout_list(self):
        response = self.client.get('/completed_workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts.html')


class TestWorkoutDetailViews(TestCase):

    def test_view_workout(self):
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

    def test_view_create_workout(self):
        user = User.objects.create_user('tester', password='test')
        user.user_permissions.add(
            Permission.objects.get(codename='add_workout'))
        self.client.login(username='tester', password='test')
        response = self.client.get('/new_workout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_workout.html')


class TestEditWorkoutViews(TestCase):

    def test_view_edit_workout(self):
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

    def test_view_delete_workout_confirmation(self):
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

    def test_save_workout(self):
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

    def test_complete_workout(self):
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
