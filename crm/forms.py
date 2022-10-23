from django import forms
from .models import Student, Event, Club

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ( 'student_name', 'email', 'phone', 'city', 'state','nu_id','role')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ( 'event_name', 'event_category', 'description', 'location', 'event_date','event_time')

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ( 'club_name', 'club_role', 'club_category', 'club_description', 'created_date')
