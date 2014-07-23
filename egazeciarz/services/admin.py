from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib import admin
from models import (
    Days,
    Hours,
    ReceiverType,
    Service,
    SubPattern,
    Subscriptions,
    UserProfile,
    UserSubs,
)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)
admin.site.register(ReceiverType)
admin.site.register(Hours)
admin.site.register(Days)
admin.site.register(Subscriptions)
admin.site.register(UserSubs)
admin.site.register(SubPattern)
admin.site.register(Service)
