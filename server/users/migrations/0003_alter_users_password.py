# Generated by Django 4.1.4 on 2023-04-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(default='somevalue', max_length=20),
        ),
    ]
