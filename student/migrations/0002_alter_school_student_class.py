# Generated by Django 4.0 on 2022-01-03 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CLASS', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='student_class',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CLASS.class_detail'),
        ),
    ]
