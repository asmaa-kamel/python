from django import forms
from . models import Course, Enrollment

class course_form(forms.ModelForm):
    class Meta:
        model =Course
        fields =['title','description','price','instructor']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = []    
        
class EnrollmentEditForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['is_complete']        