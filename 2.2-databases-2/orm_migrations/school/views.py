from django.shortcuts import render
from school.models import Student

def students_list(request):
    context = {
        'object_list': Student.objects.all().order_by("group").prefetch_related('teachers')
    }
    return render(request, 'students_list.html', context)