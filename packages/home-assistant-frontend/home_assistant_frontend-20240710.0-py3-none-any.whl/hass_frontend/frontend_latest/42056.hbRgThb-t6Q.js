/*! For license information please see 42056.hbRgThb-t6Q.js.LICENSE.txt */
export const id=42056;export const ids=[42056];export const modules={36639:(t,i,e)=>{e.d(i,{l:()=>o});e(55888);const o=async t=>{if(navigator.clipboard)try{return void await navigator.clipboard.writeText(t)}catch(t){}const i=document.createElement("textarea");i.value=t,document.body.appendChild(i),i.select(),document.execCommand("copy"),document.body.removeChild(i)}},25285:(t,i,e)=>{var o=e(62659),a=(e(21950),e(8339),e(40924)),n=e(18791);(0,o.A)([(0,n.EM)("ha-dialog-header")],(function(t,i){return{F:class extends i{constructor(...i){super(...i),t(this)}},d:[{kind:"method",key:"render",value:function(){return a.qy` <header class="header"> <div class="header-bar"> <section class="header-navigation-icon"> <slot name="navigationIcon"></slot> </section> <section class="header-title"> <slot name="title"></slot> </section> <section class="header-action-items"> <slot name="actionItems"></slot> </section> </div> <slot></slot> </header> `}},{kind:"get",static:!0,key:"styles",value:function(){return[a.AH`:host{display:block}:host([show-border]){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.header-bar{display:flex;flex-direction:row;align-items:flex-start;padding:4px;box-sizing:border-box}.header-title{flex:1;font-size:22px;line-height:28px;font-weight:400;padding:10px 4px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}@media all and (min-width:450px) and (min-height:500px){.header-bar{padding:12px}}.header-navigation-icon{flex:none;min-width:8px;height:100%;display:flex;flex-direction:row}.header-action-items{flex:none;min-width:8px;height:100%;display:flex;flex-direction:row}`]}}]}}),a.WF)},95439:(t,i,e)=>{e.d(i,{l:()=>m});var o=e(62659),a=e(76504),n=e(80792),s=(e(86176),e(21950),e(8339),e(12387)),l=e(52280),r=e(40924),d=e(18791),c=e(25465);e(12731);const h=["button","ha-list-item"],m=(t,i)=>{var e;return r.qy` <div class="header_title"> <span>${i}</span> <ha-icon-button .label="${null!==(e=null==t?void 0:t.localize("ui.dialogs.generic.close"))&&void 0!==e?e:"Close"}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}" dialogAction="close" class="header_button"></ha-icon-button> </div> `};(0,o.A)([(0,d.EM)("ha-dialog")],(function(t,i){class e extends i{constructor(...i){super(...i),t(this)}}return{F:e,d:[{kind:"field",key:c.Xr,value:void 0},{kind:"method",key:"scrollToPos",value:function(t,i){var e;null===(e=this.contentElement)||void 0===e||e.scrollTo(t,i)}},{kind:"method",key:"renderHeading",value:function(){return r.qy`<slot name="heading"> ${(0,a.A)((0,n.A)(e.prototype),"renderHeading",this).call(this)} </slot>`}},{kind:"method",key:"firstUpdated",value:function(){var t;(0,a.A)((0,n.A)(e.prototype),"firstUpdated",this).call(this),this.suppressDefaultPressSelector=[this.suppressDefaultPressSelector,h].join(", "),this._updateScrolledAttribute(),null===(t=this.contentElement)||void 0===t||t.addEventListener("scroll",this._onScroll,{passive:!0})}},{kind:"method",key:"disconnectedCallback",value:function(){(0,a.A)((0,n.A)(e.prototype),"disconnectedCallback",this).call(this),this.contentElement.removeEventListener("scroll",this._onScroll)}},{kind:"field",key:"_onScroll",value(){return()=>{this._updateScrolledAttribute()}}},{kind:"method",key:"_updateScrolledAttribute",value:function(){this.contentElement&&this.toggleAttribute("scrolled",0!==this.contentElement.scrollTop)}},{kind:"field",static:!0,key:"styles",value:()=>[l.R,r.AH`:host([scrolled]) ::slotted(ha-dialog-header){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.mdc-dialog{--mdc-dialog-scroll-divider-color:var(
          --dialog-scroll-divider-color,
          var(--divider-color)
        );z-index:var(--dialog-z-index,8);-webkit-backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));--mdc-dialog-box-shadow:var(--dialog-box-shadow, none);--mdc-typography-headline6-font-weight:400;--mdc-typography-headline6-font-size:1.574rem}.mdc-dialog__actions{justify-content:var(--justify-action-buttons,flex-end);padding-bottom:max(env(safe-area-inset-bottom),24px)}.mdc-dialog__actions span:first-child{flex:var(--secondary-action-button-flex,unset)}.mdc-dialog__actions span:nth-child(2){flex:var(--primary-action-button-flex,unset)}.mdc-dialog__container{align-items:var(--vertical-align-dialog,center)}.mdc-dialog__title{padding:24px 24px 0 24px}.mdc-dialog__actions{padding:12px 24px 12px 24px}.mdc-dialog__title::before{content:unset}.mdc-dialog .mdc-dialog__content{position:var(--dialog-content-position,relative);padding:var(--dialog-content-padding,24px)}:host([hideactions]) .mdc-dialog .mdc-dialog__content{padding-bottom:max(var(--dialog-content-padding,24px),env(safe-area-inset-bottom))}.mdc-dialog .mdc-dialog__surface{position:var(--dialog-surface-position,relative);top:var(--dialog-surface-top);margin-top:var(--dialog-surface-margin-top);min-height:var(--mdc-dialog-min-height,auto);border-radius:var(--ha-dialog-border-radius,28px);-webkit-backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);background:var(--ha-dialog-surface-background,var(--mdc-theme-surface,#fff))}:host([flexContent]) .mdc-dialog .mdc-dialog__content{display:flex;flex-direction:column}.header_title{position:relative;padding-right:40px;padding-inline-end:40px;padding-inline-start:initial;direction:var(--direction)}.header_title span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block}.header_button{position:absolute;right:-12px;top:-12px;text-decoration:none;color:inherit;inset-inline-start:initial;inset-inline-end:-12px;direction:var(--direction)}.dialog-actions{inset-inline-start:initial!important;inset-inline-end:0px!important;direction:var(--direction)}`]}]}}),s.u)},42056:(t,i,e)=>{e.a(t,(async(t,o)=>{try{e.r(i);var a=e(62659),n=e(76504),s=e(80792),l=(e(53501),e(21950),e(55888),e(98168),e(8339),e(87777),e(40924)),r=e(18791),d=e(77664),c=e(36639),h=(e(12261),e(95439),e(25285),e(12731),e(1683),e(58587)),m=e(41361),p=e(14126),u=e(92483),g=e(75610),f=e(34605),y=t([f]);f=(y.then?(await y)():y)[0];const v="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",_="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z";let b=(0,a.A)(null,(function(t,i){class e extends i{constructor(...i){super(...i),t(this)}}return{F:e,d:[{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_manifest",value:void 0},{kind:"method",key:"showDialog",value:async function(t){this._params=t,this._manifest=void 0,await this.updateComplete}},{kind:"method",key:"closeDialog",value:function(){this._params=void 0,(0,d.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"updated",value:function(t){if((0,n.A)((0,s.A)(e.prototype),"updated",this).call(this,t),!t.has("_params")||!this._params)return;const i=(0,m.Fu)(this._params.item);i&&this._fetchManifest(i)}},{kind:"method",key:"render",value:function(){if(!this._params)return l.s6;const t=this._params.item,i=(0,m.Fu)(t),e=this._manifest&&(this._manifest.is_built_in||!this._manifest.documentation.includes("://www.home-assistant.io")),o=this.hass.localize("ui.panel.config.logs.details",{level:l.qy`<span class="${t.level}">${this.hass.localize(`ui.panel.config.logs.level.${t.level}`)}</span>`});return l.qy` <ha-dialog open @closed="${this.closeDialog}" hideActions .heading="${o}"> <ha-dialog-header slot="heading"> <ha-icon-button slot="navigationIcon" dialogAction="cancel" .label="${this.hass.localize("ui.common.close")}" .path="${v}"></ha-icon-button> <span slot="title">${o}</span> <ha-icon-button id="copy" @click="${this._copyLog}" slot="actionItems" .label="${this.hass.localize("ui.panel.config.logs.copy")}" .path="${_}"></ha-icon-button> </ha-dialog-header> ${this.isCustomIntegration?l.qy`<ha-alert alert-type="warning"> ${this.hass.localize("ui.panel.config.logs.error_from_custom_integration")} </ha-alert>`:""} <div class="contents" tabindex="-1" dialogInitialFocus> <p> ${this.hass.localize("ui.panel.config.logs.detail.logger")}: ${t.name}<br> ${this.hass.localize("ui.panel.config.logs.detail.source")}: ${t.source.join(":")} ${i?l.qy` <br> ${this.hass.localize("ui.panel.config.logs.detail.integration")}: ${(0,h.p$)(this.hass.localize,i)} ${this._manifest&&e?l.qy` (<a href="${this._manifest.is_built_in?(0,u.o)(this.hass,`/integrations/${this._manifest.domain}`):this._manifest.documentation}" target="_blank" rel="noreferrer">${this.hass.localize("ui.panel.config.logs.detail.documentation")}</a>${this._manifest.is_built_in||this._manifest.issue_tracker?l.qy`, <a href="${(0,h.QQ)(i,this._manifest)}" target="_blank" rel="noreferrer">${this.hass.localize("ui.panel.config.logs.detail.issues")}</a>`:""}) `:""} `:""} <br> ${t.count>0?l.qy` ${this.hass.localize("ui.panel.config.logs.detail.first_occurred")}: ${(0,f.I)(t.first_occurred,this.hass.locale,this.hass.config)} (${t.count} ${this.hass.localize("ui.panel.config.logs.detail.occurrences")}) <br> `:""} ${this.hass.localize("ui.panel.config.logs.detail.last_logged")}: ${(0,f.I)(t.timestamp,this.hass.locale,this.hass.config)} </p> ${t.message.length>1?l.qy` <ul> ${t.message.map((t=>l.qy` <li>${t}</li> `))} </ul> `:t.message[0]} ${t.exception?l.qy` <pre>${t.exception}</pre> `:l.s6} </div> </ha-dialog> `}},{kind:"get",key:"isCustomIntegration",value:function(){return this._manifest?!this._manifest.is_built_in:(0,m.gk)(this._params.item)}},{kind:"method",key:"_fetchManifest",value:async function(t){try{this._manifest=await(0,h.QC)(this.hass,t)}catch(t){}}},{kind:"method",key:"_copyLog",value:async function(){var t;let i=(null===(t=this.shadowRoot)||void 0===t?void 0:t.querySelector(".contents")).innerText;this.isCustomIntegration&&(i=this.hass.localize("ui.panel.config.logs.error_from_custom_integration")+"\n\n"+i),await(0,c.l)(i),(0,g.P)(this,{message:this.hass.localize("ui.common.copied_clipboard")})}},{kind:"get",static:!0,key:"styles",value:function(){return[p.nA,l.AH`ha-dialog{--dialog-content-padding:0px}a{color:var(--primary-color)}p{margin-top:0}pre{margin-bottom:0;font-family:var(--code-font-family, monospace)}ha-alert{display:block;margin:-4px 0}.contents{padding:16px;outline:0;direction:ltr}.error{color:var(--error-color)}.warning{color:var(--warning-color)}@media all and (min-width:451px) and (min-height:501px){ha-dialog{--mdc-dialog-max-width:90vw}}`]}}]}}),l.WF);customElements.define("dialog-system-log-detail",b),o()}catch(t){o(t)}}))},86176:()=>{Element.prototype.toggleAttribute||(Element.prototype.toggleAttribute=function(t,i){return void 0!==i&&(i=!!i),this.hasAttribute(t)?!!i||(this.removeAttribute(t),!1):!1!==i&&(this.setAttribute(t,""),!0)})},92483:(t,i,e)=>{e.d(i,{o:()=>o});e(53501);const o=(t,i)=>`https://${t.config.version.includes("b")?"rc":t.config.version.includes("dev")?"next":"www"}.home-assistant.io${i}`},87777:(t,i,e)=>{e(66274),e(84531);var o=e(40924);class a extends o.WF{static get styles(){return[o.AH`:host{display:block;position:absolute;outline:0;z-index:1002;-moz-user-select:none;-ms-user-select:none;-webkit-user-select:none;user-select:none;cursor:default;pointer-events:none}#tooltip{display:block;outline:0;font-size:var(--simple-tooltip-font-size, 10px);line-height:1;background-color:var(--simple-tooltip-background,#616161);color:var(--simple-tooltip-text-color,#fff);padding:8px;border-radius:var(--simple-tooltip-border-radius,2px);width:var(--simple-tooltip-width)}@keyframes keyFrameScaleUp{0%{transform:scale(0)}100%{transform:scale(1)}}@keyframes keyFrameScaleDown{0%{transform:scale(1)}100%{transform:scale(0)}}@keyframes keyFrameFadeInOpacity{0%{opacity:0}100%{opacity:var(--simple-tooltip-opacity, .9)}}@keyframes keyFrameFadeOutOpacity{0%{opacity:var(--simple-tooltip-opacity, .9)}100%{opacity:0}}@keyframes keyFrameSlideDownIn{0%{transform:translateY(-2000px);opacity:0}10%{opacity:.2}100%{transform:translateY(0);opacity:var(--simple-tooltip-opacity, .9)}}@keyframes keyFrameSlideDownOut{0%{transform:translateY(0);opacity:var(--simple-tooltip-opacity, .9)}10%{opacity:.2}100%{transform:translateY(-2000px);opacity:0}}.fade-in-animation{opacity:0;animation-delay:var(--simple-tooltip-delay-in, 500ms);animation-name:keyFrameFadeInOpacity;animation-iteration-count:1;animation-timing-function:ease-in;animation-duration:var(--simple-tooltip-duration-in, 500ms);animation-fill-mode:forwards}.fade-out-animation{opacity:var(--simple-tooltip-opacity, .9);animation-delay:var(--simple-tooltip-delay-out, 0ms);animation-name:keyFrameFadeOutOpacity;animation-iteration-count:1;animation-timing-function:ease-in;animation-duration:var(--simple-tooltip-duration-out, 500ms);animation-fill-mode:forwards}.scale-up-animation{transform:scale(0);opacity:var(--simple-tooltip-opacity, .9);animation-delay:var(--simple-tooltip-delay-in, 500ms);animation-name:keyFrameScaleUp;animation-iteration-count:1;animation-timing-function:ease-in;animation-duration:var(--simple-tooltip-duration-in, 500ms);animation-fill-mode:forwards}.scale-down-animation{transform:scale(1);opacity:var(--simple-tooltip-opacity, .9);animation-delay:var(--simple-tooltip-delay-out, 500ms);animation-name:keyFrameScaleDown;animation-iteration-count:1;animation-timing-function:ease-in;animation-duration:var(--simple-tooltip-duration-out, 500ms);animation-fill-mode:forwards}.slide-down-animation{transform:translateY(-2000px);opacity:0;animation-delay:var(--simple-tooltip-delay-out, 500ms);animation-name:keyFrameSlideDownIn;animation-iteration-count:1;animation-timing-function:cubic-bezier(0,0,0.2,1);animation-duration:var(--simple-tooltip-duration-out, 500ms);animation-fill-mode:forwards}.slide-down-animation-out{transform:translateY(0);opacity:var(--simple-tooltip-opacity, .9);animation-delay:var(--simple-tooltip-delay-out, 500ms);animation-name:keyFrameSlideDownOut;animation-iteration-count:1;animation-timing-function:cubic-bezier(0.4,0,1,1);animation-duration:var(--simple-tooltip-duration-out, 500ms);animation-fill-mode:forwards}.cancel-animation{animation-delay:-30s!important}.hidden{position:absolute;left:-10000px;inset-inline-start:-10000px;inset-inline-end:initial;top:auto;width:1px;height:1px;overflow:hidden}`]}render(){return o.qy` <div id="tooltip" class="hidden" @animationend="${this._onAnimationEnd}"> <slot></slot> </div>`}static get properties(){return{...super.properties,for:{type:String},manualMode:{type:Boolean,attribute:"manual-mode"},position:{type:String},fitToVisibleBounds:{type:Boolean,attribute:"fit-to-visible-bounds"},offset:{type:Number},marginTop:{type:Number,attribute:"margin-top"},animationDelay:{type:Number,attribute:"animation-delay"},animationEntry:{type:String,attribute:"animation-entry"},animationExit:{type:String,attribute:"animation-exit"},_showing:{type:Boolean}}}static get tag(){return"simple-tooltip"}constructor(){super(),this.manualMode=!1,this.position="bottom",this.fitToVisibleBounds=!1,this.offset=14,this.marginTop=14,this.animationEntry="",this.animationExit="",this.animationConfig={entry:[{name:"fade-in-animation",node:this,timing:{delay:0}}],exit:[{name:"fade-out-animation",node:this}]},setTimeout((()=>{this.addEventListener("webkitAnimationEnd",this._onAnimationEnd.bind(this)),this.addEventListener("mouseenter",this.hide.bind(this))}),0)}get target(){var t=this.parentNode,i=this.getRootNode();return this.for?i.querySelector("#"+this.for):t.nodeType==Node.DOCUMENT_FRAGMENT_NODE?i.host:t}disconnectedCallback(){this.manualMode||this._removeListeners(),super.disconnectedCallback()}playAnimation(t){"entry"===t?this.show():"exit"===t&&this.hide()}cancelAnimation(){this.shadowRoot.querySelector("#tooltip").classList.add("cancel-animation")}show(){if(!this._showing){if(""===this.textContent.trim()){for(var t=!0,i=this.children,e=0;e<i.length;e++)if(""!==i[e].textContent.trim()){t=!1;break}if(t)return}this._showing=!0,this.shadowRoot.querySelector("#tooltip").classList.remove("hidden"),this.shadowRoot.querySelector("#tooltip").classList.remove("cancel-animation"),this.shadowRoot.querySelector("#tooltip").classList.remove(this._getAnimationType("exit")),this.updatePosition(),this._animationPlaying=!0,this.shadowRoot.querySelector("#tooltip").classList.add(this._getAnimationType("entry"))}}hide(){if(this._showing){if(this._animationPlaying)return this._showing=!1,void this._cancelAnimation();this._onAnimationFinish(),this._showing=!1,this._animationPlaying=!0,clearTimeout(this.__debounceCancel),this.__debounceCancel=setTimeout((()=>{this._cancelAnimation()}),5e3)}}updatePosition(){if(this._target&&this.offsetParent){var t=this.offset;14!=this.marginTop&&14==this.offset&&(t=this.marginTop);var i,e,o=this.offsetParent.getBoundingClientRect(),a=this._target.getBoundingClientRect(),n=this.getBoundingClientRect(),s=(a.width-n.width)/2,l=(a.height-n.height)/2,r=a.left-o.left,d=a.top-o.top;switch(this.position){case"top":i=r+s,e=d-n.height-t;break;case"bottom":i=r+s,e=d+a.height+t;break;case"left":i=r-n.width-t,e=d+l;break;case"right":i=r+a.width+t,e=d+l}this.fitToVisibleBounds?(o.left+i+n.width>window.innerWidth?(this.style.right="0px",this.style.left="auto"):(this.style.left=Math.max(0,i)+"px",this.style.right="auto"),o.top+e+n.height>window.innerHeight?(this.style.bottom=o.height-d+t+"px",this.style.top="auto"):(this.style.top=Math.max(-o.top,e)+"px",this.style.bottom="auto")):(this.style.left=i+"px",this.style.top=e+"px")}}_addListeners(){this._target&&(this._target.addEventListener("mouseenter",this.show.bind(this)),this._target.addEventListener("focus",this.show.bind(this)),this._target.addEventListener("mouseleave",this.hide.bind(this)),this._target.addEventListener("blur",this.hide.bind(this)),this._target.addEventListener("tap",this.hide.bind(this)))}_findTarget(){this.manualMode||this._removeListeners(),this._target=this.target,this.manualMode||this._addListeners()}_manualModeChanged(){this.manualMode?this._removeListeners():this._addListeners()}_cancelAnimation(){this.shadowRoot.querySelector("#tooltip").classList.remove(this._getAnimationType("entry")),this.shadowRoot.querySelector("#tooltip").classList.remove(this._getAnimationType("exit")),this.shadowRoot.querySelector("#tooltip").classList.remove("cancel-animation"),this.shadowRoot.querySelector("#tooltip").classList.add("hidden")}_onAnimationFinish(){this._showing&&(this.shadowRoot.querySelector("#tooltip").classList.remove(this._getAnimationType("entry")),this.shadowRoot.querySelector("#tooltip").classList.remove("cancel-animation"),this.shadowRoot.querySelector("#tooltip").classList.add(this._getAnimationType("exit")))}_onAnimationEnd(){this._animationPlaying=!1,this._showing||(this.shadowRoot.querySelector("#tooltip").classList.remove(this._getAnimationType("exit")),this.shadowRoot.querySelector("#tooltip").classList.add("hidden"))}_getAnimationType(t){if("entry"===t&&""!==this.animationEntry)return this.animationEntry;if("exit"===t&&""!==this.animationExit)return this.animationExit;if(this.animationConfig[t]&&"string"==typeof this.animationConfig[t][0].name){if(this.animationConfig[t][0].timing&&this.animationConfig[t][0].timing.delay&&0!==this.animationConfig[t][0].timing.delay){var i=this.animationConfig[t][0].timing.delay;"entry"===t?document.documentElement.style.setProperty("--simple-tooltip-delay-in",i+"ms"):"exit"===t&&document.documentElement.style.setProperty("--simple-tooltip-delay-out",i+"ms")}return this.animationConfig[t][0].name}}_removeListeners(){this._target&&(this._target.removeEventListener("mouseover",this.show.bind(this)),this._target.removeEventListener("focusin",this.show.bind(this)),this._target.removeEventListener("mouseout",this.hide.bind(this)),this._target.removeEventListener("focusout",this.hide.bind(this)),this._target.removeEventListener("click",this.hide.bind(this)))}firstUpdated(t){this.setAttribute("role","tooltip"),this.setAttribute("tabindex",-1),this._findTarget()}updated(t){t.forEach(((t,i)=>{"for"==i&&this._findTarget(this[i],t),"manualMode"==i&&this._manualModeChanged(this[i],t),"animationDelay"==i&&this._delayChange(this[i],t)}))}_delayChange(t){500!==t&&document.documentElement.style.setProperty("--simple-tooltip-delay-in",t+"ms")}}customElements.define(a.tag,a)}};
//# sourceMappingURL=42056.hbRgThb-t6Q.js.map