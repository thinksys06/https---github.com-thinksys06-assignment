# Generated by Django 4.0 on 2022-01-03 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_school_student_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='student_class',
            field=models.IntegerField(),
        ),
    ]