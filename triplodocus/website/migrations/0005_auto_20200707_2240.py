# Generated by Django 3.0.7 on 2020-07-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200707_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='son',
            name='realisation',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='son',
            name='resume',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='son',
            name='youtube',
            field=models.URLField(blank=True),
        ),
    ]
