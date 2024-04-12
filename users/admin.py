from django.contrib import admin
from .models import Post, Question, QuizCategory, CustomUser

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(QuizCategory)
admin.site.register(Question)
