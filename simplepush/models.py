from django.db import models
from django.conf import settings
from django.core.exceptions import FieldError

class SubscriptionInfo(models.Model):
	browser = models.CharField(max_length=100)
	endpoint = models.URLField(max_length=255)
	auth = models.CharField(max_length=100)
	p256dh = models.CharField(max_length=100)
	added_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		app_label = 'simplepush'


class PushInformation(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='simplepush_info', blank=True, null=True)
	subscription = models.ForeignKey(SubscriptionInfo)
	added_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		app_label = 'simplepush'