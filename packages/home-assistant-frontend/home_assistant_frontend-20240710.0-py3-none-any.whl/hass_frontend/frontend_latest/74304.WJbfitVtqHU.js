/*! For license information please see 74304.WJbfitVtqHU.js.LICENSE.txt */
export const id=74304;export const ids=[74304,4596];export const modules={68286:(e,r,t)=>{function o(e){return void 0===e||Array.isArray(e)?e:[e]}t.d(r,{e:()=>o})},1751:(e,r,t)=>{t.d(r,{g:()=>o});t(53501);const o=e=>(r,t)=>e.includes(r,t)},36471:(e,r,t)=>{t.d(r,{_:()=>a});t(27934),t(21950),t(66274),t(84531),t(8339);var o=t(40924),i=t(3358);const a=(0,i.u$)(class extends i.WL{constructor(e){if(super(e),this._element=void 0,e.type!==i.OA.CHILD)throw new Error("dynamicElementDirective can only be used in content bindings")}update(e,[r,t]){return this._element&&this._element.localName===r?(t&&Object.entries(t).forEach((([e,r])=>{this._element[e]=r})),o.c0):this.render(r,t)}render(e,r){return this._element=document.createElement(e),r&&Object.entries(r).forEach((([e,r])=>{this._element[e]=r})),this._element}})},66596:(e,r,t)=>{t.d(r,{t:()=>i});var o=t(47038);const i=e=>(0,o.m)(e.entity_id)},16327:(e,r,t)=>{t.d(r,{$:()=>o});const o=(e,r)=>i(e.attributes,r),i=(e,r)=>!!(e.supported_features&r)},61003:(e,r,t)=>{var o=t(62659),i=(t(21950),t(8339),t(58068),t(40924)),a=t(18791);t(4596),t(1683);(0,o.A)([(0,a.EM)("ha-progress-button")],(function(e,r){return{F:class extends r{constructor(...r){super(...r),e(this)}},d:[{kind:"field",decorators:[(0,a.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,a.MZ)({type:Boolean})],key:"progress",value:()=>!1},{kind:"field",decorators:[(0,a.MZ)({type:Boolean})],key:"raised",value:()=>!1},{kind:"field",decorators:[(0,a.wk)()],key:"_result",value:void 0},{kind:"method",key:"render",value:function(){const e=this._result||this.progress;return i.qy` <mwc-button ?raised="${this.raised}" .disabled="${this.disabled||this.progress}" @click="${this._buttonTapped}" class="${this._result||""}"> <slot></slot> </mwc-button> ${e?i.qy` <div class="progress"> ${"success"===this._result?i.qy`<ha-svg-icon .path="${"M9,20.42L2.79,14.21L5.62,11.38L9,14.77L18.88,4.88L21.71,7.71L9,20.42Z"}"></ha-svg-icon>`:"error"===this._result?i.qy`<ha-svg-icon .path="${"M2.2,16.06L3.88,12L2.2,7.94L6.26,6.26L7.94,2.2L12,3.88L16.06,2.2L17.74,6.26L21.8,7.94L20.12,12L21.8,16.06L17.74,17.74L16.06,21.8L12,20.12L7.94,21.8L6.26,17.74L2.2,16.06M13,17V15H11V17H13M13,13V7H11V13H13Z"}"></ha-svg-icon>`:this.progress?i.qy` <ha-circular-progress size="small" indeterminate></ha-circular-progress> `:""} </div> `:i.s6} `}},{kind:"method",key:"actionSuccess",value:function(){this._setResult("success")}},{kind:"method",key:"actionError",value:function(){this._setResult("error")}},{kind:"method",key:"_setResult",value:function(e){this._result=e,setTimeout((()=>{this._result=void 0}),2e3)}},{kind:"method",key:"_buttonTapped",value:function(e){this.progress&&e.stopPropagation()}},{kind:"get",static:!0,key:"styles",value:function(){return i.AH`:host{outline:0;display:inline-block;position:relative}mwc-button{transition:all 1s}mwc-button.success{--mdc-theme-primary:white;background-color:var(--success-color);transition:none;border-radius:4px;pointer-events:none}mwc-button[raised].success{--mdc-theme-primary:var(--success-color);--mdc-theme-on-primary:white}mwc-button.error{--mdc-theme-primary:white;background-color:var(--error-color);transition:none;border-radius:4px;pointer-events:none}mwc-button[raised].error{--mdc-theme-primary:var(--error-color);--mdc-theme-on-primary:white}.progress{bottom:4px;position:absolute;text-align:center;top:4px;width:100%}ha-svg-icon{color:#fff}mwc-button.error slot,mwc-button.success slot{visibility:hidden}`}}]}}),i.WF)},4596:(e,r,t)=>{t.r(r),t.d(r,{HaCircularProgress:()=>l});var o=t(62659),i=t(76504),a=t(80792),s=(t(21950),t(8339),t(57305)),n=t(40924),c=t(18791);let l=(0,o.A)([(0,c.EM)("ha-circular-progress")],(function(e,r){class t extends r{constructor(...r){super(...r),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,c.MZ)({attribute:"aria-label",type:String})],key:"ariaLabel",value:()=>"Loading"},{kind:"field",decorators:[(0,c.MZ)()],key:"size",value:()=>"medium"},{kind:"method",key:"updated",value:function(e){if((0,i.A)((0,a.A)(t.prototype),"updated",this).call(this,e),e.has("size"))switch(this.size){case"tiny":this.style.setProperty("--md-circular-progress-size","16px");break;case"small":this.style.setProperty("--md-circular-progress-size","28px");break;case"medium":this.style.setProperty("--md-circular-progress-size","48px");break;case"large":this.style.setProperty("--md-circular-progress-size","68px")}}},{kind:"field",static:!0,key:"styles",value(){return[...(0,i.A)((0,a.A)(t),"styles",this),n.AH`:host{--md-sys-color-primary:var(--primary-color);--md-circular-progress-size:48px}`]}}]}}),s.U)},17876:(e,r,t)=>{t.d(r,{L:()=>i,z:()=>a});var o=t(1751);const i=["input_boolean","input_button","input_text","input_number","input_datetime","input_select","counter","timer","schedule"],a=(0,o.g)(i)},12797:(e,r,t)=>{t.r(r);var o=t(62659),i=(t(53501),t(21950),t(55888),t(26777),t(8339),t(40924)),a=t(18791),s=t(45081),n=t(77664),c=t(12249),l=(t(61003),t(23006),t(12731),t(45177)),d=t(27096),u=t(14126),h=t(92483);const v=(0,s.A)(((e,r,t,o)=>[{name:"name",required:!0,disabled:r,selector:{text:{}}},{name:"usage",required:!0,type:"select",options:[[d.h1.BACKUP,e("ui.panel.config.storage.network_mounts.mount_usage.backup")],[d.h1.MEDIA,e("ui.panel.config.storage.network_mounts.mount_usage.media")],[d.h1.SHARE,e("ui.panel.config.storage.network_mounts.mount_usage.share")]]},{name:"server",required:!0,selector:{text:{}}},{name:"type",required:!0,type:"select",options:[[d.Wu.CIFS,e("ui.panel.config.storage.network_mounts.mount_type.cifs")],[d.Wu.NFS,e("ui.panel.config.storage.network_mounts.mount_type.nfs")]]},..."nfs"===t?[{name:"path",required:!0,selector:{text:{}}}]:"cifs"===t?[...o?[{name:"version",required:!0,selector:{select:{options:[{label:e("ui.panel.config.storage.network_mounts.cifs_versions.auto"),value:"auto"},{label:e("ui.panel.config.storage.network_mounts.cifs_versions.legacy",{version:"2.0"}),value:"2.0"},{label:e("ui.panel.config.storage.network_mounts.cifs_versions.legacy",{version:"1.0"}),value:"1.0"}],mode:"dropdown"}}}]:[],{name:"share",required:!0,selector:{text:{}}},{name:"username",required:!1,selector:{text:{}}},{name:"password",required:!1,selector:{text:{type:"password"}}}]:[]]));(0,o.A)([(0,a.EM)("dialog-mount-view")],(function(e,r){return{F:class extends r{constructor(...r){super(...r),e(this)}},d:[{kind:"field",decorators:[(0,a.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_data",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_waiting",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_validationError",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_validationWarning",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_existing",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_showCIFSVersion",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_reloadMounts",value:void 0},{kind:"method",key:"showDialog",value:async function(e){var r;this._data=e.mount,this._existing=void 0!==e.mount,this._reloadMounts=e.reloadMounts,"cifs"===(null===(r=e.mount)||void 0===r?void 0:r.type)&&e.mount.version&&"auto"!==e.mount.version&&(this._showCIFSVersion=!0)}},{kind:"method",key:"closeDialog",value:function(){this._data=void 0,this._waiting=void 0,this._error=void 0,this._validationError=void 0,this._validationWarning=void 0,this._existing=void 0,this._showCIFSVersion=void 0,this._reloadMounts=void 0,(0,n.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){var e;return void 0===this._existing?i.s6:i.qy` <ha-dialog open scrimClickAction escapeKeyAction .heading="${this._existing?this.hass.localize("ui.panel.config.storage.network_mounts.update_title"):this.hass.localize("ui.panel.config.storage.network_mounts.add_title")}" @closed="${this.closeDialog}"> <ha-dialog-header slot="heading"> <span slot="title">${this._existing?this.hass.localize("ui.panel.config.storage.network_mounts.update_title"):this.hass.localize("ui.panel.config.storage.network_mounts.add_title")} </span> <a slot="actionItems" class="header_button" href="${(0,h.o)(this.hass,"/common-tasks/os#network-storage")}" title="${this.hass.localize("ui.panel.config.storage.network_mounts.documentation")}" target="_blank" rel="noreferrer" dir="${(0,c.Vc)(this.hass)}"> <ha-icon-button .path="${"M15.07,11.25L14.17,12.17C13.45,12.89 13,13.5 13,15H11V14.5C11,13.39 11.45,12.39 12.17,11.67L13.41,10.41C13.78,10.05 14,9.55 14,9C14,7.89 13.1,7 12,7A2,2 0 0,0 10,9H8A4,4 0 0,1 12,5A4,4 0 0,1 16,9C16,9.88 15.64,10.67 15.07,11.25M13,19H11V17H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12C22,6.47 17.5,2 12,2Z"}"></ha-icon-button> </a> </ha-dialog-header> ${this._error?i.qy`<ha-alert alert-type="error">${this._error}</ha-alert>`:i.s6} <ha-form .data="${this._data}" .schema="${v(this.hass.localize,this._existing,null===(e=this._data)||void 0===e?void 0:e.type,this._showCIFSVersion)}" .error="${this._validationError}" .warning="${this._validationWarning}" .computeLabel="${this._computeLabelCallback}" .computeHelper="${this._computeHelperCallback}" .computeError="${this._computeErrorCallback}" .computeWarning="${this._computeWarningCallback}" @value-changed="${this._valueChanged}" dialogInitialFocus></ha-form> <div slot="secondaryAction"> <mwc-button @click="${this.closeDialog}" dialogInitialFocus> ${this.hass.localize("ui.common.cancel")} </mwc-button> ${this._existing?i.qy`<mwc-button @click="${this._deleteMount}" class="delete-btn"> ${this.hass.localize("ui.common.delete")} </mwc-button>`:i.s6} </div> <ha-progress-button .progress="${this._waiting}" slot="primaryAction" @click="${this._connectMount}"> ${this._existing?this.hass.localize("ui.panel.config.storage.network_mounts.update"):this.hass.localize("ui.panel.config.storage.network_mounts.connect")} </ha-progress-button> </ha-dialog> `}},{kind:"field",key:"_computeLabelCallback",value(){return e=>this.hass.localize(`ui.panel.config.storage.network_mounts.options.${e.name}.title`)}},{kind:"field",key:"_computeHelperCallback",value(){return e=>this.hass.localize(`ui.panel.config.storage.network_mounts.options.${e.name}.description`)}},{kind:"field",key:"_computeErrorCallback",value(){return e=>this.hass.localize(`ui.panel.config.storage.network_mounts.errors.${e}`)||e}},{kind:"field",key:"_computeWarningCallback",value(){return e=>this.hass.localize(`ui.panel.config.storage.network_mounts.warnings.${e}`)||e}},{kind:"method",key:"_valueChanged",value:function(e){var r,t,o;this._validationError={},this._validationWarning={},this._data=e.detail.value,null!==(r=this._data)&&void 0!==r&&r.name&&!/^\w+$/.test(this._data.name)&&(this._validationError.name="invalid_name"),"cifs"!==(null===(t=this._data)||void 0===t?void 0:t.type)||this._data.version||(this._data.version="auto"),"cifs"===(null===(o=this._data)||void 0===o?void 0:o.type)&&this._data.version&&["1.0","2.0"].includes(this._data.version)&&(this._validationWarning.version="not_recomeded_cifs_version")}},{kind:"method",key:"_connectMount",value:async function(e){const r=e.target;this._error=void 0,this._waiting=!0;const t={...this._data};"cifs"===t.type&&"auto"===t.version&&(t.version=void 0);try{this._existing?await(0,d.Bt)(this.hass,t):await(0,d.Qf)(this.hass,t)}catch(e){return this._error=(0,l.VR)(e),this._waiting=!1,r.actionError(),void("cifs"!==this._data.type||this._showCIFSVersion||(this._showCIFSVersion=!0))}this._reloadMounts&&this._reloadMounts(),this.closeDialog()}},{kind:"method",key:"_deleteMount",value:async function(){this._error=void 0,this._waiting=!0;try{await(0,d.wZ)(this.hass,this._data.name)}catch(e){return this._error=(0,l.VR)(e),void(this._waiting=!1)}this._reloadMounts&&this._reloadMounts(),this.closeDialog()}},{kind:"get",static:!0,key:"styles",value:function(){return[u.RF,u.nA,i.AH`ha-icon-button{color:var(--primary-text-color)}.delete-btn{--mdc-theme-primary:var(--error-color)}`]}}]}}),i.WF)},79372:(e,r,t)=>{var o=t(73155),i=t(33817),a=t(3429),s=t(75077);e.exports=function(e,r){r&&"string"==typeof e||i(e);var t=s(e);return a(i(void 0!==t?o(t,e):e))}},18684:(e,r,t)=>{var o=t(87568),i=t(42509),a=t(30356),s=t(51607),n=t(95124),c=t(79635);o({target:"Array",proto:!0},{flatMap:function(e){var r,t=s(this),o=n(t);return a(e),(r=c(t,0)).length=i(r,t,t,o,0,1,e,arguments.length>1?arguments[1]:void 0),r}})},74991:(e,r,t)=>{t(33523)("flatMap")},69704:(e,r,t)=>{var o=t(87568),i=t(73155),a=t(30356),s=t(33817),n=t(3429),c=t(79372),l=t(23408),d=t(44933),u=t(89385),h=l((function(){for(var e,r,t=this.iterator,o=this.mapper;;){if(r=this.inner)try{if(!(e=s(i(r.next,r.iterator))).done)return e.value;this.inner=null}catch(e){d(t,"throw",e)}if(e=s(i(this.next,t)),this.done=!!e.done)return;try{this.inner=c(o(e.value,this.counter++),!1)}catch(e){d(t,"throw",e)}}}));o({target:"Iterator",proto:!0,real:!0,forced:u},{flatMap:function(e){return s(this),a(e),new h(n(this),{mapper:e,inner:null})}})},67371:(e,r,t)=>{t.d(r,{F:()=>a});t(21950),t(8339),t(26777),t(73842);const o=["role","ariaAtomic","ariaAutoComplete","ariaBusy","ariaChecked","ariaColCount","ariaColIndex","ariaColSpan","ariaCurrent","ariaDisabled","ariaExpanded","ariaHasPopup","ariaHidden","ariaInvalid","ariaKeyShortcuts","ariaLabel","ariaLevel","ariaLive","ariaModal","ariaMultiLine","ariaMultiSelectable","ariaOrientation","ariaPlaceholder","ariaPosInSet","ariaPressed","ariaReadOnly","ariaRequired","ariaRoleDescription","ariaRowCount","ariaRowIndex","ariaRowSpan","ariaSelected","ariaSetSize","ariaSort","ariaValueMax","ariaValueMin","ariaValueNow","ariaValueText"];o.map(i);function i(e){return e.replace("aria","aria-").replace(/Elements?/g,"").toLowerCase()}function a(e){for(const r of o)e.createProperty(r,{attribute:i(r),reflect:!0});e.addInitializer((e=>{const r={hostConnected(){e.setAttribute("role","presentation")}};e.addController(r)}))}},57305:(e,r,t)=>{t.d(r,{U:()=>u});var o=t(76513),i=t(18791),a=t(40924),s=(t(21950),t(8339),t(69760)),n=t(67371);class c extends a.WF{constructor(){super(...arguments),this.value=0,this.max=1,this.indeterminate=!1,this.fourColor=!1}render(){const{ariaLabel:e}=this;return a.qy` <div class="progress ${(0,s.H)(this.getRenderClasses())}" role="progressbar" aria-label="${e||a.s6}" aria-valuemin="0" aria-valuemax="${this.max}" aria-valuenow="${this.indeterminate?a.s6:this.value}">${this.renderIndicator()}</div> `}getRenderClasses(){return{indeterminate:this.indeterminate,"four-color":this.fourColor}}}(0,n.F)(c),(0,o.__decorate)([(0,i.MZ)({type:Number})],c.prototype,"value",void 0),(0,o.__decorate)([(0,i.MZ)({type:Number})],c.prototype,"max",void 0),(0,o.__decorate)([(0,i.MZ)({type:Boolean})],c.prototype,"indeterminate",void 0),(0,o.__decorate)([(0,i.MZ)({type:Boolean,attribute:"four-color"})],c.prototype,"fourColor",void 0);class l extends c{renderIndicator(){return this.indeterminate?this.renderIndeterminateContainer():this.renderDeterminateContainer()}renderDeterminateContainer(){const e=100*(1-this.value/this.max);return a.qy` <svg viewBox="0 0 4800 4800"> <circle class="track" pathLength="100"></circle> <circle class="active-track" pathLength="100" stroke-dashoffset="${e}"></circle> </svg> `}renderIndeterminateContainer(){return a.qy` <div class="spinner"> <div class="left"> <div class="circle"></div> </div> <div class="right"> <div class="circle"></div> </div> </div>`}}const d=a.AH`:host{--_active-indicator-color:var(--md-circular-progress-active-indicator-color, var(--md-sys-color-primary, #6750a4));--_active-indicator-width:var(--md-circular-progress-active-indicator-width, 10);--_four-color-active-indicator-four-color:var(--md-circular-progress-four-color-active-indicator-four-color, var(--md-sys-color-tertiary-container, #ffd8e4));--_four-color-active-indicator-one-color:var(--md-circular-progress-four-color-active-indicator-one-color, var(--md-sys-color-primary, #6750a4));--_four-color-active-indicator-three-color:var(--md-circular-progress-four-color-active-indicator-three-color, var(--md-sys-color-tertiary, #7d5260));--_four-color-active-indicator-two-color:var(--md-circular-progress-four-color-active-indicator-two-color, var(--md-sys-color-primary-container, #eaddff));--_size:var(--md-circular-progress-size, 48px);display:inline-flex;vertical-align:middle;width:var(--_size);height:var(--_size);position:relative;align-items:center;justify-content:center;contain:strict;content-visibility:auto}.progress{flex:1;align-self:stretch;margin:4px}.active-track,.circle,.left,.progress,.right,.spinner,.track,svg{position:absolute;inset:0}svg{transform:rotate(-90deg)}circle{cx:50%;cy:50%;r:calc(50%*(1 - var(--_active-indicator-width)/ 100));stroke-width:calc(var(--_active-indicator-width)*1%);stroke-dasharray:100;fill:rgba(0,0,0,0)}.active-track{transition:stroke-dashoffset .5s cubic-bezier(0, 0, .2, 1);stroke:var(--_active-indicator-color)}.track{stroke:rgba(0,0,0,0)}.progress.indeterminate{animation:linear infinite linear-rotate;animation-duration:1.568s}.spinner{animation:infinite both rotate-arc;animation-duration:5332ms;animation-timing-function:cubic-bezier(0.4,0,0.2,1)}.left{overflow:hidden;inset:0 50% 0 0}.right{overflow:hidden;inset:0 0 0 50%}.circle{box-sizing:border-box;border-radius:50%;border:solid calc(var(--_active-indicator-width)/ 100*(var(--_size) - 8px));border-color:var(--_active-indicator-color) var(--_active-indicator-color) transparent transparent;animation:expand-arc;animation-iteration-count:infinite;animation-fill-mode:both;animation-duration:1333ms,5332ms;animation-timing-function:cubic-bezier(0.4,0,0.2,1)}.four-color .circle{animation-name:expand-arc,four-color}.left .circle{rotate:135deg;inset:0 -100% 0 0}.right .circle{rotate:100deg;inset:0 0 0 -100%;animation-delay:-.666s,0s}@media(forced-colors:active){.active-track{stroke:CanvasText}.circle{border-color:CanvasText CanvasText Canvas Canvas}}@keyframes expand-arc{0%{transform:rotate(265deg)}50%{transform:rotate(130deg)}100%{transform:rotate(265deg)}}@keyframes rotate-arc{12.5%{transform:rotate(135deg)}25%{transform:rotate(270deg)}37.5%{transform:rotate(405deg)}50%{transform:rotate(540deg)}62.5%{transform:rotate(675deg)}75%{transform:rotate(810deg)}87.5%{transform:rotate(945deg)}100%{transform:rotate(1080deg)}}@keyframes linear-rotate{to{transform:rotate(360deg)}}@keyframes four-color{0%{border-top-color:var(--_four-color-active-indicator-one-color);border-right-color:var(--_four-color-active-indicator-one-color)}15%{border-top-color:var(--_four-color-active-indicator-one-color);border-right-color:var(--_four-color-active-indicator-one-color)}25%{border-top-color:var(--_four-color-active-indicator-two-color);border-right-color:var(--_four-color-active-indicator-two-color)}40%{border-top-color:var(--_four-color-active-indicator-two-color);border-right-color:var(--_four-color-active-indicator-two-color)}50%{border-top-color:var(--_four-color-active-indicator-three-color);border-right-color:var(--_four-color-active-indicator-three-color)}65%{border-top-color:var(--_four-color-active-indicator-three-color);border-right-color:var(--_four-color-active-indicator-three-color)}75%{border-top-color:var(--_four-color-active-indicator-four-color);border-right-color:var(--_four-color-active-indicator-four-color)}90%{border-top-color:var(--_four-color-active-indicator-four-color);border-right-color:var(--_four-color-active-indicator-four-color)}100%{border-top-color:var(--_four-color-active-indicator-one-color);border-right-color:var(--_four-color-active-indicator-one-color)}}`;let u=class extends l{};u.styles=[d],u=(0,o.__decorate)([(0,i.EM)("md-circular-progress")],u)},3358:(e,r,t)=>{t.d(r,{OA:()=>o.OA,WL:()=>o.WL,u$:()=>o.u$});var o=t(2154)}};
//# sourceMappingURL=74304.WJbfitVtqHU.js.map