from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from .models import Students
from courses.models import Course
from django.http import Http404
import pickle
import pandas as pd
# Create your views here.


def index(request):
    obj = Course.objects.all()
    template_name = 'index.html'
    context = {
        'obj': obj,
    }
    return render(request,  template_name, context)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('desktop:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('desktop:signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # Log user in and redirect to setting page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Students.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('/')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('desktop:signup')
    else:
        template_name = "register.html"
        return render(request, template_name)
    

def signin(request):
    if request.method == 'POST':
        print('yes')
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)

        if user is not None:
            auth.login(request, user)
            print('done')
            return redirect('/')
        else:
            messages.info(request, 'Crdentials Invaild')
            print('invalid')
            return redirect('desktop:signin')

    else:
        return render(request, "login.html")


def courses(request):
    obj = Course.objects.all()
    context = {
        'obj': obj,
    }
    template_name = "courses.html"
    return render(request, template_name, context)

def about(request):
    template_name = "about.html"
    return render(request, template_name)

def blog(request):
    template_name = "blog.html"
    return render(request, template_name)
    
def blog_detail(request):
    template_name = "blog_details.html"
    return render(request, template_name)

def element(request):
    template_name = "elements.html"
    return render(request, template_name)

def specified(request, course_id):
    course = Course.objects.filter(course_id=course_id)
    template_name = "python.html"
    context={
        'course':course,
    } 
    return render(request, template_name, context)


def profile(request):
    username = request.user
    print(username)
    try:
        person = Students.objects.get(user=username)
    except Students.DoesNotExist:
        raise Http404("Student does not exist")

    template_name = "profile.html"
    print(person)
    
    context = {
        'person': person,
    }
    return render(request, template_name, context)



def recommendationCourse(request):
    if request.method == 'POST':
        course_dict = pickle.load(open("D:/educational_website/education/desktop/recommandation/df.pkl", "rb"))
        similarity = pickle.load(open("D:/educational_website/education/desktop/recommandation/similarity.pkl", "rb"))
        courses = pd.DataFrame(course_dict)

        course_name = request.POST.get('course')
        print(course_name)
        
        if course_name in courses['clean_course_title'].values:
            course_index = courses[courses['clean_course_title'] == course_name].index[0]
            print('yes')
            print(course_index)
            distance = similarity[course_index]
            print(distance)
            course_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_course = []
            for i in course_list:
                recommended_course.append(courses.iloc[i[0]]['clean_course_title'])

            recommended_course

            return render(request, 'recommendation.html', {'recommended_courses': recommended_course})
        else:
            return render(request, 'recommendation.html', {'error_message': 'Course not found'})
    else:
        return render(request, 'recommendation.html', {'error_message': 'Invalid request method'})


def contect(request):
    template_name = "contact.html"
    return render(request, template_name)