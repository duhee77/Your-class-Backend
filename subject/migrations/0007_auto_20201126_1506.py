# Generated by Django 3.1 on 2020-11-26 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0006_auto_20201125_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='subjectId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subject.subject'),
        ),
    ]
