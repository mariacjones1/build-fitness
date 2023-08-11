from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


CATEGORIES = [
        ("running", "Running"),
        ("full body", "Full Body"),
        ("upper body", "Upper Body"),
        ("lower body", "Lower Body"),
        ("mobility", "Mobility"),
    ]


ROLES = [
    (0, "admin"),
    (1, "standard"),
]


class Exercise(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    sets = models.IntegerField()
    reps = models.IntegerField()

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
    category = models.CharField(
        max_length=50, choices=CATEGORIES, default="full body")
    image = CloudinaryField("image", default="placeholder")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    exercises = models.ManyToManyField(Exercise)
    saves = models.ManyToManyField(
        User, related_name="workout_saves", blank=True)
    completed = models.ManyToManyField(
        User, related_name="workout_completed", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()

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
    instance.profile.save()


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
