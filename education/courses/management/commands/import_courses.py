import csv
import requests
from django.core.management.base import BaseCommand
from courses.models import Course
import random
import datetime

class Command(BaseCommand):
    help = 'Import courses from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        video_links = [
            'https://youtu.be/nLRL_NcnK-4',
            'https://www.youtube.com/watch?v=XKHEtdqhLK8',
            'http://www.youtube.com/watch?v=rfscVS0vtbw',
            'https://www.youtube.com/watch?v=kqtD5dpn9C8',
            'https://www.youtube.com/watch?v=BGTx91t8q50',
            'https://www.youtube.com/watch?v=xk4_1vDrzzo',
            'https://www.youtube.com/watch?v=eIrMbAQSU34',
            'https://www.youtube.com/watch?v=RRubcjpTkks',
            'https://www.youtube.com/watch?v=A74TOX803D0',
            'https://www.youtube.com/watch?v=-ctjMEIYyiw',
            'https://www.youtube.com/playlist?list=PLWKjhJtqVAbnupwRFOq9zGOWjdvPRtCmO',
            'https://www.youtube.com/watch?v=sdom7zBIfkE',
            'https://www.youtube.com/watch?v=12WMPhSm5rU',
            'https://www.youtube.com/watch?v=xfzGZB4HhEE',
            'https://www.youtube.com/watch?v=pF6QNV5jsGY',
        ]

        # Fetch image URL from Unsplash API
        response = requests.get(
            'https://api.unsplash.com/photos/random/?client_id=ekudPmYouAOqvrVxsvim-MD-I6NqTqKHjX15qfs0YXo&query=courses images coding')
        res_data = response.json()

        course_image_url = res_data['urls']['full']

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Choose a random video link from the list
                random_video_url = random.choice(video_links)
                # Parse the duration string from the CSV file into a timedelta object
                course_duration = int(row['course_duration']) 
                # Create a new Course instance with data from the CSV
                course = Course(
                    course_name=row['course_name'],
                    instructor=row['instructor'],
                    video_url=random_video_url,  # Assuming 'video_url' is a column in your CSV file
                    course_image=course_image_url,
                    course_description=row['course_description'],
                    review_avg=0,
                    review_count=0,
                    course_duration=datetime.timedelta(hours=course_duration),
                    level=row['level'],
                    discount_price=float(row['discount_price']),
                    original_price=float(row['original_price']),
                    student_count=0,
                )
                course.save()

        self.stdout.write(self.style.SUCCESS('Courses imported successfully!'))
