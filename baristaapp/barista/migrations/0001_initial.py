# Generated by Django 4.2.7 on 2023-11-13 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('source_name', models.CharField(max_length=100, unique=True)),
                ('metadata', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Beans',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('bean_name', models.CharField(max_length=100, unique=True)),
                ('ideal_prep', models.JSONField()),
                ('source_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barista.source')),
            ],
        ),
    ]
