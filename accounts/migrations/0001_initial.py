# Generated by Django 3.1.2 on 2020-11-25 10:15

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='프로필 이미지')),
                ('selfpr', models.CharField(blank=True, max_length=100, null=True, verbose_name='자기소개')),
                ('nickname', models.CharField(max_length=20)),
                ('genre_prefer1', models.IntegerField(choices=[(28, '액션'), (12, '모험'), (16, '애니메이션'), (35, '코미디'), (80, '범죄'), (99, '다큐멘터리'), (18, '드라마'), (10751, '가족'), (14, '판타지'), (36, '역사'), (27, '공포'), (10402, '음악'), (9648, '미스터리'), (10749, '로맨스'), (878, 'Sf'), (10770, 'Tv영화'), (53, '스릴러'), (10752, '전쟁'), (37, '서부')], verbose_name='선호장르1 *')),
                ('genre_prefer2', models.IntegerField(choices=[(28, '액션'), (12, '모험'), (16, '애니메이션'), (35, '코미디'), (80, '범죄'), (99, '다큐멘터리'), (18, '드라마'), (10751, '가족'), (14, '판타지'), (36, '역사'), (27, '공포'), (10402, '음악'), (9648, '미스터리'), (10749, '로맨스'), (878, 'Sf'), (10770, 'Tv영화'), (53, '스릴러'), (10752, '전쟁'), (37, '서부')], verbose_name='선호장르2 *')),
                ('genre_prefer3', models.IntegerField(choices=[(28, '액션'), (12, '모험'), (16, '애니메이션'), (35, '코미디'), (80, '범죄'), (99, '다큐멘터리'), (18, '드라마'), (10751, '가족'), (14, '판타지'), (36, '역사'), (27, '공포'), (10402, '음악'), (9648, '미스터리'), (10749, '로맨스'), (878, 'Sf'), (10770, 'Tv영화'), (53, '스릴러'), (10752, '전쟁'), (37, '서부')], verbose_name='선호장르3 *')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserSimilarMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.IntegerField()),
                ('vote_count', models.IntegerField()),
                ('video', models.BooleanField()),
                ('poster_path', models.TextField()),
                ('movie_id', models.IntegerField()),
                ('original_language', models.TextField()),
                ('original_title', models.TextField()),
                ('genre_ids', models.TextField()),
                ('title', models.TextField()),
                ('vote_average', models.IntegerField()),
                ('overview', models.TextField()),
                ('release_date', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFavoriteMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.IntegerField()),
                ('vote_count', models.IntegerField()),
                ('video', models.BooleanField()),
                ('poster_path', models.TextField()),
                ('movie_id', models.IntegerField()),
                ('original_language', models.TextField()),
                ('original_title', models.TextField()),
                ('genre_ids', models.TextField()),
                ('title', models.TextField()),
                ('vote_average', models.IntegerField()),
                ('overview', models.TextField()),
                ('release_date', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
