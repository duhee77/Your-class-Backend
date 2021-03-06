# Generated by Django 3.1 on 2020-11-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subjectClass',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='subjectGrade',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='invitationCode',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
    ]
