"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[1109],{59216:function(t,n,e){e.d(n,{A:function(){return a}});e(77052);var i=function(t){return t<10?"0".concat(t):t};function a(t){var n=Math.floor(t/3600),e=Math.floor(t%3600/60),a=Math.floor(t%3600%60);return n>0?"".concat(n,":").concat(i(e),":").concat(i(a)):e>0?"".concat(e,":").concat(i(a)):a>0?""+a:null}},10829:function(t,n,e){e.d(n,{PF:function(){return u},CR:function(){return r},pZ:function(){return c},kL:function(){return a},ls:function(){return o},r9:function(){return s}});e(77052),e(43859),e(36724),e(650),e(98168);var i=e(59216),a=function(t){return t.callWS({type:"timer/list"})},r=function(t,n){return t.callWS(Object.assign({type:"timer/create"},n))},s=function(t,n,e){return t.callWS(Object.assign({type:"timer/update",timer_id:n},e))},c=function(t,n){return t.callWS({type:"timer/delete",timer_id:n})},o=function(t){if(t.attributes.remaining){var n,e,i=(n=t.attributes.remaining,3600*(e=n.split(":").map(Number))[0]+60*e[1]+e[2]);if("active"===t.state){var a=(new Date).getTime(),r=new Date(t.last_changed).getTime();i=Math.max(i-(a-r)/1e3,0)}return i}},u=function(t,n,e){if(!n)return null;if("idle"===n.state||0===e)return t.formatEntityState(n);var a=(0,i.A)(e||0);return"paused"===n.state&&(a="".concat(a," (").concat(t.formatEntityState(n),")")),a}},1109:function(t,n,e){var i=e(1781).A,a=e(94881).A;e.a(t,function(){var t=i(a().mark((function t(i,r){var s,c,o,u,l,h,f,d,v,k,_,m,g,y,p,w,A,b,I;return a().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(t.prev=0,e.r(n),s=e(6238),c=e(36683),o=e(89231),u=e(29864),l=e(83647),h=e(8364),f=e(76504),d=e(80792),v=e(27934),k=e(77052),_=e(40924),m=e(196),g=e(10829),y=e(15821),p=e(21242),w=e(76158),!(A=i([p])).then){t.next=28;break}return t.next=24,A;case 24:t.t1=t.sent,t.t0=(0,t.t1)(),t.next=29;break;case 28:t.t0=A;case 29:p=t.t0[0],(0,h.A)([(0,m.EM)("hui-timer-entity-row")],(function(t,n){var e=function(n){function e(){var n;(0,o.A)(this,e);for(var i=arguments.length,a=new Array(i),r=0;r<i;r++)a[r]=arguments[r];return n=(0,u.A)(this,e,[].concat(a)),t(n),n}return(0,l.A)(e,n),(0,c.A)(e)}(n);return{F:e,d:[{kind:"field",decorators:[(0,m.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,m.wk)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,m.wk)()],key:"_timeRemaining",value:void 0},{kind:"field",key:"_interval",value:void 0},{kind:"method",key:"setConfig",value:function(t){if(!t)throw new Error("Invalid configuration");if(this._config=t,this.hass){var n=this.hass.states[this._config.entity];n?this._startInterval(n):this._clearInterval()}}},{kind:"method",key:"disconnectedCallback",value:function(){(0,f.A)((0,d.A)(e.prototype),"disconnectedCallback",this).call(this),this._clearInterval()}},{kind:"method",key:"connectedCallback",value:function(){if((0,f.A)((0,d.A)(e.prototype),"connectedCallback",this).call(this),this._config&&this._config.entity){var t,n=null===(t=this.hass)||void 0===t?void 0:t.states[this._config.entity];n&&this._startInterval(n)}}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return _.s6;var t=this.hass.states[this._config.entity];return t?(0,_.qy)(I||(I=(0,s.A)([' <hui-generic-entity-row .hass="','" .config="','"> <div class="text-content"> '," </div> </hui-generic-entity-row> "])),this.hass,this._config,(0,g.PF)(this.hass,t,this._timeRemaining)):(0,_.qy)(b||(b=(0,s.A)([" <hui-warning> "," </hui-warning> "])),(0,w.j)(this.hass,this._config.entity))}},{kind:"method",key:"shouldUpdate",value:function(t){return!!t.has("_timeRemaining")||(0,y.LX)(this,t)}},{kind:"method",key:"updated",value:function(t){if((0,f.A)((0,d.A)(e.prototype),"updated",this).call(this,t),this._config&&t.has("hass")){var n=this.hass.states[this._config.entity],i=t.get("hass");(i?i.states[this._config.entity]:void 0)!==n?this._startInterval(n):n||this._clearInterval()}}},{kind:"method",key:"_clearInterval",value:function(){this._interval&&(window.clearInterval(this._interval),this._interval=void 0)}},{kind:"method",key:"_startInterval",value:function(t){var n=this;this._clearInterval(),this._calculateRemaining(t),"active"===t.state&&(this._interval=window.setInterval((function(){return n._calculateRemaining(t)}),1e3))}},{kind:"method",key:"_calculateRemaining",value:function(t){this._timeRemaining=(0,g.ls)(t)}}]}}),_.WF),r(),t.next=37;break;case 34:t.prev=34,t.t2=t.catch(0),r(t.t2);case 37:case"end":return t.stop()}}),t,null,[[0,34]])})));return function(n,e){return t.apply(this,arguments)}}())}}]);
//# sourceMappingURL=1109.Fb2D8WGX5GQ.js.map