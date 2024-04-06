from django.contrib import admin
from school.models import Student, Teacher, TeacherStudent

class TeacherStudentInLine(admin.TabularInline):
    model = TeacherStudent
    extra = 0

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [TeacherStudentInLine]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass