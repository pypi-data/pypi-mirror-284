"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[24086],{11753:function(t,e,r){r.d(e,{A:function(){return o}});r(27934),r(86245),r(26777),r(3359),r(73842);var n=function(t){var e=parseFloat(t);if(isNaN(e))throw new Error("".concat(t," is not a number"));return e};function o(t){if(!t)return null;try{if(t.endsWith("%"))return{w:100,h:n(t.substr(0,t.length-1))};var e=t.replace(":","x").split("x");return 0===e.length?null:1===e.length?{w:n(e[0]),h:1}:{w:n(e[0]),h:n(e[1])}}catch(r){}return null}},24086:function(t,e,r){r.r(e),r.d(e,{HuiIframeCard:function(){return k}});var n,o,i,a=r(6238),c=r(94881),l=r(1781),u=r(36683),s=r(89231),f=r(29864),d=r(83647),h=r(8364),p=(r(27934),r(77052),r(21950),r(650),r(86150),r(68113),r(55888),r(26777),r(58971),r(56262),r(73842),r(8339),r(29734),r(72134),r(7146),r(97157),r(56648),r(72435),r(40924)),g=r(196),v=r(79278),w=r(80204),_=r(11753),m=(r(12261),r(54373),r(74541)),k=(0,h.A)([(0,g.EM)("hui-iframe-card")],(function(t,e){var h,k=function(e){function r(){var e;(0,s.A)(this,r);for(var n=arguments.length,o=new Array(n),i=0;i<n;i++)o[i]=arguments[i];return e=(0,f.A)(this,r,[].concat(o)),t(e),e}return(0,d.A)(r,e),(0,u.A)(r)}(e);return{F:k,d:[{kind:"method",static:!0,key:"getConfigElement",value:(h=(0,l.A)((0,c.A)().mark((function t(){return(0,c.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,Promise.all([r.e(33066),r.e(4556)]).then(r.bind(r,24527));case 2:return t.abrupt("return",document.createElement("hui-iframe-card-editor"));case 3:case"end":return t.stop()}}),t)}))),function(){return h.apply(this,arguments)})},{kind:"method",static:!0,key:"getStubConfig",value:function(){return{type:"iframe",url:"https://www.home-assistant.io",aspect_ratio:"50%"}}},{kind:"field",decorators:[(0,g.MZ)({type:Boolean,reflect:!0})],key:"isPanel",value:function(){return!1}},{kind:"field",decorators:[(0,g.MZ)({attribute:!1})],key:"layout",value:void 0},{kind:"field",decorators:[(0,g.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,g.wk)()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function(){return this._config?1+(this._config.aspect_ratio?Number(this._config.aspect_ratio.replace("%","")):50)/25:5}},{kind:"method",key:"setConfig",value:function(t){if(!t.url)throw new Error("URL required");this._config=t}},{kind:"method",key:"render",value:function(){var t;if(!this._config||!this.hass)return p.s6;var e="";if(!(this.isPanel||"grid"===this.layout))if(this._config.aspect_ratio){var r=(0,_.A)(this._config.aspect_ratio);r&&r.w>0&&r.h>0&&(e="".concat((100*r.h/r.w).toFixed(2),"%"))}else e="50%";var i=new URL(this._config.url,location.toString()).protocol;if("https:"===location.protocol&&"https:"!==i)return(0,p.qy)(n||(n=(0,a.A)([' <ha-alert alert-type="error"> '," </ha-alert> "])),this.hass.localize("ui.panel.lovelace.cards.iframe.error_secure_context",{target_protocol:i,context_protocol:location.protocol}));var c="";return this._config.allow_open_top_navigation&&(c+="allow-top-navigation-by-user-activation"),(0,p.qy)(o||(o=(0,a.A)([' <ha-card .header="','"> <div id="root" style="','"> <iframe title="','" src="','" .sandbox="','" allow="','"></iframe> </div> </ha-card> '])),this._config.title,(0,w.W)({"padding-top":e}),(0,v.J)(this._config.title),this._config.url,"".concat(c," ").concat(m.D),null!==(t=this._config.allow)&&void 0!==t?t:"fullscreen")}},{kind:"method",key:"getLayoutOptions",value:function(){return{grid_columns:4,grid_rows:4,grid_min_rows:2}}},{kind:"get",static:!0,key:"styles",value:function(){return(0,p.AH)(i||(i=(0,a.A)(["ha-card{overflow:hidden;width:100%;height:100%;display:flex;flex-direction:column}#root{width:100%;height:100%;position:relative}iframe{position:absolute;border:none;width:100%;height:100%;top:0;left:0}"])))}}]}}),p.WF)},74541:function(t,e,r){r.d(e,{D:function(){return n}});var n="allow-forms allow-popups allow-pointer-lock allow-same-origin allow-scripts allow-modals allow-downloads"},86150:function(t,e,r){var n=r(87568),o=r(82374),i=r(94905),a=r(8242),c=r(69015),l=r(32565),u=RangeError,s=String,f=Math.floor,d=o(c),h=o("".slice),p=o(1..toFixed),g=function(t,e,r){return 0===e?r:e%2==1?g(t,e-1,r*t):g(t*t,e/2,r)},v=function(t,e,r){for(var n=-1,o=r;++n<6;)o+=e*t[n],t[n]=o%1e7,o=f(o/1e7)},w=function(t,e){for(var r=6,n=0;--r>=0;)n+=t[r],t[r]=f(n/e),n=n%e*1e7},_=function(t){for(var e=6,r="";--e>=0;)if(""!==r||0===e||0!==t[e]){var n=s(t[e]);r=""===r?n:r+d("0",7-n.length)+n}return r};n({target:"Number",proto:!0,forced:l((function(){return"0.000"!==p(8e-5,3)||"1"!==p(.9,0)||"1.25"!==p(1.255,2)||"1000000000000000128"!==p(0xde0b6b3a7640080,0)}))||!l((function(){p({})}))},{toFixed:function(t){var e,r,n,o,c=a(this),l=i(t),f=[0,0,0,0,0,0],p="",m="0";if(l<0||l>20)throw new u("Incorrect fraction digits");if(c!=c)return"NaN";if(c<=-1e21||c>=1e21)return s(c);if(c<0&&(p="-",c=-c),c>1e-21)if(r=(e=function(t){for(var e=0,r=t;r>=4096;)e+=12,r/=4096;for(;r>=2;)e+=1,r/=2;return e}(c*g(2,69,1))-69)<0?c*g(2,-e,1):c/g(2,e,1),r*=4503599627370496,(e=52-e)>0){for(v(f,0,r),n=l;n>=7;)v(f,1e7,0),n-=7;for(v(f,g(10,n,1),0),n=e-1;n>=23;)w(f,1<<23),n-=23;w(f,1<<n),v(f,1,1),w(f,2),m=_(f)}else v(f,0,r),v(f,1<<-e,0),m=_(f)+d("0",l);return m=l>0?p+((o=m.length)<=l?"0."+d("0",l-o)+m:h(m,0,o-l)+"."+h(m,o-l)):p+m}})}}]);
//# sourceMappingURL=24086.HOcAxZ0Wp_s.js.map