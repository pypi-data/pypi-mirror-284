(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[10454],{95439:function(t,i,e){"use strict";e.d(i,{l:function(){return b}});var n,o,a,r=e(36683),l=e(89231),s=e(29864),d=e(83647),c=e(8364),p=e(76504),h=e(80792),m=e(6238),u=(e(86176),e(77052),e(53156),e(12387)),g=e(52280),f=e(40924),v=e(196),y=e(25465),x=(e(12731),["button","ha-list-item"]),b=function(t,i){var e;return(0,f.qy)(n||(n=(0,m.A)([' <div class="header_title"> <span>','</span> <ha-icon-button .label="','" .path="','" dialogAction="close" class="header_button"></ha-icon-button> </div> '])),i,null!==(e=null==t?void 0:t.localize("ui.dialogs.generic.close"))&&void 0!==e?e:"Close","M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z")};(0,c.A)([(0,v.EM)("ha-dialog")],(function(t,i){var e=function(i){function e(){var i;(0,l.A)(this,e);for(var n=arguments.length,o=new Array(n),a=0;a<n;a++)o[a]=arguments[a];return i=(0,s.A)(this,e,[].concat(o)),t(i),i}return(0,d.A)(e,i),(0,r.A)(e)}(i);return{F:e,d:[{kind:"field",key:y.Xr,value:void 0},{kind:"method",key:"scrollToPos",value:function(t,i){var e;null===(e=this.contentElement)||void 0===e||e.scrollTo(t,i)}},{kind:"method",key:"renderHeading",value:function(){return(0,f.qy)(o||(o=(0,m.A)(['<slot name="heading"> '," </slot>"])),(0,p.A)((0,h.A)(e.prototype),"renderHeading",this).call(this))}},{kind:"method",key:"firstUpdated",value:function(){var t;(0,p.A)((0,h.A)(e.prototype),"firstUpdated",this).call(this),this.suppressDefaultPressSelector=[this.suppressDefaultPressSelector,x].join(", "),this._updateScrolledAttribute(),null===(t=this.contentElement)||void 0===t||t.addEventListener("scroll",this._onScroll,{passive:!0})}},{kind:"method",key:"disconnectedCallback",value:function(){(0,p.A)((0,h.A)(e.prototype),"disconnectedCallback",this).call(this),this.contentElement.removeEventListener("scroll",this._onScroll)}},{kind:"field",key:"_onScroll",value:function(){var t=this;return function(){t._updateScrolledAttribute()}}},{kind:"method",key:"_updateScrolledAttribute",value:function(){this.contentElement&&this.toggleAttribute("scrolled",0!==this.contentElement.scrollTop)}},{kind:"field",static:!0,key:"styles",value:function(){return[g.R,(0,f.AH)(a||(a=(0,m.A)([":host([scrolled]) ::slotted(ha-dialog-header){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.mdc-dialog{--mdc-dialog-scroll-divider-color:var(\n          --dialog-scroll-divider-color,\n          var(--divider-color)\n        );z-index:var(--dialog-z-index,8);-webkit-backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));--mdc-dialog-box-shadow:var(--dialog-box-shadow, none);--mdc-typography-headline6-font-weight:400;--mdc-typography-headline6-font-size:1.574rem}.mdc-dialog__actions{justify-content:var(--justify-action-buttons,flex-end);padding-bottom:max(env(safe-area-inset-bottom),24px)}.mdc-dialog__actions span:first-child{flex:var(--secondary-action-button-flex,unset)}.mdc-dialog__actions span:nth-child(2){flex:var(--primary-action-button-flex,unset)}.mdc-dialog__container{align-items:var(--vertical-align-dialog,center)}.mdc-dialog__title{padding:24px 24px 0 24px}.mdc-dialog__actions{padding:12px 24px 12px 24px}.mdc-dialog__title::before{content:unset}.mdc-dialog .mdc-dialog__content{position:var(--dialog-content-position,relative);padding:var(--dialog-content-padding,24px)}:host([hideactions]) .mdc-dialog .mdc-dialog__content{padding-bottom:max(var(--dialog-content-padding,24px),env(safe-area-inset-bottom))}.mdc-dialog .mdc-dialog__surface{position:var(--dialog-surface-position,relative);top:var(--dialog-surface-top);margin-top:var(--dialog-surface-margin-top);min-height:var(--mdc-dialog-min-height,auto);border-radius:var(--ha-dialog-border-radius,28px);-webkit-backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);background:var(--ha-dialog-surface-background,var(--mdc-theme-surface,#fff))}:host([flexContent]) .mdc-dialog .mdc-dialog__content{display:flex;flex-direction:column}.header_title{position:relative;padding-right:40px;padding-inline-end:40px;padding-inline-start:initial;direction:var(--direction)}.header_title span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block}.header_button{position:absolute;right:-12px;top:-12px;text-decoration:none;color:inherit;inset-inline-start:initial;inset-inline-end:-12px;direction:var(--direction)}.dialog-actions{inset-inline-start:initial!important;inset-inline-end:0px!important;direction:var(--direction)}"])))]}}]}}),u.u)},39335:function(t,i,e){"use strict";var n,o,a,r=e(6238),l=e(36683),s=e(89231),d=e(29864),c=e(83647),p=e(8364),h=e(76504),m=e(80792),u=(e(77052),e(46175)),g=e(45592),f=e(40924),v=e(196);(0,p.A)([(0,v.EM)("ha-list-item")],(function(t,i){var e=function(i){function e(){var i;(0,s.A)(this,e);for(var n=arguments.length,o=new Array(n),a=0;a<n;a++)o[a]=arguments[a];return i=(0,d.A)(this,e,[].concat(o)),t(i),i}return(0,c.A)(e,i),(0,l.A)(e)}(i);return{F:e,d:[{kind:"method",key:"renderRipple",value:function(){return this.noninteractive?"":(0,h.A)((0,m.A)(e.prototype),"renderRipple",this).call(this)}},{kind:"get",static:!0,key:"styles",value:function(){return[g.R,(0,f.AH)(n||(n=(0,r.A)([":host{padding-left:var(--mdc-list-side-padding-left,var(--mdc-list-side-padding,20px));padding-inline-start:var(--mdc-list-side-padding-left,var(--mdc-list-side-padding,20px));padding-right:var(--mdc-list-side-padding-right,var(--mdc-list-side-padding,20px));padding-inline-end:var(--mdc-list-side-padding-right,var(--mdc-list-side-padding,20px))}:host([graphic=avatar]:not([twoLine])),:host([graphic=icon]:not([twoLine])){height:48px}span.material-icons:first-of-type{margin-inline-start:0px!important;margin-inline-end:var(--mdc-list-item-graphic-margin,16px)!important;direction:var(--direction)!important}span.material-icons:last-of-type{margin-inline-start:auto!important;margin-inline-end:0px!important;direction:var(--direction)!important}.mdc-deprecated-list-item__meta{display:var(--mdc-list-item-meta-display);align-items:center;flex-shrink:0}:host([graphic=icon]:not([twoline])) .mdc-deprecated-list-item__graphic{margin-inline-end:var(--mdc-list-item-graphic-margin,20px)!important}:host([multiline-secondary]){height:auto}:host([multiline-secondary]) .mdc-deprecated-list-item__text{padding:8px 0}:host([multiline-secondary]) .mdc-deprecated-list-item__secondary-text{text-overflow:initial;white-space:normal;overflow:auto;display:inline-block;margin-top:10px}:host([multiline-secondary]) .mdc-deprecated-list-item__primary-text{margin-top:10px}:host([multiline-secondary]) .mdc-deprecated-list-item__secondary-text::before{display:none}:host([multiline-secondary]) .mdc-deprecated-list-item__primary-text::before{display:none}:host([disabled]){color:var(--disabled-text-color)}:host([noninteractive]){pointer-events:unset}"]))),"rtl"===document.dir?(0,f.AH)(o||(o=(0,r.A)(["span.material-icons:first-of-type,span.material-icons:last-of-type{direction:rtl!important;--direction:rtl}"]))):(0,f.AH)(a||(a=(0,r.A)([""])))]}}]}}),u.J)},2888:function(t,i,e){"use strict";e.r(i);var n,o,a=e(6238),r=e(94881),l=e(1781),s=e(36683),d=e(89231),c=e(29864),p=e(83647),h=e(8364),m=(e(77052),e(29805),e(40924)),u=e(196),g=e(77664),f=e(95439),v=(e(39335),"M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z");(0,h.A)([(0,u.EM)("community-dialog")],(function(t,i){var e,h,y=function(i){function e(){var i;(0,d.A)(this,e);for(var n=arguments.length,o=new Array(n),a=0;a<n;a++)o[a]=arguments[a];return i=(0,c.A)(this,e,[].concat(o)),t(i),i}return(0,p.A)(e,i),(0,s.A)(e)}(i);return{F:y,d:[{kind:"field",decorators:[(0,u.MZ)({attribute:!1})],key:"localize",value:void 0},{kind:"method",key:"showDialog",value:(h=(0,l.A)((0,r.A)().mark((function t(i){return(0,r.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:this.localize=i.localize;case 1:case"end":return t.stop()}}),t,this)}))),function(t){return h.apply(this,arguments)})},{kind:"method",key:"closeDialog",value:(e=(0,l.A)((0,r.A)().mark((function t(){return(0,r.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:this.localize=void 0,(0,g.r)(this,"dialog-closed",{dialog:this.localName});case 2:case"end":return t.stop()}}),t,this)}))),function(){return e.apply(this,arguments)})},{kind:"method",key:"render",value:function(){return this.localize?(0,m.qy)(n||(n=(0,a.A)(['<ha-dialog open hideActions @closed="','" .heading="','"> <mwc-list> <a target="_blank" rel="noreferrer noopener" href="https://community.home-assistant.io/"> <ha-list-item hasMeta graphic="icon"> <img src="/static/icons/favicon-192x192.png" slot="graphic"> ',' <ha-svg-icon slot="meta" .path="','"></ha-svg-icon> </ha-list-item> </a> <a target="_blank" rel="noreferrer noopener" href="https://newsletter.openhomefoundation.org/"> <ha-list-item hasMeta graphic="icon"> <img src="/static/icons/favicon-192x192.png" slot="graphic"> ',' <ha-svg-icon slot="meta" .path="','"></ha-svg-icon> </ha-list-item> </a> <a target="_blank" rel="noreferrer noopener" href="https://www.home-assistant.io/join-chat"> <ha-list-item hasMeta graphic="icon"> <img src="/static/images/logo_discord.png" slot="graphic"> ',' <ha-svg-icon slot="meta" .path="','"></ha-svg-icon> </ha-list-item> </a> <a target="_blank" rel="noreferrer noopener" href="https://x.com/home_assistant"> <ha-list-item hasMeta graphic="icon"> <img class="x" src="/static/images/logo_x.svg" slot="graphic"> ',' <ha-svg-icon slot="meta" .path="','"></ha-svg-icon> </ha-list-item> </a> </mwc-list> </ha-dialog>'])),this.closeDialog,(0,f.l)(void 0,this.localize("ui.panel.page-onboarding.welcome.community")),this.localize("ui.panel.page-onboarding.welcome.forums"),v,this.localize("ui.panel.page-onboarding.welcome.open_home_newsletter"),v,this.localize("ui.panel.page-onboarding.welcome.discord"),v,this.localize("ui.panel.page-onboarding.welcome.x"),v):m.s6}},{kind:"field",static:!0,key:"styles",value:function(){return(0,m.AH)(o||(o=(0,a.A)(["ha-dialog{--mdc-dialog-min-width:min(400px, 90vw);--dialog-content-padding:0}ha-list-item{height:56px;--mdc-list-item-meta-size:20px}a{text-decoration:none}@media (prefers-color-scheme:light){img.x{filter:invert(1) hue-rotate(180deg)}}"])))}}]}}),m.WF)},86176:function(){Element.prototype.toggleAttribute||(Element.prototype.toggleAttribute=function(t,i){return void 0!==i&&(i=!!i),this.hasAttribute(t)?!!i||(this.removeAttribute(t),!1):!1!==i&&(this.setAttribute(t,""),!0)})},66584:function(t,i,e){function n(i){return t.exports=n="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},t.exports.__esModule=!0,t.exports.default=t.exports,n(i)}e(8485),e(98809),e(77817),e(21950),e(68113),e(56262),e(8339),t.exports=n,t.exports.__esModule=!0,t.exports.default=t.exports},49716:function(t,i,e){"use strict";var n=e(95124);t.exports=function(t,i,e){for(var o=0,a=arguments.length>2?e:n(i),r=new t(a);a>o;)r[o]=i[o++];return r}},21903:function(t,i,e){"use strict";var n=e(16230),o=e(82374),a=e(43973),r=e(51607),l=e(75011),s=e(95124),d=e(17998),c=e(49716),p=Array,h=o([].push);t.exports=function(t,i,e,o){for(var m,u,g,f=r(t),v=a(f),y=n(i,e),x=d(null),b=s(v),_=0;b>_;_++)g=v[_],(u=l(y(g,_,f)))in x?h(x[u],g):x[u]=[g];if(o&&(m=o(f))!==p)for(u in x)x[u]=c(m,x[u]);return x}},15176:function(t,i,e){"use strict";var n=e(87568),o=e(21903),a=e(33523);n({target:"Array",proto:!0},{group:function(t){return o(this,t,arguments.length>1?arguments[1]:void 0)}}),a("group")}}]);
//# sourceMappingURL=10454.mqYTOh2ddMk.js.map