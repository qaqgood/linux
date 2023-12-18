# forms.py
from django import forms
from .models import Course, Course_Type
from .models import Student
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_hours', 'type_id', 'course_status', 'course_reqs', 'course_point', 'course_memo', 'course_textbook_pic']
        # 添加一个隐藏的课程编号字段
        course_no = forms.IntegerField(widget=forms.HiddenInput())


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'age', 'sex', 'class_name']


class CourseTypeForm(forms.ModelForm):
    class Meta:
        model = Course_Type
        fields = ['type_name']
