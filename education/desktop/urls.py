from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import signin, signup, courses, about, blog, blog_detail,element, specified, profile, recommendationCourse, contect


app_name = 'desktop'

urlpatterns = [
    path('signin/', signin, name="signin"),
    path('signup/', signup, name="signup"),
    path('courses/', courses, name="courses"),
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('blog-details/', blog_detail, name="blog_detail"),
    path('element/', element, name="element"),
    path('specified/<str:course_id>', specified, name="specified"),
    path('profile/', profile, name="profile"),
    path('recommendation/', recommendationCourse, name="recommendationCourse"),
    path('contect/', contect, name="contect")

] 


