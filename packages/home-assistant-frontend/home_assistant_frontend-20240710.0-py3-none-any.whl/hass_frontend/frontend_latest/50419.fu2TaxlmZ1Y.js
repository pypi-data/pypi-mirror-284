export const id=50419;export const ids=[50419];export const modules={95206:(e,t,o)=>{o.d(t,{E:()=>a});o(21950),o(15445),o(24483),o(13478),o(46355),o(14612),o(53691),o(48455),o(8339);const i=(e,t,o=true)=>{var a;if(!e||e===document.body)return null;if((e=null!==(a=e.assignedSlot)&&void 0!==a?a:e).parentElement)e=e.parentElement;else{const t=e.getRootNode();e=t instanceof ShadowRoot?t.host:null}return(o?Object.prototype.hasOwnProperty.call(e,t):e&&t in e)?e:i(e,t,o)},a=(e,t,o=true)=>{const a=new Set;for(;e;)a.add(e),e=i(e,t,o);return a}},70213:(e,t,o)=>{o.d(t,{n:()=>i});const i=(e=document)=>{var t;return null!==(t=e.activeElement)&&void 0!==t&&null!==(t=t.shadowRoot)&&void 0!==t&&t.activeElement?i(e.activeElement.shadowRoot):e.activeElement}},34800:(e,t,o)=>{o.d(t,{E:()=>a,m:()=>i});o(55888);const i=e=>{requestAnimationFrame((()=>setTimeout(e,0)))},a=()=>new Promise((e=>{i(e)}))},95439:(e,t,o)=>{o.d(t,{l:()=>u});var i=o(62659),a=o(76504),r=o(80792),n=(o(86176),o(21950),o(8339),o(12387)),l=o(52280),d=o(40924),s=o(18791),c=o(25465);o(12731);const p=["button","ha-list-item"],u=(e,t)=>{var o;return d.qy` <div class="header_title"> <span>${t}</span> <ha-icon-button .label="${null!==(o=null==e?void 0:e.localize("ui.dialogs.generic.close"))&&void 0!==o?o:"Close"}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}" dialogAction="close" class="header_button"></ha-icon-button> </div> `};(0,i.A)([(0,s.EM)("ha-dialog")],(function(e,t){class o extends t{constructor(...t){super(...t),e(this)}}return{F:o,d:[{kind:"field",key:c.Xr,value:void 0},{kind:"method",key:"scrollToPos",value:function(e,t){var o;null===(o=this.contentElement)||void 0===o||o.scrollTo(e,t)}},{kind:"method",key:"renderHeading",value:function(){return d.qy`<slot name="heading"> ${(0,a.A)((0,r.A)(o.prototype),"renderHeading",this).call(this)} </slot>`}},{kind:"method",key:"firstUpdated",value:function(){var e;(0,a.A)((0,r.A)(o.prototype),"firstUpdated",this).call(this),this.suppressDefaultPressSelector=[this.suppressDefaultPressSelector,p].join(", "),this._updateScrolledAttribute(),null===(e=this.contentElement)||void 0===e||e.addEventListener("scroll",this._onScroll,{passive:!0})}},{kind:"method",key:"disconnectedCallback",value:function(){(0,a.A)((0,r.A)(o.prototype),"disconnectedCallback",this).call(this),this.contentElement.removeEventListener("scroll",this._onScroll)}},{kind:"field",key:"_onScroll",value(){return()=>{this._updateScrolledAttribute()}}},{kind:"method",key:"_updateScrolledAttribute",value:function(){this.contentElement&&this.toggleAttribute("scrolled",0!==this.contentElement.scrollTop)}},{kind:"field",static:!0,key:"styles",value:()=>[l.R,d.AH`:host([scrolled]) ::slotted(ha-dialog-header){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.mdc-dialog{--mdc-dialog-scroll-divider-color:var(
          --dialog-scroll-divider-color,
          var(--divider-color)
        );z-index:var(--dialog-z-index,8);-webkit-backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));--mdc-dialog-box-shadow:var(--dialog-box-shadow, none);--mdc-typography-headline6-font-weight:400;--mdc-typography-headline6-font-size:1.574rem}.mdc-dialog__actions{justify-content:var(--justify-action-buttons,flex-end);padding-bottom:max(env(safe-area-inset-bottom),24px)}.mdc-dialog__actions span:first-child{flex:var(--secondary-action-button-flex,unset)}.mdc-dialog__actions span:nth-child(2){flex:var(--primary-action-button-flex,unset)}.mdc-dialog__container{align-items:var(--vertical-align-dialog,center)}.mdc-dialog__title{padding:24px 24px 0 24px}.mdc-dialog__actions{padding:12px 24px 12px 24px}.mdc-dialog__title::before{content:unset}.mdc-dialog .mdc-dialog__content{position:var(--dialog-content-position,relative);padding:var(--dialog-content-padding,24px)}:host([hideactions]) .mdc-dialog .mdc-dialog__content{padding-bottom:max(var(--dialog-content-padding,24px),env(safe-area-inset-bottom))}.mdc-dialog .mdc-dialog__surface{position:var(--dialog-surface-position,relative);top:var(--dialog-surface-top);margin-top:var(--dialog-surface-margin-top);min-height:var(--mdc-dialog-min-height,auto);border-radius:var(--ha-dialog-border-radius,28px);-webkit-backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);background:var(--ha-dialog-surface-background,var(--mdc-theme-surface,#fff))}:host([flexContent]) .mdc-dialog .mdc-dialog__content{display:flex;flex-direction:column}.header_title{position:relative;padding-right:40px;padding-inline-end:40px;padding-inline-start:initial;direction:var(--direction)}.header_title span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block}.header_button{position:absolute;right:-12px;top:-12px;text-decoration:none;color:inherit;inset-inline-start:initial;inset-inline-end:-12px;direction:var(--direction)}.dialog-actions{inset-inline-start:initial!important;inset-inline-end:0px!important;direction:var(--direction)}`]}]}}),n.u)},50419:(e,t,o)=>{o.r(t),o.d(t,{HaImagecropperDialog:()=>p});var i=o(62659),a=(o(21950),o(26777),o(73842),o(8339),o(29734),o(72134),o(7146),o(97157),o(56648),o(72435),o(58068),o(56889)),r=o.n(a),n=o(32609),l=o(40924),d=o(18791),s=o(69760),c=(o(95439),o(14126));let p=(0,i.A)([(0,d.EM)("image-cropper-dialog")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,d.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,d.wk)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,d.wk)()],key:"_open",value:()=>!1},{kind:"field",decorators:[(0,d.P)("img",!0)],key:"_image",value:void 0},{kind:"field",key:"_cropper",value:void 0},{kind:"method",key:"showDialog",value:function(e){this._params=e,this._open=!0}},{kind:"method",key:"closeDialog",value:function(){var e;this._open=!1,this._params=void 0,null===(e=this._cropper)||void 0===e||e.destroy(),this._cropper=void 0}},{kind:"method",key:"updated",value:function(e){e.has("_params")&&this._params&&(this._cropper?this._cropper.replace(URL.createObjectURL(this._params.file)):(this._image.src=URL.createObjectURL(this._params.file),this._cropper=new(r())(this._image,{aspectRatio:this._params.options.aspectRatio,viewMode:1,dragMode:"move",minCropBoxWidth:50,ready:()=>{URL.revokeObjectURL(this._image.src)}})))}},{kind:"method",key:"render",value:function(){var e;return l.qy`<ha-dialog @closed="${this.closeDialog}" scrimClickAction escapeKeyAction .open="${this._open}"> <div class="container ${(0,s.H)({round:Boolean(null===(e=this._params)||void 0===e?void 0:e.options.round)})}"> <img alt="${this.hass.localize("ui.dialogs.image_cropper.crop_image")}"> </div> <mwc-button slot="secondaryAction" @click="${this.closeDialog}"> ${this.hass.localize("ui.common.cancel")} </mwc-button> <mwc-button slot="primaryAction" @click="${this._cropImage}"> ${this.hass.localize("ui.dialogs.image_cropper.crop")} </mwc-button> </ha-dialog>`}},{kind:"method",key:"_cropImage",value:function(){this._cropper.getCroppedCanvas().toBlob((e=>{if(!e)return;const t=new File([e],this._params.file.name,{type:this._params.options.type||this._params.file.type});this._params.croppedCallback(t),this.closeDialog()}),this._params.options.type||this._params.file.type,this._params.options.quality)}},{kind:"get",static:!0,key:"styles",value:function(){return[c.nA,l.AH`${(0,l.iz)(n)} .container{max-width:640px}img{max-width:100%}.container.round .cropper-face,.container.round .cropper-view-box{border-radius:50%}.cropper-line,.cropper-point,.cropper-point.point-se::before{background-color:var(--primary-color)}`]}}]}}),l.WF)},25465:(e,t,o)=>{o.d(t,{Xr:()=>d,oO:()=>p,ui:()=>s,zU:()=>c});o(21950),o(55888),o(8339);var i=o(51150),a=o(95206);if(26240!=o.j)var r=o(70213);var n=o(34800);const l={},d=Symbol.for("HA focus target"),s=async(e,t,o,n,s,c=!0)=>{var p;if(!(o in l)){if(!s)return!1;l[o]={element:s().then((()=>{const t=document.createElement(o);return e.provideHass(t),t}))}}if(null!==(p=i.G.history.state)&&void 0!==p&&p.replaced?(l[o].closedFocusTargets=l[i.G.history.state.dialog].closedFocusTargets,delete l[i.G.history.state.dialog].closedFocusTargets):l[o].closedFocusTargets=(0,a.E)((0,r.n)(),d),c){var h,m;i.G.history.replaceState({dialog:o,open:!1,oldState:null!==(h=i.G.history.state)&&void 0!==h&&h.open&&(null===(m=i.G.history.state)||void 0===m?void 0:m.dialog)!==o?i.G.history.state:null},"");try{i.G.history.pushState({dialog:o,dialogParams:n,open:!0},"")}catch(e){i.G.history.pushState({dialog:o,dialogParams:null,open:!0},"")}}const g=await l[o].element;return g.addEventListener("dialog-closed",u),t.appendChild(g),g.showDialog(n),!0},c=async e=>{if(!(e in l))return!0;const t=await l[e].element;return!t.closeDialog||!1!==t.closeDialog()},p=(e,t)=>{e.addEventListener("show-dialog",(o=>{const{dialogTag:i,dialogImport:a,dialogParams:r,addHistory:n}=o.detail;s(e,t,i,r,a,n)}))},u=async e=>{const t=l[e.detail.dialog].closedFocusTargets;if(delete l[e.detail.dialog].closedFocusTargets,!t)return;let o=(0,r.n)();o instanceof HTMLElement&&o.blur(),await(0,n.E)();for(const e of t)if(e instanceof HTMLElement&&(e.focus(),o=(0,r.n)(),o&&o!==document.body))return}},86176:()=>{Element.prototype.toggleAttribute||(Element.prototype.toggleAttribute=function(e,t){return void 0!==t&&(t=!!t),this.hasAttribute(e)?!!t||(this.removeAttribute(e),!1):!1!==t&&(this.setAttribute(e,""),!0)})}};
//# sourceMappingURL=50419.fu2TaxlmZ1Y.js.map