# Generated by Django 3.0.7 on 2020-07-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200724_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='son',
            name='deezer',
            field=models.URLField(default=False),
        ),
        migrations.AlterField(
            model_name='son',
            name='realisation',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='son',
            name='resume',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='son',
            name='spotify',
            field=models.URLField(default=False),
        ),
        migrations.AlterField(
            model_name='son',
            name='youtube',
            field=models.URLField(default=False),
        ),
    ]
