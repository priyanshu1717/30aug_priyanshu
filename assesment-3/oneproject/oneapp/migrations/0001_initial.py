# Generated by Django 4.1.7 on 2023-02-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.BigIntegerField(max_length=12)),
                ('state', models.CharField(max_length=10)),
                ('zip', models.IntegerField(max_length=10)),
            ],
        ),
    ]
