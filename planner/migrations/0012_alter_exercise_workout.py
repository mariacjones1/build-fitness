# Generated by Django 3.2.20 on 2023-08-19 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0011_auto_20230819_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='planner.workout'),
        ),
    ]
