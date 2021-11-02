from django.contrib import admin

from .models import Homework, HomeworkResult, Student, Teacher

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Homework)
admin.site.register(HomeworkResult)
