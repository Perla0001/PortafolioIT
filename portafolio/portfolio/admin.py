from django.contrib import admin
from .models import Technology, Project, Certificate, ContactMessage, Greeting

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_visible", "display_order", "created_at")
    list_editable = ("is_visible", "display_order")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "is_read")
    list_filter = ("is_read",)


admin.site.register(Technology)
admin.site.register(Certificate)
admin.site.register(Greeting)