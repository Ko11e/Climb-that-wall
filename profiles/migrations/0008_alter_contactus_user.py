# Generated by Django 5.0.6 on 2024-08-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='user',
            field=models.CharField(default='Nonregistered User', max_length=75),
        ),
    ]
