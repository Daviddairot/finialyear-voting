# Generated by Django 5.0.6 on 2024-06-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuapp', '0002_clique_of_the_year_entrepreneur_of_the_year_female_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
