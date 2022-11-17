from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from .forms import UserRegistrationForm



now = timezone.now()

def register(request):
    if request.method == 'POST':
        student_form = UserRegistrationForm(request.POST)
        if student_form.is_valid():
            new_user = student_form.save(commit=False)
            new_user.set_password(student_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        student_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'student_form': student_form})


def home(request):
    return render(request, 'crm/home.html',
                  {'crm': home})

@login_required
def student_list(request):
    student = Student.objects.filter()
    return render(request, 'crm/student_list.html',
                  {'students': student})

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        # update
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.updated_date = timezone.now()
            student.save()
            student = Student.objects.filter()
            return render(request, 'crm/student_list.html',
                          {'students': student})
    else:
        # edit
        form = StudentForm(instance=student)
    return render(request, 'crm/student_edit.html', {'form': form})
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('crm:student_list')
@login_required
def event_list(request):
    event = Event.objects.filter()
    return render(request, 'crm/event_list.html',
                  {'events': event})

@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        # update
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.updated_date = timezone.now()
            event.save()
            event = Event.objects.filter()
            return render(request, 'crm/event_list.html',
                          {'events': event})
    else:
        # edit
        form = EventForm(instance=event)
    return render(request, 'crm/event_edit.html', {'form': form})
@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('crm:event_list')




@login_required
def club_list(request):
    club = Club.objects.filter()
    return render(request, 'crm/club_list.html',
                  {'clubs': club})

@login_required
def club_edit(request, pk):
    club = get_object_or_404(Club, pk=pk)
    if request.method == "POST":
        # update
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            club = form.save(commit=False)
            club.updated_date = timezone.now()
            club.save()
            club = Club.objects.filter()
            return render(request, 'crm/club_list.html',
                          {'clubs': club})
    else:
        # edit
        form = ClubForm(instance=club)
    return render(request, 'crm/club_edit.html', {'form': form})
@login_required
def club_delete(request, pk):
    club = get_object_or_404(Club, pk=pk)
    club.delete()
    return redirect('crm:club_list')


