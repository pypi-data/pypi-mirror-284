"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[32630,23141],{87653:function(t,e,i){i.d(e,{ZS:function(){return v},is:function(){return p.i}});var n,r,o=i(89231),a=i(36683),s=i(29864),c=i(76504),l=i(80792),d=i(83647),h=(i(35848),i(56262),i(76513)),u=i(196),p=i(71086),f=null!==(r=null===(n=window.ShadyDOM)||void 0===n?void 0:n.inUse)&&void 0!==r&&r,v=function(t){function e(){var t;return(0,o.A)(this,e),(t=(0,s.A)(this,e,arguments)).disabled=!1,t.containingForm=null,t.formDataListener=function(e){t.disabled||t.setFormData(e.formData)},t}return(0,d.A)(e,t),(0,a.A)(e,[{key:"findFormElement",value:function(){if(!this.shadowRoot||f)return null;for(var t=this.getRootNode().querySelectorAll("form"),e=0,i=Array.from(t);e<i.length;e++){var n=i[e];if(n.contains(this))return n}return null}},{key:"connectedCallback",value:function(){var t;(0,c.A)((0,l.A)(e.prototype),"connectedCallback",this).call(this),this.containingForm=this.findFormElement(),null===(t=this.containingForm)||void 0===t||t.addEventListener("formdata",this.formDataListener)}},{key:"disconnectedCallback",value:function(){var t;(0,c.A)((0,l.A)(e.prototype),"disconnectedCallback",this).call(this),null===(t=this.containingForm)||void 0===t||t.removeEventListener("formdata",this.formDataListener),this.containingForm=null}},{key:"click",value:function(){this.formElement&&!this.disabled&&(this.formElement.focus(),this.formElement.click())}},{key:"firstUpdated",value:function(){var t=this;(0,c.A)((0,l.A)(e.prototype),"firstUpdated",this).call(this),this.shadowRoot&&this.mdcRoot.addEventListener("change",(function(e){t.dispatchEvent(new Event("change",e))}))}}])}(p.O);v.shadowRootOptions={mode:"open",delegatesFocus:!0},(0,h.__decorate)([(0,u.MZ)({type:Boolean})],v.prototype,"disabled",void 0)},87565:function(t,e,i){i.d(e,{h:function(){return b}});var n=i(94881),r=i(1781),o=i(6238),a=i(89231),s=i(36683),c=i(29864),l=i(83647),d=i(76513),h=i(196),u=i(51497),p=i(48678),f=function(t){function e(){return(0,a.A)(this,e),(0,c.A)(this,e,arguments)}return(0,l.A)(e,t),(0,s.A)(e)}(u.L);f.styles=[p.R],f=(0,d.__decorate)([(0,h.EM)("mwc-checkbox")],f);var v,m,g,k=i(40924),y=i(69760),b=function(t){function e(){var t;return(0,a.A)(this,e),(t=(0,c.A)(this,e,arguments)).left=!1,t.graphic="control",t}return(0,l.A)(e,t),(0,s.A)(e,[{key:"render",value:function(){var t={"mdc-deprecated-list-item__graphic":this.left,"mdc-deprecated-list-item__meta":!this.left},e=this.renderText(),i=this.graphic&&"control"!==this.graphic&&!this.left?this.renderGraphic():(0,k.qy)(v||(v=(0,o.A)([""]))),n=this.hasMeta&&this.left?this.renderMeta():(0,k.qy)(m||(m=(0,o.A)([""]))),r=this.renderRipple();return(0,k.qy)(g||(g=(0,o.A)([" "," "," ",' <span class="','"> <mwc-checkbox reducedTouchTarget tabindex="','" .checked="','" ?disabled="','" @change="','"> </mwc-checkbox> </span> '," ",""])),r,i,this.left?"":e,(0,y.H)(t),this.tabindex,this.selected,this.disabled,this.onChange,this.left?e:"",n)}},{key:"onChange",value:(i=(0,r.A)((0,n.A)().mark((function t(e){var i;return(0,n.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(i=e.target,this.selected===i.checked){t.next=8;break}return this._skipPropRequest=!0,this.selected=i.checked,t.next=7,this.updateComplete;case 7:this._skipPropRequest=!1;case 8:case"end":return t.stop()}}),t,this)}))),function(t){return i.apply(this,arguments)})}]);var i}(i(46175).J);(0,d.__decorate)([(0,h.P)("slot")],b.prototype,"slotElement",void 0),(0,d.__decorate)([(0,h.P)("mwc-checkbox")],b.prototype,"checkboxElement",void 0),(0,d.__decorate)([(0,h.MZ)({type:Boolean})],b.prototype,"left",void 0),(0,d.__decorate)([(0,h.MZ)({type:String,reflect:!0})],b.prototype,"graphic",void 0)},56220:function(t,e,i){i.d(e,{R:function(){return o}});var n,r=i(6238),o=(0,i(40924).AH)(n||(n=(0,r.A)([":host(:not([twoline])){height:56px}:host(:not([left])) .mdc-deprecated-list-item__meta{height:40px;width:40px}"])))},33315:function(t,e,i){i.d(e,{a:function(){return r}});var n=(0,i(81053).n)((function(t){history.replaceState({scrollPosition:t},"")}),300),r=function(t){return function(e){return{kind:"method",placement:"prototype",key:e.key,descriptor:{set:function(t){n(t),this["__".concat(String(e.key))]=t},get:function(){var t;return this["__".concat(String(e.key))]||(null===(t=history.state)||void 0===t?void 0:t.scrollPosition)},enumerable:!0,configurable:!0},finisher:function(i){var n=i.prototype.connectedCallback;i.prototype.connectedCallback=function(){var i=this;n.call(this);var r=this[e.key];r&&this.updateComplete.then((function(){var e=i.renderRoot.querySelector(t);e&&setTimeout((function(){e.scrollTop=r}),0)}))}}}}}},45759:function(t,e,i){i.d(e,{s:function(){return n}});var n=function(t){return!(!t.detail.selected||"property"!==t.detail.source)&&(t.currentTarget.selected=!1,!0)}},81053:function(t,e,i){i.d(e,{n:function(){return n}});var n=function(t,e){var i,n=!(arguments.length>2&&void 0!==arguments[2])||arguments[2],r=!(arguments.length>3&&void 0!==arguments[3])||arguments[3],o=0,a=function(){for(var a=arguments.length,s=new Array(a),c=0;c<a;c++)s[c]=arguments[c];var l=Date.now();o||!1!==n||(o=l);var d=e-(l-o);d<=0||d>e?(i&&(clearTimeout(i),i=void 0),o=l,t.apply(void 0,s)):i||!1===r||(i=window.setTimeout((function(){o=!1===n?0:Date.now(),i=void 0,t.apply(void 0,s)}),d))};return a.cancel=function(){clearTimeout(i),i=void 0,o=0},a}},24630:function(t,e,i){var n,r=i(6238),o=i(94881),a=i(1781),s=i(36683),c=i(89231),l=i(29864),d=i(83647),h=i(8364),u=i(76504),p=i(80792),f=(i(77052),i(40924)),v=i(87565),m=i(56220),g=i(45592),k=i(196),y=i(77664);(0,h.A)([(0,k.EM)("ha-check-list-item")],(function(t,e){var i,h=function(e){function i(){var e;(0,c.A)(this,i);for(var n=arguments.length,r=new Array(n),o=0;o<n;o++)r[o]=arguments[o];return e=(0,l.A)(this,i,[].concat(r)),t(e),e}return(0,d.A)(i,e),(0,s.A)(i)}(e);return{F:h,d:[{kind:"method",key:"onChange",value:(i=(0,a.A)((0,o.A)().mark((function t(e){return(0,o.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:(0,u.A)((0,p.A)(h.prototype),"onChange",this).call(this,e),(0,y.r)(this,e.type);case 2:case"end":return t.stop()}}),t,this)}))),function(t){return i.apply(this,arguments)})},{kind:"field",static:!0,key:"styles",value:function(){return[g.R,m.R,(0,f.AH)(n||(n=(0,r.A)([":host{--mdc-theme-secondary:var(--primary-color)}:host([graphic=avatar]) .mdc-deprecated-list-item__graphic,:host([graphic=control]) .mdc-deprecated-list-item__graphic,:host([graphic=large]) .mdc-deprecated-list-item__graphic,:host([graphic=medium]) .mdc-deprecated-list-item__graphic{margin-inline-end:var(--mdc-list-item-graphic-margin,16px);margin-inline-start:0px;direction:var(--direction)}.mdc-deprecated-list-item__meta{flex-shrink:0;direction:var(--direction);margin-inline-start:auto;margin-inline-end:0}.mdc-deprecated-list-item__graphic{margin-top:var(--check-list-item-graphic-margin-top)}:host([graphic=icon]) .mdc-deprecated-list-item__graphic{margin-inline-start:0;margin-inline-end:var(--mdc-list-item-graphic-margin,32px)}"])))]}}]}}),v.h)},45522:function(t,e,i){i.r(e),i.d(e,{HaIconButtonArrowPrev:function(){return p}});var n,r=i(6238),o=i(36683),a=i(89231),s=i(29864),c=i(83647),l=i(8364),d=(i(77052),i(40924)),h=i(196),u=i(51150),p=(i(12731),(0,l.A)([(0,h.EM)("ha-icon-button-arrow-prev")],(function(t,e){var i=function(e){function i(){var e;(0,a.A)(this,i);for(var n=arguments.length,r=new Array(n),o=0;o<n;o++)r[o]=arguments[o];return e=(0,s.A)(this,i,[].concat(r)),t(e),e}return(0,c.A)(i,e),(0,o.A)(i)}(e);return{F:i,d:[{kind:"field",decorators:[(0,h.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,h.MZ)({type:Boolean})],key:"disabled",value:function(){return!1}},{kind:"field",decorators:[(0,h.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,h.wk)()],key:"_icon",value:function(){return"rtl"===u.G.document.dir?"M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z":"M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"}},{kind:"method",key:"render",value:function(){var t;return(0,d.qy)(n||(n=(0,r.A)([' <ha-icon-button .disabled="','" .label="','" .path="','"></ha-icon-button> '])),this.disabled,this.label||(null===(t=this.hass)||void 0===t?void 0:t.localize("ui.common.back"))||"Back",this._icon)}}]}}),d.WF))},52287:function(t,e,i){var n,r,o,a,s,c=i(6238),l=i(36683),d=i(89231),h=i(29864),u=i(83647),p=i(8364),f=(i(77052),i(40924)),v=i(196),m=i(33315),g=(i(45522),i(78361),i(14126));(0,p.A)([(0,v.EM)("hass-subpage")],(function(t,e){var i=function(e){function i(){var e;(0,d.A)(this,i);for(var n=arguments.length,r=new Array(n),o=0;o<n;o++)r[o]=arguments[o];return e=(0,h.A)(this,i,[].concat(r)),t(e),e}return(0,u.A)(i,e),(0,l.A)(i)}(e);return{F:i,d:[{kind:"field",decorators:[(0,v.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,v.MZ)()],key:"header",value:void 0},{kind:"field",decorators:[(0,v.MZ)({type:Boolean,attribute:"main-page"})],key:"mainPage",value:function(){return!1}},{kind:"field",decorators:[(0,v.MZ)({type:String,attribute:"back-path"})],key:"backPath",value:void 0},{kind:"field",decorators:[(0,v.MZ)({attribute:!1})],key:"backCallback",value:void 0},{kind:"field",decorators:[(0,v.MZ)({type:Boolean,reflect:!0})],key:"narrow",value:function(){return!1}},{kind:"field",decorators:[(0,v.MZ)({type:Boolean})],key:"supervisor",value:function(){return!1}},{kind:"field",decorators:[(0,m.a)(".content")],key:"_savedScrollPos",value:void 0},{kind:"method",key:"render",value:function(){var t;return(0,f.qy)(n||(n=(0,c.A)([' <div class="toolbar"> ',' <div class="main-title"><slot name="header">','</slot></div> <slot name="toolbar-icon"></slot> </div> <div class="content ha-scrollbar" @scroll="','"> <slot></slot> </div> <div id="fab"> <slot name="fab"></slot> </div> '])),this.mainPage||null!==(t=history.state)&&void 0!==t&&t.root?(0,f.qy)(r||(r=(0,c.A)([' <ha-menu-button .hassio="','" .hass="','" .narrow="','"></ha-menu-button> '])),this.supervisor,this.hass,this.narrow):this.backPath?(0,f.qy)(o||(o=(0,c.A)([' <a href="','"> <ha-icon-button-arrow-prev .hass="','"></ha-icon-button-arrow-prev> </a> '])),this.backPath,this.hass):(0,f.qy)(a||(a=(0,c.A)([' <ha-icon-button-arrow-prev .hass="','" @click="','"></ha-icon-button-arrow-prev> '])),this.hass,this._backTapped),this.header,this._saveScrollPos)}},{kind:"method",decorators:[(0,v.Ls)({passive:!0})],key:"_saveScrollPos",value:function(t){this._savedScrollPos=t.target.scrollTop}},{kind:"method",key:"_backTapped",value:function(){this.backCallback?this.backCallback():history.back()}},{kind:"get",static:!0,key:"styles",value:function(){return[g.dp,(0,f.AH)(s||(s=(0,c.A)([":host{display:block;height:100%;background-color:var(--primary-background-color);overflow:hidden;position:relative}:host([narrow]){width:100%;position:fixed}.toolbar{display:flex;align-items:center;font-size:20px;height:var(--header-height);padding:8px 12px;background-color:var(--app-header-background-color);font-weight:400;color:var(--app-header-text-color,#fff);border-bottom:var(--app-header-border-bottom,none);box-sizing:border-box}@media (max-width:599px){.toolbar{padding:4px}}.toolbar a{color:var(--sidebar-text-color);text-decoration:none}::slotted([slot=toolbar-icon]),ha-icon-button-arrow-prev,ha-menu-button{pointer-events:auto;color:var(--sidebar-icon-color)}.main-title{margin:var(--margin-title);line-height:20px;flex-grow:1}.content{position:relative;width:100%;height:calc(100% - 1px - var(--header-height));overflow-y:auto;overflow:auto;-webkit-overflow-scrolling:touch}#fab{position:absolute;right:calc(16px + env(safe-area-inset-right));inset-inline-end:calc(16px + env(safe-area-inset-right));inset-inline-start:initial;bottom:calc(16px + env(safe-area-inset-bottom));z-index:1;display:flex;flex-wrap:wrap;justify-content:flex-end;gap:8px}:host([narrow]) #fab.tabs{bottom:calc(84px + env(safe-area-inset-bottom))}#fab[is-wide]{bottom:24px;right:24px;inset-inline-end:24px;inset-inline-start:initial}"])))]}}]}}),f.WF)},97053:function(t,e,i){var n=i(1781).A,r=i(94881).A;i.a(t,function(){var t=n(r().mark((function t(n,o){var a,s,c,l,d,h,u,p,f,v,m,g,k,y,b,A,w,_,x,M,I,P,L,q,C,S,Z,E,F,T,R,D,z,B,H,j,O,U,W,G,Q,V,J,N,K;return r().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(t.prev=0,i.r(e),a=i(6238),s=i(61780),c=i(66123),l=i(36683),d=i(89231),h=i(29864),u=i(83647),p=i(8364),f=i(76504),v=i(80792),m=i(77052),g=i(69466),k=i(21950),y=i(14460),b=i(68113),A=i(57733),w=i(56262),_=i(66274),x=i(85038),M=i(15445),I=i(24483),P=i(13478),L=i(46355),q=i(14612),C=i(53691),S=i(48455),Z=i(8339),E=i(40924),F=i(196),T=i(45081),R=i(6699),D=i(45759),z=i(28825),B=i(19887),i(54373),i(24630),H=i(60283),i(52287),j=i(94027),O=i(54347),U=i(78393),W=i(86291),!(G=n([O])).then){t.next=69;break}return t.next=65,G;case 65:t.t1=t.sent,t.t0=(0,t.t1)(),t.next=70;break;case 69:t.t0=G;case 70:O=t.t0[0],(0,p.A)([(0,F.EM)("ha-config-repairs-dashboard")],(function(t,e){var i=function(e){function i(){var e;(0,d.A)(this,i);for(var n=arguments.length,r=new Array(n),o=0;o<n;o++)r[o]=arguments[o];return e=(0,h.A)(this,i,[].concat(r)),t(e),e}return(0,u.A)(i,e),(0,l.A)(i)}(e);return{F:i,d:[{kind:"field",decorators:[(0,F.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,F.MZ)({type:Boolean})],key:"narrow",value:function(){return!1}},{kind:"field",decorators:[(0,F.wk)()],key:"_repairsIssues",value:function(){return[]}},{kind:"field",decorators:[(0,F.wk)()],key:"_showIgnored",value:function(){return!1}},{kind:"field",key:"_getFilteredIssues",value:function(){return(0,T.A)((function(t,e){return t?e:e.filter((function(t){return!t.ignored}))}))}},{kind:"method",key:"connectedCallback",value:function(){(0,f.A)((0,v.A)(i.prototype),"connectedCallback",this).call(this),"system-health"===(0,B.p9)("dialog")&&((0,z.o)("/config/repairs",{replace:!0}),(0,W.h)(this))}},{kind:"method",key:"hassSubscribe",value:function(){var t=this;return[(0,H.TP)(this.hass.connection,(function(e){t._repairsIssues=e.issues.sort((function(t,e){return H.Qk[t.severity]-H.Qk[e.severity]}));var i,n=new Set,r=(0,c.A)(t._repairsIssues);try{for(r.s();!(i=r.n()).done;){var o=i.value;n.add(o.domain)}}catch(a){r.e(a)}finally{r.f()}t.hass.loadBackendTranslation("issues",(0,s.A)(n))}))]}},{kind:"method",key:"render",value:function(){var t=this._getFilteredIssues(this._showIgnored,this._repairsIssues);return(0,E.qy)(Q||(Q=(0,a.A)([' <hass-subpage back-path="/config/system" .hass="','" .narrow="','" .header="','"> <div slot="toolbar-icon"> <ha-button-menu multi> <ha-icon-button slot="trigger" .label="','" .path="','"></ha-icon-button> <ha-check-list-item left @request-selected="','" .selected="','"> ',' </ha-check-list-item> <li divider role="separator"></li> ',' <mwc-list-item @request-selected="','"> ',' </mwc-list-item> </ha-button-menu> </div> <div class="content"> <ha-card outlined> <div class="card-content"> '," </div> </ha-card> </div> </hass-subpage> "])),this.hass,this.narrow,this.hass.localize("ui.panel.config.repairs.caption"),this.hass.localize("ui.common.menu"),"M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z",this._toggleIgnored,this._showIgnored,this.hass.localize("ui.panel.config.repairs.show_ignored"),(0,R.x)(this.hass,"system_health")||(0,R.x)(this.hass,"hassio")?(0,E.qy)(V||(V=(0,a.A)([' <mwc-list-item @request-selected="','"> '," </mwc-list-item> "])),this._showSystemInformationDialog,this.hass.localize("ui.panel.config.repairs.system_information")):"",this._showIntegrationStartupDialog,this.hass.localize("ui.panel.config.repairs.integration_startup_time"),t.length?(0,E.qy)(J||(J=(0,a.A)([' <ha-config-repairs .hass="','" .narrow="','" .repairsIssues="','"></ha-config-repairs> '])),this.hass,this.narrow,t):(0,E.qy)(N||(N=(0,a.A)([' <div class="no-repairs"> '," </div> "])),this.hass.localize("ui.panel.config.repairs.no_repairs")))}},{kind:"method",key:"_showSystemInformationDialog",value:function(t){(0,D.s)(t)&&(0,W.h)(this)}},{kind:"method",key:"_showIntegrationStartupDialog",value:function(t){(0,D.s)(t)&&(0,U.R)(this)}},{kind:"method",key:"_toggleIgnored",value:function(t){"property"===t.detail.source&&(this._showIgnored=!this._showIgnored)}},{kind:"field",static:!0,key:"styles",value:function(){return(0,E.AH)(K||(K=(0,a.A)([".content{padding:28px 20px 0;max-width:1040px;margin:0 auto}ha-card{max-width:600px;margin:0 auto;height:100%;justify-content:space-between;flex-direction:column;display:flex;margin-bottom:max(24px,env(safe-area-inset-bottom))}.card-content{display:flex;justify-content:space-between;flex-direction:column;padding:0}.no-repairs{padding:16px}li[divider]{border-bottom-color:var(--divider-color)}"])))}}]}}),(0,j.E)(E.WF)),o(),t.next=79;break;case 76:t.prev=76,t.t2=t.catch(0),o(t.t2);case 79:case"end":return t.stop()}}),t,null,[[0,76]])})));return function(e,i){return t.apply(this,arguments)}}())},78393:function(t,e,i){i.d(e,{R:function(){return o}});i(21950),i(68113),i(55888),i(56262),i(8339);var n=i(77664),r=function(){return Promise.all([i.e(29292),i.e(22658),i.e(52518)]).then(i.bind(i,52518))},o=function(t){(0,n.r)(t,"show-dialog",{dialogTag:"dialog-integration-startup",dialogImport:r,dialogParams:{}})}},86291:function(t,e,i){i.d(e,{h:function(){return o}});i(21950),i(68113),i(55888),i(56262),i(8339);var n=i(77664),r=function(){return Promise.all([i.e(29292),i.e(22658),i.e(80505)]).then(i.bind(i,80505))},o=function(t){(0,n.r)(t,"show-dialog",{dialogTag:"dialog-system-information",dialogImport:r,dialogParams:void 0})}}}]);
//# sourceMappingURL=32630.cPgf9XxTqEo.js.map