# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import PushInformation, SubscriptionInfo


class PushInformationAdmin(admin.ModelAdmin):
	raw_id_fields = ('user', 'subscription')
	list_display = ['user','added_on', 'subscription']


admin.site.register(SubscriptionInfo)
admin.site.register(PushInformation, PushInformationAdmin)
