# Generated by Django 3.2.6 on 2021-10-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_blog_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(blank=True, max_length=100000, null=True),
        ),
    ]
