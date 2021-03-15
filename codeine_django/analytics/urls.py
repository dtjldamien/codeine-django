from django.urls import path

from . import views

urlpatterns = [
    # analytics views
    path('', views.post_log_view, name='Create Event Log'),
    path('/course-conversion-rate', views.course_conversion_rate_view, name='Course conversion metrics'),
    path('/course-material-time', views.course_material_average_time_view, name='Course material time metrics'),
]
