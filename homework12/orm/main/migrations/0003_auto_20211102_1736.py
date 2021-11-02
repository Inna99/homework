from datetime import timedelta

from django.db import migrations
from django.utils import timezone


def create_homeworks(apps, schema_editor):
    homework_model = apps.get_model("main", "Homework")
    homework = homework_model()
    homework.text = "TEXT"
    homework.created = timezone.now()
    homework.deadline = timezone.now() + timedelta(days=7)
    homework.save()


def create_homeworks_results(apps, schema_editor):
    student_model = apps.get_model("main", "Student")
    homework_model = apps.get_model("main", "Homework")

    homework_result_model = apps.get_model("main", "HomeworkResult")
    homework_result = homework_result_model()
    homework_result.solution = "Solution"
    homework_result.done = False
    homework_result.author = student_model.objects.all()[0]
    homework_result.homework_src = homework_model.objects.all()[0]
    homework_result.save()


def create_students(apps, schema_editor):
    student_model = apps.get_model("main", "Student")
    student = student_model()
    student.first_name = "Student"
    student.last_name = "Testing"
    student.save()


def create_teachers(apps, schema_editor):
    teacher_model = apps.get_model("main", "Teacher")
    teacher = teacher_model()
    teacher.first_name = "Teacher"
    teacher.last_name = "Testing"
    teacher.save()


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_auto_20211102_0344"),
    ]

    operations = [
        migrations.RunPython(create_homeworks),
        migrations.RunPython(create_teachers),
        migrations.RunPython(create_students),
        migrations.RunPython(create_homeworks_results),
    ]
