# Generated by Django 4.2.4 on 2023-09-05 14:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.EmailValidator(message='Invalid email address.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(limit_value=5, message='Name must be at least 5 characters long.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(limit_value=8, message='Password must be at least 8 characters long.'), django.core.validators.RegexValidator(message='Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character.', regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@#$%^&+=!]).*$')]),
        ),
    ]