# Generated by Django 4.0.2 on 2022-02-01 18:41

import app.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', djongo.models.fields.EmbeddedField(model_container=app.models.Author)),
            ],
        ),
    ]
