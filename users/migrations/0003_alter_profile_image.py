# Generated by Django 4.1.7 on 2023-04-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]
