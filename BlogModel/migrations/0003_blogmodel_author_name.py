# Generated by Django 5.0.7 on 2024-08-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogModel', '0002_blogmodel_blog_likes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='author_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
