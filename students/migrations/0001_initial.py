# Generated by Django 4.2.7 on 2023-12-06 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_no', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='课程编号')),
                ('course_name', models.CharField(max_length=255, verbose_name='课程名称')),
                ('course_hours', models.IntegerField(verbose_name='课程学时')),
                ('type_id', models.IntegerField(verbose_name='类型')),
                ('course_status', models.CharField(max_length=20, verbose_name='课程状态')),
                ('course_reqs', models.CharField(blank=True, max_length=20, null=True, verbose_name='需求')),
                ('course_point', models.FloatField(verbose_name='课程学分')),
                ('course_memo', models.TextField(blank=True, null=True, verbose_name='课程备注')),
                ('course_textbook_pic', models.URLField(blank=True, null=True, verbose_name='课程图片URL')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Course_Type',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'students_course_type',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_number', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'students_user',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], max_length=1)),
                ('class_name', models.CharField(max_length=255)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_enrollments', to='students.student', verbose_name='学生')),
            ],
            options={
                'db_table': 'students_student',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('enrollment_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='选课编号')),
                ('enrollment_date', models.DateField(auto_now_add=True, verbose_name='选课日期')),
                ('course_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='students.course', verbose_name='课程')),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='students.student', verbose_name='学生')),
            ],
            options={
                'db_table': 'enrollment',
                'unique_together': {('roll_number', 'course_no')},
            },
        ),
    ]