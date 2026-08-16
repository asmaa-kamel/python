from .models import Course, Instructor ,Enrollment
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .forms import course_form , EnrollmentForm, EnrollmentEditForm


# Create your views here.
def view_all_courses(request, pk=None):
    if pk is not None:
        courses = get_object_or_404(Course, pk=pk)
    else:
        courses = Course.objects.all()
    return render(request, 'courses/view_courses.html', {'courses': courses})


def view_course_detail(request, course_id):
    course= Course.objects.get(id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def search_courses(request):
    query =request.GET.get('q')
    if query:
        courses = Course.objects.filter(title__icontains=query)
    else:
        courses = Course.objects.none()    
    return render(request, 'courses/search_courses.html', {'courses': courses, 'query': query})



def filter_by_instructor(request):
    instructor_id = request.GET.get('category')
    instructors = Instructor.objects.all()

    if instructor_id:
        courses = Course.objects.filter(instructor__id=instructor_id)
    else:
        courses = Course.objects.all()

    return render(request, 'courses/instructor_courses.html', {
        'courses': courses,
        'instructors': instructors,
        'instructor_id': instructor_id,
    })


@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = request.user.student

    already_enrolled = Enrollment.objects.filter(course=course, student=student).exists()

    if already_enrolled:
        return render(request, 'courses/enroll_form.html', {
            'course': course,
            'already_enrolled': True,
        })

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.course = course
            enrollment.student = student
            enrollment.save()
            return redirect('view_all_courses')
    else:
        form = EnrollmentForm()

    return render(request, 'courses/enroll_form.html', {
        'form': form,
        'course': course,
    })
    

###forms 
@login_required
def edit_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id, student=request.user.student)

    if request.method == 'POST':
        form = EnrollmentEditForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EnrollmentEditForm(instance=enrollment)

    return render(request, 'courses/enrollment_edit_form.html', {
        'form': form,
        'enrollment': enrollment,
    })
    

@login_required
def remove_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('view_courses')
    return render(request, 'courses/confirm_delete.html', {'course': course}) 

@login_required
def remove_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id, student=request.user.student)

    if request.method == 'POST':
        enrollment.delete()
        return redirect('profile')

    return render(request, 'courses/confirm_delete.html', {'enrollment': enrollment}) 
    