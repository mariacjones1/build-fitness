# Generated by Django 3.2.20 on 2023-08-15 15:05

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_alter_exercise_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('running', 'Running'), ('full body', 'Full Body'), ('upper body', 'Upper Body'), ('lower body', 'Lower Body'), ('mobility', 'Mobility')], max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise10_reps',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise10_sets',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise1_reps',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise1_sets',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise2_reps',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise2_sets',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise3_reps',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise3_sets',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise4_reps',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise4_sets',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise5_reps',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise5_sets',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise6_reps',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise6_sets',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise7_reps',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise7_sets',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise8_reps',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise8_sets',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise9_reps',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise9_sets',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
