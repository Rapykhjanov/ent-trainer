from django.contrib import admin
from .models import Category, Task
from django import forms # Импортируем forms для кастомного виджета
from django.utils.html import format_html # Для форматированного вывода

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

# Создаем кастомную форму для модели Task
class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'answer_options': forms.Textarea(attrs={
                'rows': 5, # Увеличиваем высоту текстового поля
                'placeholder': 'Введите варианты ответа, разделяя их запятыми (например: Опция A, Опция B, Опция C)',
                'style': 'width: 90%;', # Ширина для удобства
            }),
        }

class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm # Используем нашу кастомную форму для админки

    list_display = ('category', 'difficulty', 'topic', 'question_number', 'question', 'display_answer_options_simple')
    list_filter = ('category', 'difficulty')
    search_fields = ('question', 'topic', 'correct_answer')

    # Опционально: Организация полей с помощью fieldsets для лучшей читаемости
    fieldsets = (
        (None, {
            'fields': ('category', 'difficulty', 'topic', 'question_number', 'question'),
        }),
        ('Ответы', {
            'fields': ('answer_options', 'correct_answer'),
            'description': 'Введите варианты ответа, разделяя их запятыми.',
        }),
    )

    def display_answer_options_simple(self, obj):
        # Просто возвращаем содержимое поля как есть
        if obj.answer_options:
            return obj.answer_options
        return "Нет вариантов"

    display_answer_options_simple.short_description = "Варианты ответа"


admin.site.register(Task, TaskAdmin)