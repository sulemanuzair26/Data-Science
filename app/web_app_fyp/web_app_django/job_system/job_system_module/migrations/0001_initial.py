# Generated by Django 3.0.3 on 2020-04-14 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('window_id', models.IntegerField()),
                ('title', models.CharField(max_length=5000)),
                ('description', models.CharField(max_length=5000)),
                ('requirement', models.CharField(max_length=5000)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip5', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('title_original', models.CharField(max_length=5000)),
                ('description_original', models.CharField(max_length=5000)),
                ('requirements_original', models.CharField(max_length=5000)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('window_id', models.IntegerField()),
                ('split', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('degree_type', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=5000)),
                ('graduation_date', models.DateTimeField()),
                ('work_history_count', models.IntegerField()),
                ('total_years_experience', models.FloatField()),
                ('currently_employed', models.BooleanField()),
                ('managed_others', models.BooleanField()),
                ('managed_how_many', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('window_id', models.IntegerField()),
                ('split', models.CharField(max_length=20)),
                ('sequence', models.IntegerField()),
                ('job_title', models.CharField(max_length=5000)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_system_module.User')),
            ],
            options={
                'db_table': 'user_histories',
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('window_id', models.IntegerField()),
                ('split', models.CharField(max_length=20)),
                ('application_date', models.DateTimeField()),
                ('job_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_system_module.Job')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_system_module.User')),
            ],
            options={
                'db_table': 'job_applications',
            },
        ),
    ]
