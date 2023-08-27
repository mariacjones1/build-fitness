from django.contrib import admin
from django.apps import apps
from .models import *

planner_models = apps.get_app_config('planner').get_models()


class ExerciseAdmin(admin.TabularInline):
    model = Exercise


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_filter = ('created_on', 'category')
    list_display = ('name', 'slug', 'category', 'created_on')
    search_fields = ['name']
    inlines = [ExerciseAdmin, ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


for model in planner_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
