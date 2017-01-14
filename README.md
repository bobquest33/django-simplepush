#Django-Simplepush
------

A plugable django app to send chrome/firefox push notifications through GCM with Notification icon support.
a brief overview can be found here: [Google WebPushNotications](https://developers.google.com/web/fundamentals/getting-started/codelabs/push-notifications/)
This app uses latest ServiceWorkers so push notifications may not be supported in your browser, please check here: [Can I Use Web Pushnotifactions](http://caniuse.com/#search=notification)
Notice that Web Pushnotifcations are a work in progress so all features might not be supported.
[Notification Spec](https://notifications.spec.whatwg.org/)

##Installation:
You can install it easily from pypi by running
	pip install django-simplepush

After installing the package, add ``simplepush`` in in your
``INSTALLED_APPS`` settings

	INSTALLED_APPS = (
	    ...
	    'simplepush',
	)

If you would like to send notification to Google Chrome Users, you need
to add a ``SIMPLEPUSH_SETTINGS`` entry with the **Google Cloud Messanging
ID and Key** Like following:

    SIMPLEPUSH_SETTINGS = {
        "GCM_ID": "Your GCM ID",
        "GCM_KEY":"Your GCM KEY"
    }

**Replace ``"Your GCM ID"`` and ``"Your GCM KEY"`` with your Google
Cloud Messanging ID and Key**
To know how to obtain GCM ID and Key please see this [Documentation from Google Developers](https://developers.google.com/web/fundamentals/getting-started/push-notifications/step-04?hl=en) and the [MDN Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Push_API/Using_the_Push_API#Setting_up_Google_Cloud_Messaging)

Then include ``simplepush`` in the ``urls.py``
    urlpatterns =

        url(r'^simplepush/', include('simplepush.urls'))
    ]

Then run Migration by **``python manage.py migrate``**

##Usage:

###Adding Simplepush in Django Template
---------------------------------------

So in html template, you need to load ``simplepush_tags`` custom template tag by following: 
If you are using built in templating engine, add ``{% load simplepush_tags %}`` in the template.Remember to load static files first with ``{% load static %}``. The service worker wont register if you did not put ``{% simplepush_html %}`` tag inside <head></head> Tags. If you are using jinja or other templating engine, you can manually add the html header and button and other information such as:

```html
	<script id="simplepush-js" type="text/javascript" src="/static/simplepush/simplepush.js"></script>
	<script id="service-worker-js" type="text/javascript" src="/static/simplepush/simplepush_serviceworker.js"></script>
	<link rel="manifest" href="/simplepush/manifest">

```
Next, inside the ``<head></head>`` tag add ``{% simplepush_html %}``. Like following
```html
	<head>
	  {% simplepush_html %}
	</head>
```

Next, inside the ``<body></body>`` tag, insert ``{% simplepush_html_button %}``
where you would like to see the **Subscribe to Push Messaging** Button.
Like following
```html
    <body>
      <p> Hello World! </p>
      {% simplepush_html_button %}
    </body>
```

    **Note:** The Push Notification Button will show only if the user is logged in.
Or for jinja templates:

```html
	<button id="simplepush-subscribe-button" data-url="/simplepush/save_information">Subscribe to Push Messaging</button>
```

###Sending Web Push Notification
--------------------------------
A Web Push generally have a header and body. According to the W3C Specification, the data should be encrypted in transmission. the data is addressed as payload generally. Also a TTL header should be included indicating how much time the web push server store the data if the user is not online.

You can send push notification as:

```python
	from simplepush import send_user_notification
	payload = {"head":"Hello World", "body":"Testing Push Notification", "icon":"http://loremflickr.com/320/240", "link":"https://github.com/subhajeet2107/django-simplepush"}
	send_user_notification(user=user, payload=payload, ttl=1000)

	"""
	The user in this is subscribed user which will get notification to all of his subscribed browser, a user can have multiple subscriptions through various browsers or devices.
	The link key in payload specifies the url which can be opened when clicking on Notification
	"""

```