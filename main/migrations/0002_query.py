# Generated by Django 4.2.4 on 2023-09-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=80)),
                ('message', models.TextField()),
            ],
        ),
    ]
