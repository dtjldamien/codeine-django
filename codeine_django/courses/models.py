from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError

import uuid


def image_directory_path(instance, filename):
    return 'course_{0}/image_{1}'.format(instance.id, filename)
# end def

def zipfile_directory_path(instance, filename):
    return 'course_{0}/{1}'.format(instance.id, filename)
# end def

def validate_rating(value):
    if (value < 1 or value > 5):
        raise ValidationError(_('%(value)s is not a valid rating'), params={'value': value})
    # end if
# end def



class Course(models.Model):
    CODING_LANGUAGES = (
        ('PY', 'Python'),
        ('JAVA', 'Java'),
        ('JS', 'Javascript'),
        ('CPP', 'C++'),
        ('CS', 'C#'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('RUBY', 'Ruby'),
    )

    LANGUAGES = (
        ('ENG', 'English'),
        ('MAN', 'Mandarin'),
        ('FRE', 'French'),
    )

    CATEGORIES = (
        ('SEC', 'Security'),
        ('DB', 'Database Administration'),
        ('FE', 'Frontend'),
        ('BE', 'Backend'),
        ('UI', 'UI/UX'),
        ('ML', 'Machine Learning'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    learning_objectives = models.JSONField()  # list of objectives
    requirements = models.JSONField()  # list of requirements
    description = models.TextField()
    introduction_video_url = models.CharField(max_length=255)
    github_repo = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to=image_directory_path, max_length=100, null=True, default=None)
    views = models.PositiveIntegerField()

    # enums
    coding_languages = MultiSelectField(choices=CODING_LANGUAGES)
    languages = MultiSelectField(choices=LANGUAGES)
    categories = MultiSelectField(choices=CATEGORIES)

    # publishing details
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, default=None, blank=True)

    # availability 
    is_available = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    # price in cents
    price = models.PositiveIntegerField()

    # cert in html
    certificate = models.TextField(null=True, default=None, blank=True)

    # provider ref
    content_provider = models.ForeignKey('common.ContentProvider', on_delete=models.SET_NULL, related_name='courses', null=True)
# end class

class Chapter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField(null=True, default='')

    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='chapters')
# end class

class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, default='', blank=True)
    video_url = models.CharField(max_length=255)
    google_drive_link = models.CharField(max_length=255)
    
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name='sections')
# end class

class Enrollment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2)

    # ref for course
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, related_name='enrollments')

    # ref for member
    member = models.ForeignKey('common.Member', on_delete=models.CASCADE, related_name='enrollments')
# end class

class CourseReview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    rating = models.PositiveSmallIntegerField(validators=[validate_rating])
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # ref for course
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, related_name='course_reviews')

    # ref for member
    member = models.ForeignKey('common.Member', on_delete=models.CASCADE, related_name='course_reviews')
# end class

