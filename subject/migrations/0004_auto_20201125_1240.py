# Generated by Django 3.1 on 2020-11-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_enroll_waitinglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='invitationCode',
            field=models.CharField(max_length=16, null=True),
        ),
    ]