/*! For license information please see 15149.molEFXcJHkA.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[15149],{94027:function(t,e,n){n.d(e,{E:function(){return l}});var a=n(66123),r=n(36683),i=n(89231),s=n(29864),u=n(83647),o=n(8364),c=n(76504),d=n(80792),h=(n(77052),n(53501),n(21950),n(68113),n(55888),n(34517),n(66274),n(22836),n(8339),n(196)),l=function(t){var e=(0,o.A)(null,(function(t,e){var n=function(e){function n(){var e;(0,i.A)(this,n);for(var a=arguments.length,r=new Array(a),u=0;u<a;u++)r[u]=arguments[u];return e=(0,s.A)(this,n,[].concat(r)),t(e),e}return(0,u.A)(n,e),(0,r.A)(n)}(e);return{F:n,d:[{kind:"field",decorators:[(0,h.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:void 0},{kind:"field",key:"__unsubs",value:void 0},{kind:"method",key:"connectedCallback",value:function(){(0,c.A)((0,d.A)(n.prototype),"connectedCallback",this).call(this),this.__checkSubscribed()}},{kind:"method",key:"disconnectedCallback",value:function(){if((0,c.A)((0,d.A)(n.prototype),"disconnectedCallback",this).call(this),this.__unsubs){for(;this.__unsubs.length;){var t=this.__unsubs.pop();t instanceof Promise?t.then((function(t){return t()})):t()}this.__unsubs=void 0}}},{kind:"method",key:"updated",value:function(t){if((0,c.A)((0,d.A)(n.prototype),"updated",this).call(this,t),t.has("hass"))this.__checkSubscribed();else if(this.hassSubscribeRequiredHostProps){var e,r=(0,a.A)(t.keys());try{for(r.s();!(e=r.n()).done;){var i=e.value;if(this.hassSubscribeRequiredHostProps.includes(i))return void this.__checkSubscribed()}}catch(s){r.e(s)}finally{r.f()}}}},{kind:"method",key:"hassSubscribe",value:function(){return[]}},{kind:"method",key:"__checkSubscribed",value:function(){var t,e=this;void 0!==this.__unsubs||!this.isConnected||void 0===this.hass||null!==(t=this.hassSubscribeRequiredHostProps)&&void 0!==t&&t.some((function(t){return void 0===e[t]}))||(this.__unsubs=this.hassSubscribe())}}]}}),t);return e}},59122:function(t,e,n){var a=n(1781).A,r=n(94881).A;n.a(t,function(){var t=a(r().mark((function t(a,i){var s,u,o,c,d,h,l,f,v,p,k,b,g,_,y,m,A,x,w,C,D,S,M,P,F,N,H,z,E,q,R,Y,T,W,I,O,Z,$;return r().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(t.prev=0,n.r(e),n.d(e,{HuiEnergyDevicesGraphCard:function(){return $}}),s=n(94881),u=n(1781),o=n(6238),c=n(36683),d=n(89231),h=n(29864),l=n(83647),f=n(8364),v=n(77052),p=n(4187),k=n(36724),b=n(71936),g=n(14460),_=n(848),y=n(68113),m=n(66274),A=n(85767),x=n(84531),w=n(98168),C=n(34290),D=n(95948),S=n(40924),M=n(196),P=n(69760),F=n(45081),N=n(76502),H=n(77664),z=n(56601),n(43690),n(54373),E=n(41525),q=n(74959),R=n(94027),Y=n(15821),!(T=a([D,z,E])).then){t.next=57;break}return t.next=53,T;case 53:t.t1=t.sent,t.t0=(0,t.t1)(),t.next=58;break;case 57:t.t0=T;case 58:W=t.t0,D=W[0],z=W[1],E=W[2],$=(0,f.A)([(0,M.EM)("hui-energy-devices-graph-card")],(function(t,e){var n,a=function(e){function n(){var e;(0,d.A)(this,n);for(var a=arguments.length,r=new Array(a),i=0;i<a;i++)r[i]=arguments[i];return e=(0,h.A)(this,n,[].concat(r)),t(e),e}return(0,l.A)(n,e),(0,c.A)(n)}(e);return{F:a,d:[{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,M.wk)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,M.wk)()],key:"_chartData",value:function(){return{datasets:[]}}},{kind:"field",decorators:[(0,M.wk)()],key:"_data",value:void 0},{kind:"field",decorators:[(0,M.P)("ha-chart-base")],key:"_chart",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:function(){return["_config"]}},{kind:"method",key:"hassSubscribe",value:function(){var t,e=this;return[(0,E.tb)(this.hass,{key:null===(t=this._config)||void 0===t?void 0:t.collection_key}).subscribe((function(t){e._data=t,e._getStatistics(t)}))]}},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"setConfig",value:function(t){this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return(0,Y.xP)(this,t)||t.size>1||!t.has("hass")}},{kind:"method",key:"render",value:function(){var t;return this.hass&&this._config?(0,S.qy)(I||(I=(0,o.A)([" <ha-card> ",' <div class="content ','"> <ha-chart-base .hass="','" .data="','" .options="','" .height="','" chart-type="bar"></ha-chart-base> </div> </ha-card> '])),this._config.title?(0,S.qy)(O||(O=(0,o.A)(['<h1 class="card-header">',"</h1>"])),this._config.title):"",(0,P.H)({"has-header":!!this._config.title}),this.hass,this._chartData,this._createOptions(this.hass.locale),28*((null===(t=this._chartData)||void 0===t||null===(t=t.datasets[0])||void 0===t?void 0:t.data.length)||0)+50):S.s6}},{kind:"field",key:"_createOptions",value:function(){var t=this;return(0,F.A)((function(e){return{parsing:!1,animation:!1,responsive:!0,maintainAspectRatio:!1,indexAxis:"y",scales:{y:{type:"category",ticks:{autoSkip:!1,callback:function(e){var n=t._chartData.datasets[0].data[e].y;return t.getDeviceName(n)}}},x:{title:{display:!0,text:"kWh"}}},elements:{bar:{borderWidth:1,borderRadius:4}},plugins:{tooltip:{mode:"nearest",callbacks:{title:function(e){var n=e[0].label;return t.getDeviceName(n)},label:function(t){return"".concat(t.dataset.label,": ").concat((0,z.ZV)(t.parsed.x,e)," kWh")}}}},locale:(0,z.Yf)(t.hass.locale),onClick:function(e){var n,a=e.chart,r=(0,D.gP)(e,a),i=Math.abs(a.scales.y.getValueForPixel(r.y));(0,H.r)(t,"hass-more-info",{entityId:null===(n=t._chartData)||void 0===n||null===(n=n.datasets[0])||void 0===n||null===(n=n.data[i])||void 0===n?void 0:n.y}),a.canvas.dispatchEvent(new Event("mouseout"))}}}))}},{kind:"method",key:"getDeviceName",value:function(t){var e,n;return(null===(e=this._data)||void 0===e||null===(e=e.prefs.device_consumption.find((function(e){return e.stat_consumption===t})))||void 0===e?void 0:e.name)||(0,q.$O)(this.hass,t,null===(n=this._data)||void 0===n?void 0:n.statsMetadata[t])}},{kind:"method",key:"_getStatistics",value:(n=(0,u.A)((0,s.A)().mark((function t(e){var n,a,r,i,u,o,c,d,h,l,f,v;return(0,s.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return r=e.stats,i=e.statsCompare,u=[],o=[],c=[],d=[],h=[],l=[],f=[{label:this.hass.localize("ui.panel.lovelace.cards.energy.energy_devices_graph.energy_usage"),borderColor:c,backgroundColor:h,data:u,barThickness:i?10:20}],i&&f.push({label:this.hass.localize("ui.panel.lovelace.cards.energy.energy_devices_graph.previous_energy_usage"),borderColor:d,backgroundColor:l,data:o,barThickness:10}),e.prefs.device_consumption.forEach((function(t,e){var n=t.stat_consumption in r&&(0,q.$j)(r[t.stat_consumption])||0;if(u.push({y:t.stat_consumption,x:n,idx:e}),i){var a=t.stat_consumption in i&&(0,q.$j)(i[t.stat_consumption])||0;o.push({y:t.stat_consumption,x:a,idx:e})}})),u.sort((function(t,e){return e.x-t.x})),u.length=(null===(n=this._config)||void 0===n?void 0:n.max_devices)||u.length,v=getComputedStyle(this),u.forEach((function(t){var e=(0,N.fI)(t.idx,v);c.push(e),h.push(e+"7F")})),o.forEach((function(t){var e=(0,N.fI)(t.idx,v);d.push(e+"7F"),l.push(e+"32")})),this._chartData={labels:u.map((function(t){return t.y})),datasets:f},t.next=19,this.updateComplete;case 19:null===(a=this._chart)||void 0===a||a.updateChart("none");case 20:case"end":return t.stop()}}),t,this)}))),function(t){return n.apply(this,arguments)})},{kind:"get",static:!0,key:"styles",value:function(){return(0,S.AH)(Z||(Z=(0,o.A)([".card-header{padding-bottom:0}.content{padding:16px}.has-header{padding-top:0}ha-chart-base{--chart-max-height:none}"])))}}]}}),(0,R.E)(S.WF)),i(),t.next=69;break;case 66:t.prev=66,t.t2=t.catch(0),i(t.t2);case 69:case"end":return t.stop()}}),t,null,[[0,66]])})));return function(e,n){return t.apply(this,arguments)}}())},30069:function(t,e,n){var a=n(1781).A,r=n(94881).A;n.a(t,function(){var t=a(r().mark((function t(a,i){var s,u;return r().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(t.prev=0,n.d(e,{gP:function(){return s.z}}),s=n(55285),!(u=a([s])).then){t.next=11;break}return t.next=7,u;case 7:t.t1=t.sent,t.t0=(0,t.t1)(),t.next=12;break;case 11:t.t0=u;case 12:s=t.t0[0],i(),t.next=19;break;case 16:t.prev=16,t.t2=t.catch(0),i(t.t2);case 19:case"end":return t.stop()}}),t,null,[[0,16]])})));return function(e,n){return t.apply(this,arguments)}}())},95948:function(t,e,n){var a=n(1781).A,r=n(94881).A;n.a(t,function(){var t=a(r().mark((function t(a,i){var s,u;return r().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(t.prev=0,n.d(e,{gP:function(){return s.gP}}),s=n(30069),!(u=a([s])).then){t.next=11;break}return t.next=7,u;case 7:t.t1=t.sent,t.t0=(0,t.t1)(),t.next=12;break;case 11:t.t0=u;case 12:s=t.t0[0],i(),t.next=19;break;case 16:t.prev=16,t.t2=t.catch(0),i(t.t2);case 19:case"end":return t.stop()}}),t,null,[[0,16]])})));return function(e,n){return t.apply(this,arguments)}}())},94061:function(t,e,n){n.d(e,{f:function(){return i}});var a=n(74396),r=n(86174);function i(t,e){var n=(0,a.a)(t);return isNaN(e)?(0,r.w)(t,NaN):e?(n.setDate(n.getDate()+e),n):n}},84749:function(t,e,n){n.d(e,{L:function(){return i}});var a=n(87930),r=n(49518);function i(t,e){return(0,a.A)(t,e*r.s0)}},87930:function(t,e,n){n.d(e,{A:function(){return i}});var a=n(74396),r=n(86174);function i(t,e){var n=+(0,a.a)(t);return(0,r.w)(t,n+e)}},39937:function(t,e,n){n.d(e,{P:function(){return i}});var a=n(74396),r=n(86174);function i(t,e){var n=(0,a.a)(t);if(isNaN(e))return(0,r.w)(t,NaN);if(!e)return n;var i=n.getDate(),s=(0,r.w)(t,n.getTime());return s.setMonth(n.getMonth()+e+1,0),i>=s.getDate()?s:(n.setFullYear(s.getFullYear(),s.getMonth(),i),n)}},10871:function(t,e,n){n.d(e,{z:function(){return r}});var a=n(74396);function r(t,e){var n=(0,a.a)(t),r=(0,a.a)(e),i=n.getTime()-r.getTime();return i<0?-1:i>0?1:i}},23177:function(t,e,n){n.d(e,{W:function(){return u}});n(650);var a=n(10871),r=n(74396);function i(t,e){var n=(0,r.a)(t),a=(0,r.a)(e);return 12*(n.getFullYear()-a.getFullYear())+(n.getMonth()-a.getMonth())}var s=n(57442);function u(t,e){var n,u=(0,r.a)(t),o=(0,r.a)(e),c=(0,a.z)(u,o),d=Math.abs(i(u,o));if(d<1)n=0;else{1===u.getMonth()&&u.getDate()>27&&u.setDate(30),u.setMonth(u.getMonth()-c*d);var h=(0,a.z)(u,o)===-c;(0,s.c)((0,r.a)(t))&&1===d&&1===(0,a.z)(t,o)&&(h=!1),n=c*(d-Number(h))}return 0===n?0:n}},79113:function(t,e,n){n.d(e,{D:function(){return r}});var a=n(74396);function r(t){var e=(0,a.a)(t);return e.setHours(23,59,59,999),e}},3889:function(t,e,n){n.d(e,{p:function(){return r}});var a=n(74396);function r(t){var e=(0,a.a)(t),n=e.getMonth();return e.setFullYear(e.getFullYear(),n+1,0),e.setHours(23,59,59,999),e}},72502:function(t,e,n){n.d(e,{e:function(){return r}});var a=n(74396);function r(t){return 1===(0,a.a)(t).getDate()}},57442:function(t,e,n){n.d(e,{c:function(){return s}});var a=n(79113),r=n(3889),i=n(74396);function s(t){var e=(0,i.a)(t);return+(0,a.D)(e)==+(0,r.p)(e)}}}]);
//# sourceMappingURL=15149.molEFXcJHkA.js.map