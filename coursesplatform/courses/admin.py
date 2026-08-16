from django.contrib import admin
from .models import Course, Instructor, Enrollment

admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Enrollment)