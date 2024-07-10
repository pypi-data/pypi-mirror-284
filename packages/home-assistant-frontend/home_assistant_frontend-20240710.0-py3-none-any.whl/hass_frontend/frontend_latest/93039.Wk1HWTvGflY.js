/*! For license information please see 93039.Wk1HWTvGflY.js.LICENSE.txt */
export const id=93039;export const ids=[93039];export const modules={87653:(e,t,i)=>{i.d(t,{ZS:()=>s,is:()=>l.i});i(21950),i(8339);var r,o,n=i(76513),a=i(18791),l=i(71086);const d=null!==(o=null===(r=window.ShadyDOM)||void 0===r?void 0:r.inUse)&&void 0!==o&&o;class s extends l.O{constructor(){super(...arguments),this.disabled=!1,this.containingForm=null,this.formDataListener=e=>{this.disabled||this.setFormData(e.formData)}}findFormElement(){if(!this.shadowRoot||d)return null;const e=this.getRootNode().querySelectorAll("form");for(const t of Array.from(e))if(t.contains(this))return t;return null}connectedCallback(){var e;super.connectedCallback(),this.containingForm=this.findFormElement(),null===(e=this.containingForm)||void 0===e||e.addEventListener("formdata",this.formDataListener)}disconnectedCallback(){var e;super.disconnectedCallback(),null===(e=this.containingForm)||void 0===e||e.removeEventListener("formdata",this.formDataListener),this.containingForm=null}click(){this.formElement&&!this.disabled&&(this.formElement.focus(),this.formElement.click())}firstUpdated(){super.firstUpdated(),this.shadowRoot&&this.mdcRoot.addEventListener("change",(e=>{this.dispatchEvent(new Event("change",e))}))}}s.shadowRootOptions={mode:"open",delegatesFocus:!0},(0,n.__decorate)([(0,a.MZ)({type:Boolean})],s.prototype,"disabled",void 0)},80487:(e,t,i)=>{i.d(t,{M:()=>h});i(21950),i(55888),i(8339);var r=i(76513),o=i(4943),n={ROOT:"mdc-form-field"},a={LABEL_SELECTOR:".mdc-form-field > label"};const l=function(e){function t(i){var o=e.call(this,(0,r.__assign)((0,r.__assign)({},t.defaultAdapter),i))||this;return o.click=function(){o.handleClick()},o}return(0,r.__extends)(t,e),Object.defineProperty(t,"cssClasses",{get:function(){return n},enumerable:!1,configurable:!0}),Object.defineProperty(t,"strings",{get:function(){return a},enumerable:!1,configurable:!0}),Object.defineProperty(t,"defaultAdapter",{get:function(){return{activateInputRipple:function(){},deactivateInputRipple:function(){},deregisterInteractionHandler:function(){},registerInteractionHandler:function(){}}},enumerable:!1,configurable:!0}),t.prototype.init=function(){this.adapter.registerInteractionHandler("click",this.click)},t.prototype.destroy=function(){this.adapter.deregisterInteractionHandler("click",this.click)},t.prototype.handleClick=function(){var e=this;this.adapter.activateInputRipple(),requestAnimationFrame((function(){e.adapter.deactivateInputRipple()}))},t}(o.I);var d=i(71086),s=i(87653),c=i(16584),f=i(40924),m=i(18791),p=i(69760);class h extends d.O{constructor(){super(...arguments),this.alignEnd=!1,this.spaceBetween=!1,this.nowrap=!1,this.label="",this.mdcFoundationClass=l}createAdapter(){return{registerInteractionHandler:(e,t)=>{this.labelEl.addEventListener(e,t)},deregisterInteractionHandler:(e,t)=>{this.labelEl.removeEventListener(e,t)},activateInputRipple:async()=>{const e=this.input;if(e instanceof s.ZS){const t=await e.ripple;t&&t.startPress()}},deactivateInputRipple:async()=>{const e=this.input;if(e instanceof s.ZS){const t=await e.ripple;t&&t.endPress()}}}}get input(){var e,t;return null!==(t=null===(e=this.slottedInputs)||void 0===e?void 0:e[0])&&void 0!==t?t:null}render(){const e={"mdc-form-field--align-end":this.alignEnd,"mdc-form-field--space-between":this.spaceBetween,"mdc-form-field--nowrap":this.nowrap};return f.qy` <div class="mdc-form-field ${(0,p.H)(e)}"> <slot></slot> <label class="mdc-label" @click="${this._labelClick}">${this.label}</label> </div>`}click(){this._labelClick()}_labelClick(){const e=this.input;e&&(e.focus(),e.click())}}(0,r.__decorate)([(0,m.MZ)({type:Boolean})],h.prototype,"alignEnd",void 0),(0,r.__decorate)([(0,m.MZ)({type:Boolean})],h.prototype,"spaceBetween",void 0),(0,r.__decorate)([(0,m.MZ)({type:Boolean})],h.prototype,"nowrap",void 0),(0,r.__decorate)([(0,m.MZ)({type:String}),(0,c.P)((async function(e){var t;null===(t=this.input)||void 0===t||t.setAttribute("aria-label",e)}))],h.prototype,"label",void 0),(0,r.__decorate)([(0,m.P)(".mdc-form-field")],h.prototype,"mdcRoot",void 0),(0,r.__decorate)([(0,m.gZ)("",!0,"*")],h.prototype,"slottedInputs",void 0),(0,r.__decorate)([(0,m.P)("label")],h.prototype,"labelEl",void 0)},4258:(e,t,i)=>{i.d(t,{R:()=>r});const r=i(40924).AH`.mdc-form-field{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto,sans-serif;font-family:var(--mdc-typography-body2-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:.875rem;font-size:var(--mdc-typography-body2-font-size, .875rem);line-height:1.25rem;line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:400;font-weight:var(--mdc-typography-body2-font-weight,400);letter-spacing:.0178571429em;letter-spacing:var(--mdc-typography-body2-letter-spacing, .0178571429em);text-decoration:inherit;text-decoration:var(--mdc-typography-body2-text-decoration,inherit);text-transform:inherit;text-transform:var(--mdc-typography-body2-text-transform,inherit);color:rgba(0,0,0,.87);color:var(--mdc-theme-text-primary-on-background,rgba(0,0,0,.87));display:inline-flex;align-items:center;vertical-align:middle}.mdc-form-field>label{margin-left:0;margin-right:auto;padding-left:4px;padding-right:0;order:0}.mdc-form-field>label[dir=rtl],[dir=rtl] .mdc-form-field>label{margin-left:auto;margin-right:0}.mdc-form-field>label[dir=rtl],[dir=rtl] .mdc-form-field>label{padding-left:0;padding-right:4px}.mdc-form-field--nowrap>label{text-overflow:ellipsis;overflow:hidden;white-space:nowrap}.mdc-form-field--align-end>label{margin-left:auto;margin-right:0;padding-left:0;padding-right:4px;order:-1}.mdc-form-field--align-end>label[dir=rtl],[dir=rtl] .mdc-form-field--align-end>label{margin-left:0;margin-right:auto}.mdc-form-field--align-end>label[dir=rtl],[dir=rtl] .mdc-form-field--align-end>label{padding-left:4px;padding-right:0}.mdc-form-field--space-between{justify-content:space-between}.mdc-form-field--space-between>label{margin:0}.mdc-form-field--space-between>label[dir=rtl],[dir=rtl] .mdc-form-field--space-between>label{margin:0}:host{display:inline-flex}.mdc-form-field{width:100%}::slotted(*){-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto,sans-serif;font-family:var(--mdc-typography-body2-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:.875rem;font-size:var(--mdc-typography-body2-font-size, .875rem);line-height:1.25rem;line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:400;font-weight:var(--mdc-typography-body2-font-weight,400);letter-spacing:.0178571429em;letter-spacing:var(--mdc-typography-body2-letter-spacing, .0178571429em);text-decoration:inherit;text-decoration:var(--mdc-typography-body2-text-decoration,inherit);text-transform:inherit;text-transform:var(--mdc-typography-body2-text-transform,inherit);color:rgba(0,0,0,.87);color:var(--mdc-theme-text-primary-on-background,rgba(0,0,0,.87))}::slotted(mwc-switch){margin-right:10px}::slotted(mwc-switch[dir=rtl]),[dir=rtl] ::slotted(mwc-switch){margin-left:10px}`},78207:(e,t,i)=>{var r=i(76513),o=i(18791),n=i(80487),a=i(4258);let l=class extends n.M{};l.styles=[a.R],l=(0,r.__decorate)([(0,o.EM)("mwc-formfield")],l)},61674:(e,t,i)=>{var r=i(62659),o=(i(21950),i(8339),i(51497)),n=i(48678),a=i(40924),l=i(18791);(0,r.A)([(0,l.EM)("ha-checkbox")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",static:!0,key:"styles",value:()=>[n.R,a.AH`:host{--mdc-theme-secondary:var(--primary-color)}`]}]}}),o.L)},93039:(e,t,i)=>{i.r(t),i.d(t,{HaFormBoolean:()=>l});var r=i(62659),o=(i(21950),i(8339),i(78207),i(40924)),n=i(18791),a=i(77664);i(61674);let l=(0,r.A)([(0,n.EM)("ha-form-boolean")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"schema",value:void 0},{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,n.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,n.P)("ha-checkbox",!0)],key:"_input",value:void 0},{kind:"method",key:"focus",value:function(){this._input&&this._input.focus()}},{kind:"method",key:"render",value:function(){return o.qy` <mwc-formfield .label="${this.label}"> <ha-checkbox .checked="${this.data}" .disabled="${this.disabled}" @change="${this._valueChanged}"></ha-checkbox> </mwc-formfield> `}},{kind:"method",key:"_valueChanged",value:function(e){(0,a.r)(this,"value-changed",{value:e.target.checked})}}]}}),o.WF)}};
//# sourceMappingURL=93039.Wk1HWTvGflY.js.map