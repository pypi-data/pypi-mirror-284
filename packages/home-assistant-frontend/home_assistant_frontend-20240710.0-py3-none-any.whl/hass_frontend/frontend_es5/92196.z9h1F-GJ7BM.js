(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[92196],{95439:function(o,t,i){"use strict";i.d(t,{l:function(){return _}});var e,a,n,l=i(36683),r=i(89231),d=i(29864),c=i(83647),s=i(8364),u=i(76504),h=i(80792),p=i(6238),g=(i(86176),i(77052),i(53156),i(12387)),f=i(52280),m=i(40924),v=i(196),k=i(25465),b=(i(12731),["button","ha-list-item"]),_=function(o,t){var i;return(0,m.qy)(e||(e=(0,p.A)([' <div class="header_title"> <span>','</span> <ha-icon-button .label="','" .path="','" dialogAction="close" class="header_button"></ha-icon-button> </div> '])),t,null!==(i=null==o?void 0:o.localize("ui.dialogs.generic.close"))&&void 0!==i?i:"Close","M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z")};(0,s.A)([(0,v.EM)("ha-dialog")],(function(o,t){var i=function(t){function i(){var t;(0,r.A)(this,i);for(var e=arguments.length,a=new Array(e),n=0;n<e;n++)a[n]=arguments[n];return t=(0,d.A)(this,i,[].concat(a)),o(t),t}return(0,c.A)(i,t),(0,l.A)(i)}(t);return{F:i,d:[{kind:"field",key:k.Xr,value:void 0},{kind:"method",key:"scrollToPos",value:function(o,t){var i;null===(i=this.contentElement)||void 0===i||i.scrollTo(o,t)}},{kind:"method",key:"renderHeading",value:function(){return(0,m.qy)(a||(a=(0,p.A)(['<slot name="heading"> '," </slot>"])),(0,u.A)((0,h.A)(i.prototype),"renderHeading",this).call(this))}},{kind:"method",key:"firstUpdated",value:function(){var o;(0,u.A)((0,h.A)(i.prototype),"firstUpdated",this).call(this),this.suppressDefaultPressSelector=[this.suppressDefaultPressSelector,b].join(", "),this._updateScrolledAttribute(),null===(o=this.contentElement)||void 0===o||o.addEventListener("scroll",this._onScroll,{passive:!0})}},{kind:"method",key:"disconnectedCallback",value:function(){(0,u.A)((0,h.A)(i.prototype),"disconnectedCallback",this).call(this),this.contentElement.removeEventListener("scroll",this._onScroll)}},{kind:"field",key:"_onScroll",value:function(){var o=this;return function(){o._updateScrolledAttribute()}}},{kind:"method",key:"_updateScrolledAttribute",value:function(){this.contentElement&&this.toggleAttribute("scrolled",0!==this.contentElement.scrollTop)}},{kind:"field",static:!0,key:"styles",value:function(){return[f.R,(0,m.AH)(n||(n=(0,p.A)([":host([scrolled]) ::slotted(ha-dialog-header){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.mdc-dialog{--mdc-dialog-scroll-divider-color:var(\n          --dialog-scroll-divider-color,\n          var(--divider-color)\n        );z-index:var(--dialog-z-index,8);-webkit-backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));--mdc-dialog-box-shadow:var(--dialog-box-shadow, none);--mdc-typography-headline6-font-weight:400;--mdc-typography-headline6-font-size:1.574rem}.mdc-dialog__actions{justify-content:var(--justify-action-buttons,flex-end);padding-bottom:max(env(safe-area-inset-bottom),24px)}.mdc-dialog__actions span:first-child{flex:var(--secondary-action-button-flex,unset)}.mdc-dialog__actions span:nth-child(2){flex:var(--primary-action-button-flex,unset)}.mdc-dialog__container{align-items:var(--vertical-align-dialog,center)}.mdc-dialog__title{padding:24px 24px 0 24px}.mdc-dialog__actions{padding:12px 24px 12px 24px}.mdc-dialog__title::before{content:unset}.mdc-dialog .mdc-dialog__content{position:var(--dialog-content-position,relative);padding:var(--dialog-content-padding,24px)}:host([hideactions]) .mdc-dialog .mdc-dialog__content{padding-bottom:max(var(--dialog-content-padding,24px),env(safe-area-inset-bottom))}.mdc-dialog .mdc-dialog__surface{position:var(--dialog-surface-position,relative);top:var(--dialog-surface-top);margin-top:var(--dialog-surface-margin-top);min-height:var(--mdc-dialog-min-height,auto);border-radius:var(--ha-dialog-border-radius,28px);-webkit-backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);background:var(--ha-dialog-surface-background,var(--mdc-theme-surface,#fff))}:host([flexContent]) .mdc-dialog .mdc-dialog__content{display:flex;flex-direction:column}.header_title{position:relative;padding-right:40px;padding-inline-end:40px;padding-inline-start:initial;direction:var(--direction)}.header_title span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block}.header_button{position:absolute;right:-12px;top:-12px;text-decoration:none;color:inherit;inset-inline-start:initial;inset-inline-end:-12px;direction:var(--direction)}.dialog-actions{inset-inline-start:initial!important;inset-inline-end:0px!important;direction:var(--direction)}"])))]}}]}}),g.u)},92196:function(o,t,i){"use strict";i.r(t),i.d(t,{DialogManageCloudhook:function(){return w}});var e,a,n,l,r=i(94881),d=i(1781),c=i(6238),s=i(36683),u=i(89231),h=i(29864),p=i(83647),g=i(8364),f=(i(77052),i(848),i(34069),i(40924)),m=i(196),v=i(77664),k=i(36639),b=i(95439),_=(i(42398),i(98876)),x=i(14126),A=i(92483),y=i(75610),w=(0,g.A)(null,(function(o,t){var i,g,w=function(t){function i(){var t;(0,u.A)(this,i);for(var e=arguments.length,a=new Array(e),n=0;n<e;n++)a[n]=arguments[n];return t=(0,h.A)(this,i,[].concat(a)),o(t),t}return(0,p.A)(i,t),(0,s.A)(i)}(t);return{F:w,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[(0,m.wk)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,m.P)("ha-textfield")],key:"_input",value:void 0},{kind:"method",key:"showDialog",value:function(o){this._params=o}},{kind:"method",key:"closeDialog",value:function(){this._params=void 0,(0,v.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){if(!this._params)return f.s6;var o=this._params,t=o.webhook,i=o.cloudhook,l="automation"===t.domain?(0,A.o)(this.hass,"/docs/automation/trigger/#webhook-trigger"):(0,A.o)(this.hass,"/integrations/".concat(t.domain,"/"));return(0,f.qy)(e||(e=(0,c.A)([' <ha-dialog open hideActions @closed="','" .heading="','"> <div> <p> ',' <br> <a href="','" target="_blank" rel="noreferrer"> ',' <ha-svg-icon .path="','"></ha-svg-icon> </a> </p> <ha-textfield .label="','" .value="','" iconTrailing readOnly="readOnly" @click="','"> <ha-icon-button @click="','" slot="trailingIcon" .path="','"></ha-icon-button> </ha-textfield> </div> <a href="','" target="_blank" rel="noreferrer" slot="secondaryAction"> <mwc-button> ',' </mwc-button> </a> <mwc-button @click="','" slot="primaryAction"> '," </mwc-button> </ha-dialog> "])),this.closeDialog,(0,b.l)(this.hass,this.hass.localize("ui.panel.config.cloud.dialog_cloudhook.webhook_for",{name:t.name})),i.managed?(0,f.qy)(n||(n=(0,c.A)([" ",' <button class="link" @click="','"> ',"</button>. "])),this.hass.localize("ui.panel.config.cloud.dialog_cloudhook.info_disable_webhook"),this._disableWebhook,this.hass.localize("ui.panel.config.cloud.dialog_cloudhook.link_disable_webhook")):(0,f.qy)(a||(a=(0,c.A)([" "," "])),this.hass.localize("ui.panel.config.cloud.dialog_cloudhook.managed_by_integration")),l,this.hass.localize("ui.panel.config.cloud.dialog_cloudhook.view_documentation"),"M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z",this.hass.localize("ui.panel.config.cloud.dialog_cloudhook.public_url"),i.cloudhook_url,this.focusInput,this._copyUrl,"M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z",l,this.hass.localize("ui.panel.config.cloud.dialog_cloudhook.view_documentation"),this.closeDialog,this.hass.localize("ui.panel.config.cloud.dialog_cloudhook.close"))}},{kind:"method",key:"_disableWebhook",value:(g=(0,d.A)((0,r.A)().mark((function o(){return(0,r.A)().wrap((function(o){for(;;)switch(o.prev=o.next){case 0:return o.next=2,(0,_.showConfirmationDialog)(this,{title:this.hass.localize("ui.panel.config.cloud.dialog_cloudhook.confirm_disable_title"),text:this.hass.localize("ui.panel.config.cloud.dialog_cloudhook.confirm_disable_text",{name:this._params.webhook.name}),dismissText:this.hass.localize("ui.common.cancel"),confirmText:this.hass.localize("ui.common.disable"),destructive:!0});case 2:o.sent&&(this._params.disableHook(),this.closeDialog());case 4:case"end":return o.stop()}}),o,this)}))),function(){return g.apply(this,arguments)})},{kind:"method",key:"focusInput",value:function(o){o.currentTarget.select()}},{kind:"method",key:"_copyUrl",value:(i=(0,d.A)((0,r.A)().mark((function o(t){var i,e;return(0,r.A)().wrap((function(o){for(;;)switch(o.prev=o.next){case 0:if(this.hass){o.next=2;break}return o.abrupt("return");case 2:return t.stopPropagation(),(i=t.target.parentElement).select(),e=this.hass.hassUrl(i.value),o.next=8,(0,k.l)(e);case 8:(0,y.P)(this,{message:this.hass.localize("ui.common.copied_clipboard")});case 9:case"end":return o.stop()}}),o,this)}))),function(o){return i.apply(this,arguments)})},{kind:"get",static:!0,key:"styles",value:function(){return[x.RF,x.nA,(0,f.AH)(l||(l=(0,c.A)(["ha-dialog{width:650px}ha-textfield{display:block}ha-textfield>ha-icon-button{--mdc-icon-button-size:24px;--mdc-icon-size:18px}button.link{color:var(--primary-color);text-decoration:none}a{text-decoration:none}a ha-svg-icon{--mdc-icon-size:16px}p{margin-top:0;margin-bottom:16px}"])))]}}]}}),f.WF);customElements.define("dialog-manage-cloudhook",w)},86176:function(){Element.prototype.toggleAttribute||(Element.prototype.toggleAttribute=function(o,t){return void 0!==t&&(t=!!t),this.hasAttribute(o)?!!t||(this.removeAttribute(o),!1):!1!==t&&(this.setAttribute(o,""),!0)})},92483:function(o,t,i){"use strict";i.d(t,{o:function(){return e}});i(77052),i(53501),i(34517);var e=function(o,t){return"https://".concat(o.config.version.includes("b")?"rc":o.config.version.includes("dev")?"next":"www",".home-assistant.io").concat(t)}}}]);
//# sourceMappingURL=92196.z9h1F-GJ7BM.js.map