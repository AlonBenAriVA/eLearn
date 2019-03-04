# Generated by Django 2.0 on 2019-02-22 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadDiscussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_content', models.CharField(max_length=150)),
                ('last_updated', models.DateTimeField()),
                ('discussed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('video_file', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VidTopics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, unique=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('starter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL)),
                ('vids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='learn.Vids')),
            ],
        ),
        migrations.AddField(
            model_name='threaddiscussion',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjetcs', to='learn.VidTopics'),
        ),
    ]