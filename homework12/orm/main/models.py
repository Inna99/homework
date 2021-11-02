from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Homework(models.Model):
    text = models.TextField(default="homework text")
    deadline = models.DateTimeField(blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, editable=False)

    def is_active(self) -> bool:
        from django.utils import timezone

        if self.deadline > timezone.now():
            return True
        else:
            return False

    def __str__(self):
        return self.text


class HomeworkResult(models.Model):
    solution = models.TextField(default="homework solution", blank=True)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework_src = models.ForeignKey(Homework, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author}, Done: {self.done}"
