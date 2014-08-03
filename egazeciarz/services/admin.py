from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib import admin
from models import (
    Day,
    Hour,
    ReceiverType,
    Service,
    SubPattern,
    Subscription,
    UserProfile,
    UsersSubs,
)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)
admin.site.register(ReceiverType)
admin.site.register(Hour)
admin.site.register(Day)
admin.site.register(Subscription)
admin.site.register(UsersSubs)
admin.site.register(SubPattern)
admin.site.register(Service)
