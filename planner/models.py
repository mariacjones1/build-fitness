from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField
from colorfield.fields import ColorField
from cloudinary.models import CloudinaryField

ROLES = [
    (0, "admin"),
    (1, "standard"),
]


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    image = CloudinaryField("image", default="placeholder")
    color = ColorField(default="#FFFFFF")
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Workout(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="workouts")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = CloudinaryField("image", default="placeholder")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
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


class Exercise(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    sets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True)
    reps = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        null=True, blank=True)
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="exercises", null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


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
