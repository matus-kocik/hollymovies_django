# Generated by Django 4.2.7 on 2023-11-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_comment_user_movie_actors_movie_directors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_cz',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_sk',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
