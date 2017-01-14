import json

from .helpers import send_notification_to_user


def send_user_notification(user, payload, ttl=0):
	payload = json.dumps(payload)
	send_notification_to_user(user, payload, ttl)