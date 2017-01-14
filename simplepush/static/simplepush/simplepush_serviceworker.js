self.addEventListener('install', function(event) {
  //Automatically take over the previous worker.
  event.waitUntil(self.skipWaiting());
});


// Register event listener for the 'push' event.
self.addEventListener('push', function(event) {
  // Retrieve the textual payload from event.data (a PushMessageData object).
  // Other formats are supported (ArrayBuffer, Blob, JSON), check out the documentation
  // on https://developer.mozilla.org/en-US/docs/Web/API/PushMessageData.
    var payload = event.data ? event.data.text() : {"head": "No Content", "Body": "No Content"};
    data = JSON.parse(payload),
    head = data.head,
    icon = data.icon,
    body = data.body;
    

  // Keep the service worker alive until the notification is created.
  event.waitUntil(
    // Show a notification with title 'ServiceWorker Cookbook' and use the payload
    // as the body.
    self.registration.showNotification(head, {
      body: body,
      icon: icon,
      vibrate: [200, 100, 200, 100, 200, 100, 200],
    })
  );
});

self.addEventListener('notificationclick', function(event) {
    event.notification.close();
    data = JSON.parse(self.payload),
    url = data.body.link;
    
    event.waitUntil(
        clients.matchAll({
          type: 'window'
        })
        .then(function(windowClients) {
          console.log('WindowClients', windowClients);
          for (var i = 0; i < windowClients.length; i++) {
            var client = windowClients[i];
            if (client.url === url && 'focus' in client) {
              return client.focus();
            }
          }
          if (clients.openWindow) {
            return clients.openWindow(url);
          }
        })
    );
});