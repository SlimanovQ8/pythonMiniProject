# Generated by Django 4.0.6 on 2022-07-28 23:42

from django.db import migrations, models
import event_planner.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100, validators=[event_planner.models.NameValidation])),
                ('email', models.CharField(max_length=254, validators=[event_planner.models.EmailValidation])),
                ('image', models.TextField(max_length=1000)),
                ('num_of_seats', models.PositiveIntegerField(validators=[event_planner.models.SeatsMinimumNumberValidation])),
                ('booked_seats', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateField(validators=[event_planner.models.isDateAfterToday])),
                ('end_date', models.DateField()),
            ],
        ),
    ]
