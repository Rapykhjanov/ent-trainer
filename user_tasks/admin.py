from django.contrib import admin
from .models import UserTask
from django.utils.html import format_html
import json

class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'answer', 'is_correct', 'skipped', 'answered_at', 'view_answer_options')
    list_filter = ('user', 'task', 'is_correct')
    date_hierarchy = 'answered_at'
    readonly_fields = ('is_correct', 'skipped', 'answered_at', 'answer_options')
    fieldsets = (
        (None, {
            'fields': ('user', 'task', 'answer'),
        }),
        ('Submission Details', {
            'fields': ('is_correct', 'skipped', 'answered_at', 'answer_options'),
            'classes': ('collapse',),
        }),
    )

    def view_answer_options(self, obj):
        if obj.answer_options:
            options_str = json.dumps(obj.answer_options, indent=2, ensure_ascii=False)
            return format_html("<pre>{}</pre>", options_str)
        else:
            return "No options"

    view_answer_options.short_description = "Answer Options"

admin.site.register(UserTask, UserTaskAdmin)