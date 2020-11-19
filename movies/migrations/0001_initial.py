# Generated by Django 3.1.2 on 2020-11-19 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.IntegerField()),
                ('vote_count', models.IntegerField()),
                ('video', models.BooleanField()),
                ('poster_path', models.TextField()),
                ('original_language', models.TextField()),
                ('original_title', models.TextField()),
                ('genre_ids', models.TextField()),
                ('title', models.TextField()),
                ('vote_average', models.IntegerField()),
                ('overview', models.TextField()),
                ('release_date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.TextField()),
                ('rank_average', models.IntegerField()),
                ('rank', models.IntegerField(choices=[(5, 'Best'), (4, 'Good'), (3, 'Normal'), (2, 'Bad'), (1, 'Worst')])),
            ],
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
