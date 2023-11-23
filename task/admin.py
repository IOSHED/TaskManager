from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'send_notify_at', 'create_at', 'update_at', 'complete_at', 'is_complete')
    list_filter = ('user', 'send_notify_at', 'create_at', 'update_at', 'complete_at', 'is_complete')
    search_fields = ('name', 'description')
    ordering = ('-send_notify_at', '-create_at')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)
