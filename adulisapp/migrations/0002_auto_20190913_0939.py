# Generated by Django 2.2.4 on 2019-09-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adulisapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
