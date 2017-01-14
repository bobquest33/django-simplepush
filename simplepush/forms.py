from django import forms

from .models import PushInformation, SubscriptionInfo



class SimplePushForm(forms.Form):
	status_type = forms.ChoiceField(choices=[
									  ('subscribe', 'subscribe'),
									  ('unsubscribe', 'unsubscribe')
									])

	def save_or_delete(self, subscription, user, status_type):
		data = {}
		if user.is_authenticated():
			data["user"] = user
			
		data["subscription"] = subscription
		push_info, created = PushInformation.objects.get_or_create(**data)

		# If unsubscribe is called, that means need to delete the browser
		# and notification info from server. 
		if status_type == "unsubscribe":
			push_info.delete()
			subscription.delete()


class SubscriptionForm(forms.ModelForm):

	class Meta:
		model = SubscriptionInfo
		fields = ('browser', 'endpoint', 'auth', 'p256dh')


	def get_or_save(self, subscription_data):
		subscription, created = SubscriptionInfo.objects.get_or_create(**subscription_data)
		return subscription