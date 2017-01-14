from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^save_information', views.save_info, name='save_simplepush_info'),
	url(r'^manifest', views.generate_manifest, name='simplepush_manifest_json'),
]
