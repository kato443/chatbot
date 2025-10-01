# student_chatbot/admin.py
from django.contrib import admin
from .models import UCUQuestion, StudentService

admin.site.register(UCUQuestion)
admin.site.register(StudentService)


admin.site.site_header = "UGANDA CHRISTIAN UNIVERSITY STUDENT CHATBOT"
admin.site.site_title = "UCU Chatbot Admin Portal"
admin.site.index_title = "Welcome to the UCU Chatbot Admin"