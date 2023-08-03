// service-worker.js

self.addEventListener("install", function (event) {
  // Do nothing or keep it empty
});

self.addEventListener("fetch", function (event) {
  event.respondWith(
    caches.match(event.request).then(function (response) {
      return response || fetch(event.request);
    })
  );
});
