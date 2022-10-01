# Generated by Django 3.2.15 on 2022-10-01 01:59

from django.db import migrations, models

from ara.setup import ara_version

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='playbook',
            name='client_version',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='playbook',
            name='server_version',
            field=models.CharField(default=ara_version, max_length=255),
        ),
        migrations.AddField(
            model_name='playbook',
            name='python_version',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
