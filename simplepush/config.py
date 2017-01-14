from django.conf import settings

MANIFEST = {}
if hasattr(settings,'SIMPLEPUSH_SETTINGS'):
	MANIFEST["gcm_sender_id"] = settings.SIMPLEPUSH_SETTINGS['GCM_ID']