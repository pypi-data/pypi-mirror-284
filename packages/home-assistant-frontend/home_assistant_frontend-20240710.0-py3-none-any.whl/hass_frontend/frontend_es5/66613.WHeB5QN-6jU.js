"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[66613],{66613:function(n,t,r){r.d(t,{IU:function(){return a},Jt:function(){return i},Yd:function(){return u},hZ:function(){return f},y$:function(){return o}});var e;r(539),r(21950),r(36724),r(71936),r(68113),r(55888),r(56262),r(66274),r(84531),r(98168),r(34290),r(8339);function u(n){return new Promise((function(t,r){n.oncomplete=n.onsuccess=function(){return t(n.result)},n.onabort=n.onerror=function(){return r(n.error)}}))}function o(n,t){var r=indexedDB.open(n);r.onupgradeneeded=function(){return r.result.createObjectStore(t)};var e=u(r);return function(n,r){return e.then((function(e){return r(e.transaction(t,n).objectStore(t))}))}}function c(){return e||(e=o("keyval-store","keyval")),e}function i(n){return(arguments.length>1&&void 0!==arguments[1]?arguments[1]:c())("readonly",(function(t){return u(t.get(n))}))}function f(n,t){return(arguments.length>2&&void 0!==arguments[2]?arguments[2]:c())("readwrite",(function(r){return r.put(t,n),u(r.transaction)}))}function a(){return(arguments.length>0&&void 0!==arguments[0]?arguments[0]:c())("readwrite",(function(n){return n.clear(),u(n.transaction)}))}}}]);
//# sourceMappingURL=66613.WHeB5QN-6jU.js.map