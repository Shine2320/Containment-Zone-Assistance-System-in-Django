from django.contrib import admin
from django.utils.html import format_html
from main_app.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse, re_path

# Register your models here.
class AdminUser(admin.ModelAdmin):
    def accept_user(self, request, user_id):
        user = User.objects.get(id=user_id)
        if user and request.user.is_superuser:
            user.status = User.ACCEPTED
            user.save()
        return HttpResponseRedirect("/admin/main_app/user/")

    def reject_user(self, request, user_id):
        user = User.objects.get(id=user_id)
        if user and request.user.is_superuser:
            user.status = User.REJECTED
            user.save()
        return HttpResponseRedirect("/admin/main_app/user/")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            re_path(
                r"^(?P<user_id>.+)/accept/$",
                self.admin_site.admin_view(self.accept_user),
                name="user-accept",
            ),
            re_path(
                r"^(?P<user_id>.+)/reject/$",
                self.admin_site.admin_view(self.reject_user),
                name="user-reject",
            ),
        ]
        return custom_urls + urls

    def status_actions(self, obj):
        user = obj 
        if user.status:
            if user.status == 2:
                return format_html(
                    '<a class="button" href="{}">Accept</a>&nbsp;',
                    reverse("admin:user-accept", args=[obj.pk]),
                )
            elif user.status == 1:
                return format_html(
                    '<a class="button" href="{}">Reject</a>',
                    reverse("admin:user-reject", args=[obj.pk]),
                )
        

    status_actions.short_description = "User status"
    status_actions.allow_tags = True
    list_display = ("id", "user_type", "status", "status_actions")
    list_filter = ("user_type",)
class AdminService(admin.ModelAdmin):
    list_display = ("id", "service",)
    

admin.site.register(User, AdminUser)
admin.site.register(Service,AdminService)