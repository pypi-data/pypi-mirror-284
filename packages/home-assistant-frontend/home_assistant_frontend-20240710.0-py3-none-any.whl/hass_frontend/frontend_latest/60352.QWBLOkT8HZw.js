/*! For license information please see 60352.QWBLOkT8HZw.js.LICENSE.txt */
export const id=60352;export const ids=[60352,25917,18657,48298,85854,63473,31620,31806,17604,82687,5068,37925,60306,72211,94592];export const modules={87653:(t,e,i)=>{i.d(e,{ZS:()=>c,is:()=>s.i});i(21950),i(8339);var o,a,r=i(76513),n=i(18791),s=i(71086);const d=null!==(a=null===(o=window.ShadyDOM)||void 0===o?void 0:o.inUse)&&void 0!==a&&a;class c extends s.O{constructor(){super(...arguments),this.disabled=!1,this.containingForm=null,this.formDataListener=t=>{this.disabled||this.setFormData(t.formData)}}findFormElement(){if(!this.shadowRoot||d)return null;const t=this.getRootNode().querySelectorAll("form");for(const e of Array.from(t))if(e.contains(this))return e;return null}connectedCallback(){var t;super.connectedCallback(),this.containingForm=this.findFormElement(),null===(t=this.containingForm)||void 0===t||t.addEventListener("formdata",this.formDataListener)}disconnectedCallback(){var t;super.disconnectedCallback(),null===(t=this.containingForm)||void 0===t||t.removeEventListener("formdata",this.formDataListener),this.containingForm=null}click(){this.formElement&&!this.disabled&&(this.formElement.focus(),this.formElement.click())}firstUpdated(){super.firstUpdated(),this.shadowRoot&&this.mdcRoot.addEventListener("change",(t=>{this.dispatchEvent(new Event("change",t))}))}}c.shadowRootOptions={mode:"open",delegatesFocus:!0},(0,r.__decorate)([(0,n.MZ)({type:Boolean})],c.prototype,"disabled",void 0)},32082:(t,e,i)=>{var o=i(76513),a=i(40924),r=i(18791);const n=a.AH`:host{font-family:var(--mdc-icon-font, "Material Icons");font-weight:400;font-style:normal;font-size:var(--mdc-icon-size, 24px);line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;-moz-osx-font-smoothing:grayscale;font-feature-settings:"liga"}`;let s=class extends a.WF{render(){return a.qy`<span><slot></slot></span>`}};s.styles=[n],s=(0,o.__decorate)([(0,r.EM)("mwc-icon")],s)},46175:(t,e,i)=>{i.d(e,{J:()=>c});i(21950),i(15176),i(8339);var o=i(76513),a=(i(86395),i(16584)),r=i(90523),n=i(40924),s=i(18791),d=i(69760);class c extends n.WF{constructor(){super(...arguments),this.value="",this.group=null,this.tabindex=-1,this.disabled=!1,this.twoline=!1,this.activated=!1,this.graphic=null,this.multipleGraphics=!1,this.hasMeta=!1,this.noninteractive=!1,this.selected=!1,this.shouldRenderRipple=!1,this._managingList=null,this.boundOnClick=this.onClick.bind(this),this._firstChanged=!0,this._skipPropRequest=!1,this.rippleHandlers=new r.I((()=>(this.shouldRenderRipple=!0,this.ripple))),this.listeners=[{target:this,eventNames:["click"],cb:()=>{this.onClick()}},{target:this,eventNames:["mouseenter"],cb:this.rippleHandlers.startHover},{target:this,eventNames:["mouseleave"],cb:this.rippleHandlers.endHover},{target:this,eventNames:["focus"],cb:this.rippleHandlers.startFocus},{target:this,eventNames:["blur"],cb:this.rippleHandlers.endFocus},{target:this,eventNames:["mousedown","touchstart"],cb:t=>{const e=t.type;this.onDown("mousedown"===e?"mouseup":"touchend",t)}}]}get text(){const t=this.textContent;return t?t.trim():""}render(){const t=this.renderText(),e=this.graphic?this.renderGraphic():n.qy``,i=this.hasMeta?this.renderMeta():n.qy``;return n.qy` ${this.renderRipple()} ${e} ${t} ${i}`}renderRipple(){return this.shouldRenderRipple?n.qy` <mwc-ripple .activated="${this.activated}"> </mwc-ripple>`:this.activated?n.qy`<div class="fake-activated-ripple"></div>`:""}renderGraphic(){const t={multi:this.multipleGraphics};return n.qy` <span class="mdc-deprecated-list-item__graphic material-icons ${(0,d.H)(t)}"> <slot name="graphic"></slot> </span>`}renderMeta(){return n.qy` <span class="mdc-deprecated-list-item__meta material-icons"> <slot name="meta"></slot> </span>`}renderText(){const t=this.twoline?this.renderTwoline():this.renderSingleLine();return n.qy` <span class="mdc-deprecated-list-item__text"> ${t} </span>`}renderSingleLine(){return n.qy`<slot></slot>`}renderTwoline(){return n.qy` <span class="mdc-deprecated-list-item__primary-text"> <slot></slot> </span> <span class="mdc-deprecated-list-item__secondary-text"> <slot name="secondary"></slot> </span> `}onClick(){this.fireRequestSelected(!this.selected,"interaction")}onDown(t,e){const i=()=>{window.removeEventListener(t,i),this.rippleHandlers.endPress()};window.addEventListener(t,i),this.rippleHandlers.startPress(e)}fireRequestSelected(t,e){if(this.noninteractive)return;const i=new CustomEvent("request-selected",{bubbles:!0,composed:!0,detail:{source:e,selected:t}});this.dispatchEvent(i)}connectedCallback(){super.connectedCallback(),this.noninteractive||this.setAttribute("mwc-list-item","");for(const t of this.listeners)for(const e of t.eventNames)t.target.addEventListener(e,t.cb,{passive:!0})}disconnectedCallback(){super.disconnectedCallback();for(const t of this.listeners)for(const e of t.eventNames)t.target.removeEventListener(e,t.cb);this._managingList&&(this._managingList.debouncedLayout?this._managingList.debouncedLayout(!0):this._managingList.layout(!0))}firstUpdated(){const t=new Event("list-item-rendered",{bubbles:!0,composed:!0});this.dispatchEvent(t)}}(0,o.__decorate)([(0,s.P)("slot")],c.prototype,"slotElement",void 0),(0,o.__decorate)([(0,s.nJ)("mwc-ripple")],c.prototype,"ripple",void 0),(0,o.__decorate)([(0,s.MZ)({type:String})],c.prototype,"value",void 0),(0,o.__decorate)([(0,s.MZ)({type:String,reflect:!0})],c.prototype,"group",void 0),(0,o.__decorate)([(0,s.MZ)({type:Number,reflect:!0})],c.prototype,"tabindex",void 0),(0,o.__decorate)([(0,s.MZ)({type:Boolean,reflect:!0}),(0,a.P)((function(t){t?this.setAttribute("aria-disabled","true"):this.setAttribute("aria-disabled","false")}))],c.prototype,"disabled",void 0),(0,o.__decorate)([(0,s.MZ)({type:Boolean,reflect:!0})],c.prototype,"twoline",void 0),(0,o.__decorate)([(0,s.MZ)({type:Boolean,reflect:!0})],c.prototype,"activated",void 0),(0,o.__decorate)([(0,s.MZ)({type:String,reflect:!0})],c.prototype,"graphic",void 0),(0,o.__decorate)([(0,s.MZ)({type:Boolean})],c.prototype,"multipleGraphics",void 0),(0,o.__decorate)([(0,s.MZ)({type:Boolean})],c.prototype,"hasMeta",void 0),(0,o.__decorate)([(0,s.MZ)({type:Boolean,reflect:!0}),(0,a.P)((function(t){t?(this.removeAttribute("aria-checked"),this.removeAttribute("mwc-list-item"),this.selected=!1,this.activated=!1,this.tabIndex=-1):this.setAttribute("mwc-list-item","")}))],c.prototype,"noninteractive",void 0),(0,o.__decorate)([(0,s.MZ)({type:Boolean,reflect:!0}),(0,a.P)((function(t){const e=this.getAttribute("role"),i="gridcell"===e||"option"===e||"row"===e||"tab"===e;i&&t?this.setAttribute("aria-selected","true"):i&&this.setAttribute("aria-selected","false"),this._firstChanged?this._firstChanged=!1:this._skipPropRequest||this.fireRequestSelected(t,"property")}))],c.prototype,"selected",void 0),(0,o.__decorate)([(0,s.wk)()],c.prototype,"shouldRenderRipple",void 0),(0,o.__decorate)([(0,s.wk)()],c.prototype,"_managingList",void 0)},45592:(t,e,i)=>{i.d(e,{R:()=>o});const o=i(40924).AH`:host{cursor:pointer;user-select:none;-webkit-tap-highlight-color:transparent;height:48px;display:flex;position:relative;align-items:center;justify-content:flex-start;overflow:hidden;padding:0;padding-left:var(--mdc-list-side-padding,16px);padding-right:var(--mdc-list-side-padding,16px);outline:0;height:48px;color:rgba(0,0,0,.87);color:var(--mdc-theme-text-primary-on-background,rgba(0,0,0,.87))}:host:focus{outline:0}:host([activated]){color:#6200ee;color:var(--mdc-theme-primary,#6200ee);--mdc-ripple-color:var( --mdc-theme-primary, #6200ee )}:host([activated]) .mdc-deprecated-list-item__graphic{color:#6200ee;color:var(--mdc-theme-primary,#6200ee)}:host([activated]) .fake-activated-ripple::before{position:absolute;display:block;top:0;bottom:0;left:0;right:0;width:100%;height:100%;pointer-events:none;z-index:1;content:"";opacity:.12;opacity:var(--mdc-ripple-activated-opacity, .12);background-color:#6200ee;background-color:var(--mdc-ripple-color,var(--mdc-theme-primary,#6200ee))}.mdc-deprecated-list-item__graphic{flex-shrink:0;align-items:center;justify-content:center;fill:currentColor;display:inline-flex}.mdc-deprecated-list-item__graphic ::slotted(*){flex-shrink:0;align-items:center;justify-content:center;fill:currentColor;width:100%;height:100%;text-align:center}.mdc-deprecated-list-item__meta{width:var(--mdc-list-item-meta-size,24px);height:var(--mdc-list-item-meta-size,24px);margin-left:auto;margin-right:0;color:rgba(0,0,0,.38);color:var(--mdc-theme-text-hint-on-background,rgba(0,0,0,.38))}.mdc-deprecated-list-item__meta.multi{width:auto}.mdc-deprecated-list-item__meta ::slotted(*){width:var(--mdc-list-item-meta-size,24px);line-height:var(--mdc-list-item-meta-size, 24px)}.mdc-deprecated-list-item__meta ::slotted(.material-icons),.mdc-deprecated-list-item__meta ::slotted(mwc-icon){line-height:var(--mdc-list-item-meta-size, 24px)!important}.mdc-deprecated-list-item__meta ::slotted(:not(.material-icons):not(mwc-icon)){-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto,sans-serif;font-family:var(--mdc-typography-caption-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:.75rem;font-size:var(--mdc-typography-caption-font-size, .75rem);line-height:1.25rem;line-height:var(--mdc-typography-caption-line-height, 1.25rem);font-weight:400;font-weight:var(--mdc-typography-caption-font-weight,400);letter-spacing:.0333333333em;letter-spacing:var(--mdc-typography-caption-letter-spacing, .0333333333em);text-decoration:inherit;text-decoration:var(--mdc-typography-caption-text-decoration,inherit);text-transform:inherit;text-transform:var(--mdc-typography-caption-text-transform,inherit)}.mdc-deprecated-list-item__meta[dir=rtl],[dir=rtl] .mdc-deprecated-list-item__meta{margin-left:0;margin-right:auto}.mdc-deprecated-list-item__meta ::slotted(*){width:100%;height:100%}.mdc-deprecated-list-item__text{text-overflow:ellipsis;white-space:nowrap;overflow:hidden}.mdc-deprecated-list-item__text ::slotted([for]),.mdc-deprecated-list-item__text[for]{pointer-events:none}.mdc-deprecated-list-item__primary-text{text-overflow:ellipsis;white-space:nowrap;overflow:hidden;display:block;margin-top:0;line-height:normal;margin-bottom:-20px;display:block}.mdc-deprecated-list-item__primary-text::before{display:inline-block;width:0;height:32px;content:"";vertical-align:0}.mdc-deprecated-list-item__primary-text::after{display:inline-block;width:0;height:20px;content:"";vertical-align:-20px}.mdc-deprecated-list-item__secondary-text{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto,sans-serif;font-family:var(--mdc-typography-body2-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:.875rem;font-size:var(--mdc-typography-body2-font-size, .875rem);line-height:1.25rem;line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:400;font-weight:var(--mdc-typography-body2-font-weight,400);letter-spacing:.0178571429em;letter-spacing:var(--mdc-typography-body2-letter-spacing, .0178571429em);text-decoration:inherit;text-decoration:var(--mdc-typography-body2-text-decoration,inherit);text-transform:inherit;text-transform:var(--mdc-typography-body2-text-transform,inherit);text-overflow:ellipsis;white-space:nowrap;overflow:hidden;display:block;margin-top:0;line-height:normal;display:block}.mdc-deprecated-list-item__secondary-text::before{display:inline-block;width:0;height:20px;content:"";vertical-align:0}.mdc-deprecated-list--dense .mdc-deprecated-list-item__secondary-text{font-size:inherit}* ::slotted(a),a{color:inherit;text-decoration:none}:host([twoline]){height:72px}:host([twoline]) .mdc-deprecated-list-item__text{align-self:flex-start}:host([disabled]),:host([noninteractive]){cursor:default;pointer-events:none}:host([disabled]) .mdc-deprecated-list-item__text ::slotted(*){opacity:.38}:host([disabled]) .mdc-deprecated-list-item__primary-text ::slotted(*),:host([disabled]) .mdc-deprecated-list-item__secondary-text ::slotted(*),:host([disabled]) .mdc-deprecated-list-item__text ::slotted(*){color:#000;color:var(--mdc-theme-on-surface,#000)}.mdc-deprecated-list-item__secondary-text ::slotted(*){color:rgba(0,0,0,.54);color:var(--mdc-theme-text-secondary-on-background,rgba(0,0,0,.54))}.mdc-deprecated-list-item__graphic ::slotted(*){background-color:transparent;color:rgba(0,0,0,.38);color:var(--mdc-theme-text-icon-on-background,rgba(0,0,0,.38))}.mdc-deprecated-list-group__subheader ::slotted(*){color:rgba(0,0,0,.87);color:var(--mdc-theme-text-primary-on-background,rgba(0,0,0,.87))}:host([graphic=avatar]) .mdc-deprecated-list-item__graphic{width:var(--mdc-list-item-graphic-size,40px);height:var(--mdc-list-item-graphic-size,40px)}:host([graphic=avatar]) .mdc-deprecated-list-item__graphic.multi{width:auto}:host([graphic=avatar]) .mdc-deprecated-list-item__graphic ::slotted(*){width:var(--mdc-list-item-graphic-size,40px);line-height:var(--mdc-list-item-graphic-size, 40px)}:host([graphic=avatar]) .mdc-deprecated-list-item__graphic ::slotted(.material-icons),:host([graphic=avatar]) .mdc-deprecated-list-item__graphic ::slotted(mwc-icon){line-height:var(--mdc-list-item-graphic-size, 40px)!important}:host([graphic=avatar]) .mdc-deprecated-list-item__graphic ::slotted(*){border-radius:50%}:host([graphic=avatar]) .mdc-deprecated-list-item__graphic,:host([graphic=control]) .mdc-deprecated-list-item__graphic,:host([graphic=large]) .mdc-deprecated-list-item__graphic,:host([graphic=medium]) .mdc-deprecated-list-item__graphic{margin-left:0;margin-right:var(--mdc-list-item-graphic-margin,16px)}:host([graphic=avatar]) .mdc-deprecated-list-item__graphic[dir=rtl],:host([graphic=control]) .mdc-deprecated-list-item__graphic[dir=rtl],:host([graphic=large]) .mdc-deprecated-list-item__graphic[dir=rtl],:host([graphic=medium]) .mdc-deprecated-list-item__graphic[dir=rtl],[dir=rtl] :host([graphic=avatar]) .mdc-deprecated-list-item__graphic,[dir=rtl] :host([graphic=control]) .mdc-deprecated-list-item__graphic,[dir=rtl] :host([graphic=large]) .mdc-deprecated-list-item__graphic,[dir=rtl] :host([graphic=medium]) .mdc-deprecated-list-item__graphic{margin-left:var(--mdc-list-item-graphic-margin,16px);margin-right:0}:host([graphic=icon]) .mdc-deprecated-list-item__graphic{width:var(--mdc-list-item-graphic-size,24px);height:var(--mdc-list-item-graphic-size,24px);margin-left:0;margin-right:var(--mdc-list-item-graphic-margin,32px)}:host([graphic=icon]) .mdc-deprecated-list-item__graphic.multi{width:auto}:host([graphic=icon]) .mdc-deprecated-list-item__graphic ::slotted(*){width:var(--mdc-list-item-graphic-size,24px);line-height:var(--mdc-list-item-graphic-size, 24px)}:host([graphic=icon]) .mdc-deprecated-list-item__graphic ::slotted(.material-icons),:host([graphic=icon]) .mdc-deprecated-list-item__graphic ::slotted(mwc-icon){line-height:var(--mdc-list-item-graphic-size, 24px)!important}:host([graphic=icon]) .mdc-deprecated-list-item__graphic[dir=rtl],[dir=rtl] :host([graphic=icon]) .mdc-deprecated-list-item__graphic{margin-left:var(--mdc-list-item-graphic-margin,32px);margin-right:0}:host([graphic=avatar]:not([twoLine])),:host([graphic=icon]:not([twoLine])){height:56px}:host([graphic=large]:not([twoLine])),:host([graphic=medium]:not([twoLine])){height:72px}:host([graphic=large]) .mdc-deprecated-list-item__graphic,:host([graphic=medium]) .mdc-deprecated-list-item__graphic{width:var(--mdc-list-item-graphic-size,56px);height:var(--mdc-list-item-graphic-size,56px)}:host([graphic=large]) .mdc-deprecated-list-item__graphic.multi,:host([graphic=medium]) .mdc-deprecated-list-item__graphic.multi{width:auto}:host([graphic=large]) .mdc-deprecated-list-item__graphic ::slotted(*),:host([graphic=medium]) .mdc-deprecated-list-item__graphic ::slotted(*){width:var(--mdc-list-item-graphic-size,56px);line-height:var(--mdc-list-item-graphic-size, 56px)}:host([graphic=large]) .mdc-deprecated-list-item__graphic ::slotted(.material-icons),:host([graphic=large]) .mdc-deprecated-list-item__graphic ::slotted(mwc-icon),:host([graphic=medium]) .mdc-deprecated-list-item__graphic ::slotted(.material-icons),:host([graphic=medium]) .mdc-deprecated-list-item__graphic ::slotted(mwc-icon){line-height:var(--mdc-list-item-graphic-size, 56px)!important}:host([graphic=large]){padding-left:0px}`},49716:(t,e,i)=>{var o=i(95124);t.exports=function(t,e,i){for(var a=0,r=arguments.length>2?i:o(e),n=new t(r);r>a;)n[a]=e[a++];return n}},21903:(t,e,i)=>{var o=i(16230),a=i(82374),r=i(43973),n=i(51607),s=i(75011),d=i(95124),c=i(17998),l=i(49716),h=Array,m=a([].push);t.exports=function(t,e,i,a){for(var p,g,u,_=n(t),f=r(_),y=o(e,i),v=c(null),b=d(f),w=0;b>w;w++)u=f[w],(g=s(y(u,w,_)))in v?m(v[g],u):v[g]=[u];if(a&&(p=a(_))!==h)for(g in v)v[g]=l(p,v[g]);return v}},15176:(t,e,i)=>{var o=i(87568),a=i(21903),r=i(33523);o({target:"Array",proto:!0},{group:function(t){return a(this,t,arguments.length>1?arguments[1]:void 0)}}),r("group")},38129:(t,e,i)=>{var o=i(87568),a=i(59598),r=i(30356),n=i(33817),s=i(3429);o({target:"Iterator",proto:!0,real:!0},{every:function(t){n(this),r(t);var e=s(this),i=0;return!a(e,(function(e,o){if(!t(e,i++))return o()}),{IS_RECORD:!0,INTERRUPTED:!0}).stopped}})},87777:(t,e,i)=>{i(66274),i(84531);var o=i(40924);class a extends o.WF{static get styles(){return[o.AH`:host{display:block;position:absolute;outline:0;z-index:1002;-moz-user-select:none;-ms-user-select:none;-webkit-user-select:none;user-select:none;cursor:default;pointer-events:none}#tooltip{display:block;outline:0;font-size:var(--simple-tooltip-font-size, 10px);line-height:1;background-color:var(--simple-tooltip-background,#616161);color:var(--simple-tooltip-text-color,#fff);padding:8px;border-radius:var(--simple-tooltip-border-radius,2px);width:var(--simple-tooltip-width)}@keyframes keyFrameScaleUp{0%{transform:scale(0)}100%{transform:scale(1)}}@keyframes keyFrameScaleDown{0%{transform:scale(1)}100%{transform:scale(0)}}@keyframes keyFrameFadeInOpacity{0%{opacity:0}100%{opacity:var(--simple-tooltip-opacity, .9)}}@keyframes keyFrameFadeOutOpacity{0%{opacity:var(--simple-tooltip-opacity, .9)}100%{opacity:0}}@keyframes keyFrameSlideDownIn{0%{transform:translateY(-2000px);opacity:0}10%{opacity:.2}100%{transform:translateY(0);opacity:var(--simple-tooltip-opacity, .9)}}@keyframes keyFrameSlideDownOut{0%{transform:translateY(0);opacity:var(--simple-tooltip-opacity, .9)}10%{opacity:.2}100%{transform:translateY(-2000px);opacity:0}}.fade-in-animation{opacity:0;animation-delay:var(--simple-tooltip-delay-in, 500ms);animation-name:keyFrameFadeInOpacity;animation-iteration-count:1;animation-timing-function:ease-in;animation-duration:var(--simple-tooltip-duration-in, 500ms);animation-fill-mode:forwards}.fade-out-animation{opacity:var(--simple-tooltip-opacity, .9);animation-delay:var(--simple-tooltip-delay-out, 0ms);animation-name:keyFrameFadeOutOpacity;animation-iteration-count:1;animation-timing-function:ease-in;animation-duration:var(--simple-tooltip-duration-out, 500ms);animation-fill-mode:forwards}.scale-up-animation{transform:scale(0);opacity:var(--simple-tooltip-opacity, .9);animation-delay:var(--simple-tooltip-delay-in, 500ms);animation-name:keyFrameScaleUp;animation-iteration-count:1;animation-timing-function:ease-in;animation-duration:var(--simple-tooltip-duration-in, 500ms);animation-fill-mode:forwards}.scale-down-animation{transform:scale(1);opacity:var(--simple-tooltip-opacity, .9);animation-delay:var(--simple-tooltip-delay-out, 500ms);animation-name:keyFrameScaleDown;animation-iteration-count:1;animation-timing-function:ease-in;animation-duration:var(--simple-tooltip-duration-out, 500ms);animation-fill-mode:forwards}.slide-down-animation{transform:translateY(-2000px);opacity:0;animation-delay:var(--simple-tooltip-delay-out, 500ms);animation-name:keyFrameSlideDownIn;animation-iteration-count:1;animation-timing-function:cubic-bezier(0,0,0.2,1);animation-duration:var(--simple-tooltip-duration-out, 500ms);animation-fill-mode:forwards}.slide-down-animation-out{transform:translateY(0);opacity:var(--simple-tooltip-opacity, .9);animation-delay:var(--simple-tooltip-delay-out, 500ms);animation-name:keyFrameSlideDownOut;animation-iteration-count:1;animation-timing-function:cubic-bezier(0.4,0,1,1);animation-duration:var(--simple-tooltip-duration-out, 500ms);animation-fill-mode:forwards}.cancel-animation{animation-delay:-30s!important}.hidden{position:absolute;left:-10000px;inset-inline-start:-10000px;inset-inline-end:initial;top:auto;width:1px;height:1px;overflow:hidden}`]}render(){return o.qy` <div id="tooltip" class="hidden" @animationend="${this._onAnimationEnd}"> <slot></slot> </div>`}static get properties(){return{...super.properties,for:{type:String},manualMode:{type:Boolean,attribute:"manual-mode"},position:{type:String},fitToVisibleBounds:{type:Boolean,attribute:"fit-to-visible-bounds"},offset:{type:Number},marginTop:{type:Number,attribute:"margin-top"},animationDelay:{type:Number,attribute:"animation-delay"},animationEntry:{type:String,attribute:"animation-entry"},animationExit:{type:String,attribute:"animation-exit"},_showing:{type:Boolean}}}static get tag(){return"simple-tooltip"}constructor(){super(),this.manualMode=!1,this.position="bottom",this.fitToVisibleBounds=!1,this.offset=14,this.marginTop=14,this.animationEntry="",this.animationExit="",this.animationConfig={entry:[{name:"fade-in-animation",node:this,timing:{delay:0}}],exit:[{name:"fade-out-animation",node:this}]},setTimeout((()=>{this.addEventListener("webkitAnimationEnd",this._onAnimationEnd.bind(this)),this.addEventListener("mouseenter",this.hide.bind(this))}),0)}get target(){var t=this.parentNode,e=this.getRootNode();return this.for?e.querySelector("#"+this.for):t.nodeType==Node.DOCUMENT_FRAGMENT_NODE?e.host:t}disconnectedCallback(){this.manualMode||this._removeListeners(),super.disconnectedCallback()}playAnimation(t){"entry"===t?this.show():"exit"===t&&this.hide()}cancelAnimation(){this.shadowRoot.querySelector("#tooltip").classList.add("cancel-animation")}show(){if(!this._showing){if(""===this.textContent.trim()){for(var t=!0,e=this.children,i=0;i<e.length;i++)if(""!==e[i].textContent.trim()){t=!1;break}if(t)return}this._showing=!0,this.shadowRoot.querySelector("#tooltip").classList.remove("hidden"),this.shadowRoot.querySelector("#tooltip").classList.remove("cancel-animation"),this.shadowRoot.querySelector("#tooltip").classList.remove(this._getAnimationType("exit")),this.updatePosition(),this._animationPlaying=!0,this.shadowRoot.querySelector("#tooltip").classList.add(this._getAnimationType("entry"))}}hide(){if(this._showing){if(this._animationPlaying)return this._showing=!1,void this._cancelAnimation();this._onAnimationFinish(),this._showing=!1,this._animationPlaying=!0,clearTimeout(this.__debounceCancel),this.__debounceCancel=setTimeout((()=>{this._cancelAnimation()}),5e3)}}updatePosition(){if(this._target&&this.offsetParent){var t=this.offset;14!=this.marginTop&&14==this.offset&&(t=this.marginTop);var e,i,o=this.offsetParent.getBoundingClientRect(),a=this._target.getBoundingClientRect(),r=this.getBoundingClientRect(),n=(a.width-r.width)/2,s=(a.height-r.height)/2,d=a.left-o.left,c=a.top-o.top;switch(this.position){case"top":e=d+n,i=c-r.height-t;break;case"bottom":e=d+n,i=c+a.height+t;break;case"left":e=d-r.width-t,i=c+s;break;case"right":e=d+a.width+t,i=c+s}this.fitToVisibleBounds?(o.left+e+r.width>window.innerWidth?(this.style.right="0px",this.style.left="auto"):(this.style.left=Math.max(0,e)+"px",this.style.right="auto"),o.top+i+r.height>window.innerHeight?(this.style.bottom=o.height-c+t+"px",this.style.top="auto"):(this.style.top=Math.max(-o.top,i)+"px",this.style.bottom="auto")):(this.style.left=e+"px",this.style.top=i+"px")}}_addListeners(){this._target&&(this._target.addEventListener("mouseenter",this.show.bind(this)),this._target.addEventListener("focus",this.show.bind(this)),this._target.addEventListener("mouseleave",this.hide.bind(this)),this._target.addEventListener("blur",this.hide.bind(this)),this._target.addEventListener("tap",this.hide.bind(this)))}_findTarget(){this.manualMode||this._removeListeners(),this._target=this.target,this.manualMode||this._addListeners()}_manualModeChanged(){this.manualMode?this._removeListeners():this._addListeners()}_cancelAnimation(){this.shadowRoot.querySelector("#tooltip").classList.remove(this._getAnimationType("entry")),this.shadowRoot.querySelector("#tooltip").classList.remove(this._getAnimationType("exit")),this.shadowRoot.querySelector("#tooltip").classList.remove("cancel-animation"),this.shadowRoot.querySelector("#tooltip").classList.add("hidden")}_onAnimationFinish(){this._showing&&(this.shadowRoot.querySelector("#tooltip").classList.remove(this._getAnimationType("entry")),this.shadowRoot.querySelector("#tooltip").classList.remove("cancel-animation"),this.shadowRoot.querySelector("#tooltip").classList.add(this._getAnimationType("exit")))}_onAnimationEnd(){this._animationPlaying=!1,this._showing||(this.shadowRoot.querySelector("#tooltip").classList.remove(this._getAnimationType("exit")),this.shadowRoot.querySelector("#tooltip").classList.add("hidden"))}_getAnimationType(t){if("entry"===t&&""!==this.animationEntry)return this.animationEntry;if("exit"===t&&""!==this.animationExit)return this.animationExit;if(this.animationConfig[t]&&"string"==typeof this.animationConfig[t][0].name){if(this.animationConfig[t][0].timing&&this.animationConfig[t][0].timing.delay&&0!==this.animationConfig[t][0].timing.delay){var e=this.animationConfig[t][0].timing.delay;"entry"===t?document.documentElement.style.setProperty("--simple-tooltip-delay-in",e+"ms"):"exit"===t&&document.documentElement.style.setProperty("--simple-tooltip-delay-out",e+"ms")}return this.animationConfig[t][0].name}}_removeListeners(){this._target&&(this._target.removeEventListener("mouseover",this.show.bind(this)),this._target.removeEventListener("focusin",this.show.bind(this)),this._target.removeEventListener("mouseout",this.hide.bind(this)),this._target.removeEventListener("focusout",this.hide.bind(this)),this._target.removeEventListener("click",this.hide.bind(this)))}firstUpdated(t){this.setAttribute("role","tooltip"),this.setAttribute("tabindex",-1),this._findTarget()}updated(t){t.forEach(((t,e)=>{"for"==e&&this._findTarget(this[e],t),"manualMode"==e&&this._manualModeChanged(this[e],t),"animationDelay"==e&&this._delayChange(this[e],t)}))}_delayChange(t){500!==t&&document.documentElement.style.setProperty("--simple-tooltip-delay-in",t+"ms")}}customElements.define(a.tag,a)},66613:(t,e,i)=>{i.d(e,{IU:()=>c,Jt:()=>s,Yd:()=>o,hZ:()=>d,y$:()=>a});i(21950),i(71936),i(55888),i(66274),i(84531),i(98168),i(8339);function o(t){return new Promise(((e,i)=>{t.oncomplete=t.onsuccess=()=>e(t.result),t.onabort=t.onerror=()=>i(t.error)}))}function a(t,e){const i=indexedDB.open(t);i.onupgradeneeded=()=>i.result.createObjectStore(e);const a=o(i);return(t,i)=>a.then((o=>i(o.transaction(e,t).objectStore(e))))}let r;function n(){return r||(r=a("keyval-store","keyval")),r}function s(t,e=n()){return e("readonly",(e=>o(e.get(t))))}function d(t,e,i=n()){return i("readwrite",(i=>(i.put(e,t),o(i.transaction))))}function c(t=n()){return t("readwrite",(t=>(t.clear(),o(t.transaction))))}},3267:(t,e,i)=>{i.d(e,{Kq:()=>h});i(21950),i(15445),i(24483),i(13478),i(46355),i(14612),i(53691),i(48455),i(8339);var o=i(3982),a=i(2154);const r=(t,e)=>{var i,o;const a=t._$AN;if(void 0===a)return!1;for(const t of a)null===(o=(i=t)._$AO)||void 0===o||o.call(i,e,!1),r(t,e);return!0},n=t=>{let e,i;do{if(void 0===(e=t._$AM))break;i=e._$AN,i.delete(t),t=e}while(0===(null==i?void 0:i.size))},s=t=>{for(let e;e=t._$AM;t=e){let i=e._$AN;if(void 0===i)e._$AN=i=new Set;else if(i.has(t))break;i.add(t),l(e)}};function d(t){void 0!==this._$AN?(n(this),this._$AM=t,s(this)):this._$AM=t}function c(t,e=!1,i=0){const o=this._$AH,a=this._$AN;if(void 0!==a&&0!==a.size)if(e)if(Array.isArray(o))for(let t=i;t<o.length;t++)r(o[t],!1),n(o[t]);else null!=o&&(r(o,!1),n(o));else r(this,t)}const l=t=>{var e,i,o,r;t.type==a.OA.CHILD&&(null!==(e=(o=t)._$AP)&&void 0!==e||(o._$AP=c),null!==(i=(r=t)._$AQ)&&void 0!==i||(r._$AQ=d))};class h extends a.WL{constructor(){super(...arguments),this._$AN=void 0}_$AT(t,e,i){super._$AT(t,e,i),s(this),this.isConnected=t._$AU}_$AO(t,e=!0){var i,o;t!==this.isConnected&&(this.isConnected=t,t?null===(i=this.reconnected)||void 0===i||i.call(this):null===(o=this.disconnected)||void 0===o||o.call(this)),e&&(r(this,t),n(this))}setValue(t){if((0,o.Rt)(this._$Ct))this._$Ct._$AI(t,this);else{const e=[...this._$Ct._$AH];e[this._$Ci]=t,this._$Ct._$AI(e,this,0)}}disconnected(){}reconnected(){}}},3982:(t,e,i)=>{i.d(e,{Dx:()=>l,Jz:()=>_,KO:()=>u,Rt:()=>d,cN:()=>g,lx:()=>h,mY:()=>p,ps:()=>s,qb:()=>n,sO:()=>r});var o=i(34078);const{I:a}=o.ge,r=t=>null===t||"object"!=typeof t&&"function"!=typeof t,n=(t,e)=>void 0===e?void 0!==(null==t?void 0:t._$litType$):(null==t?void 0:t._$litType$)===e,s=t=>{var e;return null!=(null===(e=null==t?void 0:t._$litType$)||void 0===e?void 0:e.h)},d=t=>void 0===t.strings,c=()=>document.createComment(""),l=(t,e,i)=>{var o;const r=t._$AA.parentNode,n=void 0===e?t._$AB:e._$AA;if(void 0===i){const e=r.insertBefore(c(),n),o=r.insertBefore(c(),n);i=new a(e,o,t,t.options)}else{const e=i._$AB.nextSibling,a=i._$AM,s=a!==t;if(s){let e;null===(o=i._$AQ)||void 0===o||o.call(i,t),i._$AM=t,void 0!==i._$AP&&(e=t._$AU)!==a._$AU&&i._$AP(e)}if(e!==n||s){let t=i._$AA;for(;t!==e;){const e=t.nextSibling;r.insertBefore(t,n),t=e}}}return i},h=(t,e,i=t)=>(t._$AI(e,i),t),m={},p=(t,e=m)=>t._$AH=e,g=t=>t._$AH,u=t=>{var e;null===(e=t._$AP)||void 0===e||e.call(t,!1,!0);let i=t._$AA;const o=t._$AB.nextSibling;for(;i!==o;){const t=i.nextSibling;i.remove(),i=t}},_=t=>{t._$AR()}},86625:(t,e,i)=>{i.d(e,{T:()=>m});i(21950),i(55888),i(66274),i(85767),i(8339);var o=i(34078),a=i(3982),r=i(3267);class n{constructor(t){this.G=t}disconnect(){this.G=void 0}reconnect(t){this.G=t}deref(){return this.G}}class s{constructor(){this.Y=void 0,this.Z=void 0}get(){return this.Y}pause(){var t;null!==(t=this.Y)&&void 0!==t||(this.Y=new Promise((t=>this.Z=t)))}resume(){var t;null===(t=this.Z)||void 0===t||t.call(this),this.Y=this.Z=void 0}}var d=i(2154);const c=t=>!(0,a.sO)(t)&&"function"==typeof t.then,l=1073741823;class h extends r.Kq{constructor(){super(...arguments),this._$C_t=l,this._$Cwt=[],this._$Cq=new n(this),this._$CK=new s}render(...t){var e;return null!==(e=t.find((t=>!c(t))))&&void 0!==e?e:o.c0}update(t,e){const i=this._$Cwt;let a=i.length;this._$Cwt=e;const r=this._$Cq,n=this._$CK;this.isConnected||this.disconnected();for(let t=0;t<e.length&&!(t>this._$C_t);t++){const o=e[t];if(!c(o))return this._$C_t=t,o;t<a&&o===i[t]||(this._$C_t=l,a=0,Promise.resolve(o).then((async t=>{for(;n.get();)await n.get();const e=r.deref();if(void 0!==e){const i=e._$Cwt.indexOf(o);i>-1&&i<e._$C_t&&(e._$C_t=i,e.setValue(t))}})))}return o.c0}disconnected(){this._$Cq.disconnect(),this._$CK.pause()}reconnected(){this._$Cq.reconnect(this),this._$CK.resume()}}const m=(0,d.u$)(h)}};
//# sourceMappingURL=60352.QWBLOkT8HZw.js.map