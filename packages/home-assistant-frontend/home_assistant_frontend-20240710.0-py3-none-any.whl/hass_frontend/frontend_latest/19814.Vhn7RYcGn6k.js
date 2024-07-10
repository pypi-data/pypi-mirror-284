/*! For license information please see 19814.Vhn7RYcGn6k.js.LICENSE.txt */
export const id=19814;export const ids=[19814];export const modules={47451:(e,t,i)=>{i.d(t,{u:()=>h});i(21950),i(8339);var a=i(76513),s=i(94400),o=i(40924),l=i(18791),n=i(69760),r=i(79278),d=i(43821);const c={fromAttribute:e=>null!==e&&(""===e||e),toAttribute:e=>"boolean"==typeof e?e?"":null:e};class h extends s.J{constructor(){super(...arguments),this.rows=2,this.cols=20,this.charCounter=!1}render(){const e=this.charCounter&&-1!==this.maxLength,t=e&&"internal"===this.charCounter,i=e&&!t,a=!!this.helper||!!this.validationMessage||i,s={"mdc-text-field--disabled":this.disabled,"mdc-text-field--no-label":!this.label,"mdc-text-field--filled":!this.outlined,"mdc-text-field--outlined":this.outlined,"mdc-text-field--end-aligned":this.endAligned,"mdc-text-field--with-internal-counter":t};return o.qy` <label class="mdc-text-field mdc-text-field--textarea ${(0,n.H)(s)}"> ${this.renderRipple()} ${this.outlined?this.renderOutline():this.renderLabel()} ${this.renderInput()} ${this.renderCharCounter(t)} ${this.renderLineRipple()} </label> ${this.renderHelperText(a,i)} `}renderInput(){const e=this.label?"label":void 0,t=-1===this.minLength?void 0:this.minLength,i=-1===this.maxLength?void 0:this.maxLength,a=this.autocapitalize?this.autocapitalize:void 0;return o.qy` <textarea aria-labelledby="${(0,r.J)(e)}" class="mdc-text-field__input" .value="${(0,d.V)(this.value)}" rows="${this.rows}" cols="${this.cols}" ?disabled="${this.disabled}" placeholder="${this.placeholder}" ?required="${this.required}" ?readonly="${this.readOnly}" minlength="${(0,r.J)(t)}" maxlength="${(0,r.J)(i)}" name="${(0,r.J)(""===this.name?void 0:this.name)}" inputmode="${(0,r.J)(this.inputMode)}" autocapitalize="${(0,r.J)(a)}" @input="${this.handleInputChange}" @blur="${this.onInputBlur}">
      </textarea>`}}(0,a.__decorate)([(0,l.P)("textarea")],h.prototype,"formElement",void 0),(0,a.__decorate)([(0,l.MZ)({type:Number})],h.prototype,"rows",void 0),(0,a.__decorate)([(0,l.MZ)({type:Number})],h.prototype,"cols",void 0),(0,a.__decorate)([(0,l.MZ)({converter:c})],h.prototype,"charCounter",void 0)},72692:(e,t,i)=>{i.d(t,{R:()=>a});const a=i(40924).AH`.mdc-text-field{height:100%}.mdc-text-field__input{resize:none}`},24930:(e,t,i)=>{i.d(t,{I:()=>o});i(71936),i(59092),i(66274),i(84531),i(32877);class a{constructor(e=window.localStorage){this.storage=void 0,this._storage={},this._listeners={},this.storage=e,e===window.localStorage&&window.addEventListener("storage",(e=>{e.key&&this.hasKey(e.key)&&(this._storage[e.key]=e.newValue?JSON.parse(e.newValue):e.newValue,this._listeners[e.key]&&this._listeners[e.key].forEach((t=>t(e.oldValue?JSON.parse(e.oldValue):e.oldValue,this._storage[e.key]))))}))}addFromStorage(e){if(!this._storage[e]){const t=this.storage.getItem(e);t&&(this._storage[e]=JSON.parse(t))}}subscribeChanges(e,t){return this._listeners[e]?this._listeners[e].push(t):this._listeners[e]=[t],()=>{this.unsubscribeChanges(e,t)}}unsubscribeChanges(e,t){if(!(e in this._listeners))return;const i=this._listeners[e].indexOf(t);-1!==i&&this._listeners[e].splice(i,1)}hasKey(e){return e in this._storage}getValue(e){return this._storage[e]}setValue(e,t){const i=this._storage[e];this._storage[e]=t;try{void 0===t?this.storage.removeItem(e):this.storage.setItem(e,JSON.stringify(t))}catch(e){}finally{this._listeners[e]&&this._listeners[e].forEach((e=>e(i,t)))}}}const s={},o=e=>t=>{const i=e.storage||"localStorage";let o;i&&i in s?o=s[i]:(o=new a(window[i]),s[i]=o);const l=String(t.key),n=e.key||String(t.key),r=t.initializer?t.initializer():void 0;o.addFromStorage(n);const d=!1!==e.subscribe?e=>o.subscribeChanges(n,((i,a)=>{e.requestUpdate(t.key,i)})):void 0,c=()=>o.hasKey(n)?e.deserializer?e.deserializer(o.getValue(n)):o.getValue(n):r;return{kind:"method",placement:"prototype",key:t.key,descriptor:{set(i){((i,a)=>{let s;e.state&&(s=c()),o.setValue(n,e.serializer?e.serializer(a):a),e.state&&i.requestUpdate(t.key,s)})(this,i)},get:()=>c(),enumerable:!0,configurable:!0},finisher(i){if(e.state&&e.subscribe){const e=i.prototype.connectedCallback,t=i.prototype.disconnectedCallback;i.prototype.connectedCallback=function(){e.call(this),this[`__unbsubLocalStorage${l}`]=null==d?void 0:d(this)},i.prototype.disconnectedCallback=function(){var e;t.call(this),null===(e=this[`__unbsubLocalStorage${l}`])||void 0===e||e.call(this),this[`__unbsubLocalStorage${l}`]=void 0}}e.state&&i.createProperty(t.key,{noAccessor:!0,...e.stateOptions})}}}},95439:(e,t,i)=>{i.d(t,{l:()=>u});var a=i(62659),s=i(76504),o=i(80792),l=(i(86176),i(21950),i(8339),i(12387)),n=i(52280),r=i(40924),d=i(18791),c=i(25465);i(12731);const h=["button","ha-list-item"],u=(e,t)=>{var i;return r.qy` <div class="header_title"> <span>${t}</span> <ha-icon-button .label="${null!==(i=null==e?void 0:e.localize("ui.dialogs.generic.close"))&&void 0!==i?i:"Close"}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}" dialogAction="close" class="header_button"></ha-icon-button> </div> `};(0,a.A)([(0,d.EM)("ha-dialog")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",key:c.Xr,value:void 0},{kind:"method",key:"scrollToPos",value:function(e,t){var i;null===(i=this.contentElement)||void 0===i||i.scrollTo(e,t)}},{kind:"method",key:"renderHeading",value:function(){return r.qy`<slot name="heading"> ${(0,s.A)((0,o.A)(i.prototype),"renderHeading",this).call(this)} </slot>`}},{kind:"method",key:"firstUpdated",value:function(){var e;(0,s.A)((0,o.A)(i.prototype),"firstUpdated",this).call(this),this.suppressDefaultPressSelector=[this.suppressDefaultPressSelector,h].join(", "),this._updateScrolledAttribute(),null===(e=this.contentElement)||void 0===e||e.addEventListener("scroll",this._onScroll,{passive:!0})}},{kind:"method",key:"disconnectedCallback",value:function(){(0,s.A)((0,o.A)(i.prototype),"disconnectedCallback",this).call(this),this.contentElement.removeEventListener("scroll",this._onScroll)}},{kind:"field",key:"_onScroll",value(){return()=>{this._updateScrolledAttribute()}}},{kind:"method",key:"_updateScrolledAttribute",value:function(){this.contentElement&&this.toggleAttribute("scrolled",0!==this.contentElement.scrollTop)}},{kind:"field",static:!0,key:"styles",value:()=>[n.R,r.AH`:host([scrolled]) ::slotted(ha-dialog-header){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.mdc-dialog{--mdc-dialog-scroll-divider-color:var(
          --dialog-scroll-divider-color,
          var(--divider-color)
        );z-index:var(--dialog-z-index,8);-webkit-backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));--mdc-dialog-box-shadow:var(--dialog-box-shadow, none);--mdc-typography-headline6-font-weight:400;--mdc-typography-headline6-font-size:1.574rem}.mdc-dialog__actions{justify-content:var(--justify-action-buttons,flex-end);padding-bottom:max(env(safe-area-inset-bottom),24px)}.mdc-dialog__actions span:first-child{flex:var(--secondary-action-button-flex,unset)}.mdc-dialog__actions span:nth-child(2){flex:var(--primary-action-button-flex,unset)}.mdc-dialog__container{align-items:var(--vertical-align-dialog,center)}.mdc-dialog__title{padding:24px 24px 0 24px}.mdc-dialog__actions{padding:12px 24px 12px 24px}.mdc-dialog__title::before{content:unset}.mdc-dialog .mdc-dialog__content{position:var(--dialog-content-position,relative);padding:var(--dialog-content-padding,24px)}:host([hideactions]) .mdc-dialog .mdc-dialog__content{padding-bottom:max(var(--dialog-content-padding,24px),env(safe-area-inset-bottom))}.mdc-dialog .mdc-dialog__surface{position:var(--dialog-surface-position,relative);top:var(--dialog-surface-top);margin-top:var(--dialog-surface-margin-top);min-height:var(--mdc-dialog-min-height,auto);border-radius:var(--ha-dialog-border-radius,28px);-webkit-backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);background:var(--ha-dialog-surface-background,var(--mdc-theme-surface,#fff))}:host([flexContent]) .mdc-dialog .mdc-dialog__content{display:flex;flex-direction:column}.header_title{position:relative;padding-right:40px;padding-inline-end:40px;padding-inline-start:initial;direction:var(--direction)}.header_title span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block}.header_button{position:absolute;right:-12px;top:-12px;text-decoration:none;color:inherit;inset-inline-start:initial;inset-inline-end:-12px;direction:var(--direction)}.dialog-actions{inset-inline-start:initial!important;inset-inline-end:0px!important;direction:var(--direction)}`]}]}}),l.u)},86021:(e,t,i)=>{var a=i(62659),s=i(76504),o=i(80792),l=(i(21950),i(8339),i(47451)),n=i(65050),r=i(72692),d=i(40924),c=i(18791);(0,a.A)([(0,c.EM)("ha-textarea")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,c.MZ)({type:Boolean,reflect:!0})],key:"autogrow",value:()=>!1},{kind:"method",key:"updated",value:function(e){(0,s.A)((0,o.A)(i.prototype),"updated",this).call(this,e),this.autogrow&&e.has("value")&&(this.mdcRoot.dataset.value=this.value+'=​"')}},{kind:"field",static:!0,key:"styles",value:()=>[n.R,r.R,d.AH`:host([autogrow]) .mdc-text-field{position:relative;min-height:74px;min-width:178px;max-height:200px}:host([autogrow]) .mdc-text-field:after{content:attr(data-value);margin-top:23px;margin-bottom:9px;line-height:1.5rem;min-height:42px;padding:0px 32px 0 16px;letter-spacing:var(
          --mdc-typography-subtitle1-letter-spacing,
          .009375em
        );visibility:hidden;white-space:pre-wrap}:host([autogrow]) .mdc-text-field__input{position:absolute;height:calc(100% - 32px)}:host([autogrow]) .mdc-text-field.mdc-text-field--no-label:after{margin-top:16px;margin-bottom:16px}.mdc-floating-label{inset-inline-start:16px!important;inset-inline-end:initial!important;transform-origin:var(--float-start) top}`]}]}}),l.u)},28408:(e,t,i)=>{i.d(t,{EF:()=>l,S_:()=>a,Xv:()=>n,ni:()=>o,u1:()=>r,z3:()=>d});const a=(e,t)=>e.callApi("POST","tts_get_url",t),s="media-source://tts/",o=e=>e.startsWith(s),l=e=>e.substring(19),n=(e,t,i)=>e.callWS({type:"tts/engine/list",language:t,country:i}),r=(e,t)=>e.callWS({type:"tts/engine/get",engine_id:t}),d=(e,t,i)=>e.callWS({type:"tts/engine/voices",engine_id:t,language:i})},19814:(e,t,i)=>{i.r(t),i.d(t,{TTSTryDialog:()=>h});var a=i(62659),s=(i(21950),i(55888),i(8339),i(40924)),o=i(18791),l=i(24930),n=i(77664),r=(i(99535),i(95439)),d=(i(86021),i(28408)),c=i(98876);i(4596);let h=(0,a.A)([(0,o.EM)("dialog-tts-try")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.wk)()],key:"_loadingExample",value:()=>!1},{kind:"field",decorators:[(0,o.wk)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,o.wk)()],key:"_valid",value:()=>!1},{kind:"field",decorators:[(0,o.P)("#message")],key:"_messageInput",value:void 0},{kind:"field",decorators:[(0,l.I)({key:"ttsTryMessages",state:!1,subscribe:!1})],key:"_messages",value:void 0},{kind:"method",key:"showDialog",value:function(e){this._params=e,this._valid=Boolean(this._defaultMessage)}},{kind:"method",key:"closeDialog",value:function(){this._params=void 0,(0,n.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"get",key:"_defaultMessage",value:function(){var e,t;const i=null===(e=this._params.language)||void 0===e?void 0:e.substring(0,2),a=this.hass.locale.language.substring(0,2);return i&&null!==(t=this._messages)&&void 0!==t&&t[i]?this._messages[i]:i===a?this.hass.localize("ui.dialogs.tts-try.message_example"):""}},{kind:"method",key:"render",value:function(){return this._params?s.qy` <ha-dialog open @closed="${this.closeDialog}" .heading="${(0,r.l)(this.hass,this.hass.localize("ui.dialogs.tts-try.header"))}"> <ha-textarea autogrow id="message" .label="${this.hass.localize("ui.dialogs.tts-try.message")}" .placeholder="${this.hass.localize("ui.dialogs.tts-try.message_placeholder")}" .value="${this._defaultMessage}" @input="${this._inputChanged}" ?dialogInitialFocus="${!this._defaultMessage}"> </ha-textarea> ${this._loadingExample?s.qy` <ha-circular-progress size="small" indeterminate slot="primaryAction" class="loading"></ha-circular-progress> `:s.qy` <ha-button ?dialogInitialFocus="${Boolean(this._defaultMessage)}" slot="primaryAction" .label="${this.hass.localize("ui.dialogs.tts-try.play")}" @click="${this._playExample}" .disabled="${!this._valid}"> <ha-svg-icon slot="icon" .path="${"M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M10,16.5L16,12L10,7.5V16.5Z"}"></ha-svg-icon> </ha-button> `} </ha-dialog> `:s.s6}},{kind:"method",key:"_inputChanged",value:async function(){var e;this._valid=Boolean(null===(e=this._messageInput)||void 0===e?void 0:e.value)}},{kind:"method",key:"_playExample",value:async function(){var e;const t=null===(e=this._messageInput)||void 0===e?void 0:e.value;if(!t)return;const i=this._params.engine,a=this._params.language,s=this._params.voice;a&&(this._messages={...this._messages,[a.substring(0,2)]:t}),this._loadingExample=!0;const o=new Audio;let l;o.play();try{l=(await(0,d.S_)(this.hass,{platform:i,message:t,language:a,options:{voice:s}})).path}catch(e){return this._loadingExample=!1,void(0,c.showAlertDialog)(this,{text:`Unable to load example. ${e.error||e.body||e}`,warning:!0})}o.src=l,o.addEventListener("canplaythrough",(()=>o.play())),o.addEventListener("playing",(()=>{this._loadingExample=!1})),o.addEventListener("error",(()=>{(0,c.showAlertDialog)(this,{title:"Error playing audio."}),this._loadingExample=!1}))}},{kind:"get",static:!0,key:"styles",value:function(){return s.AH`ha-dialog{--mdc-dialog-max-width:500px}ha-select,ha-textarea{width:100%}ha-select{margin-top:8px}.loading{height:36px}`}}]}}),s.WF)},86176:()=>{Element.prototype.toggleAttribute||(Element.prototype.toggleAttribute=function(e,t){return void 0!==t&&(t=!!t),this.hasAttribute(e)?!!t||(this.removeAttribute(e),!1):!1!==t&&(this.setAttribute(e,""),!0)})}};
//# sourceMappingURL=19814.Vhn7RYcGn6k.js.map