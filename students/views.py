from django.contrib.auth.decorators import login_required
from django.db import models

# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import Student, User, Course_Type, Course, Enrollment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CourseForm, StudentForm, CourseTypeForm
from django.http import HttpResponse, JsonResponse
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        usernumber = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(user_number=usernumber).first()
        if user and user.user_password == password:
            return redirect('index')
        else:
            return render(request, 'students/login.html')
    else:
        return render(request, 'students/login.html')

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '课程添加成功！')  # 添加成功消息
            return redirect('add_course')
    else:
        form = CourseForm()
    response = render(request, 'students/add_course.html', {'form': form})
    response['X-Frame-Options'] = 'ALLOWALL'
    return response

@csrf_protect
def delete_course(request):
    if request.method == 'POST':
        course_no = request.POST.get('course_no')
        # 执行删除逻辑
        try:
            course = Course.objects.get(course_no=course_no)
            course.delete()
            return JsonResponse({'message': 'Course deleted successfully'})
        except Course.DoesNotExist:
            return JsonResponse({'message': 'Course not found'}, status=404)
    return JsonResponse({'message': 'Invalid request method'}, status=400)

def edit_course(request, course_no):
    course = get_object_or_404(Course, course_no=course_no)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'students/edit_course.html', {'form': form, 'course': course})


def course_list(request):
    query = request.GET.get('query', '')
    courses = Course.objects.all()
    if query:
        courses = Course.objects.filter(course_name__icontains=query)
    # 分页处理
    paginated_courses = paginator(request, courses)
    response = render(request, 'students/course_list.html', {'courses': paginated_courses, 'query': query})

    response['X-Frame-Options'] = 'ALLOWALL'

    return response

def student_list(request):
    query = request.GET.get('query', '')
    students = Student.objects.all()
    if query:
        students = Student.objects.filter( name__icontains=query)

    paginated_students = paginator(request, students)
    # 创建 HttpResponse 对象
    response = render(request, 'students/student_list.html', {'students': paginated_students})
    # 设置 X-Frame-Options 头为 'ALLOWALL'
    response['X-Frame-Options'] = 'ALLOWALL'
    return response




def course_type(request):
    courses = Course_Type.objects.all()
    paginated_courses = paginator(request, courses)
    # 创建 HttpResponse 对 象
    response = render(request, 'students/course_type.html', {'courses': paginated_courses})
    # 设置 X-Frame-Options 头为 'ALLOWALL'
    response['X-Frame-Options'] = 'ALLOWALL'
    return response


def paginator(request, data):
    per_page = 3
    paginator = Paginator(data, per_page)
    page = request.GET.get('page')
    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        paginated_data = paginator.page(1)
    except EmptyPage:
        paginated_data = paginator.page(paginator.num_pages)
    return paginated_data




@csrf_protect
def delete_course_type(request):
    if request.method == 'POST':
        course_type_id = request.POST.get('course_type_id')
        # 执行删除逻辑
        try:
            course_type = Course_Type.objects.get(id=course_type_id)
            course_type.delete()
            return JsonResponse({'message': 'Course type deleted successfully'})
        except Course_Type.DoesNotExist:
            return JsonResponse({'message': 'Course type not found'}, status=404)
    return JsonResponse({'message': 'Invalid request method'}, status=400)


def edit_course_type(request, id):
    course_type = get_object_or_404(Course_Type, id=id)
    if request.method == 'POST':
        form = CourseTypeForm(request.POST, instance=course_type)
        if form.is_valid():
            form.save()
            return redirect('course_type')
    else:

        form = CourseTypeForm(instance=course_type)

    return render(request, 'students/edit_course_type.html', {'form': form, 'course_type': course_type})

def create_course_type(request):
    if request.method == 'POST':
        form = CourseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_type')
    else:
        form = CourseTypeForm()

    return render(request, 'students/create_course_type.html', {'form': form})


def query_student_courses_view(request):

    if request.method == 'POST':
        student_roll_number = request.POST.get('student_roll_number')
        student = get_object_or_404(Student, roll_number=student_roll_number)
        return redirect('student_courses_view', student_roll_number=student.roll_number)
    else:
        return redirect('enrollment_view')


def student_courses_view(request,student_roll_number):
    student = get_object_or_404(Student, roll_number=int(student_roll_number))
    print(student.roll_number)
    enrollments = Enrollment.objects.filter(roll_number_id=student.roll_number)
    courses=[]
    for enrollment in enrollments:
        course_no_id = enrollment.course_no_id
        course = Course.objects.get(course_no=course_no_id)
        courses.append(course)

    contexts = {'student': student, 'enrollments': enrollments, 'course': courses}
    return render(request, 'students/student_courses.html',contexts)


def choose_courses_view(request):
    if request.method == 'POST':
        student_roll_number = request.POST.get('student_roll_number')
        student = get_object_or_404(Student, roll_number=student_roll_number)
        enrollments = Enrollment.objects.filter(roll_number_id=student.roll_number)
        courses = Course.objects.filter(course_status='开课')
        context = {'student': student, 'enrollments': enrollments, 'courses': courses}
        return render(request, 'students/choose_courses.html', context)

@csrf_exempt
def save_choose_courses(request):
    if request.method == 'POST':
        student_roll_number = request.POST.get('student_roll_number')
        course_no = request.POST.get('course_no')
        student = get_object_or_404(Student, roll_number=student_roll_number)
        course = get_object_or_404(Course, course_no=course_no)

        if Enrollment.objects.filter(roll_number=student.roll_number, course_no_id=course.course_no).exists():
            return JsonResponse({'message': '学生已选择该课程'})
        # 创建新的选课记录
        else:
            try:
                enrollment = Enrollment.objects.create(roll_number_id=student.roll_number, course_no_id=course.course_no)
                if enrollment.course_no_id==course.course_no:

                    return JsonResponse({'message': '选课成功'})
            except:
                  print("no")
    return JsonResponse({'message': '无效的请求'})




def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # 重定向到学生列表页面
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})

def enrollment_view(request):
    return render(request ,'students/enrollment.html')

def index(request):
    return render(request,'students/index.html')