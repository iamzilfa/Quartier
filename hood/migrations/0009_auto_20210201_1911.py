# Generated by Django 3.1.5 on 2021-02-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_remove_neighbourhood_occupants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='profile_pic/'),
        ),
    ]
