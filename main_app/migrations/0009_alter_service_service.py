# Generated by Django 4.1 on 2022-11-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_service_myservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'medicine'), (1, 'grocery'), (2, 'electronics'), (3, 'foods'), (4, 'drinks')], null=True),
        ),
    ]