# Generated by Django 4.0.1 on 2022-02-01 15:40

from django.db import migrations
import users.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', users.manager.CustomUserManager()),
            ],
        ),
    ]