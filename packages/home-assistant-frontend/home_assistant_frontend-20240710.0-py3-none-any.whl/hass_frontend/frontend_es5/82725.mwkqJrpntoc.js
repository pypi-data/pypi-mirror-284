"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[82725],{82725:function(t,e,n){n.r(e),n.d(e,{CastManager:function(){return d},getCastManager:function(){return v}});var s,i,a=n(66123),r=n(89231),o=n(36683),c=(n(27934),n(75658),n(71936),n(60060),n(1158),n(32877),n(49150),n(68113),n(55888),n(72450)),u=n(33173),h=n(25737),f=n(46340),d=function(){return(0,o.A)((function t(e){var n=this;(0,r.A)(this,t),this.auth=void 0,this.status=void 0,this._eventListeners={},this._sessionStateChanged=function(t){"SESSION_STARTED"===t.sessionState||"SESSION_RESUMED"===t.sessionState?(n.auth?(0,f.oK)(n,n.auth):n.sendMessage({type:"get_status"}),n._attachMessageListener()):"SESSION_ENDED"===t.sessionState&&(n.status=void 0,n._fireEvent("connection-changed"))},this._castStateChanged=function(t){n._fireEvent("state-changed")},this.auth=e;var s=this.castContext;s.setOptions({receiverApplicationId:u.gk,autoJoinPolicy:chrome.cast.AutoJoinPolicy.ORIGIN_SCOPED}),s.addEventListener(cast.framework.CastContextEventType.SESSION_STATE_CHANGED,this._sessionStateChanged),s.addEventListener(cast.framework.CastContextEventType.CAST_STATE_CHANGED,this._castStateChanged)}),[{key:"addEventListener",value:function(t,e){var n=this;return t in this._eventListeners||(this._eventListeners[t]=[]),this._eventListeners[t].push(e),function(){n._eventListeners[t].splice(n._eventListeners[t].indexOf(e))}}},{key:"castConnectedToOurHass",get:function(){return void 0!==this.status&&void 0!==this.auth&&this.status.connected&&(this.status.hassUrl===this.auth.data.hassUrl||u.oS&&this.status.hassUrl===h.I)}},{key:"sendMessage",value:function(t){this.castSession.sendMessage(u.Oc,t)}},{key:"castState",get:function(){return this.castContext.getCastState()}},{key:"castContext",get:function(){return cast.framework.CastContext.getInstance()}},{key:"castSession",get:function(){return this.castContext.getCurrentSession()}},{key:"requestSession",value:function(){return this.castContext.requestSession()}},{key:"_fireEvent",value:function(t){var e,n=(0,a.A)(this._eventListeners[t]||[]);try{for(n.s();!(e=n.n()).done;){(0,e.value)()}}catch(s){n.e(s)}finally{n.f()}}},{key:"_receiveMessage",value:function(t){"receiver_status"===t.type&&(this.status=t,this._fireEvent("connection-changed"))}},{key:"_attachMessageListener",value:function(){var t=this;this.castSession.addMessageListener(u.Oc,(function(e,n){return t._receiveMessage(JSON.parse(n))}))}}])}(),v=function(t){return i||(i=function(){if(s)return s;s=new Promise((function(t){window.__onGCastApiAvailable=t}));var t=document.createElement("div");return t.id="cast",document.body.append(t),(0,c.kG)("https://www.gstatic.com/cv/js/sender/v1/cast_sender.js?loadCastFramework=1"),s}().then((function(e){if(!e)throw new Error("No Cast API available");return new d(t)}))),i}},72450:function(t,e,n){n.d(e,{Vw:function(){return r},kG:function(){return a},y6:function(){return i}});n(68113),n(55888);var s=function(t,e,n){return new Promise((function(s,i){var a=document.createElement(t),r="src",o="body";switch(a.onload=function(){return s(e)},a.onerror=function(){return i(e)},t){case"script":a.async=!0,n&&(a.type=n);break;case"link":a.type="text/css",a.rel="stylesheet",r="href",o="head"}a[r]=e,document[o].appendChild(a)}))},i=function(t){return s("link",t)},a=function(t){return s("script",t)},r=function(t){return s("script",t,"module")}}}]);
//# sourceMappingURL=82725.mwkqJrpntoc.js.map