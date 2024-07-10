"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[4429],{94027:function(e,t,r){r.d(t,{E:function(){return u}});var a=r(66123),i=r(36683),n=r(89231),o=r(29864),s=r(83647),c=r(8364),l=r(76504),d=r(80792),h=(r(77052),r(53501),r(21950),r(68113),r(55888),r(34517),r(66274),r(22836),r(8339),r(196)),u=function(e){var t=(0,c.A)(null,(function(e,t){var r=function(t){function r(){var t;(0,n.A)(this,r);for(var a=arguments.length,i=new Array(a),s=0;s<a;s++)i[s]=arguments[s];return t=(0,o.A)(this,r,[].concat(i)),e(t),t}return(0,s.A)(r,t),(0,i.A)(r)}(t);return{F:r,d:[{kind:"field",decorators:[(0,h.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:void 0},{kind:"field",key:"__unsubs",value:void 0},{kind:"method",key:"connectedCallback",value:function(){(0,l.A)((0,d.A)(r.prototype),"connectedCallback",this).call(this),this.__checkSubscribed()}},{kind:"method",key:"disconnectedCallback",value:function(){if((0,l.A)((0,d.A)(r.prototype),"disconnectedCallback",this).call(this),this.__unsubs){for(;this.__unsubs.length;){var e=this.__unsubs.pop();e instanceof Promise?e.then((function(e){return e()})):e()}this.__unsubs=void 0}}},{kind:"method",key:"updated",value:function(e){if((0,l.A)((0,d.A)(r.prototype),"updated",this).call(this,e),e.has("hass"))this.__checkSubscribed();else if(this.hassSubscribeRequiredHostProps){var t,i=(0,a.A)(e.keys());try{for(i.s();!(t=i.n()).done;){var n=t.value;if(this.hassSubscribeRequiredHostProps.includes(n))return void this.__checkSubscribed()}}catch(o){i.e(o)}finally{i.f()}}}},{kind:"method",key:"hassSubscribe",value:function(){return[]}},{kind:"method",key:"__checkSubscribed",value:function(){var e,t=this;void 0!==this.__unsubs||!this.isConnected||void 0===this.hass||null!==(e=this.hassSubscribeRequiredHostProps)&&void 0!==e&&e.some((function(e){return void 0===t[e]}))||(this.__unsubs=this.hassSubscribe())}}]}}),e);return t}},48498:function(e,t,r){var a=r(1781).A,i=r(94881).A;r.a(e,function(){var e=a(i().mark((function e(a,n){var o,s,c,l,d,h,u,v,g,f,p,y,b,m,k,x,_,w,M,L,A,C,H,V,F,W,q,z,Z,D,J,S,P,E,N,Y,R,j,T,B,K,O,U,$,G,I,Q,X,ee,te,re,ae,ie,ne,oe,se,ce,le,de,he,ue,ve,ge,fe;return i().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(e.prev=0,r.r(t),o=r(6238),s=r(36683),c=r(89231),l=r(29864),d=r(83647),h=r(8364),u=r(77052),v=r(36724),g=r(19954),f=r(68113),p=r(84368),y=r(66274),b=r(98168),m=r(91078),r(34069),k=r(40924),x=r(196),_=r(69760),w=r(56601),r(54373),r(1683),M=r(41525),L=r(74959),A=r(94027),C=r(15821),!(H=a([w,M])).then){e.next=43;break}return e.next=39,H;case 39:e.t1=e.sent,e.t0=(0,e.t1)(),e.next=44;break;case 43:e.t0=H;case 44:V=e.t0,w=V[0],M=V[1],ge="M12,20A6,6 0 0,1 6,14C6,10 12,3.25 12,3.25C12,3.25 18,10 18,14A6,6 0 0,1 12,20Z",fe=238.76104,(0,h.A)([(0,x.EM)("hui-energy-distribution-card")],(function(e,t){var r=function(t){function r(){var t;(0,c.A)(this,r);for(var a=arguments.length,i=new Array(a),n=0;n<a;n++)i[n]=arguments[n];return t=(0,l.A)(this,r,[].concat(i)),e(t),t}return(0,d.A)(r,t),(0,s.A)(r)}(t);return{F:r,d:[{kind:"field",decorators:[(0,x.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,x.wk)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,x.wk)()],key:"_data",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:function(){return["_config"]}},{kind:"method",key:"setConfig",value:function(e){this._config=e}},{kind:"method",key:"hassSubscribe",value:function(){var e,t=this;return[(0,M.tb)(this.hass,{key:null===(e=this._config)||void 0===e?void 0:e.collection_key}).subscribe((function(e){t._data=e}))]}},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"shouldUpdate",value:function(e){var t;return(0,C.xP)(this,e)||e.size>1||!e.has("hass")||!(null===(t=this._data)||void 0===t||!t.co2SignalEntity)&&this.hass.states[this._data.co2SignalEntity]!==e.get("hass").states[this._data.co2SignalEntity]}},{kind:"method",key:"render",value:function(){var e,t;if(!this._config)return k.s6;if(!this._data)return(0,k.qy)(F||(F=(0,o.A)(["",""])),this.hass.localize("ui.panel.lovelace.cards.energy.loading"));var r,a=this._data.prefs,i=(0,M.E$)(a),n=void 0!==i.solar,s=void 0!==i.battery,c=void 0!==i.gas,l=void 0!==i.water,d=i.grid[0].flow_to.length>0,h=null!==(e=(0,L.gF)(this._data.stats,i.grid[0].flow_from.map((function(e){return e.stat_energy_from}))))&&void 0!==e?e:0,u=null;l&&(u=null!==(r=(0,L.gF)(this._data.stats,i.water.map((function(e){return e.stat_energy_from}))))&&void 0!==r?r:0);var v,g=null;c&&(g=null!==(v=(0,L.gF)(this._data.stats,i.gas.map((function(e){return e.stat_energy_from}))))&&void 0!==v?v:0);var f=null;n&&(f=(0,L.gF)(this._data.stats,i.solar.map((function(e){return e.stat_energy_from})))||0);var p=null,y=null;s&&(p=(0,L.gF)(this._data.stats,i.battery.map((function(e){return e.stat_energy_to})))||0,y=(0,L.gF)(this._data.stats,i.battery.map((function(e){return e.stat_energy_from})))||0);var b=null;d&&(b=(0,L.gF)(this._data.stats,i.grid[0].flow_to.map((function(e){return e.stat_energy_to})))||0);var m=null;n&&(m=(f||0)-(b||0)-(p||0));var x=null,A=null;null!==m&&m<0&&(s&&(x=-1*m)>h&&(A=x-h,x=h),m=0);var C=null;n&&s?(A||(A=Math.max(0,(b||0)-(f||0)-(p||0)-(x||0))),C=p-(x||0)):!n&&s&&(A=b);var H=null;s&&(H=(y||0)-(A||0));var V,ve,pe,ye,be,me=Math.max(0,h-(x||0)),ke=Math.max(0,me+(m||0)+(H||0));n&&(V=fe*(m/ke)),H&&(ve=fe*(H/ke));var xe="https://app.electricitymap.org";if(this._data.co2SignalEntity&&this._data.fossilEnergyConsumption){var _e=Object.values(this._data.fossilEnergyConsumption).reduce((function(e,t){return e+t}),0),we=this.hass.states[this._data.co2SignalEntity];if(null!=we&&we.attributes.country_code&&(xe+="/zone/".concat(we.attributes.country_code)),null!==_e)pe=h-_e,ye=fe-(V||0)-(ve||0)-(be=fe*((me!==h?_e*(me/h):_e)/ke))}var Me=me+(m||0)+(b?b-(A||0):0)+(C||0)+(H||0)+(x||0)+(A||0);return(0,k.qy)(W||(W=(0,o.A)([' <ha-card .header="','"> <div class="card-content"> ',' <div class="row"> <div class="circle-container grid"> <div class="circle"> <ha-svg-icon .path="','"></ha-svg-icon> ',' <span class="consumption"> ',"",' kWh </span> </div> <span class="label">','</span> </div> <div class="circle-container home"> <div class="circle ','"> <ha-svg-icon .path="','"></ha-svg-icon> '," kWh "," </div> "," </div> </div> ",' <div class="lines ','"> <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice"> '," "," "," ",' <path class="grid" id="grid" d="M0,',' H100" vector-effect="non-scaling-stroke"></path> '," "," "," "," "," "," "," </svg> </div> </div> "," </ha-card> "])),this._config.title,void 0!==pe||n||c||l?(0,k.qy)(q||(q=(0,o.A)(['<div class="row"> '," "," "," </div>"])),void 0===pe?(0,k.qy)(z||(z=(0,o.A)(['<div class="spacer"></div>']))):(0,k.qy)(Z||(Z=(0,o.A)(['<div class="circle-container low-carbon"> <span class="label">','</span> <a class="circle" href="','" target="_blank" rel="noopener no referrer"> <ha-svg-icon .path="','"></ha-svg-icon> ',' kWh </a> <svg width="80" height="30"> <line x1="40" y1="0" x2="40" y2="30"></line> </svg> </div>'])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.low_carbon"),xe,"M17,8C8,10 5.9,16.17 3.82,21.34L5.71,22L6.66,19.7C7.14,19.87 7.64,20 8,20C19,20 22,3 22,3C21,5 14,5.25 9,6.25C4,7.25 2,11.5 2,13.5C2,15.5 3.75,17.25 3.75,17.25C7,8 17,8 17,8Z",(0,w.ZV)(pe||0,this.hass.locale,{maximumFractionDigits:1})),n?(0,k.qy)(D||(D=(0,o.A)(['<div class="circle-container solar"> <span class="label">','</span> <div class="circle"> <ha-svg-icon .path="','"></ha-svg-icon> '," kWh </div> </div>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.solar"),"M11.45,2V5.55L15,3.77L11.45,2M10.45,8L8,10.46L11.75,11.71L10.45,8M2,11.45L3.77,15L5.55,11.45H2M10,2H2V10C2.57,10.17 3.17,10.25 3.77,10.25C7.35,10.26 10.26,7.35 10.27,3.75C10.26,3.16 10.17,2.57 10,2M17,22V16H14L19,7V13H22L17,22Z",(0,w.ZV)(f||0,this.hass.locale,{maximumFractionDigits:1})):c||l?(0,k.qy)(J||(J=(0,o.A)(['<div class="spacer"></div>']))):"",c?(0,k.qy)(S||(S=(0,o.A)(['<div class="circle-container gas"> <span class="label">','</span> <div class="circle"> <ha-svg-icon .path="','"></ha-svg-icon> '," ",' </div> <svg width="80" height="30"> <path d="M40 0 v30" id="gas"/> '," </svg> </div>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.gas"),"M17.66 11.2C17.43 10.9 17.15 10.64 16.89 10.38C16.22 9.78 15.46 9.35 14.82 8.72C13.33 7.26 13 4.85 13.95 3C13 3.23 12.17 3.75 11.46 4.32C8.87 6.4 7.85 10.07 9.07 13.22C9.11 13.32 9.15 13.42 9.15 13.55C9.15 13.77 9 13.97 8.8 14.05C8.57 14.15 8.33 14.09 8.14 13.93C8.08 13.88 8.04 13.83 8 13.76C6.87 12.33 6.69 10.28 7.45 8.64C5.78 10 4.87 12.3 5 14.47C5.06 14.97 5.12 15.47 5.29 15.97C5.43 16.57 5.7 17.17 6 17.7C7.08 19.43 8.95 20.67 10.96 20.92C13.1 21.19 15.39 20.8 17.03 19.32C18.86 17.66 19.5 15 18.56 12.72L18.43 12.46C18.22 12 17.66 11.2 17.66 11.2M14.5 17.5C14.22 17.74 13.76 18 13.4 18.1C12.28 18.5 11.16 17.94 10.5 17.28C11.69 17 12.4 16.12 12.61 15.23C12.78 14.43 12.46 13.77 12.33 13C12.21 12.26 12.23 11.63 12.5 10.94C12.69 11.32 12.89 11.7 13.13 12C13.9 13 15.11 13.44 15.37 14.8C15.41 14.94 15.43 15.08 15.43 15.23C15.46 16.05 15.1 16.95 14.5 17.5H14.5Z",(0,w.ZV)(g||0,this.hass.locale,{maximumFractionDigits:1}),(0,M.KJ)(this.hass,a,this._data.statsMetadata)||"m³",g?(0,k.JW)(P||(P=(0,o.A)(['<circle r="1" class="gas" vector-effect="non-scaling-stroke"> <animateMotion dur="2s" repeatCount="indefinite" calcMode="linear"> <mpath xlink:href="#gas"/> </animateMotion> </circle>']))):""):l?(0,k.qy)(E||(E=(0,o.A)(['<div class="circle-container water"> <span class="label">','</span> <div class="circle"> <ha-svg-icon .path="','"></ha-svg-icon> '," ",' </div> <svg width="80" height="30"> <path d="M40 0 v30" id="water"/> '," </svg> </div>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.water"),ge,(0,w.ZV)(u||0,this.hass.locale,{maximumFractionDigits:1}),(0,M.yM)(this.hass)||"m³",u?(0,k.JW)(N||(N=(0,o.A)(['<circle r="1" class="water" vector-effect="non-scaling-stroke"> <animateMotion dur="2s" repeatCount="indefinite" calcMode="linear"> <mpath xlink:href="#water"/> </animateMotion> </circle>']))):""):(0,k.qy)(Y||(Y=(0,o.A)(['<div class="spacer"></div>'])))):"","M8.28,5.45L6.5,4.55L7.76,2H16.23L17.5,4.55L15.72,5.44L15,4H9L8.28,5.45M18.62,8H14.09L13.3,5H10.7L9.91,8H5.38L4.1,10.55L5.89,11.44L6.62,10H17.38L18.1,11.45L19.89,10.56L18.62,8M17.77,22H15.7L15.46,21.1L12,15.9L8.53,21.1L8.3,22H6.23L9.12,11H11.19L10.83,12.35L12,14.1L13.16,12.35L12.81,11H14.88L17.77,22M11.4,15L10.5,13.65L9.32,18.13L11.4,15M14.68,18.12L13.5,13.64L12.6,15L14.68,18.12Z",null!==b?(0,k.qy)(R||(R=(0,o.A)(['<span class="return"> <ha-svg-icon class="small" .path="','"></ha-svg-icon>'," kWh </span>"])),"M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z",(0,w.ZV)(b,this.hass.locale,{maximumFractionDigits:1})):"",d?(0,k.qy)(j||(j=(0,o.A)(['<ha-svg-icon class="small" .path="','"></ha-svg-icon>'])),"M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"):"",(0,w.ZV)(h,this.hass.locale,{maximumFractionDigits:1}),this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.grid"),(0,_.H)({border:void 0===V&&void 0===ye}),"M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z",(0,w.ZV)(ke,this.hass.locale,{maximumFractionDigits:1}),void 0!==V||void 0!==ye?(0,k.qy)(T||(T=(0,o.A)(["<svg> "," "," ",' <circle class="grid" cx="40" cy="40" r="38" stroke-dasharray="'," ",'" stroke-dashoffset="0" shape-rendering="geometricPrecision"/> </svg>'])),void 0!==V?(0,k.JW)(B||(B=(0,o.A)(['<circle class="solar" cx="40" cy="40" r="38" stroke-dasharray="'," ",'" shape-rendering="geometricPrecision" stroke-dashoffset="-','"/>'])),V,fe-V,fe-V):"",ve?(0,k.JW)(K||(K=(0,o.A)(['<circle class="battery" cx="40" cy="40" r="38" stroke-dasharray="'," ",'" stroke-dashoffset="-','" shape-rendering="geometricPrecision"/>'])),ve,fe-ve,fe-ve-(V||0)):"",ye?(0,k.JW)(O||(O=(0,o.A)(['<circle class="low-carbon" cx="40" cy="40" r="38" stroke-dasharray="'," ",'" stroke-dashoffset="-','" shape-rendering="geometricPrecision"/>'])),ye,fe-ye,fe-ye-(ve||0)-(V||0)):"",null!==(t=be)&&void 0!==t?t:fe-V-(ve||0),void 0!==be?fe-be:V+(ve||0)):"",c&&l?"":(0,k.qy)(U||(U=(0,o.A)(['<span class="label">',"</span>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.home")),s||c&&l?(0,k.qy)($||($=(0,o.A)(['<div class="row"> <div class="spacer"></div> '," "," </div>"])),s?(0,k.qy)(G||(G=(0,o.A)([' <div class="circle-container battery"> <div class="circle"> <ha-svg-icon .path="','"></ha-svg-icon> <span class="battery-in"> <ha-svg-icon class="small" .path="','"></ha-svg-icon>',' kWh</span> <span class="battery-out"> <ha-svg-icon class="small" .path="','"></ha-svg-icon>',' kWh</span> </div> <span class="label">',"</span> </div>"])),"M16 20H8V6H16M16.67 4H15V2H9V4H7.33C6.6 4 6 4.6 6 5.33V20.67C6 21.4 6.6 22 7.33 22H16.67C17.41 22 18 21.41 18 20.67V5.33C18 4.6 17.4 4 16.67 4M15 16H9V19H15V16M15 7H9V10H15V7M15 11.5H9V14.5H15V11.5Z","M11,4H13V16L18.5,10.5L19.92,11.92L12,19.84L4.08,11.92L5.5,10.5L11,16V4Z",(0,w.ZV)(p||0,this.hass.locale,{maximumFractionDigits:1}),"M13,20H11V8L5.5,13.5L4.08,12.08L12,4.16L19.92,12.08L18.5,13.5L13,8V20Z",(0,w.ZV)(y||0,this.hass.locale,{maximumFractionDigits:1}),this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.battery")):(0,k.qy)(I||(I=(0,o.A)(['<div class="spacer"></div>']))),c&&l?(0,k.qy)(Q||(Q=(0,o.A)(['<div class="circle-container water bottom"> <svg width="80" height="30"> <path d="M40 30 v-30" id="water"/> ',' </svg> <div class="circle"> <ha-svg-icon .path="','"></ha-svg-icon> '," ",' </div> <span class="label">',"</span> </div>"])),u?(0,k.JW)(X||(X=(0,o.A)(['<circle r="1" class="water" vector-effect="non-scaling-stroke"> <animateMotion dur="2s" repeatCount="indefinite" calcMode="linear"> <mpath xlink:href="#water"/> </animateMotion> </circle>']))):"",ge,(0,w.ZV)(u||0,this.hass.locale,{maximumFractionDigits:1}),(0,M.yM)(this.hass)||"m³",this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.water")):(0,k.qy)(ee||(ee=(0,o.A)(['<div class="spacer"></div>'])))):"",(0,_.H)({high:s||c&&l}),d&&n?(0,k.JW)(te||(te=(0,o.A)(['<path id="return" class="return" d="M',",0 v15 c0,",' h-20" vector-effect="non-scaling-stroke"></path> '])),s?45:47,s?"35 -10,30 -30,30":"40 -10,35 -30,35"):"",n?(0,k.JW)(re||(re=(0,o.A)(['<path id="solar" class="solar" d="M',",0 v15 c0,",' h20" vector-effect="non-scaling-stroke"></path>'])),s?55:53,s?"35 10,30 30,30":"40 10,35 30,35"):"",s?(0,k.JW)(ae||(ae=(0,o.A)(['<path id="battery-house" class="battery-house" d="M55,100 v-15 c0,-35 10,-30 30,-30 h20" vector-effect="non-scaling-stroke"></path> <path id="battery-grid" class="','" d="M45,100 v-15 c0,-35 -10,-30 -30,-30 h-20" vector-effect="non-scaling-stroke"></path> '])),(0,_.H)({"battery-from-grid":Boolean(x),"battery-to-grid":Boolean(A)})):"",s&&n?(0,k.JW)(ie||(ie=(0,o.A)(['<path id="battery-solar" class="battery-solar" d="M50,0 V100" vector-effect="non-scaling-stroke"></path>']))):"",s?50:n?56:53,b&&n?(0,k.JW)(ne||(ne=(0,o.A)(['<circle r="1" class="return" vector-effect="non-scaling-stroke"> <animateMotion dur="','s" repeatCount="indefinite" calcMode="linear"> <mpath xlink:href="#return"/> </animateMotion> </circle>'])),6-(b-(A||0))/Me*6):"",m?(0,k.JW)(oe||(oe=(0,o.A)(['<circle r="1" class="solar" vector-effect="non-scaling-stroke"> <animateMotion dur="','s" repeatCount="indefinite" calcMode="linear"> <mpath xlink:href="#solar"/> </animateMotion> </circle>'])),6-m/Me*5):"",me?(0,k.JW)(se||(se=(0,o.A)(['<circle r="1" class="grid" vector-effect="non-scaling-stroke"> <animateMotion dur="','s" repeatCount="indefinite" calcMode="linear"> <mpath xlink:href="#grid"/> </animateMotion> </circle>'])),6-me/Me*5):"",C?(0,k.JW)(ce||(ce=(0,o.A)(['<circle r="1" class="battery-solar" vector-effect="non-scaling-stroke"> <animateMotion dur="','s" repeatCount="indefinite" calcMode="linear"> <mpath xlink:href="#battery-solar"/> </animateMotion> </circle>'])),6-C/Me*5):"",H?(0,k.JW)(le||(le=(0,o.A)(['<circle r="1" class="battery-house" vector-effect="non-scaling-stroke"> <animateMotion dur="','s" repeatCount="indefinite" calcMode="linear"> <mpath xlink:href="#battery-house"/> </animateMotion> </circle>'])),6-H/Me*5):"",x?(0,k.JW)(de||(de=(0,o.A)(['<circle r="1" class="battery-from-grid" vector-effect="non-scaling-stroke"> <animateMotion dur="','s" repeatCount="indefinite" keyPoints="1;0" keyTimes="0;1" calcMode="linear"> <mpath xlink:href="#battery-grid"/> </animateMotion> </circle>'])),6-x/Me*5):"",A?(0,k.JW)(he||(he=(0,o.A)(['<circle r="1" class="battery-to-grid" vector-effect="non-scaling-stroke"> <animateMotion dur="','s" repeatCount="indefinite" calcMode="linear"> <mpath xlink:href="#battery-grid"/> </animateMotion> </circle>'])),6-A/Me*5):"",this._config.link_dashboard?(0,k.qy)(ue||(ue=(0,o.A)([' <div class="card-actions"> <a href="/energy"><mwc-button> '," </mwc-button></a> </div> "])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_distribution.go_to_energy_dashboard")):"")}},{kind:"field",static:!0,key:"styles",value:function(){return(0,k.AH)(ve||(ve=(0,o.A)([":host{--mdc-icon-size:24px}ha-card{min-width:210px}.card-content{position:relative;direction:ltr}.lines{position:absolute;bottom:0;left:0;width:100%;height:146px;display:flex;justify-content:center;padding:0 16px 16px;box-sizing:border-box}.lines.high{bottom:100px;height:156px}.lines svg{width:calc(100% - 160px);height:100%;max-width:340px}.row{display:flex;justify-content:space-between;max-width:500px;margin:0 auto}.circle-container{display:flex;flex-direction:column;align-items:center}.circle-container.low-carbon{margin-right:4px}.circle-container.solar{margin:0 4px;height:130px}.circle-container.gas{margin-left:4px;height:130px}.circle-container.water{margin-left:4px;height:130px}.circle-container.water.bottom{position:relative;top:-20px;margin-bottom:-20px}.circle-container.battery{height:110px;justify-content:flex-end}.spacer{width:84px}.circle{width:80px;height:80px;border-radius:50%;box-sizing:border-box;border:2px solid;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-size:12px;line-height:12px;position:relative;text-decoration:none;color:var(--primary-text-color)}ha-svg-icon{padding-bottom:2px}ha-svg-icon.small{--mdc-icon-size:12px}.label{color:var(--secondary-text-color);font-size:12px;opacity:1;height:20px;overflow:hidden;text-overflow:ellipsis;max-width:80px;white-space:nowrap}line,path{stroke:var(--primary-text-color);stroke-width:1;fill:none}.circle svg{position:absolute;fill:none;stroke-width:4px;width:100%;height:100%;top:0;left:0}.gas circle,.gas path{stroke:var(--energy-gas-color)}circle.gas{stroke-width:4;fill:var(--energy-gas-color)}.gas .circle{border-color:var(--energy-gas-color)}.water circle,.water path{stroke:var(--energy-water-color)}circle.water{stroke-width:4;fill:var(--energy-water-color)}.water .circle{border-color:var(--energy-water-color)}.low-carbon line{stroke:var(--energy-non-fossil-color)}.low-carbon .circle{border-color:var(--energy-non-fossil-color)}.low-carbon ha-svg-icon{color:var(--energy-non-fossil-color)}circle.low-carbon{stroke:var(--energy-non-fossil-color);fill:var(--energy-non-fossil-color)}.solar .circle{border-color:var(--energy-solar-color)}circle.solar,path.solar{stroke:var(--energy-solar-color)}circle.solar{stroke-width:4;fill:var(--energy-solar-color)}.battery .circle{border-color:var(--energy-battery-in-color)}circle.battery,path.battery{stroke:var(--energy-battery-out-color)}circle.battery-house,path.battery-house{stroke:var(--energy-battery-out-color)}circle.battery-house{stroke-width:4;fill:var(--energy-battery-out-color)}circle.battery-solar,path.battery-solar{stroke:var(--energy-battery-in-color)}circle.battery-solar{stroke-width:4;fill:var(--energy-battery-in-color)}.battery-in{color:var(--energy-battery-in-color)}.battery-out{color:var(--energy-battery-out-color)}path.battery-from-grid{stroke:var(--energy-grid-consumption-color)}path.battery-to-grid{stroke:var(--energy-grid-return-color)}circle.battery-to-grid,circle.return,path.return{stroke:var(--energy-grid-return-color)}circle.battery-to-grid,circle.return{stroke-width:4;fill:var(--energy-grid-return-color)}.return{color:var(--energy-grid-return-color)}.grid .circle{border-color:var(--energy-grid-consumption-color)}.consumption{color:var(--energy-grid-consumption-color)}circle.battery-from-grid,circle.grid,path.grid{stroke:var(--energy-grid-consumption-color)}circle.battery-from-grid,circle.grid{stroke-width:4;fill:var(--energy-grid-consumption-color)}.home .circle{border-width:0;border-color:var(--primary-color)}.home .circle.border{border-width:2px}.circle svg circle{animation:rotate-in .6s ease-in;transition:stroke-dashoffset .4s,stroke-dasharray .4s;fill:none}@keyframes rotate-in{from{stroke-dashoffset:238.76104;stroke-dasharray:238.76104}}.card-actions a{text-decoration:none}"])))}}]}}),(0,A.E)(k.WF)),n(),e.next=66;break;case 63:e.prev=63,e.t2=e.catch(0),n(e.t2);case 66:case"end":return e.stop()}}),e,null,[[0,63]])})));return function(t,r){return e.apply(this,arguments)}}())},94061:function(e,t,r){r.d(t,{f:function(){return n}});var a=r(74396),i=r(86174);function n(e,t){var r=(0,a.a)(e);return isNaN(t)?(0,i.w)(e,NaN):t?(r.setDate(r.getDate()+t),r):r}},84749:function(e,t,r){r.d(t,{L:function(){return n}});var a=r(87930),i=r(49518);function n(e,t){return(0,a.A)(e,t*i.s0)}},87930:function(e,t,r){r.d(t,{A:function(){return n}});var a=r(74396),i=r(86174);function n(e,t){var r=+(0,a.a)(e);return(0,i.w)(e,r+t)}},39937:function(e,t,r){r.d(t,{P:function(){return n}});var a=r(74396),i=r(86174);function n(e,t){var r=(0,a.a)(e);if(isNaN(t))return(0,i.w)(e,NaN);if(!t)return r;var n=r.getDate(),o=(0,i.w)(e,r.getTime());return o.setMonth(r.getMonth()+t+1,0),n>=o.getDate()?o:(r.setFullYear(o.getFullYear(),o.getMonth(),n),r)}},10871:function(e,t,r){r.d(t,{z:function(){return i}});var a=r(74396);function i(e,t){var r=(0,a.a)(e),i=(0,a.a)(t),n=r.getTime()-i.getTime();return n<0?-1:n>0?1:n}},23177:function(e,t,r){r.d(t,{W:function(){return s}});r(650);var a=r(10871),i=r(74396);function n(e,t){var r=(0,i.a)(e),a=(0,i.a)(t);return 12*(r.getFullYear()-a.getFullYear())+(r.getMonth()-a.getMonth())}var o=r(57442);function s(e,t){var r,s=(0,i.a)(e),c=(0,i.a)(t),l=(0,a.z)(s,c),d=Math.abs(n(s,c));if(d<1)r=0;else{1===s.getMonth()&&s.getDate()>27&&s.setDate(30),s.setMonth(s.getMonth()-l*d);var h=(0,a.z)(s,c)===-l;(0,o.c)((0,i.a)(e))&&1===d&&1===(0,a.z)(e,c)&&(h=!1),r=l*(d-Number(h))}return 0===r?0:r}},79113:function(e,t,r){r.d(t,{D:function(){return i}});var a=r(74396);function i(e){var t=(0,a.a)(e);return t.setHours(23,59,59,999),t}},3889:function(e,t,r){r.d(t,{p:function(){return i}});var a=r(74396);function i(e){var t=(0,a.a)(e),r=t.getMonth();return t.setFullYear(t.getFullYear(),r+1,0),t.setHours(23,59,59,999),t}},72502:function(e,t,r){r.d(t,{e:function(){return i}});var a=r(74396);function i(e){return 1===(0,a.a)(e).getDate()}},57442:function(e,t,r){r.d(t,{c:function(){return o}});var a=r(79113),i=r(3889),n=r(74396);function o(e){var t=(0,n.a)(e);return+(0,a.D)(t)==+(0,i.p)(t)}}}]);
//# sourceMappingURL=4429.v1mT1cJIYV4.js.map