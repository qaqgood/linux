
from django.db import models

class User(models.Model):
    user_number = models.CharField(max_length=20)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    class Meta:
        db_table = 'students_user'
    def __str__(self):
        return self.user_number
class Course_Type(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_name = models.CharField(max_length=255,verbose_name='课程类型')
    class Meta:
        db_table = 'students_course_type'
    def __str__(self):
        return self.id
class Course(models.Model):
    course_no = models.AutoField(primary_key=True,verbose_name='课程编号',unique=True)
    course_name = models.CharField(max_length=255, verbose_name='课程名称')
    course_hours = models.IntegerField(verbose_name='课程学时')
    type_id = models.IntegerField(verbose_name='类型')
    course_status = models.CharField(max_length=20, verbose_name='课程状态')
    course_reqs = models.CharField(max_length=20, blank=True, null=True, verbose_name='需求')
    course_point = models.FloatField(verbose_name='课程学分')
    course_memo = models.TextField(blank=True, null=True, verbose_name='课程备注')
    course_textbook_pic = models.URLField(blank=True, null=True, verbose_name='课程图片URL')
    class Meta:
        db_table = 'course'
    def __str__(self):
        return f"{self.course_no}"

class Student(models.Model):
    GENDER_CHOICES = {
        "1": "男",
        "2": "女",
        # 可以根据需要添加其他性别选项
    }

    class Meta:
        db_table = 'students_student'

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='名字')
    roll_number = models.CharField(max_length=20, unique=True, null=True, verbose_name='学号')
    age = models.IntegerField(verbose_name='年龄')
    sex = models.CharField(max_length=1, choices=[("1", "男"), ("2", "女")], verbose_name='性别')
    class_name = models.CharField(max_length=255, verbose_name='班级')

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True, verbose_name='选课编号', unique=True)
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments', verbose_name='学生')
    course_no = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments', verbose_name='课程')
    enrollment_date = models.DateField(auto_now_add=True, verbose_name='选课日期')
    class Meta:
        unique_together = ('roll_number', 'course_no')
        db_table = 'enrollment'
    def __str__(self):
        return f"Enrollment ID: {self.enrollment_id}, Student: {self.roll_number.name}, Course: {self.course_no.course_name}"
