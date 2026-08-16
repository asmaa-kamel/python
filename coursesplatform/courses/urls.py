from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_all_courses, name='view_all_courses'),
    path('course/<int:course_id>', views.view_course_detail, name='view_course_detail'),
    path('search/',views.search_courses , name='search_courses'),
    path('filter/',views.filter_by_instructor, name='filter_by_instructor'),
    path('enroll/<int:course_id>',views.enroll, name='enroll'),
    path('enrollment/<int:enrollment_id>/edit/', views.edit_enrollment, name='edit_enrollment'),
    path('remove/<int:course_id>',views.remove_course, name='remove_course'),
    path('enrollment/<int:enrollment_id>/remove/', views.remove_enrollment, name='remove_enrollment'),
]
