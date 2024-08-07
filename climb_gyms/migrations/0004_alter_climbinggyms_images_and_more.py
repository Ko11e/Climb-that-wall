# Generated by Django 5.0.6 on 2024-08-02 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climb_gyms', '0003_alter_comments_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climbinggyms',
            name='images',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='climb_gyms.images'),
        ),
        migrations.AlterField(
            model_name='climbinggyms',
            name='socialmedia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='socialmedia', to='climb_gyms.socialmedia'),
        ),
    ]
