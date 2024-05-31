from django.contrib import admin
from .models import Post, Question, QuizCategory, CustomUser, Backtest

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(QuizCategory)
admin.site.register(Question)
admin.site.register(Backtest)
