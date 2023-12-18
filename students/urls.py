# students/urls.py
from django.urls import path

from . import views
from .views import index, student_list, login, add_course, course_type, course_list, add_student, delete_course_type, \
    edit_course, edit_course_type, create_course_type, student_courses_view, query_student_courses_view, \
    enrollment_view, choose_courses_view, save_choose_courses, delete_course

urlpatterns = [
    path('student_list/', student_list, name='student_list'),
    path('login/', login, name='login'),
    path('add_course/', add_course, name='add_course'),
    path('add_student/', add_student, name='add_student'),
    path('course_type/', course_type, name='course_type'),
    path('course_list/', course_list, name='course_list'),
    path('index/', index, name='index'),
    path('delete_course_type/', delete_course_type, name='delete_course_type'),
    path('delete_course/', delete_course, name='delete_course'),
    path('edit_course/<int:course_no>/', edit_course, name='edit_course'),
    path('edit_course_type/<int:id>/', edit_course_type, name='edit_course_type'),
    path('create_course_type/', create_course_type, name='create_course_type'),
    path('student_courses/<int:student_roll_number>/', student_courses_view, name='student_courses_view'),
    path('query_student_courses/', query_student_courses_view, name='query_student_courses'),
    path('enrollment/', enrollment_view, name='enrollment_view'),
    path('choose_courses_view/',choose_courses_view,name='choose_courses_view'),
    path('save_courses_view/', save_choose_courses, name='save_choose_courses'),
]
