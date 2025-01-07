# Generated by Django 5.1.4 on 2025-01-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='dob',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=10),
        ),
    ]
