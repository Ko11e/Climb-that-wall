# Generated by Django 5.0.6 on 2024-08-06 12:28

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climb_gyms', '0005_alter_climbinggyms_maps_alter_climbinggyms_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='headimage',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', help_text='This will be the front image of the climbing gym', keep_meta=True, quality=75, scale=None, size=[600, 300], upload_to='climbing-gyms/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 300], upload_to='climbing-gyms/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 300], upload_to='climbing-gyms/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 300], upload_to='climbing-gyms/'),
        ),
    ]
