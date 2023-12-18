# Generated by Django 4.2.7 on 2023-12-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_roll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_type',
            name='type_name',
            field=models.CharField(max_length=255, verbose_name='课程类型'),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.CharField(max_length=255, verbose_name='班级'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('1', '男'), ('2', '女')], max_length=1, verbose_name='性别'),
        ),
    ]