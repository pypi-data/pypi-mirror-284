export const id=64446;export const ids=[64446,23141,2526];export const modules={36471:(e,t,i)=>{i.d(t,{_:()=>s});i(27934),i(21950),i(66274),i(84531),i(8339);var a=i(40924),o=i(3358);const s=(0,o.u$)(class extends o.WL{constructor(e){if(super(e),this._element=void 0,e.type!==o.OA.CHILD)throw new Error("dynamicElementDirective can only be used in content bindings")}update(e,[t,i]){return this._element&&this._element.localName===t?(i&&Object.entries(i).forEach((([e,t])=>{this._element[e]=t})),a.c0):this.render(t,i)}render(e,t){return this._element=document.createElement(e),t&&Object.entries(t).forEach((([e,t])=>{this._element[e]=t})),this._element}})},4596:(e,t,i)=>{i.r(t),i.d(t,{HaCircularProgress:()=>d});var a=i(62659),o=i(76504),s=i(80792),n=(i(21950),i(8339),i(57305)),r=i(40924),l=i(18791);let d=(0,a.A)([(0,l.EM)("ha-circular-progress")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,l.MZ)({attribute:"aria-label",type:String})],key:"ariaLabel",value:()=>"Loading"},{kind:"field",decorators:[(0,l.MZ)()],key:"size",value:()=>"medium"},{kind:"method",key:"updated",value:function(e){if((0,o.A)((0,s.A)(i.prototype),"updated",this).call(this,e),e.has("size"))switch(this.size){case"tiny":this.style.setProperty("--md-circular-progress-size","16px");break;case"small":this.style.setProperty("--md-circular-progress-size","28px");break;case"medium":this.style.setProperty("--md-circular-progress-size","48px");break;case"large":this.style.setProperty("--md-circular-progress-size","68px")}}},{kind:"field",static:!0,key:"styles",value(){return[...(0,o.A)((0,s.A)(i),"styles",this),r.AH`:host{--md-sys-color-primary:var(--primary-color);--md-circular-progress-size:48px}`]}}]}}),n.U)},25285:(e,t,i)=>{var a=i(62659),o=(i(21950),i(8339),i(40924)),s=i(18791);(0,a.A)([(0,s.EM)("ha-dialog-header")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"method",key:"render",value:function(){return o.qy` <header class="header"> <div class="header-bar"> <section class="header-navigation-icon"> <slot name="navigationIcon"></slot> </section> <section class="header-title"> <slot name="title"></slot> </section> <section class="header-action-items"> <slot name="actionItems"></slot> </section> </div> <slot></slot> </header> `}},{kind:"get",static:!0,key:"styles",value:function(){return[o.AH`:host{display:block}:host([show-border]){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.header-bar{display:flex;flex-direction:row;align-items:flex-start;padding:4px;box-sizing:border-box}.header-title{flex:1;font-size:22px;line-height:28px;font-weight:400;padding:10px 4px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}@media all and (min-width:450px) and (min-height:500px){.header-bar{padding:12px}}.header-navigation-icon{flex:none;min-width:8px;height:100%;display:flex;flex-direction:row}.header-action-items{flex:none;min-width:8px;height:100%;display:flex;flex-direction:row}`]}}]}}),o.WF)},23141:(e,t,i)=>{i.r(t),i.d(t,{HaIconButtonArrowPrev:()=>r});var a=i(62659),o=(i(21950),i(8339),i(40924)),s=i(18791),n=i(51150);i(12731);let r=(0,a.A)([(0,s.EM)("ha-icon-button-arrow-prev")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,s.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,s.wk)()],key:"_icon",value:()=>"rtl"===n.G.document.dir?"M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z":"M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"},{kind:"method",key:"render",value:function(){var e;return o.qy` <ha-icon-button .disabled="${this.disabled}" .label="${this.label||(null===(e=this.hass)||void 0===e?void 0:e.localize("ui.common.back"))||"Back"}" .path="${this._icon}"></ha-icon-button> `}}]}}),o.WF)},12731:(e,t,i)=>{i.r(t),i.d(t,{HaIconButton:()=>r});var a=i(62659),o=(i(21950),i(8339),i(25413),i(40924)),s=i(18791),n=i(79278);i(1683);let r=(0,a.A)([(0,s.EM)("ha-icon-button")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({type:Boolean,reflect:!0})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,s.MZ)({type:String})],key:"path",value:void 0},{kind:"field",decorators:[(0,s.MZ)({type:String})],key:"label",value:void 0},{kind:"field",decorators:[(0,s.MZ)({type:String,attribute:"aria-haspopup"})],key:"ariaHasPopup",value:void 0},{kind:"field",decorators:[(0,s.MZ)({type:Boolean})],key:"hideTitle",value:()=>!1},{kind:"field",decorators:[(0,s.P)("mwc-icon-button",!0)],key:"_button",value:void 0},{kind:"method",key:"focus",value:function(){var e;null===(e=this._button)||void 0===e||e.focus()}},{kind:"field",static:!0,key:"shadowRootOptions",value:()=>({mode:"open",delegatesFocus:!0})},{kind:"method",key:"render",value:function(){return o.qy` <mwc-icon-button aria-label="${(0,n.J)(this.label)}" title="${(0,n.J)(this.hideTitle?void 0:this.label)}" aria-haspopup="${(0,n.J)(this.ariaHasPopup)}" .disabled="${this.disabled}"> ${this.path?o.qy`<ha-svg-icon .path="${this.path}"></ha-svg-icon>`:o.qy`<slot></slot>`} </mwc-icon-button> `}},{kind:"get",static:!0,key:"styles",value:function(){return o.AH`:host{display:inline-block;outline:0}:host([disabled]){pointer-events:none}mwc-icon-button{--mdc-theme-on-primary:currentColor;--mdc-theme-text-disabled-on-light:var(--disabled-text-color)}`}}]}}),o.WF)},2526:(e,t,i)=>{i.r(t),i.d(t,{HaIconNext:()=>r});var a=i(62659),o=(i(21950),i(8339),i(18791)),s=i(51150),n=i(1683);let r=(0,a.A)([(0,o.EM)("ha-icon-next")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.MZ)()],key:"path",value:()=>"rtl"===s.G.document.dir?"M15.41,16.58L10.83,12L15.41,7.41L14,6L8,12L14,18L15.41,16.58Z":"M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z"}]}}),n.HaSvgIcon)},56588:(e,t,i)=>{var a=i(62659),o=i(76504),s=i(80792),n=(i(21950),i(8339),i(55089)),r=i(40924),l=i(18791);(0,a.A)([(0,l.EM)("ha-list-item-new")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",static:!0,key:"styles",value(){return[...(0,o.A)((0,s.A)(i),"styles",this),r.AH`:host{--ha-icon-display:block;--md-sys-color-primary:var(--primary-text-color);--md-sys-color-secondary:var(--secondary-text-color);--md-sys-color-surface:var(--card-background-color);--md-sys-color-on-surface:var(--primary-text-color);--md-sys-color-on-surface-variant:var(--secondary-text-color)}`]}}]}}),n.n)},96e3:(e,t,i)=>{var a=i(62659),o=i(76504),s=i(80792),n=(i(21950),i(8339),i(98371)),r=i(40924),l=i(18791);(0,a.A)([(0,l.EM)("ha-list-new")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",static:!0,key:"styles",value(){return[...(0,o.A)((0,s.A)(i),"styles",this),r.AH`:host{--md-sys-color-surface:var(--card-background-color)}`]}}]}}),n.Y)},1683:(e,t,i)=>{i.r(t),i.d(t,{HaSvgIcon:()=>n});var a=i(62659),o=(i(21950),i(8339),i(40924)),s=i(18791);let n=(0,a.A)([(0,s.EM)("ha-svg-icon")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)()],key:"path",value:void 0},{kind:"field",decorators:[(0,s.MZ)()],key:"secondaryPath",value:void 0},{kind:"field",decorators:[(0,s.MZ)()],key:"viewBox",value:void 0},{kind:"method",key:"render",value:function(){return o.JW` <svg viewBox="${this.viewBox||"0 0 24 24"}" preserveAspectRatio="xMidYMid meet" focusable="false" role="img" aria-hidden="true"> <g> ${this.path?o.JW`<path class="primary-path" d="${this.path}"></path>`:o.s6} ${this.secondaryPath?o.JW`<path class="secondary-path" d="${this.secondaryPath}"></path>`:o.s6} </g> </svg>`}},{kind:"get",static:!0,key:"styles",value:function(){return o.AH`:host{display:var(--ha-icon-display,inline-flex);align-items:center;justify-content:center;position:relative;vertical-align:middle;fill:var(--icon-primary-color,currentcolor);width:var(--mdc-icon-size,24px);height:var(--mdc-icon-size,24px)}svg{width:100%;height:100%;pointer-events:none;display:block}path.primary-path{opacity:var(--icon-primary-opactity, 1)}path.secondary-path{fill:var(--icon-secondary-color,currentcolor);opacity:var(--icon-secondary-opactity, .5)}`}}]}}),o.WF)},4940:(e,t,i)=>{i.d(t,{JW:()=>f,OW:()=>m,PO:()=>d,VN:()=>r,XG:()=>c,eB:()=>u,gZ:()=>p,hM:()=>l,k2:()=>n,lU:()=>h,nc:()=>g,vX:()=>v,z1:()=>s});i(21950),i(66274),i(85038),i(85767),i(98168),i(15445),i(24483),i(13478),i(46355),i(14612),i(53691),i(48455),i(8339);var a=i(28825),o=i(1169);let s=function(e){return e.THREAD="thread",e.WIFI="wifi",e.ETHERNET="ethernet",e.UNKNOWN="unknown",e}({});const n=e=>{var t;return null===(t=e.auth.external)||void 0===t?void 0:t.config.canCommissionMatter},r=e=>e.auth.external.fireMessage({type:"matter/commission"}),l=(e,t)=>{let i;const s=(0,o.Ag)(e.connection,(e=>{if(!i)return void(i=new Set(Object.values(e).filter((e=>e.identifiers.find((e=>"matter"===e[0])))).map((e=>e.id))));const o=Object.values(e).filter((e=>e.identifiers.find((e=>"matter"===e[0]))&&!i.has(e.id)));o.length&&(s(),i=void 0,null==t||t(),(0,a.o)(`/config/devices/device/${o[0].id}`))}));return()=>{s(),i=void 0}},d=(e,t)=>e.callWS({type:"matter/commission",code:t}),c=(e,t)=>e.callWS({type:"matter/commission_on_network",pin:t}),h=(e,t,i)=>e.callWS({type:"matter/set_wifi_credentials",network_name:t,password:i}),p=(e,t)=>e.callWS({type:"matter/set_thread",thread_operation_dataset:t}),u=(e,t)=>e.callWS({type:"matter/node_diagnostics",device_id:t}),m=(e,t)=>e.callWS({type:"matter/ping_node",device_id:t}),g=(e,t)=>e.callWS({type:"matter/open_commissioning_window",device_id:t}),v=(e,t,i)=>e.callWS({type:"matter/remove_matter_fabric",device_id:t,fabric_index:i}),f=(e,t)=>e.callWS({type:"matter/interview_node",device_id:t})},64446:(e,t,i)=>{i.r(t);var a=i(62659),o=(i(21950),i(55888),i(26777),i(73842),i(66076),i(8339),i(40924)),s=i(18791),n=i(36471),r=i(77664),l=(i(25285),i(12731),i(23141),i(4940)),d=i(14126);i(2526),i(56588),i(96e3);const c=o.AH`.content{padding:16px var(--horizontal-padding,16px)}p{margin:0}p:not(:last-child){margin-bottom:8px}ol{padding-inline-start:20px;margin-block-start:0;margin-block-end:8px}li{margin-bottom:8px}.link{color:var(--primary-color);cursor:pointer;text-decoration:underline}ha-list-new{padding:0;--md-list-item-leading-space:var(--horizontal-padding, 16px);--md-list-item-trailing-space:var(--horizontal-padding, 16px);margin-bottom:16px}ha-textfield{width:100%}`;(0,a.A)([(0,s.EM)("matter-add-device-apple-home")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.wk)()],key:"_code",value:()=>""},{kind:"method",key:"render",value:function(){return o.qy` <div class="content"> <ol> <li> ${this.hass.localize("ui.dialogs.matter-add-device.apple_home.step_1",{accessory_settings:o.qy`<b>${this.hass.localize("ui.dialogs.matter-add-device.apple_home.accessory_settings")}</b>`})} </li> <li> ${this.hass.localize("ui.dialogs.matter-add-device.apple_home.step_2",{turn_on_pairing_mode:o.qy`<b>${this.hass.localize("ui.dialogs.matter-add-device.apple_home.turn_on_pairing_mode")}</b>`})} </li> <li> ${this.hass.localize("ui.dialogs.matter-add-device.apple_home.step_3")} </li> </ol> <br> <p> ${this.hass.localize("ui.dialogs.matter-add-device.apple_home.code_instructions")} </p> <ha-textfield label="${this.hass.localize("ui.dialogs.matter-add-device.apple_home.setup_code")}" .value="${this._code}" @input="${this._onCodeChanged}"></ha-textfield> </div> `}},{kind:"method",key:"_onCodeChanged",value:function(e){const t=e.currentTarget.value;this._code=t,(0,r.r)(this,"pairing-code-changed",{code:t})}},{kind:"field",static:!0,key:"styles",value:()=>[c]}]}}),o.WF);(0,a.A)([(0,s.EM)("matter-add-device-existing")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"method",key:"render",value:function(){return o.qy` <div class="content"> <p> ${this.hass.localize("ui.dialogs.matter-add-device.existing.question")} </p> </div> <ha-list-new> <ha-list-item-new interactive type="button" .step="${"google_home"}" @click="${this._onItemClick}" @keydown="${this._onItemClick}"> <img src="/static/images/logo_google_home.png" alt="" class="logo" slot="start"> <span slot="headline"> ${this.hass.localize("ui.dialogs.matter-add-device.existing.answer_google_home")} </span> <ha-icon-next slot="end"></ha-icon-next> </ha-list-item-new> <ha-list-item-new interactive type="button" .step="${"apple_home"}" @click="${this._onItemClick}" @keydown="${this._onItemClick}"> <img src="/static/images/logo_apple_home.png" alt="" class="logo" slot="start"> <span slot="headline"> ${this.hass.localize("ui.dialogs.matter-add-device.existing.answer_apple_home")} </span> <ha-icon-next slot="end"></ha-icon-next> </ha-list-item-new> <ha-list-item-new interactive type="button" .step="${"generic"}" @click="${this._onItemClick}" @keydown="${this._onItemClick}"> <div class="logo" slot="start"> <ha-svg-icon path="${"M12,3L2,12H5V20H19V12H22L12,3M12,8.5C14.34,8.5 16.46,9.43 18,10.94L16.8,12.12C15.58,10.91 13.88,10.17 12,10.17C10.12,10.17 8.42,10.91 7.2,12.12L6,10.94C7.54,9.43 9.66,8.5 12,8.5M12,11.83C13.4,11.83 14.67,12.39 15.6,13.3L14.4,14.47C13.79,13.87 12.94,13.5 12,13.5C11.06,13.5 10.21,13.87 9.6,14.47L8.4,13.3C9.33,12.39 10.6,11.83 12,11.83M12,15.17C12.94,15.17 13.7,15.91 13.7,16.83C13.7,17.75 12.94,18.5 12,18.5C11.06,18.5 10.3,17.75 10.3,16.83C10.3,15.91 11.06,15.17 12,15.17Z"}"></ha-svg-icon> </div> <span slot="headline"> ${this.hass.localize("ui.dialogs.matter-add-device.existing.answer_generic")} </span> <ha-icon-next slot="end"></ha-icon-next> </ha-list-item-new> </ha-list-new> `}},{kind:"method",key:"_onItemClick",value:function(e){if("keydown"===e.type&&"Enter"!==e.key&&" "!==e.key)return;const t=e.currentTarget.step;(0,r.r)(this,"step-selected",{step:t})}},{kind:"field",static:!0,key:"styles",value:()=>[c,o.AH`.logo{width:48px;height:48px;border-radius:12px;border:1px solid var(--divider-color);padding:10px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;object-fit:contain}.logo ha-svg-icon{--mdc-icon-size:36px}`]}]}}),o.WF),(0,a.A)([(0,s.EM)("matter-add-device-generic")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.wk)()],key:"_code",value:()=>""},{kind:"method",key:"render",value:function(){return o.qy` <div class="content"> <p> ${this.hass.localize("ui.dialogs.matter-add-device.generic.code_instructions")} </p> <ha-textfield label="${this.hass.localize("ui.dialogs.matter-add-device.generic.setup_code")}" .value="${this._code}" @input="${this._onCodeChanged}"></ha-textfield> </div> `}},{kind:"method",key:"_onCodeChanged",value:function(e){const t=e.currentTarget.value;this._code=t,(0,r.r)(this,"pairing-code-changed",{code:t})}},{kind:"field",static:!0,key:"styles",value:()=>[c]}]}}),o.WF),(0,a.A)([(0,s.EM)("matter-add-device-google-home")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"method",key:"render",value:function(){return o.qy` <div class="content"> <ol> <li> ${this.hass.localize("ui.dialogs.matter-add-device.google_home.step_1")} </li> <li> ${this.hass.localize("ui.dialogs.matter-add-device.google_home.step_2",{linked_matter_apps_services:o.qy`<b>${this.hass.localize("ui.dialogs.matter-add-device.google_home.linked_matter_apps_services")}</b>`})} </li> <li> ${this.hass.localize("ui.dialogs.matter-add-device.google_home.step_3",{link_apps_services:o.qy`<b>${this.hass.localize("ui.dialogs.matter-add-device.google_home.link_apps_services")}</b>`,home_assistant:o.qy`<b>Home Assistant</b>`})} <br> <span class="link" type="button" tabindex="0" @keydown="${this._nextStep}" @click="${this._nextStep}"> ${this.hass.localize("ui.dialogs.matter-add-device.google_home.no_home_assistant")} </span> </li> </ol> <br> <p> ${this.hass.localize("ui.dialogs.matter-add-device.google_home.redirect")} </p> </div> `}},{kind:"method",key:"_nextStep",value:function(){(0,r.r)(this,"step-selected",{step:"google_home_fallback"})}},{kind:"field",static:!0,key:"styles",value:()=>[c]}]}}),o.WF),(0,a.A)([(0,s.EM)("matter-add-device-google-home-fallback")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.wk)()],key:"_code",value:()=>""},{kind:"method",key:"render",value:function(){return o.qy` <div class="content"> <ol> <li> ${this.hass.localize("ui.dialogs.matter-add-device.google_home_fallback.step_1")} </li> <li> ${this.hass.localize("ui.dialogs.matter-add-device.google_home_fallback.step_2",{linked_matter_apps_services:o.qy`<b>${this.hass.localize("ui.dialogs.matter-add-device.google_home_fallback.linked_matter_apps_services")}</b>`})} </li> <li> ${this.hass.localize("ui.dialogs.matter-add-device.google_home_fallback.step_3",{link_apps_services:o.qy`<b>${this.hass.localize("ui.dialogs.matter-add-device.google_home_fallback.link_apps_services")}</b>`,use_pairing_code:o.qy`<b>${this.hass.localize("ui.dialogs.matter-add-device.google_home_fallback.use_pairing_code")}</b>`})} </li> </ol> <br> <p> ${this.hass.localize("ui.dialogs.matter-add-device.google_home_fallback.code_instructions")} </p> <ha-textfield label="${this.hass.localize("ui.dialogs.matter-add-device.google_home_fallback.pairing_code")}" .value="${this._code}" @input="${this._onCodeChanged}"></ha-textfield> </div> `}},{kind:"method",key:"_onCodeChanged",value:function(e){const t=e.currentTarget.value;this._code=t,(0,r.r)(this,"pairing-code-changed",{code:t})}},{kind:"field",static:!0,key:"styles",value:()=>[c]}]}}),o.WF),(0,a.A)([(0,s.EM)("matter-add-device-main")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"method",key:"render",value:function(){return o.qy` <div class="content"> <p class="text"> ${this.hass.localize("ui.dialogs.matter-add-device.main.question")} </p> </div> <ha-list-new> <ha-list-item-new interactive type="button" .step="${"new"}" @click="${this._onItemClick}" @keydown="${this._onItemClick}"> <span slot="headline"> ${this.hass.localize("ui.dialogs.matter-add-device.main.answer_new")} </span> <span slot="supporting-text"> ${this.hass.localize("ui.dialogs.matter-add-device.main.answer_new_description")} </span> <ha-icon-next slot="end"></ha-icon-next> </ha-list-item-new> <ha-list-item-new interactive type="button" .step="${"existing"}" @click="${this._onItemClick}" @keydown="${this._onItemClick}"> <span slot="headline"> ${this.hass.localize("ui.dialogs.matter-add-device.main.answer_existing")} </span> <span slot="supporting-text"> ${this.hass.localize("ui.dialogs.matter-add-device.main.answer_existing_description")} </span> <ha-icon-next slot="end"></ha-icon-next> </ha-list-item-new> </ha-list-new> `}},{kind:"method",key:"_onItemClick",value:function(e){if("keydown"===e.type&&"Enter"!==e.key&&" "!==e.key)return;const t=e.currentTarget.step;(0,r.r)(this,"step-selected",{step:t})}},{kind:"field",static:!0,key:"styles",value:()=>[c]}]}}),o.WF);i(4596);(0,a.A)([(0,s.EM)("matter-add-device-new")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"method",key:"firstUpdated",value:function(){(0,l.k2)(this.hass)&&(0,l.VN)(this.hass)}},{kind:"method",key:"render",value:function(){return(0,l.k2)(this.hass)?o.qy` <div class="content"> <ha-circular-progress size="medium" indeterminate></ha-circular-progress> </div> `:o.qy` <div class="content"> <p>${this.hass.localize("ui.dialogs.matter-add-device.new.note")}</p> <p> ${this.hass.localize("ui.dialogs.matter-add-device.new.download_app")} </p> <div class="app-qr"> <a target="_blank" rel="noreferrer noopener" href="https://apps.apple.com/app/home-assistant/id1099568401?mt=8"> <img loading="lazy" src="/static/images/appstore.svg" alt="${this.hass.localize("ui.dialogs.matter-add-device.new.appstore")}" class="icon"> <img loading="lazy" src="/static/images/qr-appstore.svg" alt="${this.hass.localize("ui.dialogs.matter-add-device.new.appstore")}"> </a> <a target="_blank" rel="noreferrer noopener" href="https://play.google.com/store/apps/details?id=io.homeassistant.companion.android"> <img loading="lazy" src="/static/images/playstore.svg" alt="${this.hass.localize("ui.dialogs.matter-add-device.new.playstore")}" class="icon"> <img loading="lazy" src="/static/images/qr-playstore.svg" alt="${this.hass.localize("ui.dialogs.matter-add-device.new.playstore")}"> </a> </div> </div> `}},{kind:"field",static:!0,key:"styles",value:()=>[c,o.AH`.app-qr{margin:24px auto 0 auto;display:flex;justify-content:space-between;padding:0 24px;box-sizing:border-box;gap:16px;width:100%;max-width:400px}.app-qr a,.app-qr img{flex:1}`]}]}}),o.WF),(0,a.A)([(0,s.EM)("matter-add-device-commissioning")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"method",key:"render",value:function(){return o.qy` <div class="content"> <ha-circular-progress size="medium" indeterminate></ha-circular-progress> <p> ${this.hass.localize("ui.dialogs.matter-add-device.commissioning.note")} </p> </div> `}},{kind:"field",static:!0,key:"styles",value:()=>[c,o.AH`.content{display:flex;align-items:center;flex-direction:column;text-align:center}ha-circular-progress{margin-bottom:24px}`]}]}}),o.WF);var h=i(75610);const p={main:void 0,new:"main",existing:"main",google_home:"existing",google_home_fallback:"google_home",apple_home:"existing",generic:"existing",commissioning:void 0};(0,a.A)([(0,s.EM)("dialog-matter-add-device")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.wk)()],key:"_open",value:()=>!1},{kind:"field",decorators:[(0,s.wk)()],key:"_pairingCode",value:()=>""},{kind:"field",decorators:[(0,s.wk)()],key:"_step",value:()=>"main"},{kind:"field",key:"_unsub",value:void 0},{kind:"method",key:"showDialog",value:function(){this._open=!0,this._unsub=(0,l.hM)(this.hass,(()=>this.closeDialog()))}},{kind:"method",key:"closeDialog",value:function(){var e;this._open=!1,this._step="main",this._pairingCode="",null===(e=this._unsub)||void 0===e||e.call(this),this._unsub=void 0,(0,r.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"_handleStepSelected",value:function(e){this._step=e.detail.step,this._pairingCode=""}},{kind:"method",key:"_handlePairingCodeChanged",value:function(e){this._pairingCode=e.detail.code}},{kind:"method",key:"_back",value:function(){const e=p[this._step];e&&(this._step=e)}},{kind:"method",key:"_renderStep",value:function(){return o.qy` <div @pairing-code-changed="${this._handlePairingCodeChanged}" @step-selected="${this._handleStepSelected}" .hass="${this.hass}"> ${(0,n._)(`matter-add-device-${this._step.replaceAll("_","-")}`,{hass:this.hass})} </div> `}},{kind:"method",key:"_addDevice",value:async function(){const e=this._pairingCode,t=this._step;try{this._step="commissioning",await(0,l.PO)(this.hass,e)}catch(e){(0,h.P)(this,{message:this.hass.localize("ui.dialogs.matter-add-device.add_device_failed"),duration:2e3})}this._step=t}},{kind:"method",key:"_renderActions",value:function(){return"apple_home"===this._step||"google_home_fallback"===this._step||"generic"===this._step?o.qy` <ha-button slot="primaryAction" @click="${this._addDevice}" .disabled="${!this._pairingCode}"> ${this.hass.localize("ui.dialogs.matter-add-device.add_device")} </ha-button> `:"new"===this._step?o.qy` <ha-button slot="primaryAction" @click="${this.closeDialog}"> ${this.hass.localize("ui.common.ok")} </ha-button> `:o.s6}},{kind:"method",key:"render",value:function(){if(!this._open)return o.s6;const e=this.hass.localize(`ui.dialogs.matter-add-device.${this._step}.header`),t=p[this._step],i=this._renderActions();return o.qy` <ha-dialog open @closed="${this.closeDialog}" .heading="${e}" ?hideActions="${i===o.s6}" scrimClickAction escapeKeyAction> <ha-dialog-header slot="heading"> ${t?o.qy` <ha-icon-button-arrow-prev slot="navigationIcon" .hass="${this.hass}" @click="${this._back}"></ha-icon-button-arrow-prev> `:o.qy` <ha-icon-button slot="navigationIcon" dialogAction="cancel" .label="${this.hass.localize("ui.common.close")}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}"></ha-icon-button> `} <span slot="title">${e}</span> </ha-dialog-header> ${this._renderStep()} ${i} </ha-dialog> `}},{kind:"field",static:!0,key:"styles",value:()=>[d.nA,o.AH`:host{--horizontal-padding:24px}ha-dialog{--dialog-content-padding:0}ha-dialog{--mdc-dialog-min-width:450px;--mdc-dialog-max-width:450px}@media all and (max-width:450px),all and (max-height:500px){:host{--horizontal-padding:16px}ha-dialog{--mdc-dialog-min-width:calc(
            100vw - env(safe-area-inset-right) - env(safe-area-inset-left)
          );--mdc-dialog-max-width:calc(
            100vw - env(safe-area-inset-right) - env(safe-area-inset-left)
          )}}.loading{padding:24px;display:flex;align-items:center;justify-content:center}`]}]}}),o.WF)},14126:(e,t,i)=>{i.d(t,{RF:()=>s,dp:()=>r,nA:()=>n,og:()=>o});var a=i(40924);const o=a.AH`button.link{background:0 0;color:inherit;border:none;padding:0;font:inherit;text-align:left;text-decoration:underline;cursor:pointer;outline:0}`,s=a.AH`:host{font-family:var(--paper-font-body1_-_font-family);-webkit-font-smoothing:var(--paper-font-body1_-_-webkit-font-smoothing);font-size:var(--paper-font-body1_-_font-size);font-weight:var(--paper-font-body1_-_font-weight);line-height:var(--paper-font-body1_-_line-height)}app-header div[sticky]{height:48px}app-toolbar [main-title]{margin-left:20px;margin-inline-start:20px;margin-inline-end:initial}h1{font-family:var(--paper-font-headline_-_font-family);-webkit-font-smoothing:var(--paper-font-headline_-_-webkit-font-smoothing);white-space:var(--paper-font-headline_-_white-space);overflow:var(--paper-font-headline_-_overflow);text-overflow:var(--paper-font-headline_-_text-overflow);font-size:var(--paper-font-headline_-_font-size);font-weight:var(--paper-font-headline_-_font-weight);line-height:var(--paper-font-headline_-_line-height)}h2{font-family:var(--paper-font-title_-_font-family);-webkit-font-smoothing:var(--paper-font-title_-_-webkit-font-smoothing);white-space:var(--paper-font-title_-_white-space);overflow:var(--paper-font-title_-_overflow);text-overflow:var(--paper-font-title_-_text-overflow);font-size:var(--paper-font-title_-_font-size);font-weight:var(--paper-font-title_-_font-weight);line-height:var(--paper-font-title_-_line-height)}h3{font-family:var(--paper-font-subhead_-_font-family);-webkit-font-smoothing:var(--paper-font-subhead_-_-webkit-font-smoothing);white-space:var(--paper-font-subhead_-_white-space);overflow:var(--paper-font-subhead_-_overflow);text-overflow:var(--paper-font-subhead_-_text-overflow);font-size:var(--paper-font-subhead_-_font-size);font-weight:var(--paper-font-subhead_-_font-weight);line-height:var(--paper-font-subhead_-_line-height)}a{color:var(--primary-color)}.secondary{color:var(--secondary-text-color)}.error{color:var(--error-color)}.warning{color:var(--error-color)}ha-button.warning,mwc-button.warning{--mdc-theme-primary:var(--error-color)}${o} .card-actions a{text-decoration:none}.card-actions .warning{--mdc-theme-primary:var(--error-color)}.layout.horizontal,.layout.vertical{display:flex}.layout.inline{display:inline-flex}.layout.horizontal{flex-direction:row}.layout.vertical{flex-direction:column}.layout.wrap{flex-wrap:wrap}.layout.no-wrap{flex-wrap:nowrap}.layout.center,.layout.center-center{align-items:center}.layout.bottom{align-items:flex-end}.layout.center-center,.layout.center-justified{justify-content:center}.flex{flex:1;flex-basis:0.000000001px}.flex-auto{flex:1 1 auto}.flex-none{flex:none}.layout.justified{justify-content:space-between}`,n=a.AH`ha-dialog{--mdc-dialog-min-width:400px;--mdc-dialog-max-width:600px;--mdc-dialog-max-width:min(600px, 95vw);--justify-action-buttons:space-between}ha-dialog .form{color:var(--primary-text-color)}a{color:var(--primary-color)}@media all and (max-width:450px),all and (max-height:500px){ha-dialog{--mdc-dialog-min-width:calc(
        100vw - env(safe-area-inset-right) - env(safe-area-inset-left)
      );--mdc-dialog-max-width:calc(
        100vw - env(safe-area-inset-right) - env(safe-area-inset-left)
      );--mdc-dialog-min-height:100%;--mdc-dialog-max-height:100%;--vertical-align-dialog:flex-end;--ha-dialog-border-radius:0}}ha-button.warning,mwc-button.warning{--mdc-theme-primary:var(--error-color)}.error{color:var(--error-color)}`,r=a.AH`.ha-scrollbar::-webkit-scrollbar{width:.4rem;height:.4rem}.ha-scrollbar::-webkit-scrollbar-thumb{-webkit-border-radius:4px;border-radius:4px;background:var(--scrollbar-thumb-color)}.ha-scrollbar{overflow-y:auto;scrollbar-color:var(--scrollbar-thumb-color) transparent;scrollbar-width:thin}`;a.AH`body{background-color:var(--primary-background-color);color:var(--primary-text-color);height:calc(100vh - 32px);width:100vw}`}};
//# sourceMappingURL=64446.vuIK26kAUnM.js.map