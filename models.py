

# student_chatbot/models.py
from django.db import models

class UCUQuestion(models.Model):
    question = models.CharField(max_length=255, unique=True, help_text="A common question asked by students.")
    answer = models.TextField(help_text="The answer the chatbot should provide.")

    def __str__(self):
        return self.question

class StudentService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
