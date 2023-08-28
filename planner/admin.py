from django.contrib import admin
from django.apps import apps
from .models import *

planner_models = apps.get_app_config('planner').get_models()


class ExerciseAdmin(admin.TabularInline):
    """Set Exercise model as inline to be used with Workout"""
    model = Exercise


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """
    Set Workout slug based on name, e.g. 'Workout name' becomes workout-name

    Django admin can filter by created_on (when the workout was created)
    and category

    Django admin can see the name, slug, category and creation date of each
    workout in the main table

    Django admin can search for workouts by name

    Exercise is used as inline field
    """
    prepopulated_fields = {'slug': ['name']}
    list_filter = ('created_on', 'category')
    list_display = ('name', 'slug', 'category', 'created_on')
    search_fields = ['name']
    inlines = [ExerciseAdmin, ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Set Workout slug based on name, e.g. 'Workout category'
    becomes workout-category
    """
    prepopulated_fields = {'slug': ['name']}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Django admin can filter by created_on (when the workout was created)
    and category

    Django admin can see the user, workout, body, creation date and approval
    status of each workout in the main table

    Django admin can search for comments by user or body

    Django admin can approve comments
    """
    list_display = ('user', 'workout', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """Function to approve comments in Django admin panel"""
        queryset.update(approved=True)


for model in planner_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
