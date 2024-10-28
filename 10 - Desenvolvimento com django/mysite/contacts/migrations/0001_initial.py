# Generated by Django 5.0 on 2024-10-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=250)),
                ('sender', models.EmailField(max_length=254)),
                ('cc_myself', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
