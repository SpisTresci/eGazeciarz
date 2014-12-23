from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from egazeciarz.models import ReceiverType, UserProfile
from models import Service, SubPattern, UsersSubs


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)
admin.site.register(ReceiverType)
admin.site.register(UsersSubs)
admin.site.register(SubPattern)
admin.site.register(Service)
