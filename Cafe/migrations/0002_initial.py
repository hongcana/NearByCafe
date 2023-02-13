# Generated by Django 4.1.6 on 2023-02-10 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Review", "0001_initial"),
        ("Cafe", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cafelike",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="cafekeyword",
            name="cafe_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cafe_cafe",
                to="Cafe.cafe",
            ),
        ),
        migrations.AddField(
            model_name="cafekeyword",
            name="review_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cafe_review",
                to="Review.review",
            ),
        ),
        migrations.AddField(
            model_name="cafe",
            name="location_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="Cafe.location",
            ),
        ),
    ]
