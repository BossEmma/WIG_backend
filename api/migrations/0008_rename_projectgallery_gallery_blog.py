# Generated by Django 5.0.6 on 2024-06-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_projectgallery_project_project_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectGallery',
            new_name='Gallery',
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
                ('sub_header', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sub Header')),
                ('content', models.CharField(blank=True, max_length=50, null=True, verbose_name='Main Content')),
                ('read_duration', models.CharField(blank=True, max_length=50, null=True, verbose_name='Read Duration')),
                ('post_date', models.CharField(blank=True, max_length=50, null=True, verbose_name='Post Date')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('images', models.ManyToManyField(blank=True, to='api.gallery')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
