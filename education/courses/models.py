from django.db import models
from ckeditor.fields import RichTextField

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

    def __str__(self):
        return self.course_name