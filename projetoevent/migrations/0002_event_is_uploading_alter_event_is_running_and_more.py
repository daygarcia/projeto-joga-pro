# Generated by Django 4.0.3 on 2022-08-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoevent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_uploading',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_running',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ticketlog',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]