"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[50699],{87565:function(t,e,i){i.d(e,{h:function(){return y}});var n=i(94881),s=i(1781),a=i(6238),r=i(89231),o=i(36683),c=i(29864),h=i(83647),l=i(76513),u=i(196),d=i(51497),f=i(48678),p=function(t){function e(){return(0,r.A)(this,e),(0,c.A)(this,e,arguments)}return(0,h.A)(e,t),(0,o.A)(e)}(d.L);p.styles=[f.R],p=(0,l.__decorate)([(0,u.EM)("mwc-checkbox")],p);var v,k,m,g=i(40924),_=i(69760),y=function(t){function e(){var t;return(0,r.A)(this,e),(t=(0,c.A)(this,e,arguments)).left=!1,t.graphic="control",t}return(0,h.A)(e,t),(0,o.A)(e,[{key:"render",value:function(){var t={"mdc-deprecated-list-item__graphic":this.left,"mdc-deprecated-list-item__meta":!this.left},e=this.renderText(),i=this.graphic&&"control"!==this.graphic&&!this.left?this.renderGraphic():(0,g.qy)(v||(v=(0,a.A)([""]))),n=this.hasMeta&&this.left?this.renderMeta():(0,g.qy)(k||(k=(0,a.A)([""]))),s=this.renderRipple();return(0,g.qy)(m||(m=(0,a.A)([" "," "," ",' <span class="','"> <mwc-checkbox reducedTouchTarget tabindex="','" .checked="','" ?disabled="','" @change="','"> </mwc-checkbox> </span> '," ",""])),s,i,this.left?"":e,(0,_.H)(t),this.tabindex,this.selected,this.disabled,this.onChange,this.left?e:"",n)}},{key:"onChange",value:(i=(0,s.A)((0,n.A)().mark((function t(e){var i;return(0,n.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(i=e.target,this.selected===i.checked){t.next=8;break}return this._skipPropRequest=!0,this.selected=i.checked,t.next=7,this.updateComplete;case 7:this._skipPropRequest=!1;case 8:case"end":return t.stop()}}),t,this)}))),function(t){return i.apply(this,arguments)})}]);var i}(i(46175).J);(0,l.__decorate)([(0,u.P)("slot")],y.prototype,"slotElement",void 0),(0,l.__decorate)([(0,u.P)("mwc-checkbox")],y.prototype,"checkboxElement",void 0),(0,l.__decorate)([(0,u.MZ)({type:Boolean})],y.prototype,"left",void 0),(0,l.__decorate)([(0,u.MZ)({type:String,reflect:!0})],y.prototype,"graphic",void 0)},56220:function(t,e,i){i.d(e,{R:function(){return a}});var n,s=i(6238),a=(0,i(40924).AH)(n||(n=(0,s.A)([":host(:not([twoline])){height:56px}:host(:not([left])) .mdc-deprecated-list-item__meta{height:40px;width:40px}"])))},59151:function(t,e,i){var n,s,a=i(6238),r=i(36683),o=i(89231),c=i(29864),h=i(83647),l=i(8364),u=i(76504),d=i(80792),f=(i(77052),i(650),i(68113),i(58177),i(42416),i(66274),i(84531),i(34290),i(27350),i(40924)),p=i(196),v=i(51150),k=i(25465);(0,l.A)([(0,p.EM)("ha-button-menu")],(function(t,e){var i=function(e){function i(){var e;(0,o.A)(this,i);for(var n=arguments.length,s=new Array(n),a=0;a<n;a++)s[a]=arguments[a];return e=(0,c.A)(this,i,[].concat(s)),t(e),e}return(0,h.A)(i,e),(0,r.A)(i)}(e);return{F:i,d:[{kind:"field",key:k.Xr,value:void 0},{kind:"field",decorators:[(0,p.MZ)()],key:"corner",value:function(){return"BOTTOM_START"}},{kind:"field",decorators:[(0,p.MZ)()],key:"menuCorner",value:function(){return"START"}},{kind:"field",decorators:[(0,p.MZ)({type:Number})],key:"x",value:function(){return null}},{kind:"field",decorators:[(0,p.MZ)({type:Number})],key:"y",value:function(){return null}},{kind:"field",decorators:[(0,p.MZ)({type:Boolean})],key:"multi",value:function(){return!1}},{kind:"field",decorators:[(0,p.MZ)({type:Boolean})],key:"activatable",value:function(){return!1}},{kind:"field",decorators:[(0,p.MZ)({type:Boolean})],key:"disabled",value:function(){return!1}},{kind:"field",decorators:[(0,p.MZ)({type:Boolean})],key:"fixed",value:function(){return!1}},{kind:"field",decorators:[(0,p.MZ)({type:Boolean,attribute:"no-anchor"})],key:"noAnchor",value:function(){return!1}},{kind:"field",decorators:[(0,p.P)("mwc-menu",!0)],key:"_menu",value:void 0},{kind:"get",key:"items",value:function(){var t;return null===(t=this._menu)||void 0===t?void 0:t.items}},{kind:"get",key:"selected",value:function(){var t;return null===(t=this._menu)||void 0===t?void 0:t.selected}},{kind:"method",key:"focus",value:function(){var t,e;null!==(t=this._menu)&&void 0!==t&&t.open?this._menu.focusItemAtIndex(0):null===(e=this._triggerButton)||void 0===e||e.focus()}},{kind:"method",key:"render",value:function(){return(0,f.qy)(n||(n=(0,a.A)([' <div @click="','"> <slot name="trigger" @slotchange="','"></slot> </div> <mwc-menu .corner="','" .menuCorner="','" .fixed="','" .multi="','" .activatable="','" .y="','" .x="','"> <slot></slot> </mwc-menu> '])),this._handleClick,this._setTriggerAria,this.corner,this.menuCorner,this.fixed,this.multi,this.activatable,this.y,this.x)}},{kind:"method",key:"firstUpdated",value:function(t){var e=this;(0,u.A)((0,d.A)(i.prototype),"firstUpdated",this).call(this,t),"rtl"===v.G.document.dir&&this.updateComplete.then((function(){e.querySelectorAll("mwc-list-item").forEach((function(t){var e=document.createElement("style");e.innerHTML="span.material-icons:first-of-type { margin-left: var(--mdc-list-item-graphic-margin, 32px) !important; margin-right: 0px !important;}",t.shadowRoot.appendChild(e)}))}))}},{kind:"method",key:"_handleClick",value:function(){this.disabled||(this._menu.anchor=this.noAnchor?null:this,this._menu.show())}},{kind:"get",key:"_triggerButton",value:function(){return this.querySelector('ha-icon-button[slot="trigger"], mwc-button[slot="trigger"]')}},{kind:"method",key:"_setTriggerAria",value:function(){this._triggerButton&&(this._triggerButton.ariaHasPopup="menu")}},{kind:"get",static:!0,key:"styles",value:function(){return(0,f.AH)(s||(s=(0,a.A)([":host{display:inline-block;position:relative}::slotted([disabled]){color:var(--disabled-text-color)}"])))}}]}}),f.WF)},24630:function(t,e,i){var n,s=i(6238),a=i(94881),r=i(1781),o=i(36683),c=i(89231),h=i(29864),l=i(83647),u=i(8364),d=i(76504),f=i(80792),p=(i(77052),i(40924)),v=i(87565),k=i(56220),m=i(45592),g=i(196),_=i(77664);(0,u.A)([(0,g.EM)("ha-check-list-item")],(function(t,e){var i,u=function(e){function i(){var e;(0,c.A)(this,i);for(var n=arguments.length,s=new Array(n),a=0;a<n;a++)s[a]=arguments[a];return e=(0,h.A)(this,i,[].concat(s)),t(e),e}return(0,l.A)(i,e),(0,o.A)(i)}(e);return{F:u,d:[{kind:"method",key:"onChange",value:(i=(0,r.A)((0,a.A)().mark((function t(e){return(0,a.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:(0,d.A)((0,f.A)(u.prototype),"onChange",this).call(this,e),(0,_.r)(this,e.type);case 2:case"end":return t.stop()}}),t,this)}))),function(t){return i.apply(this,arguments)})},{kind:"field",static:!0,key:"styles",value:function(){return[m.R,k.R,(0,p.AH)(n||(n=(0,s.A)([":host{--mdc-theme-secondary:var(--primary-color)}:host([graphic=avatar]) .mdc-deprecated-list-item__graphic,:host([graphic=control]) .mdc-deprecated-list-item__graphic,:host([graphic=large]) .mdc-deprecated-list-item__graphic,:host([graphic=medium]) .mdc-deprecated-list-item__graphic{margin-inline-end:var(--mdc-list-item-graphic-margin,16px);margin-inline-start:0px;direction:var(--direction)}.mdc-deprecated-list-item__meta{flex-shrink:0;direction:var(--direction);margin-inline-start:auto;margin-inline-end:0}.mdc-deprecated-list-item__graphic{margin-top:var(--check-list-item-graphic-margin-top)}:host([graphic=icon]) .mdc-deprecated-list-item__graphic{margin-inline-start:0;margin-inline-end:var(--mdc-list-item-graphic-margin,32px)}"])))]}}]}}),v.h)},94027:function(t,e,i){i.d(e,{E:function(){return d}});var n=i(66123),s=i(36683),a=i(89231),r=i(29864),o=i(83647),c=i(8364),h=i(76504),l=i(80792),u=(i(77052),i(53501),i(21950),i(68113),i(55888),i(34517),i(66274),i(22836),i(8339),i(196)),d=function(t){var e=(0,c.A)(null,(function(t,e){var i=function(e){function i(){var e;(0,a.A)(this,i);for(var n=arguments.length,s=new Array(n),o=0;o<n;o++)s[o]=arguments[o];return e=(0,r.A)(this,i,[].concat(s)),t(e),e}return(0,o.A)(i,e),(0,s.A)(i)}(e);return{F:i,d:[{kind:"field",decorators:[(0,u.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:void 0},{kind:"field",key:"__unsubs",value:void 0},{kind:"method",key:"connectedCallback",value:function(){(0,h.A)((0,l.A)(i.prototype),"connectedCallback",this).call(this),this.__checkSubscribed()}},{kind:"method",key:"disconnectedCallback",value:function(){if((0,h.A)((0,l.A)(i.prototype),"disconnectedCallback",this).call(this),this.__unsubs){for(;this.__unsubs.length;){var t=this.__unsubs.pop();t instanceof Promise?t.then((function(t){return t()})):t()}this.__unsubs=void 0}}},{kind:"method",key:"updated",value:function(t){if((0,h.A)((0,l.A)(i.prototype),"updated",this).call(this,t),t.has("hass"))this.__checkSubscribed();else if(this.hassSubscribeRequiredHostProps){var e,s=(0,n.A)(t.keys());try{for(s.s();!(e=s.n()).done;){var a=e.value;if(this.hassSubscribeRequiredHostProps.includes(a))return void this.__checkSubscribed()}}catch(r){s.e(r)}finally{s.f()}}}},{kind:"method",key:"hassSubscribe",value:function(){return[]}},{kind:"method",key:"__checkSubscribed",value:function(){var t,e=this;void 0!==this.__unsubs||!this.isConnected||void 0===this.hass||null!==(t=this.hassSubscribeRequiredHostProps)&&void 0!==t&&t.some((function(t){return void 0===e[t]}))||(this.__unsubs=this.hassSubscribe())}}]}}),t);return e}},23929:function(t,e,i){var n=i(1781).A,s=i(94881).A;i.a(t,function(){var t=n(s().mark((function t(n,a){var r,o,c,h,l,u,d,f,p,v,k,m,g,_,y;return s().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(t.prev=0,i.r(e),i.d(e,{HuiEnergyDateSelectionCard:function(){return y}}),r=i(6238),o=i(36683),c=i(89231),h=i(29864),l=i(83647),u=i(8364),d=i(77052),f=i(40924),p=i(196),v=i(15821),k=i(24168),!(m=n([k])).then){t.next=23;break}return t.next=19,m;case 19:t.t1=t.sent,t.t0=(0,t.t1)(),t.next=24;break;case 23:t.t0=m;case 24:k=t.t0[0],y=(0,u.A)([(0,p.EM)("hui-energy-date-selection-card")],(function(t,e){var i=function(e){function i(){var e;(0,c.A)(this,i);for(var n=arguments.length,s=new Array(n),a=0;a<n;a++)s[a]=arguments[a];return e=(0,h.A)(this,i,[].concat(s)),t(e),e}return(0,l.A)(i,e),(0,o.A)(i)}(e);return{F:i,d:[{kind:"field",decorators:[(0,p.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,p.wk)()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function(){return 1}},{kind:"method",key:"getLayoutOptions",value:function(){return{grid_rows:1,grid_columns:4}}},{kind:"method",key:"setConfig",value:function(t){this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return(0,v.xP)(this,t)||t.size>1||!t.has("hass")}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?(0,f.qy)(g||(g=(0,r.A)([' <ha-card> <div class="card-content"> <hui-energy-period-selector .hass="','" .collectionKey="','"></hui-energy-period-selector> </div> </ha-card> '])),this.hass,this._config.collection_key):f.s6}},{kind:"get",static:!0,key:"styles",value:function(){return(0,f.AH)(_||(_=(0,r.A)(["\n    :host {\n      ha-card {\n        height: 100%;\n        display: flex;\n        flex-direction: column;\n        justify-content: center;\n      }\n      .padded {\n        padding-left: 16px !important;\n        padding-inline-start: 16px !important;\n        padding-inline-end: initial !important;\n      }\n    "])))}}]}}),f.WF),a(),t.next=32;break;case 29:t.prev=29,t.t2=t.catch(0),a(t.t2);case 32:case"end":return t.stop()}}),t,null,[[0,29]])})));return function(e,i){return t.apply(this,arguments)}}())},24168:function(t,e,i){var n=i(1781).A,s=i(94881).A;i.a(t,function(){var t=n(s().mark((function t(e,n){var a,r,o,c,h,l,u,d,f,p,v,k,m,g,_,y,b,A,w,D,x,C,M,O,S,z,P,E,R,q,T,Z,H,B,F,W,U,N,j,K,L,Y,$,G,I,Q;return s().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(t.prev=0,a=i(6238),r=i(23141),o=i(94881),c=i(1781),h=i(36683),l=i(89231),u=i(29864),d=i(83647),f=i(8364),p=i(76504),v=i(80792),k=i(74808),m=i(77052),i(34069),g=i(93352),_=i(79113),y=i(53026),b=i(56994),A=i(70249),w=i(21748),D=i(3889),x=i(77354),C=i(92627),M=i(11213),O=i(27890),S=i(81438),z=i(72502),P=i(57442),E=i(23177),R=i(39937),q=i(94061),T=i(42180),Z=i(40924),H=i(196),B=i(45081),F=i(72586),W=i(15263),U=i(77396),N=i(47394),i(59151),i(24630),j=i(20534),i(22609),i(84297),K=i(41525),L=i(94027),!(Y=e([k,F,W,U,j,K])).then){t.next=56;break}return t.next=52,Y;case 52:t.t1=t.sent,t.t0=(0,t.t1)(),t.next=57;break;case 56:t.t0=Y;case 57:$=t.t0,k=$[0],F=$[1],W=$[2],U=$[3],j=$[4],K=$[5],(0,f.A)([(0,H.EM)("hui-energy-period-selector")],(function(t,e){var i,n=function(e){function i(){var e;(0,l.A)(this,i);for(var n=arguments.length,s=new Array(n),a=0;a<n;a++)s[a]=arguments[a];return e=(0,u.A)(this,i,[].concat(s)),t(e),e}return(0,d.A)(i,e),(0,h.A)(i)}(e);return{F:n,d:[{kind:"field",decorators:[(0,H.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,H.MZ)()],key:"collectionKey",value:void 0},{kind:"field",decorators:[(0,H.MZ)({type:Boolean,reflect:!0})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,H.wk)()],key:"_startDate",value:void 0},{kind:"field",decorators:[(0,H.wk)()],key:"_endDate",value:void 0},{kind:"field",decorators:[(0,H.wk)()],key:"_ranges",value:function(){return{}}},{kind:"field",decorators:[(0,H.wk)()],key:"_compare",value:function(){return!1}},{kind:"field",key:"_resizeObserver",value:void 0},{kind:"method",key:"hassSubscribe",value:function(){var t=this;return[(0,K.tb)(this.hass,{key:this.collectionKey}).subscribe((function(e){return t._updateDates(e)}))]}},{kind:"method",key:"_measure",value:function(){this.narrow=this.offsetWidth<450}},{kind:"method",key:"_attachObserver",value:(i=(0,c.A)((0,o.A)().mark((function t(){var e=this;return(0,o.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:this._resizeObserver||(this._resizeObserver=new ResizeObserver((0,N.s)((function(){return e._measure()}),250,!1))),this._resizeObserver.observe(this);case 2:case"end":return t.stop()}}),t,this)}))),function(){return i.apply(this,arguments)})},{kind:"method",key:"firstUpdated",value:function(){this._attachObserver()}},{kind:"method",key:"connectedCallback",value:function(){var t=this;(0,p.A)((0,v.A)(n.prototype),"connectedCallback",this).call(this),this.updateComplete.then((function(){return t._attachObserver()}))}},{kind:"method",key:"disconnectedCallback",value:function(){(0,p.A)((0,v.A)(n.prototype),"disconnectedCallback",this).call(this),this._resizeObserver&&this._resizeObserver.disconnect()}},{kind:"method",key:"willUpdate",value:function(t){var e,i;if((0,p.A)((0,v.A)(n.prototype),"willUpdate",this).call(this,t),this.hasUpdated||this._measure(),!this.hasUpdated||t.has("hass")&&(null===(e=this.hass)||void 0===e?void 0:e.localize)!==(null===(i=t.get("hass"))||void 0===i?void 0:i.localize)){var s=new Date,a=(0,W.PE)(this.hass.locale);this._ranges=(0,r.A)((0,r.A)((0,r.A)((0,r.A)((0,r.A)((0,r.A)({},this.hass.localize("ui.components.date-range-picker.ranges.today"),[(0,F.ol)(s,g.o,this.hass.locale,this.hass.config,{weekStartsOn:a}),(0,F.ol)(s,_.D,this.hass.locale,this.hass.config,{weekStartsOn:a})]),this.hass.localize("ui.components.date-range-picker.ranges.yesterday"),[(0,F.ol)((0,F.ol)(s,y.e,this.hass.locale,this.hass.config,1),g.o,this.hass.locale,this.hass.config,{weekStartsOn:a}),(0,F.ol)((0,F.ol)(s,y.e,this.hass.locale,this.hass.config,1),_.D,this.hass.locale,this.hass.config,{weekStartsOn:a})]),this.hass.localize("ui.components.date-range-picker.ranges.this_week"),[(0,F.ol)(s,b.k,this.hass.locale,this.hass.config,{weekStartsOn:a}),(0,F.ol)(s,A.$,this.hass.locale,this.hass.config,{weekStartsOn:a})]),this.hass.localize("ui.components.date-range-picker.ranges.this_month"),[(0,F.ol)(s,w.w,this.hass.locale,this.hass.config),(0,F.ol)(s,D.p,this.hass.locale,this.hass.config)]),this.hass.localize("ui.components.date-range-picker.ranges.this_quarter"),[(0,F.ol)(s,x.a,this.hass.locale,this.hass.config),(0,F.ol)(s,C.j,this.hass.locale,this.hass.config)]),this.hass.localize("ui.components.date-range-picker.ranges.this_year"),[(0,F.ol)(s,M.D,this.hass.locale,this.hass.config),(0,F.ol)(s,O.Q,this.hass.locale,this.hass.config)])}}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._startDate)return Z.s6;var t=this._simpleRange(this._startDate,this._endDate,this.hass.locale,this.hass.config);return(0,Z.qy)(G||(G=(0,a.A)([' <div class="row"> <div class="label"> ',' </div> <div class="time-handle"> <ha-icon-button-prev .label="','" @click="','"></ha-icon-button-prev> <ha-icon-button-next .label="','" @click="','"></ha-icon-button-next> <ha-date-range-picker .hass="','" .startDate="','" .endDate="','" .ranges="','" @change="','" .timePicker="','" minimal></ha-date-range-picker> </div> ',' <ha-button-menu> <ha-icon-button slot="trigger" .label="','" .path="','"></ha-icon-button> <ha-check-list-item left @request-selected="','" .selected="','"> ',' </ha-check-list-item> <slot name="overflow-menu"></slot> </ha-button-menu> </div> '])),"day"===t?this.narrow?(0,U.kz)(this._startDate,this.hass.locale,this.hass.config):(0,U.Yq)(this._startDate,this.hass.locale,this.hass.config):"month"===t?(0,U.fr)(this._startDate,this.hass.locale,this.hass.config):"year"===t?(0,U.Pm)(this._startDate,this.hass.locale,this.hass.config):"".concat((0,U.sl)(this._startDate,this.hass.locale,this.hass.config)," – ").concat((0,U.sl)(this._endDate||new Date,this.hass.locale,this.hass.config)),this.hass.localize("ui.panel.lovelace.components.energy_period_selector.previous"),this._pickPrevious,this.hass.localize("ui.panel.lovelace.components.energy_period_selector.next"),this._pickNext,this.hass,this._startDate,this._endDate||new Date,this._ranges,this._dateRangeChanged,!1,this.narrow?Z.s6:(0,Z.qy)(I||(I=(0,a.A)(['<mwc-button dense outlined @click="','"> '," </mwc-button>"])),this._pickNow,this.hass.localize("ui.panel.lovelace.components.energy_period_selector.now")),this.hass.localize("ui.common.menu"),"M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z",this._toggleCompare,this._compare,this.hass.localize("ui.panel.lovelace.components.energy_period_selector.compare"))}},{kind:"field",key:"_simpleRange",value:function(){return(0,B.A)((function(t,e,i,n){if(0===(0,S.c)(e,t))return"day";if((0,F.xo)(t,z.e,i,n)&&(0,F.xo)(e,P.c,i,n)){if(0===(0,F.EO)(e,t,E.W,i,n))return"month";if(2===(0,F.EO)(e,t,E.W,i,n)&&t.getMonth()%3==0)return"quarter"}return(0,F.xo)(t,z.e,i,n)&&(0,F.xo)(e,P.c,i,n)&&11===(0,F.EO)(e,t,E.W,i,n)?"year":"other"}))}},{kind:"method",key:"_updateCollectionPeriod",value:function(){var t=(0,K.tb)(this.hass,{key:this.collectionKey});t.setPeriod(this._startDate,this._endDate),t.refresh()}},{kind:"method",key:"_dateRangeChanged",value:function(t){var e=(0,W.PE)(this.hass.locale);this._startDate=(0,F.ol)(t.detail.startDate,g.o,this.hass.locale,this.hass.config,{weekStartsOn:e}),this._endDate=(0,F.ol)(t.detail.endDate,_.D,this.hass.locale,this.hass.config,{weekStartsOn:e}),this._updateCollectionPeriod()}},{kind:"method",key:"_pickNow",value:function(){if(this._startDate){var t=this._simpleRange(this._startDate,this._endDate,this.hass.locale,this.hass.config),e=new Date;if("month"===t)this._startDate=(0,F.ol)(e,w.w,this.hass.locale,this.hass.config),this._endDate=(0,F.ol)(e,D.p,this.hass.locale,this.hass.config);else if("quarter"===t)this._startDate=(0,F.ol)(e,x.a,this.hass.locale,this.hass.config),this._endDate=(0,F.ol)(e,C.j,this.hass.locale,this.hass.config);else if("year"===t)this._startDate=(0,F.ol)(e,M.D,this.hass.locale,this.hass.config),this._endDate=(0,F.ol)(e,O.Q,this.hass.locale,this.hass.config);else{var i=(0,W.PE)(this.hass.locale),n=(0,F.ol)(this._endDate,b.k,this.hass.locale,this.hass.config,{weekStartsOn:i}),s=(0,F.ol)(this._endDate,A.$,this.hass.locale,this.hass.config,{weekStartsOn:i});if(this._startDate.getTime()===n.getTime()&&this._endDate.getTime()===s.getTime())this._startDate=(0,F.ol)(e,b.k,this.hass.locale,this.hass.config,{weekStartsOn:i}),this._endDate=(0,F.ol)(e,A.$,this.hass.locale,this.hass.config,{weekStartsOn:i});else{var a=(0,F.EO)(this._endDate,this._startDate,S.c,this.hass.locale,this.hass.config);this._startDate=(0,F.ol)((0,F.ol)(e,y.e,this.hass.locale,this.hass.config,a),g.o,this.hass.locale,this.hass.config,{weekStartsOn:i}),this._endDate=(0,F.ol)(e,_.D,this.hass.locale,this.hass.config,{weekStartsOn:i})}}this._updateCollectionPeriod()}}},{kind:"method",key:"_pickPrevious",value:function(){this._shift(!1)}},{kind:"method",key:"_pickNext",value:function(){this._shift(!0)}},{kind:"method",key:"_shift",value:function(t){if(this._startDate){var e,i;if((0,F.xo)(this._startDate,z.e,this.hass.locale,this.hass.config)&&(0,F.xo)(this._endDate,P.c,this.hass.locale,this.hass.config)){var n=((0,F.EO)(this._endDate,this._startDate,E.W,this.hass.locale,this.hass.config)+1)*(t?1:-1);e=(0,F.ol)(this._startDate,R.P,this.hass.locale,this.hass.config,n),i=(0,F.ol)((0,F.ol)(this._endDate,R.P,this.hass.locale,this.hass.config,n),D.p,this.hass.locale,this.hass.config)}else{var s=((0,F.EO)(this._endDate,this._startDate,S.c,this.hass.locale,this.hass.config)+1)*(t?1:-1);e=(0,F.ol)(this._startDate,q.f,this.hass.locale,this.hass.config,s),i=(0,F.ol)(this._endDate,q.f,this.hass.locale,this.hass.config,s)}this._startDate=e,this._endDate=i,this._updateCollectionPeriod()}}},{kind:"method",key:"_updateDates",value:function(t){this._compare=void 0!==t.startCompare,this._startDate=t.start,this._endDate=t.end||(0,T.o)()}},{kind:"method",key:"_toggleCompare",value:function(t){if("interaction"===t.detail.source){this._compare=t.detail.selected;var e=(0,K.tb)(this.hass,{key:this.collectionKey});e.setCompare(this._compare),e.refresh()}}},{kind:"get",static:!0,key:"styles",value:function(){return(0,Z.AH)(Q||(Q=(0,a.A)([".row{display:flex;align-items:center}:host .time-handle{display:flex;justify-content:flex-end;align-items:center}:host([narrow]) .time-handle{margin-left:auto;margin-inline-start:auto;margin-inline-end:initial}.label{display:flex;align-items:center;justify-content:flex-end;font-size:20px;margin-left:auto;margin-inline-start:auto;margin-inline-end:initial}:host([narrow]) .label{margin-left:unset;margin-inline-start:unset;margin-inline-end:initial}mwc-button{margin-left:8px;margin-inline-start:8px;margin-inline-end:initial;flex-shrink:0;--mdc-button-outline-color:currentColor;--primary-color:currentColor;--mdc-theme-primary:currentColor;--mdc-theme-on-primary:currentColor;--mdc-button-disabled-outline-color:var(--disabled-text-color);--mdc-button-disabled-ink-color:var(--disabled-text-color)}"])))}}]}}),(0,L.E)(Z.WF)),n(),t.next=72;break;case 69:t.prev=69,t.t2=t.catch(0),n(t.t2);case 72:case"end":return t.stop()}}),t,null,[[0,69]])})));return function(e,i){return t.apply(this,arguments)}}())},90651:function(t,e,i){i(87568)({target:"Reflect",stat:!0},{ownKeys:i(46757)})},84749:function(t,e,i){i.d(e,{L:function(){return a}});var n=i(87930),s=i(49518);function a(t,e){return(0,n.A)(t,e*s.s0)}},87930:function(t,e,i){i.d(e,{A:function(){return a}});var n=i(74396),s=i(86174);function a(t,e){var i=+(0,n.a)(t);return(0,s.w)(t,i+e)}},10871:function(t,e,i){i.d(e,{z:function(){return s}});var n=i(74396);function s(t,e){var i=(0,n.a)(t),s=(0,n.a)(e),a=i.getTime()-s.getTime();return a<0?-1:a>0?1:a}},23177:function(t,e,i){i.d(e,{W:function(){return o}});i(650);var n=i(10871),s=i(74396);function a(t,e){var i=(0,s.a)(t),n=(0,s.a)(e);return 12*(i.getFullYear()-n.getFullYear())+(i.getMonth()-n.getMonth())}var r=i(57442);function o(t,e){var i,o=(0,s.a)(t),c=(0,s.a)(e),h=(0,n.z)(o,c),l=Math.abs(a(o,c));if(l<1)i=0;else{1===o.getMonth()&&o.getDate()>27&&o.setDate(30),o.setMonth(o.getMonth()-h*l);var u=(0,n.z)(o,c)===-h;(0,r.c)((0,s.a)(t))&&1===l&&1===(0,n.z)(t,c)&&(u=!1),i=h*(l-Number(u))}return 0===i?0:i}},92627:function(t,e,i){i.d(e,{j:function(){return s}});var n=i(74396);function s(t){var e=(0,n.a)(t),i=e.getMonth(),s=i-i%3+3;return e.setMonth(s,0),e.setHours(23,59,59,999),e}},42180:function(t,e,i){i.d(e,{o:function(){return s}});var n=i(79113);function s(){return(0,n.D)(Date.now())}},72502:function(t,e,i){i.d(e,{e:function(){return s}});var n=i(74396);function s(t){return 1===(0,n.a)(t).getDate()}},57442:function(t,e,i){i.d(e,{c:function(){return r}});var n=i(79113),s=i(3889),a=i(74396);function r(t){var e=(0,a.a)(t);return+(0,n.D)(e)==+(0,s.p)(e)}},77354:function(t,e,i){i.d(e,{a:function(){return s}});var n=i(74396);function s(t){var e=(0,n.a)(t),i=e.getMonth(),s=i-i%3;return e.setMonth(s,1),e.setHours(0,0,0,0),e}},53026:function(t,e,i){i.d(e,{e:function(){return s}});var n=i(94061);function s(t,e){return(0,n.f)(t,-e)}}}]);
//# sourceMappingURL=50699.NBwgWTFvxEQ.js.map