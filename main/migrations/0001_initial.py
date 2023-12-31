# Generated by Django 4.2.4 on 2023-09-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(blank=True, choices=[('B', 'BREAKFAST'), ('L', 'LAUNCH'), ('DI', 'DINNER'), ('DR', 'DRINK')], max_length=2)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/menu')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialChef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MasterChef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='uploads/chefs_images')),
                ('details', models.TextField()),
                ('designation', models.DateField(default='2000-1-1')),
                ('social', models.ManyToManyField(related_name='social', to='main.socialchef')),
            ],
        ),
    ]
