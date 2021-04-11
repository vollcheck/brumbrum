# Generated by Django 3.2 on 2021-04-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_cars_and_rating_models"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="avg_rating",
            field=models.FloatField(
                blank=True, null=True, verbose_name="average rating"
            ),
        ),
    ]