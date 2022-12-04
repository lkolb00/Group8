from django.contrib import admin
from .models import Student, Event, Club

#Define the admin options for the Customer table
class StudentList(admin.ModelAdmin):
    list_display = ( 'student_name', 'phone' )
    list_filter = ( 'student_name',)
    search_fields = ('student_name', )
    ordering = ['student_name']

#Define the admin options for the Service table
class EventList(admin.ModelAdmin):
    list_display = ( 'event_name', 'event_category', 'event_date')
    list_filter = ( 'event_name', 'event_date')
    search_fields = ('event_description','event_name', )
    ordering = ['event_name']

#Define the admin options for the Product table
class ClubList(admin.ModelAdmin):
    list_display = ( 'club_name', 'club_category')
    list_filter = ('club_name', 'club_category')
    search_fields = ('club_name', 'club_category')
    ordering = ['club_name']


admin.site.register(Student, StudentList)
admin.site.register(Event, EventList)
admin.site.register(Club, ClubList)
