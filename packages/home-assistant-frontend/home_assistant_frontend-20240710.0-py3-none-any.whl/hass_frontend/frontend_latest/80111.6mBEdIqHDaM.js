export const id=80111;export const ids=[80111];export const modules={95439:(t,e,i)=>{i.d(e,{l:()=>h});var o=i(62659),a=i(76504),d=i(80792),n=(i(86176),i(21950),i(8339),i(12387)),r=i(52280),l=i(40924),s=i(18791),c=i(25465);i(12731);const p=["button","ha-list-item"],h=(t,e)=>{var i;return l.qy` <div class="header_title"> <span>${e}</span> <ha-icon-button .label="${null!==(i=null==t?void 0:t.localize("ui.dialogs.generic.close"))&&void 0!==i?i:"Close"}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}" dialogAction="close" class="header_button"></ha-icon-button> </div> `};(0,o.A)([(0,s.EM)("ha-dialog")],(function(t,e){class i extends e{constructor(...e){super(...e),t(this)}}return{F:i,d:[{kind:"field",key:c.Xr,value:void 0},{kind:"method",key:"scrollToPos",value:function(t,e){var i;null===(i=this.contentElement)||void 0===i||i.scrollTo(t,e)}},{kind:"method",key:"renderHeading",value:function(){return l.qy`<slot name="heading"> ${(0,a.A)((0,d.A)(i.prototype),"renderHeading",this).call(this)} </slot>`}},{kind:"method",key:"firstUpdated",value:function(){var t;(0,a.A)((0,d.A)(i.prototype),"firstUpdated",this).call(this),this.suppressDefaultPressSelector=[this.suppressDefaultPressSelector,p].join(", "),this._updateScrolledAttribute(),null===(t=this.contentElement)||void 0===t||t.addEventListener("scroll",this._onScroll,{passive:!0})}},{kind:"method",key:"disconnectedCallback",value:function(){(0,a.A)((0,d.A)(i.prototype),"disconnectedCallback",this).call(this),this.contentElement.removeEventListener("scroll",this._onScroll)}},{kind:"field",key:"_onScroll",value(){return()=>{this._updateScrolledAttribute()}}},{kind:"method",key:"_updateScrolledAttribute",value:function(){this.contentElement&&this.toggleAttribute("scrolled",0!==this.contentElement.scrollTop)}},{kind:"field",static:!0,key:"styles",value:()=>[r.R,l.AH`:host([scrolled]) ::slotted(ha-dialog-header){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.mdc-dialog{--mdc-dialog-scroll-divider-color:var(
          --dialog-scroll-divider-color,
          var(--divider-color)
        );z-index:var(--dialog-z-index,8);-webkit-backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));--mdc-dialog-box-shadow:var(--dialog-box-shadow, none);--mdc-typography-headline6-font-weight:400;--mdc-typography-headline6-font-size:1.574rem}.mdc-dialog__actions{justify-content:var(--justify-action-buttons,flex-end);padding-bottom:max(env(safe-area-inset-bottom),24px)}.mdc-dialog__actions span:first-child{flex:var(--secondary-action-button-flex,unset)}.mdc-dialog__actions span:nth-child(2){flex:var(--primary-action-button-flex,unset)}.mdc-dialog__container{align-items:var(--vertical-align-dialog,center)}.mdc-dialog__title{padding:24px 24px 0 24px}.mdc-dialog__actions{padding:12px 24px 12px 24px}.mdc-dialog__title::before{content:unset}.mdc-dialog .mdc-dialog__content{position:var(--dialog-content-position,relative);padding:var(--dialog-content-padding,24px)}:host([hideactions]) .mdc-dialog .mdc-dialog__content{padding-bottom:max(var(--dialog-content-padding,24px),env(safe-area-inset-bottom))}.mdc-dialog .mdc-dialog__surface{position:var(--dialog-surface-position,relative);top:var(--dialog-surface-top);margin-top:var(--dialog-surface-margin-top);min-height:var(--mdc-dialog-min-height,auto);border-radius:var(--ha-dialog-border-radius,28px);-webkit-backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);background:var(--ha-dialog-surface-background,var(--mdc-theme-surface,#fff))}:host([flexContent]) .mdc-dialog .mdc-dialog__content{display:flex;flex-direction:column}.header_title{position:relative;padding-right:40px;padding-inline-end:40px;padding-inline-start:initial;direction:var(--direction)}.header_title span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block}.header_button{position:absolute;right:-12px;top:-12px;text-decoration:none;color:inherit;inset-inline-start:initial;inset-inline-end:-12px;direction:var(--direction)}.dialog-actions{inset-inline-start:initial!important;inset-inline-end:0px!important;direction:var(--direction)}`]}]}}),n.u)},80111:(t,e,i)=>{i.r(e);var o=i(62659),a=(i(53501),i(21950),i(55888),i(8339),i(40924)),d=i(18791),n=i(77664),r=i(95439);(0,o.A)([(0,d.EM)("ha-dialog-thread-dataset")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,d.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,d.wk)()],key:"_params",value:void 0},{kind:"method",key:"showDialog",value:async function(t){this._params=t}},{kind:"method",key:"closeDialog",value:function(){this._params=void 0,(0,n.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){var t;if(!this._params)return a.s6;const e=this._params.network,i=e.dataset,o=this._params.otbrInfo,d=o&&i.extended_pan_id&&(null===(t=o.active_dataset_tlvs)||void 0===t?void 0:t.includes(i.extended_pan_id));return a.qy`<ha-dialog open @closed="${this.closeDialog}" .heading="${(0,r.l)(this.hass,e.name)}"> <div> Network name: ${i.network_name}<br> Channel: ${i.channel}<br> Dataset id: ${i.dataset_id}<br> Pan id: ${i.pan_id}<br> Extended Pan id: ${i.extended_pan_id}<br> ${d?a.qy`OTBR URL: ${o.url}<br> Active dataset TLVs: ${o.active_dataset_tlvs}`:a.s6} </div> </ha-dialog>`}}]}}),a.WF)},86176:()=>{Element.prototype.toggleAttribute||(Element.prototype.toggleAttribute=function(t,e){return void 0!==e&&(e=!!e),this.hasAttribute(t)?!!e||(this.removeAttribute(t),!1):!1!==e&&(this.setAttribute(t,""),!0)})}};
//# sourceMappingURL=80111.6mBEdIqHDaM.js.map