// Cachea solo la cáscara estática. No toca datos: viven en localStorage y en Supabase (otro origen, no se intercepta).
const C="nutrifit-shell-v1",LIB="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.js";
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>Promise.all(["./","index.html","manifest.json","icon-192.png","icon-512.png"].map(u=>c.add(u)).concat(c.add(new Request(LIB,{mode:"no-cors"})).catch(()=>{})))));self.skipWaiting()});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim()});
self.addEventListener("fetch",e=>{const r=e.request,u=new URL(r.url);if(r.method!=="GET")return;
 if(r.url===LIB){e.respondWith(caches.match(r).then(m=>m||fetch(r)));return}
 if(u.origin!==location.origin)return;
 e.respondWith(fetch(r).then(x=>{const cp=x.clone();caches.open(C).then(c=>c.put(r,cp));return x}).catch(()=>caches.match(r).then(m=>m||caches.match("index.html"))))});
