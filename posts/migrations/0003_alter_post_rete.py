# Generated by Django 5.1.5 on 2025-02-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_rete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rete',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
