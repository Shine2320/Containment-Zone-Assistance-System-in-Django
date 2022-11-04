# Generated by Django 4.1 on 2022-10-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_user_condition_alter_user_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='condition',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'no covid'), (0, 'covid')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'pending'), (1, 'accepted'), (2, 'rejected')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'customer'), (1, 'staff'), (2, 'provider')], max_length=100, null=True),
        ),
    ]
