from django.db import models
from django.conf import settings
from django.db.models import Q
from ckeditor.fields import RichTextField

User = settings.AUTH_USER_MODEL

class CourseQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(course_image__icontains=query) |
            Q(course_description__icontains=query) |
            Q(instructor__icontains=query) 
        )
        return self.filter(lookup)

class CourseManager(models.Manager):
    def get_queryset(self):
        return CourseQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    video_url = models.URLField()
    course_image = models.URLField()
    course_description = RichTextField()
    review_avg = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    review_count = models.PositiveIntegerField(default=0)
    course_duration = models.DurationField()
    LEVEL_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('All', 'All')
    )
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    student_count = models.PositiveIntegerField(default=0)

    objects = CourseManager()

    def __str__(self):
        return self.course_name
    
