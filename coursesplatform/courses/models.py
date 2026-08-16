from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    instructor=models.ForeignKey('instructor', on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title
    
     
    
class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    is_complete =models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title}"
    
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name        