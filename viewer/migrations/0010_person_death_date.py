# Generated by Django 4.2.7 on 2023-12-05 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0009_person_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='death_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]