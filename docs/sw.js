const CACHE='psych-notes-2026-05-28-1026';
const ASSETS=["./", "./index.html", "./manifest.webmanifest", "./icon-192.png", "./icon-512.png", "./figs/f_11_4.jpg", "./figs/f_11_5.jpg", "./figs/f_3_16.jpg", "./figs/f_3_19.jpg", "./figs/f_3_2.jpg", "./figs/f_3_25.jpg", "./figs/f_3_27.jpg", "./figs/f_3_28.jpg", "./figs/f_3_5.jpg", "./figs/f_3_6.jpg", "./figs/f_3_8.jpg", "./figs/f_3_9.jpg", "./figs/f_4_16.jpg", "./figs/f_4_5.jpg", "./figs/f_4_7.jpg", "./figs/f_6_13.jpg", "./figs/f_6_5.jpg", "./figs/f_7_10.jpg", "./figs/f_7_11.jpg", "./figs/f_7_4.jpg", "./figs/f_8_1.jpg", "./figs/f_8_6.jpg"];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)));self.skipWaiting();});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))));self.clients.claim();});
self.addEventListener('fetch',e=>{e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));});
