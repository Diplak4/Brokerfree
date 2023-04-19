# Generated by Django 4.2 on 2023-04-19 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=500)),
                ('time', models.CharField(max_length=50)),
            ],
        ),
    ]
