# Generated by Django 3.1 on 2020-11-25 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0004_auto_20201125_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waitinglist',
            name='subjectId',
        ),
        migrations.AddField(
            model_name='subject',
            name='waitingList',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subject.waitinglist'),
        ),
    ]
