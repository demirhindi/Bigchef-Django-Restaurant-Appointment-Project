# Generated by Django 3.0.14 on 2022-06-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='accepted',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
