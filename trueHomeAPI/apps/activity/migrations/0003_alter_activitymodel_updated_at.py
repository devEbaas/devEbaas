# Generated by Django 4.0.1 on 2022-01-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_alter_activitymodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitymodel',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
