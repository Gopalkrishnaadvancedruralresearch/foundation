const CACHE_NAME = "whatsgarrf-mvp-v1";
const APP_SHELL = ["./", "./manifest.json"];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(APP_SHELL)).catch(() => {})
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Network-first so contacts.json and API calls are always fresh; fallback to cache if offline
self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  // Never cache Worker API or dynamic contacts.json
  if (url.hostname.includes("workers.dev") || url.pathname.endsWith("contacts.json")) {
    return;
  }

  event.respondWith(
    fetch(req)
      .then((res) => {
        if (res && res.status === 200 && url.origin === self.location.origin) {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((c) => c.put(req, copy)).catch(() => {});
        }
        return res;
      })
      .catch(() => caches.match(req))
  );
});

// WEB PUSH WAKE-UP HANDLER (Wakes phone in pocket / background computer)
self.addEventListener("push", (event) => {
  let data = {};
  try {
    data = event.data ? event.data.json() : {};
  } catch (_) {
    data = { title: "WhatsGARRF Alert", body: event.data ? event.data.text() : "Incoming notification" };
  }

  const isCall = data.kind === "call";
  const fromName = data.fromName || data.fromPhone || "WhatsGARRF User";
  const title = data.title || (isCall
    ? `📞 Incoming ${data.hasVideo ? "Video" : "Voice"} Call from ${fromName}`
    : `💬 New Message from ${fromName}`);

  const body = data.body || (isCall
    ? `Tap to open WhatsGARRF and answer (${data.fromPhone || "Live Call"})`
    : (data.preview || "Tap to view message"));

  const scopeUrl = self.registration.scope || "./";
  const qs = new URLSearchParams();
  if (data.fromPhone) qs.set("fromPhone", data.fromPhone);
  if (data.fromName) qs.set("fromName", data.fromName);
  if (data.roomId) qs.set("roomId", data.roomId);
  if (data.hasVideo) qs.set("video", "1");

  const targetUrl = `${scopeUrl}?${qs.toString()}`;

  const options = {
    body,
    icon: "https://garrf.in/images/logo.jpeg",
    badge: "https://garrf.in/images/logo.jpeg",
    tag: isCall ? "wg-incoming-call" : "wg-chat-msg",
    renotify: true,
    requireInteraction: true,
    vibrate: isCall ? [500, 200, 500, 200, 500, 200, 500] : [250, 100, 250],
    data: { url: targetUrl, ...data },
    actions: isCall
      ? [
          { action: "answer", title: "📞 Open & Answer" },
          { action: "dismiss", title: "Dismiss" }
        ]
      : [{ action: "open", title: "💬 Open Chat" }]
  };

  event.waitUntil(self.registration.showNotification(title, options));
});

// TAP NOTIFICATION -> FOCUS EXISTING WINDOW OR LAUNCH APP
self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  if (event.action === "dismiss") return;

  const data = event.notification.data || {};
  const targetUrl = data.url || self.registration.scope || "./";

  event.waitUntil(
    self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((clientList) => {
      for (const client of clientList) {
        if ("focus" in client) {
          client.focus();
          client.postMessage({ type: "wg-wake-open", ...data });
          return;
        }
      }
      if (self.clients.openWindow) {
        return self.clients.openWindow(targetUrl);
      }
    })
  );
});
