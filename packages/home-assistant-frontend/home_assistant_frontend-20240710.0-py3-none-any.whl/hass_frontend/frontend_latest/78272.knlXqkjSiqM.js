/*! For license information please see 78272.knlXqkjSiqM.js.LICENSE.txt */
export const id=78272;export const ids=[78272,4596];export const modules={48962:(e,t,i)=>{i.d(t,{d:()=>r});const r=e=>e.stopPropagation()},4596:(e,t,i)=>{i.r(t),i.d(t,{HaCircularProgress:()=>l});var r=i(62659),o=i(76504),a=i(80792),s=(i(21950),i(8339),i(57305)),c=i(40924),n=i(18791);let l=(0,r.A)([(0,n.EM)("ha-circular-progress")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,n.MZ)({attribute:"aria-label",type:String})],key:"ariaLabel",value:()=>"Loading"},{kind:"field",decorators:[(0,n.MZ)()],key:"size",value:()=>"medium"},{kind:"method",key:"updated",value:function(e){if((0,o.A)((0,a.A)(i.prototype),"updated",this).call(this,e),e.has("size"))switch(this.size){case"tiny":this.style.setProperty("--md-circular-progress-size","16px");break;case"small":this.style.setProperty("--md-circular-progress-size","28px");break;case"medium":this.style.setProperty("--md-circular-progress-size","48px");break;case"large":this.style.setProperty("--md-circular-progress-size","68px")}}},{kind:"field",static:!0,key:"styles",value(){return[...(0,o.A)((0,a.A)(i),"styles",this),c.AH`:host{--md-sys-color-primary:var(--primary-color);--md-circular-progress-size:48px}`]}}]}}),s.U)},59799:(e,t,i)=>{var r=i(62659),o=i(76504),a=i(80792),s=(i(21950),i(55888),i(8339),i(32503)),c=i(50988),n=i(40924),l=i(18791),d=i(47394),h=i(34800);i(12731);(0,r.A)([(0,l.EM)("ha-select")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"icon",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean,reflect:!0})],key:"clearable",value:()=>!1},{kind:"method",key:"render",value:function(){return n.qy` ${(0,o.A)((0,a.A)(i.prototype),"render",this).call(this)} ${this.clearable&&!this.required&&!this.disabled&&this.value?n.qy`<ha-icon-button label="clear" @click="${this._clearValue}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}"></ha-icon-button>`:n.s6} `}},{kind:"method",key:"renderLeadingIcon",value:function(){return this.icon?n.qy`<span class="mdc-select__icon"><slot name="icon"></slot></span>`:n.s6}},{kind:"method",key:"connectedCallback",value:function(){(0,o.A)((0,a.A)(i.prototype),"connectedCallback",this).call(this),window.addEventListener("translations-updated",this._translationsUpdated)}},{kind:"method",key:"disconnectedCallback",value:function(){(0,o.A)((0,a.A)(i.prototype),"disconnectedCallback",this).call(this),window.removeEventListener("translations-updated",this._translationsUpdated)}},{kind:"method",key:"_clearValue",value:function(){!this.disabled&&this.value&&(this.valueSetDirectly=!0,this.select(-1),this.mdcFoundation.handleChange())}},{kind:"field",key:"_translationsUpdated",value(){return(0,d.s)((async()=>{await(0,h.E)(),this.layoutOptions()}),500)}},{kind:"field",static:!0,key:"styles",value:()=>[c.R,n.AH`:host([clearable]){position:relative}.mdc-select:not(.mdc-select--disabled) .mdc-select__icon{color:var(--secondary-text-color)}.mdc-select__anchor{width:var(--ha-select-min-width,200px)}.mdc-select--filled .mdc-select__anchor{height:var(--ha-select-height,56px)}.mdc-select--filled .mdc-floating-label{inset-inline-start:12px;inset-inline-end:initial;direction:var(--direction)}.mdc-select--filled.mdc-select--with-leading-icon .mdc-floating-label{inset-inline-start:48px;inset-inline-end:initial;direction:var(--direction)}.mdc-select .mdc-select__anchor{padding-inline-start:12px;padding-inline-end:0px;direction:var(--direction)}.mdc-select__anchor .mdc-floating-label--float-above{transform-origin:var(--float-start)}.mdc-select__selected-text-container{padding-inline-end:var(--select-selected-text-padding-end,0px)}:host([clearable]) .mdc-select__selected-text-container{padding-inline-end:var(--select-selected-text-padding-end,12px)}ha-icon-button{position:absolute;top:10px;right:28px;--mdc-icon-button-size:36px;--mdc-icon-size:20px;color:var(--secondary-text-color);inset-inline-start:initial;inset-inline-end:28px;direction:var(--direction)}`]}]}}),s.o)},27687:(e,t,i)=>{i.r(t);var r=i(62659),o=(i(21950),i(55888),i(98168),i(8339),i(23981),i(40924)),a=i(18791),s=i(45081),c=i(77664),n=i(48962),l=(i(4596),i(59799),i(45177)),d=i(4377),h=i(98876),u=i(14126),v=i(10826);const p=(0,s.A)((e=>{const t=""!==e.disk_life_time?30:10,i=1e3*e.disk_used/60/t,r=4*e.startup_time/60;return 10*Math.ceil((i+r)/10)}));(0,r.A)([(0,a.EM)("dialog-move-datadisk")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,a.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_hostInfo",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_selectedDevice",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_disks",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_osInfo",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_moving",value:()=>!1},{kind:"method",key:"showDialog",value:async function(e){this._hostInfo=e.hostInfo;try{this._osInfo=await(0,d.PB)(this.hass);const e=await(0,d.xY)(this.hass);e.devices.length>0?this._disks=e.disks:(this.closeDialog(),await(0,h.showAlertDialog)(this,{title:this.hass.localize("ui.panel.config.storage.datadisk.no_devices_title"),text:this.hass.localize("ui.panel.config.storage.datadisk.no_devices_text")}))}catch(e){this.closeDialog(),await(0,h.showAlertDialog)(this,{title:this.hass.localize("ui.panel.config.hardware.available_hardware.failed_to_get"),text:(0,l.VR)(e)})}}},{kind:"method",key:"closeDialog",value:function(){this._selectedDevice=void 0,this._disks=void 0,this._moving=!1,this._hostInfo=void 0,this._osInfo=void 0,(0,c.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){return this._hostInfo&&this._osInfo&&this._disks?o.qy` <ha-dialog open scrimClickAction escapeKeyAction .heading="${this._moving?this.hass.localize("ui.panel.config.storage.datadisk.moving"):this.hass.localize("ui.panel.config.storage.datadisk.title")}" @closed="${this.closeDialog}" ?hideActions="${this._moving}"> ${this._moving?o.qy` <ha-circular-progress aria-label="Moving" size="large" indeterminate> </ha-circular-progress> <p class="progress-text"> ${this.hass.localize("ui.panel.config.storage.datadisk.moving_desc")} </p> `:o.qy` ${this.hass.localize("ui.panel.config.storage.datadisk.description",{current_path:this._osInfo.data_disk,time:p(this._hostInfo)})} <br><br> <ha-select .label="${this.hass.localize("ui.panel.config.storage.datadisk.select_device")}" @selected="${this._select_device}" @closed="${n.d}" dialogInitialFocus fixedMenuPosition> ${this._disks.map((e=>o.qy`<mwc-list-item twoline .value="${e.id}"> <span>${e.vendor} ${e.model}</span> <span slot="secondary"> ${this.hass.localize("ui.panel.config.storage.datadisk.extra_information",{size:(0,v.A)(e.size),serial:e.serial})} </span> </mwc-list-item>`))} </ha-select> <mwc-button slot="secondaryAction" @click="${this.closeDialog}" dialogInitialFocus> ${this.hass.localize("ui.panel.config.storage.datadisk.cancel")} </mwc-button> <mwc-button .disabled="${!this._selectedDevice}" slot="primaryAction" @click="${this._moveDatadisk}"> ${this.hass.localize("ui.panel.config.storage.datadisk.move")} </mwc-button> `} </ha-dialog> `:o.s6}},{kind:"method",key:"_select_device",value:function(e){this._selectedDevice=e.target.value}},{kind:"method",key:"_moveDatadisk",value:async function(){this._moving=!0;try{await(0,d.v9)(this.hass,this._selectedDevice)}catch(e){this.hass.connection.connected&&!(0,l.Tv)(e)&&(0,h.showAlertDialog)(this,{title:this.hass.localize("ui.panel.config.storage.datadisk.failed_to_move"),text:(0,l.VR)(e)})}finally{this.closeDialog()}}},{kind:"get",static:!0,key:"styles",value:function(){return[u.RF,u.nA,o.AH`ha-select{width:100%}ha-circular-progress{display:block;margin:32px;text-align:center}.progress-text{text-align:center}`]}}]}}),o.WF)},10826:(e,t,i)=>{i.d(t,{A:()=>r});const r=(e=0,t=2)=>{if(0===e)return"0 Bytes";t=t<0?0:t;const i=Math.floor(Math.log(e)/Math.log(1024));return`${parseFloat((e/1024**i).toFixed(t))} ${["Bytes","KB","MB","GB","TB","PB","EB","ZB","YB"][i]}`}},67371:(e,t,i)=>{i.d(t,{F:()=>a});i(21950),i(8339),i(26777),i(73842);const r=["role","ariaAtomic","ariaAutoComplete","ariaBusy","ariaChecked","ariaColCount","ariaColIndex","ariaColSpan","ariaCurrent","ariaDisabled","ariaExpanded","ariaHasPopup","ariaHidden","ariaInvalid","ariaKeyShortcuts","ariaLabel","ariaLevel","ariaLive","ariaModal","ariaMultiLine","ariaMultiSelectable","ariaOrientation","ariaPlaceholder","ariaPosInSet","ariaPressed","ariaReadOnly","ariaRequired","ariaRoleDescription","ariaRowCount","ariaRowIndex","ariaRowSpan","ariaSelected","ariaSetSize","ariaSort","ariaValueMax","ariaValueMin","ariaValueNow","ariaValueText"];r.map(o);function o(e){return e.replace("aria","aria-").replace(/Elements?/g,"").toLowerCase()}function a(e){for(const t of r)e.createProperty(t,{attribute:o(t),reflect:!0});e.addInitializer((e=>{const t={hostConnected(){e.setAttribute("role","presentation")}};e.addController(t)}))}},57305:(e,t,i)=>{i.d(t,{U:()=>h});var r=i(76513),o=i(18791),a=i(40924),s=(i(21950),i(8339),i(69760)),c=i(67371);class n extends a.WF{constructor(){super(...arguments),this.value=0,this.max=1,this.indeterminate=!1,this.fourColor=!1}render(){const{ariaLabel:e}=this;return a.qy` <div class="progress ${(0,s.H)(this.getRenderClasses())}" role="progressbar" aria-label="${e||a.s6}" aria-valuemin="0" aria-valuemax="${this.max}" aria-valuenow="${this.indeterminate?a.s6:this.value}">${this.renderIndicator()}</div> `}getRenderClasses(){return{indeterminate:this.indeterminate,"four-color":this.fourColor}}}(0,c.F)(n),(0,r.__decorate)([(0,o.MZ)({type:Number})],n.prototype,"value",void 0),(0,r.__decorate)([(0,o.MZ)({type:Number})],n.prototype,"max",void 0),(0,r.__decorate)([(0,o.MZ)({type:Boolean})],n.prototype,"indeterminate",void 0),(0,r.__decorate)([(0,o.MZ)({type:Boolean,attribute:"four-color"})],n.prototype,"fourColor",void 0);class l extends n{renderIndicator(){return this.indeterminate?this.renderIndeterminateContainer():this.renderDeterminateContainer()}renderDeterminateContainer(){const e=100*(1-this.value/this.max);return a.qy` <svg viewBox="0 0 4800 4800"> <circle class="track" pathLength="100"></circle> <circle class="active-track" pathLength="100" stroke-dashoffset="${e}"></circle> </svg> `}renderIndeterminateContainer(){return a.qy` <div class="spinner"> <div class="left"> <div class="circle"></div> </div> <div class="right"> <div class="circle"></div> </div> </div>`}}const d=a.AH`:host{--_active-indicator-color:var(--md-circular-progress-active-indicator-color, var(--md-sys-color-primary, #6750a4));--_active-indicator-width:var(--md-circular-progress-active-indicator-width, 10);--_four-color-active-indicator-four-color:var(--md-circular-progress-four-color-active-indicator-four-color, var(--md-sys-color-tertiary-container, #ffd8e4));--_four-color-active-indicator-one-color:var(--md-circular-progress-four-color-active-indicator-one-color, var(--md-sys-color-primary, #6750a4));--_four-color-active-indicator-three-color:var(--md-circular-progress-four-color-active-indicator-three-color, var(--md-sys-color-tertiary, #7d5260));--_four-color-active-indicator-two-color:var(--md-circular-progress-four-color-active-indicator-two-color, var(--md-sys-color-primary-container, #eaddff));--_size:var(--md-circular-progress-size, 48px);display:inline-flex;vertical-align:middle;width:var(--_size);height:var(--_size);position:relative;align-items:center;justify-content:center;contain:strict;content-visibility:auto}.progress{flex:1;align-self:stretch;margin:4px}.active-track,.circle,.left,.progress,.right,.spinner,.track,svg{position:absolute;inset:0}svg{transform:rotate(-90deg)}circle{cx:50%;cy:50%;r:calc(50%*(1 - var(--_active-indicator-width)/ 100));stroke-width:calc(var(--_active-indicator-width)*1%);stroke-dasharray:100;fill:rgba(0,0,0,0)}.active-track{transition:stroke-dashoffset .5s cubic-bezier(0, 0, .2, 1);stroke:var(--_active-indicator-color)}.track{stroke:rgba(0,0,0,0)}.progress.indeterminate{animation:linear infinite linear-rotate;animation-duration:1.568s}.spinner{animation:infinite both rotate-arc;animation-duration:5332ms;animation-timing-function:cubic-bezier(0.4,0,0.2,1)}.left{overflow:hidden;inset:0 50% 0 0}.right{overflow:hidden;inset:0 0 0 50%}.circle{box-sizing:border-box;border-radius:50%;border:solid calc(var(--_active-indicator-width)/ 100*(var(--_size) - 8px));border-color:var(--_active-indicator-color) var(--_active-indicator-color) transparent transparent;animation:expand-arc;animation-iteration-count:infinite;animation-fill-mode:both;animation-duration:1333ms,5332ms;animation-timing-function:cubic-bezier(0.4,0,0.2,1)}.four-color .circle{animation-name:expand-arc,four-color}.left .circle{rotate:135deg;inset:0 -100% 0 0}.right .circle{rotate:100deg;inset:0 0 0 -100%;animation-delay:-.666s,0s}@media(forced-colors:active){.active-track{stroke:CanvasText}.circle{border-color:CanvasText CanvasText Canvas Canvas}}@keyframes expand-arc{0%{transform:rotate(265deg)}50%{transform:rotate(130deg)}100%{transform:rotate(265deg)}}@keyframes rotate-arc{12.5%{transform:rotate(135deg)}25%{transform:rotate(270deg)}37.5%{transform:rotate(405deg)}50%{transform:rotate(540deg)}62.5%{transform:rotate(675deg)}75%{transform:rotate(810deg)}87.5%{transform:rotate(945deg)}100%{transform:rotate(1080deg)}}@keyframes linear-rotate{to{transform:rotate(360deg)}}@keyframes four-color{0%{border-top-color:var(--_four-color-active-indicator-one-color);border-right-color:var(--_four-color-active-indicator-one-color)}15%{border-top-color:var(--_four-color-active-indicator-one-color);border-right-color:var(--_four-color-active-indicator-one-color)}25%{border-top-color:var(--_four-color-active-indicator-two-color);border-right-color:var(--_four-color-active-indicator-two-color)}40%{border-top-color:var(--_four-color-active-indicator-two-color);border-right-color:var(--_four-color-active-indicator-two-color)}50%{border-top-color:var(--_four-color-active-indicator-three-color);border-right-color:var(--_four-color-active-indicator-three-color)}65%{border-top-color:var(--_four-color-active-indicator-three-color);border-right-color:var(--_four-color-active-indicator-three-color)}75%{border-top-color:var(--_four-color-active-indicator-four-color);border-right-color:var(--_four-color-active-indicator-four-color)}90%{border-top-color:var(--_four-color-active-indicator-four-color);border-right-color:var(--_four-color-active-indicator-four-color)}100%{border-top-color:var(--_four-color-active-indicator-one-color);border-right-color:var(--_four-color-active-indicator-one-color)}}`;let h=class extends l{};h.styles=[d],h=(0,r.__decorate)([(0,o.EM)("md-circular-progress")],h)},3358:(e,t,i)=>{i.d(t,{OA:()=>r.OA,WL:()=>r.WL,u$:()=>r.u$});var r=i(2154)}};
//# sourceMappingURL=78272.knlXqkjSiqM.js.map