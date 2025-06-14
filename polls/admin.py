# Register your models here.
from django.contrib import admin
from .models import Choice, Question

# This file is used to register models with the Django admin interface.
admin.site.site_header = "Polls Administration"
admin.site.site_title = "Polls Admin Portal"
admin.site.index_title = "Welcome to the Polls Admin Area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

