from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):

    list_display = ('__unicode__',)
    # list_display = ('user',)  # 'user_last_name', 'user_first_name'

    search_fields = ['user', 'user_email', 'skype', 'gender', ]
    list_filter = ['gender', 'user__is_staff', ]  # exceeds min reqs


admin.site.register(Coach, CoachAdmin)
