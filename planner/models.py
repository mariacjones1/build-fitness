from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField
from colorfield.fields import ColorField
from cloudinary.models import CloudinaryField

# CATEGORIES = [
#         ("running", "Running"),
#         ("full body", "Full Body"),
#         ("upper body", "Upper Body"),
#         ("lower body", "Lower Body"),
#         ("mobility", "Mobility"),
#     ]

ROLES = [
    (0, "admin"),
    (1, "standard"),
]


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    image = CloudinaryField("image", default="placeholder")
    color = ColorField(default="#FFFFFF")

    def __str__(self):
        return self.name


class Exercise(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    # category = MultiSelectField(choices=CATEGORIES, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Workout(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="workouts")
    # category = models.CharField(
    #     max_length=50, choices=CATEGORIES, default="full body")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = CloudinaryField("image", default="placeholder")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    exercise1 = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="exercise1",
        null=True)
    exercise1_sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    exercise1_reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)], null=True)
    exercise2 = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="exercise2",
        null=True)
    exercise2_sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    exercise2_reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)], null=True)
    exercise3 = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="exercise3",
        null=True)
    exercise3_sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    exercise3_reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)], null=True)
    exercise4 = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="exercise4",
        null=True, blank=True)
    exercise4_sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True)
    exercise4_reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        null=True, blank=True)
    exercise5 = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="exercise5",
        null=True, blank=True)
    exercise5_sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True)
    exercise5_reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        null=True, blank=True)
    exercise6 = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="exercise6",
        null=True, blank=True)
    exercise6_sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True)
    exercise6_reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        null=True, blank=True)
    exercise7 = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="exercise7",
        null=True, blank=True)
    exercise7_sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True)
    exercise7_reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        null=True, blank=True)
    exercise8 = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="exercise8",
        null=True, blank=True)
    exercise8_sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True)
    exercise8_reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        null=True, blank=True)
    exercise9 = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="exercise9",
        null=True, blank=True)
    exercise9_sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True)
    exercise9_reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        null=True, blank=True)
    exercise10 = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="exercise10",
        null=True, blank=True)
    exercise10_sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True)
    exercise10_reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        null=True, blank=True)
    saves = models.ManyToManyField(
        User, related_name="workout_saves", blank=True)
    completed = models.ManyToManyField(
        User, related_name="workout_completed", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    def number_of_saves(self):
        return self.saves.count()

    def number_of_completed(self):
        return self.completed.count()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLES, default=1)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Comment(models.Model):
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.user}"


class Save(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="saved_workout")
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="saved_workout")
    saved_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-saved_on"]


class Complete(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="completed_workout")
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="completed_workout")
    completed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-completed_on"]
