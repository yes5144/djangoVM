# Generated by Django 2.2.10 on 2020-06-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=32)),
                ('zone', models.CharField(max_length=32)),
                ('version', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(verbose_name='create time')),
                ('update_time', models.DateTimeField(verbose_name='update time')),
            ],
        ),
    ]
