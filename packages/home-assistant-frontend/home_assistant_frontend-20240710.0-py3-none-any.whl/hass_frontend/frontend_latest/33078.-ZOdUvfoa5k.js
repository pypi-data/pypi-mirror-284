export const id=33078;export const ids=[33078];export const modules={36639:(e,i,t)=>{t.d(i,{l:()=>a});t(55888);const a=async e=>{if(navigator.clipboard)try{return void await navigator.clipboard.writeText(e)}catch(e){}const i=document.createElement("textarea");i.value=e,document.body.appendChild(i),i.select(),document.execCommand("copy"),document.body.removeChild(i)}},26250:(e,i,t)=>{var a=t(62659),o=t(76504),s=t(80792),n=(t(27934),t(21950),t(71936),t(55888),t(98168),t(8339),t(40924)),r=t(18791),l=t(45081),d=t(77664),c=t(48962);t(57780);const h={key:"Mod-s",run:e=>((0,d.r)(e.dom,"editor-save"),!0)},u=e=>{const i=document.createElement("ha-icon");return i.icon=e.label,i};(0,a.A)([(0,r.EM)("ha-code-editor")],(function(e,i){class a extends i{constructor(...i){super(...i),e(this)}}return{F:a,d:[{kind:"field",key:"codemirror",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"mode",value:()=>"yaml"},{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"autofocus",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"readOnly",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"linewrap",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean,attribute:"autocomplete-entities"})],key:"autocompleteEntities",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean,attribute:"autocomplete-icons"})],key:"autocompleteIcons",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"error",value:()=>!1},{kind:"field",decorators:[(0,r.wk)()],key:"_value",value:()=>""},{kind:"field",key:"_loadedCodeMirror",value:void 0},{kind:"field",key:"_iconList",value:void 0},{kind:"set",key:"value",value:function(e){this._value=e}},{kind:"get",key:"value",value:function(){return this.codemirror?this.codemirror.state.doc.toString():this._value}},{kind:"get",key:"hasComments",value:function(){if(!this.codemirror||!this._loadedCodeMirror)return!1;const e=this._loadedCodeMirror.highlightingFor(this.codemirror.state,[this._loadedCodeMirror.tags.comment]);return!!this.renderRoot.querySelector(`span.${e}`)}},{kind:"method",key:"connectedCallback",value:function(){(0,o.A)((0,s.A)(a.prototype),"connectedCallback",this).call(this),this.hasUpdated&&this.requestUpdate(),this.addEventListener("keydown",c.d),this.codemirror&&!1!==this.autofocus&&this.codemirror.focus()}},{kind:"method",key:"disconnectedCallback",value:function(){(0,o.A)((0,s.A)(a.prototype),"disconnectedCallback",this).call(this),this.removeEventListener("keydown",c.d),this.updateComplete.then((()=>{this.codemirror.destroy(),delete this.codemirror}))}},{kind:"method",key:"scheduleUpdate",value:async function(){var e;null!==(e=this._loadedCodeMirror)&&void 0!==e||(this._loadedCodeMirror=await Promise.all([t.e(51859),t.e(380),t.e(24187),t.e(79881)]).then(t.bind(t,46054))),(0,o.A)((0,s.A)(a.prototype),"scheduleUpdate",this).call(this)}},{kind:"method",key:"update",value:function(e){if((0,o.A)((0,s.A)(a.prototype),"update",this).call(this,e),!this.codemirror)return void this._createCodeMirror();const i=[];e.has("mode")&&i.push({effects:this._loadedCodeMirror.langCompartment.reconfigure(this._mode)}),e.has("readOnly")&&i.push({effects:this._loadedCodeMirror.readonlyCompartment.reconfigure(this._loadedCodeMirror.EditorView.editable.of(!this.readOnly))}),e.has("linewrap")&&i.push({effects:this._loadedCodeMirror.linewrapCompartment.reconfigure(this.linewrap?this._loadedCodeMirror.EditorView.lineWrapping:[])}),e.has("_value")&&this._value!==this.value&&i.push({changes:{from:0,to:this.codemirror.state.doc.length,insert:this._value}}),i.length>0&&this.codemirror.dispatch(...i),e.has("error")&&this.classList.toggle("error-state",this.error)}},{kind:"get",key:"_mode",value:function(){return this._loadedCodeMirror.langs[this.mode]}},{kind:"method",key:"_createCodeMirror",value:function(){if(!this._loadedCodeMirror)throw new Error("Cannot create editor before CodeMirror is loaded");const e=[this._loadedCodeMirror.lineNumbers(),this._loadedCodeMirror.history(),this._loadedCodeMirror.drawSelection(),this._loadedCodeMirror.EditorState.allowMultipleSelections.of(!0),this._loadedCodeMirror.rectangularSelection(),this._loadedCodeMirror.crosshairCursor(),this._loadedCodeMirror.highlightSelectionMatches(),this._loadedCodeMirror.highlightActiveLine(),this._loadedCodeMirror.keymap.of([...this._loadedCodeMirror.defaultKeymap,...this._loadedCodeMirror.searchKeymap,...this._loadedCodeMirror.historyKeymap,...this._loadedCodeMirror.tabKeyBindings,h]),this._loadedCodeMirror.langCompartment.of(this._mode),this._loadedCodeMirror.haTheme,this._loadedCodeMirror.haSyntaxHighlighting,this._loadedCodeMirror.readonlyCompartment.of(this._loadedCodeMirror.EditorView.editable.of(!this.readOnly)),this._loadedCodeMirror.linewrapCompartment.of(this.linewrap?this._loadedCodeMirror.EditorView.lineWrapping:[]),this._loadedCodeMirror.EditorView.updateListener.of(this._onUpdate)];if(!this.readOnly){const i=[];this.autocompleteEntities&&this.hass&&i.push(this._entityCompletions.bind(this)),this.autocompleteIcons&&i.push(this._mdiCompletions.bind(this)),i.length>0&&e.push(this._loadedCodeMirror.autocompletion({override:i,maxRenderedOptions:10}))}this.codemirror=new this._loadedCodeMirror.EditorView({state:this._loadedCodeMirror.EditorState.create({doc:this._value,extensions:e}),parent:this.renderRoot})}},{kind:"field",key:"_getStates",value:()=>(0,l.A)((e=>{if(!e)return[];return Object.keys(e).map((i=>({type:"variable",label:i,detail:e[i].attributes.friendly_name,info:`State: ${e[i].state}`})))}))},{kind:"method",key:"_entityCompletions",value:function(e){const i=e.matchBefore(/[a-z_]{3,}\.\w*/);if(!i||i.from===i.to&&!e.explicit)return null;const t=this._getStates(this.hass.states);return t&&t.length?{from:Number(i.from),options:t,validFor:/^[a-z_]{3,}\.\w*$/}:null}},{kind:"field",key:"_getIconItems",value(){return async()=>{if(!this._iconList){let e;e=(await t.e(25143).then(t.t.bind(t,25143,19))).default,this._iconList=e.map((e=>({type:"variable",label:`mdi:${e.name}`,detail:e.keywords.join(", "),info:u})))}return this._iconList}}},{kind:"method",key:"_mdiCompletions",value:async function(e){const i=e.matchBefore(/mdi:\S*/);if(!i||i.from===i.to&&!e.explicit)return null;const t=await this._getIconItems();return{from:Number(i.from),options:t,validFor:/^mdi:\S*$/}}},{kind:"field",key:"_onUpdate",value(){return e=>{e.docChanged&&(this._value=e.state.doc.toString(),(0,d.r)(this,"value-changed",{value:this._value}))}}},{kind:"get",static:!0,key:"styles",value:function(){return n.AH`:host(.error-state) .cm-gutters{border-color:var(--error-state-color,red)}`}}]}}),n.mN)},25285:(e,i,t)=>{var a=t(62659),o=(t(21950),t(8339),t(40924)),s=t(18791);(0,a.A)([(0,s.EM)("ha-dialog-header")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"method",key:"render",value:function(){return o.qy` <header class="header"> <div class="header-bar"> <section class="header-navigation-icon"> <slot name="navigationIcon"></slot> </section> <section class="header-title"> <slot name="title"></slot> </section> <section class="header-action-items"> <slot name="actionItems"></slot> </section> </div> <slot></slot> </header> `}},{kind:"get",static:!0,key:"styles",value:function(){return[o.AH`:host{display:block}:host([show-border]){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.header-bar{display:flex;flex-direction:row;align-items:flex-start;padding:4px;box-sizing:border-box}.header-title{flex:1;font-size:22px;line-height:28px;font-weight:400;padding:10px 4px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}@media all and (min-width:450px) and (min-height:500px){.header-bar{padding:12px}}.header-navigation-icon{flex:none;min-width:8px;height:100%;display:flex;flex-direction:row}.header-action-items{flex:none;min-width:8px;height:100%;display:flex;flex-direction:row}`]}}]}}),o.WF)},95439:(e,i,t)=>{t.d(i,{l:()=>u});var a=t(62659),o=t(76504),s=t(80792),n=(t(86176),t(21950),t(8339),t(12387)),r=t(52280),l=t(40924),d=t(18791),c=t(25465);t(12731);const h=["button","ha-list-item"],u=(e,i)=>{var t;return l.qy` <div class="header_title"> <span>${i}</span> <ha-icon-button .label="${null!==(t=null==e?void 0:e.localize("ui.dialogs.generic.close"))&&void 0!==t?t:"Close"}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}" dialogAction="close" class="header_button"></ha-icon-button> </div> `};(0,a.A)([(0,d.EM)("ha-dialog")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"field",key:c.Xr,value:void 0},{kind:"method",key:"scrollToPos",value:function(e,i){var t;null===(t=this.contentElement)||void 0===t||t.scrollTo(e,i)}},{kind:"method",key:"renderHeading",value:function(){return l.qy`<slot name="heading"> ${(0,o.A)((0,s.A)(t.prototype),"renderHeading",this).call(this)} </slot>`}},{kind:"method",key:"firstUpdated",value:function(){var e;(0,o.A)((0,s.A)(t.prototype),"firstUpdated",this).call(this),this.suppressDefaultPressSelector=[this.suppressDefaultPressSelector,h].join(", "),this._updateScrolledAttribute(),null===(e=this.contentElement)||void 0===e||e.addEventListener("scroll",this._onScroll,{passive:!0})}},{kind:"method",key:"disconnectedCallback",value:function(){(0,o.A)((0,s.A)(t.prototype),"disconnectedCallback",this).call(this),this.contentElement.removeEventListener("scroll",this._onScroll)}},{kind:"field",key:"_onScroll",value(){return()=>{this._updateScrolledAttribute()}}},{kind:"method",key:"_updateScrolledAttribute",value:function(){this.contentElement&&this.toggleAttribute("scrolled",0!==this.contentElement.scrollTop)}},{kind:"field",static:!0,key:"styles",value:()=>[r.R,l.AH`:host([scrolled]) ::slotted(ha-dialog-header){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.mdc-dialog{--mdc-dialog-scroll-divider-color:var(
          --dialog-scroll-divider-color,
          var(--divider-color)
        );z-index:var(--dialog-z-index,8);-webkit-backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));--mdc-dialog-box-shadow:var(--dialog-box-shadow, none);--mdc-typography-headline6-font-weight:400;--mdc-typography-headline6-font-size:1.574rem}.mdc-dialog__actions{justify-content:var(--justify-action-buttons,flex-end);padding-bottom:max(env(safe-area-inset-bottom),24px)}.mdc-dialog__actions span:first-child{flex:var(--secondary-action-button-flex,unset)}.mdc-dialog__actions span:nth-child(2){flex:var(--primary-action-button-flex,unset)}.mdc-dialog__container{align-items:var(--vertical-align-dialog,center)}.mdc-dialog__title{padding:24px 24px 0 24px}.mdc-dialog__actions{padding:12px 24px 12px 24px}.mdc-dialog__title::before{content:unset}.mdc-dialog .mdc-dialog__content{position:var(--dialog-content-position,relative);padding:var(--dialog-content-padding,24px)}:host([hideactions]) .mdc-dialog .mdc-dialog__content{padding-bottom:max(var(--dialog-content-padding,24px),env(safe-area-inset-bottom))}.mdc-dialog .mdc-dialog__surface{position:var(--dialog-surface-position,relative);top:var(--dialog-surface-top);margin-top:var(--dialog-surface-margin-top);min-height:var(--mdc-dialog-min-height,auto);border-radius:var(--ha-dialog-border-radius,28px);-webkit-backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);background:var(--ha-dialog-surface-background,var(--mdc-theme-surface,#fff))}:host([flexContent]) .mdc-dialog .mdc-dialog__content{display:flex;flex-direction:column}.header_title{position:relative;padding-right:40px;padding-inline-end:40px;padding-inline-start:initial;direction:var(--direction)}.header_title span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block}.header_button{position:absolute;right:-12px;top:-12px;text-decoration:none;color:inherit;inset-inline-start:initial;inset-inline-end:-12px;direction:var(--direction)}.dialog-actions{inset-inline-start:initial!important;inset-inline-end:0px!important;direction:var(--direction)}`]}]}}),n.u)},20520:(e,i,t)=>{var a=t(62659),o=t(76504),s=t(80792),n=(t(21950),t(55888),t(8339),t(47420)),r=t(40924),l=t(18791),d=t(77664),c=t(14126),h=(t(26250),t(75610)),u=t(36639);(0,a.A)([(0,l.EM)("ha-yaml-editor")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,l.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,l.MZ)()],key:"value",value:void 0},{kind:"field",decorators:[(0,l.MZ)({attribute:!1})],key:"yamlSchema",value:()=>n.DEFAULT_SCHEMA},{kind:"field",decorators:[(0,l.MZ)()],key:"defaultValue",value:void 0},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"isValid",value:()=>!0},{kind:"field",decorators:[(0,l.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"autoUpdate",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"readOnly",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"required",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"copyClipboard",value:()=>!1},{kind:"field",decorators:[(0,l.wk)()],key:"_yaml",value:()=>""},{kind:"method",key:"setValue",value:function(e){try{this._yaml=e&&!(e=>{if("object"!=typeof e)return!1;for(const i in e)if(Object.prototype.hasOwnProperty.call(e,i))return!1;return!0})(e)?(0,n.dump)(e,{schema:this.yamlSchema,quotingType:'"',noRefs:!0}):""}catch(i){console.error(i,e),alert(`There was an error converting to YAML: ${i}`)}}},{kind:"method",key:"firstUpdated",value:function(){this.defaultValue&&this.setValue(this.defaultValue)}},{kind:"method",key:"willUpdate",value:function(e){(0,o.A)((0,s.A)(t.prototype),"willUpdate",this).call(this,e),this.autoUpdate&&e.has("value")&&this.setValue(this.value)}},{kind:"method",key:"render",value:function(){return void 0===this._yaml?r.s6:r.qy` ${this.label?r.qy`<p>${this.label}${this.required?" *":""}</p>`:""} <ha-code-editor .hass="${this.hass}" .value="${this._yaml}" .readOnly="${this.readOnly}" mode="yaml" autocomplete-entities autocomplete-icons .error="${!1===this.isValid}" @value-changed="${this._onChange}" dir="ltr"></ha-code-editor> ${this.copyClipboard?r.qy`<div class="card-actions"> <mwc-button @click="${this._copyYaml}"> ${this.hass.localize("ui.components.yaml-editor.copy_to_clipboard")} </mwc-button> </div>`:r.s6} `}},{kind:"method",key:"_onChange",value:function(e){let i;e.stopPropagation(),this._yaml=e.detail.value;let t=!0;if(this._yaml)try{i=(0,n.load)(this._yaml,{schema:this.yamlSchema})}catch(e){t=!1}else i={};this.value=i,this.isValid=t,(0,d.r)(this,"value-changed",{value:i,isValid:t})}},{kind:"get",key:"yaml",value:function(){return this._yaml}},{kind:"method",key:"_copyYaml",value:async function(){this.yaml&&(await(0,u.l)(this.yaml),(0,h.P)(this,{message:this.hass.localize("ui.common.copied_clipboard")}))}},{kind:"get",static:!0,key:"styles",value:function(){return[c.RF,r.AH`.card-actions{border-radius:var(--actions-border-radius,0px 0px var(--ha-card-border-radius,12px) var(--ha-card-border-radius,12px));border:1px solid var(--divider-color);padding:5px 16px}ha-code-editor{flex-grow:1}`]}}]}}),r.WF)},42866:(e,i,t)=>{var a=t(62659),o=t(76504),s=t(80792),n=(t(21950),t(8339),t(40924)),r=t(18791),l=t(69760),d=t(80204),c=t(66596),h=t(35978);(0,a.A)([(0,r.EM)("ha-user-badge")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"user",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_personPicture",value:void 0},{kind:"field",key:"_personEntityId",value:void 0},{kind:"method",key:"willUpdate",value:function(e){if((0,o.A)((0,s.A)(t.prototype),"willUpdate",this).call(this,e),e.has("user"))return void this._getPersonPicture();const i=e.get("hass");if(this._personEntityId&&i&&this.hass.states[this._personEntityId]!==i.states[this._personEntityId]){const e=this.hass.states[this._personEntityId];e?this._personPicture=e.attributes.entity_picture:this._getPersonPicture()}else!this._personEntityId&&i&&this._getPersonPicture()}},{kind:"method",key:"render",value:function(){if(!this.hass||!this.user)return n.s6;const e=this._personPicture;if(e)return n.qy`<div style="${(0,d.W)({backgroundImage:`url(${e})`})}" class="picture"></div>`;const i=(0,h._2)(this.user.name);return n.qy`<div class="initials ${(0,l.H)({long:i.length>2})}"> ${i} </div>`}},{kind:"method",key:"_getPersonPicture",value:function(){if(this._personEntityId=void 0,this._personPicture=void 0,this.hass&&this.user)for(const e of Object.values(this.hass.states))if(e.attributes.user_id===this.user.id&&"person"===(0,c.t)(e)){this._personEntityId=e.entity_id,this._personPicture=e.attributes.entity_picture;break}}},{kind:"get",static:!0,key:"styles",value:function(){return n.AH`:host{display:contents}.picture{width:40px;height:40px;background-size:cover;border-radius:50%}.initials{display:inline-block;box-sizing:border-box;width:40px;line-height:40px;border-radius:50%;text-align:center;background-color:var(--light-primary-color);text-decoration:none;color:var(--text-light-primary-color,var(--primary-text-color));overflow:hidden}.initials.long{font-size:80%}`}}]}}),n.WF)},35978:(e,i,t)=>{t.d(i,{TK:()=>r,_2:()=>d,eR:()=>o,hG:()=>l,hU:()=>s,kg:()=>n,wj:()=>a,xg:()=>c});t(71936),t(55888),t(98168);const a="system-admin",o="system-users",s=async e=>e.callWS({type:"config/auth/list"}),n=async(e,i,t,a)=>e.callWS({type:"config/auth/create",name:i,group_ids:t,local_only:a}),r=async(e,i,t)=>e.callWS({...t,type:"config/auth/update",user_id:i}),l=async(e,i)=>e.callWS({type:"config/auth/delete",user_id:i}),d=e=>e?e.trim().split(" ").slice(0,3).map((e=>e.substring(0,1))).join(""):"?",c=(e,i,t)=>{const a=[],o=i=>e.localize(`ui.panel.config.users.${i}`);return i.is_owner&&a.push(["M12 2C6.47 2 2 6.5 2 12C2 17.5 6.5 22 12 22S22 17.5 22 12 17.5 2 12 2M12 20C7.58 20 4 16.42 4 12C4 7.58 7.58 4 12 4S20 7.58 20 12C20 16.42 16.42 20 12 20M8 14L7 8L10 10L12 7L14 10L17 8L16 14H8M8.56 16C8.22 16 8 15.78 8 15.44V15H16V15.44C16 15.78 15.78 16 15.44 16H8.56Z",o("is_owner")]),t&&i.system_generated&&a.push(["M11,7H15V9H11V11H13A2,2 0 0,1 15,13V15A2,2 0 0,1 13,17H9V15H13V13H11A2,2 0 0,1 9,11V9A2,2 0 0,1 11,7M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4Z",o("is_system")]),i.local_only&&a.push(["M12 20C7.6 20 4 16.4 4 12S7.6 4 12 4 20 7.6 20 12 16.4 20 12 20M12 2C6.5 2 2 6.5 2 12S6.5 22 12 22 22 17.5 22 12 17.5 2 12 2M11 14H13V17H16V12H18L12 7L6 12H8V17H11V14",o("is_local")]),i.is_active||a.push(["M12 2C17.5 2 22 6.5 22 12S17.5 22 12 22 2 17.5 2 12 6.5 2 12 2M12 4C10.1 4 8.4 4.6 7.1 5.7L18.3 16.9C19.3 15.5 20 13.8 20 12C20 7.6 16.4 4 12 4M16.9 18.3L5.7 7.1C4.6 8.4 4 10.1 4 12C4 16.4 7.6 20 12 20C13.9 20 15.6 19.4 16.9 18.3Z",o("is_not_active")]),a}},74381:(e,i,t)=>{t.a(e,(async(e,i)=>{try{var a=t(13091),o=t(92082),s=t(52409),n=e([a,s]);[a,s]=n.then?(await n)():n;class r extends HTMLElement{get _error(){var e;return"HUI-ERROR-CARD"===(null===(e=this._element)||void 0===e?void 0:e.tagName)}constructor(){super(),this._hass=void 0,this._element=void 0,this._config=void 0,this.addEventListener("ll-rebuild",(()=>{this._cleanup(),this._config&&(this.config=this._config)}))}set hass(e){this._hass=e,this._element&&(this._element.hass=e)}set error(e){this._createBadge((0,o.G9)(`${e.type}: ${e.message}`))}set config(e){const i=this._config;this._config=e,e?this._element&&!this._error&&i&&e.type===i.type?this._element.setConfig(e):this._createBadge(e):this._cleanup()}_createBadge(e){this._cleanup(),this._element=(0,s.Y)(e),this._hass&&(this._element.hass=this._hass),this.appendChild(this._element)}_cleanup(){this._element&&(this.removeChild(this._element),this._element=void 0)}}customElements.define("hui-badge-preview",r),i()}catch(e){i(e)}}))},33078:(e,i,t)=>{t.a(e,(async(e,a)=>{try{t.r(i),t.d(i,{HuiDialogEditView:()=>M});var o=t(62659),s=(t(53501),t(21950),t(59092),t(55888),t(98168),t(8339),t(58068),t(48339),t(38716),t(40924)),n=t(18791),r=t(69760),l=t(77664),d=t(48962),c=t(28825),h=t(61314),u=(t(12261),t(4596),t(95439),t(25285),t(20520),t(47387)),v=t(98876),p=t(14126),g=t(90353),m=t(83882),_=t(44497),f=t(74381),y=t(12851),k=(t(752),t(39223)),b=(t(26847),e([g,f,k]));[g,f,k]=b.then?(await b)():b;const w="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z",x="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",C="M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z";let M=(0,o.A)([(0,n.EM)("hui-dialog-edit-view")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"_saving",value:()=>!1},{kind:"field",decorators:[(0,n.wk)()],key:"_curTab",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"_dirty",value:()=>!1},{kind:"field",decorators:[(0,n.wk)()],key:"_yamlMode",value:()=>!1},{kind:"field",decorators:[(0,n.P)("ha-yaml-editor")],key:"_editor",value:void 0},{kind:"field",key:"_curTabIndex",value:()=>0},{kind:"get",key:"_type",value:function(){return this._config?this._config.panel?m.YG:this._config.type||m.Zy:m.Zy}},{kind:"method",key:"updated",value:function(e){if(this._yamlMode&&e.has("_yamlMode")){var i;const e={...this._config};null===(i=this._editor)||void 0===i||i.setValue(e)}}},{kind:"method",key:"showDialog",value:function(e){if(this._params=e,void 0===this._params.viewIndex)return this._config={},void(this._dirty=!1);const i=this._params.lovelace.config.views[this._params.viewIndex];if((0,u.R)(i)){const{strategy:e,...t}=i;this._config=t}else this._config=i}},{kind:"method",key:"closeDialog",value:function(){this._curTabIndex=0,this._params=void 0,this._config={},this._yamlMode=!1,this._dirty=!1,(0,l.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"get",key:"_viewConfigTitle",value:function(){return this._config&&this._config.title?this.hass.localize("ui.panel.lovelace.editor.edit_view.header_name",{name:this._config.title}):this.hass.localize("ui.panel.lovelace.editor.edit_view.header")}},{kind:"method",key:"render",value:function(){var e,i,t,a,o,n,l,c;if(!this._params)return s.s6;let h;if(this._yamlMode)h=s.qy` <ha-yaml-editor .hass="${this.hass}" dialogInitialFocus @value-changed="${this._viewYamlChanged}"></ha-yaml-editor> `;else switch(this._curTab){case"tab-settings":h=s.qy` <hui-view-editor .isNew="${void 0===this._params.viewIndex}" .hass="${this.hass}" .config="${this._config}" @view-config-changed="${this._viewConfigChanged}"></hui-view-editor> `;break;case"tab-background":h=s.qy` <hui-view-background-editor .hass="${this.hass}" .config="${this._config}" @view-config-changed="${this._viewConfigChanged}"></hui-view-background-editor> `;break;case"tab-badges":h=s.qy` ${null!==(e=this._config)&&void 0!==e&&null!==(e=e.badges)&&void 0!==e&&e.length?s.qy` ${m.NI.includes(this._type)?s.qy` <ha-alert alert-type="warning"> ${this.hass.localize("ui.panel.lovelace.editor.edit_badges.view_no_badges")} </ha-alert> `:s.s6} <div class="preview-badges"> ${this._config.badges.map((e=>s.qy` <hui-badge-preview .hass="${this.hass}" .config="${e}"></hui-badge-preview> `))} </div> `:s.s6} <hui-entity-editor .hass="${this.hass}" .entities="${(null===(i=this._config)||void 0===i?void 0:i.badges)||[]}" @entities-changed="${this._badgesChanged}"></hui-entity-editor> `;break;case"tab-visibility":h=s.qy` <hui-view-visibility-editor .hass="${this.hass}" .config="${this._config}" @view-visibility-changed="${this._viewVisibilityChanged}"></hui-view-visibility-editor> `;break;case"tab-cards":h=s.qy` Cards `}const u=(null===(t=this._config)||void 0===t?void 0:t.type)===m.LQ?(null===(a=this._config)||void 0===a?void 0:a.type)===m.LQ&&!(null!==(o=this._config)&&void 0!==o&&null!==(o=o.cards)&&void 0!==o&&o.length):(null===(n=this._config)||void 0===n?void 0:n.type)!==m.LQ&&!(null!==(l=this._config)&&void 0!==l&&null!==(l=l.sections)&&void 0!==l&&l.length);return s.qy` <ha-dialog open scrimClickAction escapeKeyAction @closed="${this.closeDialog}" .heading="${this._viewConfigTitle}" class="${(0,r.H)({"yaml-mode":this._yamlMode})}"> <ha-dialog-header show-border slot="heading"> <ha-icon-button slot="navigationIcon" dialogAction="cancel" .label="${this.hass.localize("ui.common.close")}" .path="${x}"></ha-icon-button> <h2 slot="title">${this._viewConfigTitle}</h2> <ha-button-menu slot="actionItems" fixed corner="BOTTOM_END" menuCorner="END" @action="${this._handleAction}" @closed="${d.d}"> <ha-icon-button slot="trigger" .label="${this.hass.localize("ui.common.menu")}" .path="${C}"></ha-icon-button> <mwc-list-item graphic="icon"> ${this.hass.localize("ui.panel.lovelace.editor.edit_view.edit_ui")} ${this._yamlMode?"":s.qy`<ha-svg-icon class="selected_menu_item" slot="graphic" .path="${w}"></ha-svg-icon>`} </mwc-list-item> <mwc-list-item graphic="icon"> ${this.hass.localize("ui.panel.lovelace.editor.edit_view.edit_yaml")} ${this._yamlMode?s.qy`<ha-svg-icon class="selected_menu_item" slot="graphic" .path="${w}"></ha-svg-icon>`:""} </mwc-list-item> </ha-button-menu> ${u?s.s6:s.qy` <ha-alert class="incompatible" alert-type="warning"> ${(null===(c=this._config)||void 0===c?void 0:c.type)===m.LQ?this.hass.localize("ui.panel.lovelace.editor.edit_view.type_warning_sections"):this.hass.localize("ui.panel.lovelace.editor.edit_view.type_warning_others")} </ha-alert> `} ${this._yamlMode?s.s6:s.qy`<paper-tabs scrollable hide-scroll-buttons .selected="${this._curTabIndex}" @selected-item-changed="${this._handleTabSelected}"> <paper-tab id="tab-settings" dialogInitialFocus>${this.hass.localize("ui.panel.lovelace.editor.edit_view.tab_settings")}</paper-tab> <paper-tab id="tab-background">${this.hass.localize("ui.panel.lovelace.editor.edit_view.tab_background")}</paper-tab> <paper-tab id="tab-badges">${this.hass.localize("ui.panel.lovelace.editor.edit_view.tab_badges")}</paper-tab> <paper-tab id="tab-visibility">${this.hass.localize("ui.panel.lovelace.editor.edit_view.tab_visibility")}</paper-tab> </paper-tabs>`} </ha-dialog-header> ${h} ${void 0!==this._params.viewIndex?s.qy` <mwc-button class="warning" slot="secondaryAction" @click="${this._deleteConfirm}"> ${this.hass.localize("ui.panel.lovelace.editor.edit_view.delete")} </mwc-button> `:s.s6} <mwc-button slot="primaryAction" ?disabled="${!this._config||this._saving||!this._dirty||!u}" @click="${this._save}"> ${this._saving?s.qy`<ha-circular-progress indeterminate size="small" aria-label="Saving"></ha-circular-progress>`:s.s6} ${this.hass.localize("ui.common.save")}</mwc-button> </ha-dialog> `}},{kind:"method",key:"_handleAction",value:async function(e){switch(e.stopPropagation(),e.preventDefault(),e.detail.index){case 0:this._yamlMode=!1;break;case 1:this._yamlMode=!0}}},{kind:"method",key:"_delete",value:async function(){if(this._params)try{await this._params.lovelace.saveConfig((0,_.lD)(this._params.lovelace.config,this._params.viewIndex)),this.closeDialog(),(0,c.o)(`/${window.location.pathname.split("/")[1]}`)}catch(e){(0,v.showAlertDialog)(this,{text:`Deleting failed: ${e.message}`})}}},{kind:"method",key:"_deleteConfirm",value:async function(){var e,i,t,a;const o=null!==(e=this._config)&&void 0!==e&&null!==(e=e.sections)&&void 0!==e&&e.length?"sections":null!==(i=this._config)&&void 0!==i&&null!==(i=i.cards)&&void 0!==i&&i.length?"cards":"only",s=null!==(t=this._config)&&void 0!==t&&t.title?"named":"unnamed";await(0,v.showConfirmationDialog)(this,{title:this.hass.localize("ui.panel.lovelace.views.delete_title"),text:this.hass.localize(`ui.panel.lovelace.views.delete_${s}_view_${o}`,{name:null===(a=this._config)||void 0===a?void 0:a.title}),confirmText:this.hass.localize("ui.common.delete"),destructive:!0})&&this._delete()}},{kind:"method",key:"_handleTabSelected",value:function(e){e.detail.value&&(this._curTab=e.detail.value.id)}},{kind:"method",key:"_save",value:async function(){var e,i,t;if(!this._params||!this._config)return;if(!this._isConfigChanged())return void this.closeDialog();this._saving=!0;const a={...this._config};a.type!==m.LQ||null!==(e=a.sections)&&void 0!==e&&e.length?null!==(i=a.cards)&&void 0!==i&&i.length||(a.cards=[]):a.sections=[{type:"grid",cards:[]}],null!==(t=a.badges)&&void 0!==t&&t.length||delete a.badges;const o=this._params.lovelace;try{await o.saveConfig(this._creatingView?(0,_.fJ)(this.hass,o.config,a):(0,_.Iq)(this.hass,o.config,this._params.viewIndex,a)),this._params.saveCallback&&this._params.saveCallback(this._params.viewIndex||o.config.views.length,a),this.closeDialog()}catch(e){(0,v.showAlertDialog)(this,{text:`${this.hass.localize("ui.panel.lovelace.editor.edit_view.saving_failed")}: ${e.message}`})}finally{this._saving=!1}}},{kind:"method",key:"_viewConfigChanged",value:function(e){e.detail&&e.detail.config&&!(0,h.b)(this._config,e.detail.config)&&(this._config=e.detail.config,this._dirty=!0)}},{kind:"method",key:"_viewVisibilityChanged",value:function(e){e.detail.visible&&this._config&&(this._config={...this._config,visible:e.detail.visible}),this._dirty=!0}},{kind:"method",key:"_badgesChanged",value:function(e){this.hass&&e.detail&&e.detail.entities&&(this._config={...this._config,badges:(0,y._)(e.detail.entities)},this._dirty=!0)}},{kind:"method",key:"_viewYamlChanged",value:function(e){e.stopPropagation(),e.detail.isValid&&(this._config=e.detail.value,this._dirty=!0)}},{kind:"method",key:"_isConfigChanged",value:function(){return this._creatingView||JSON.stringify(this._config)!==JSON.stringify(this._params.lovelace.config.views[this._params.viewIndex])}},{kind:"get",key:"_creatingView",value:function(){return void 0===this._params.viewIndex}},{kind:"get",static:!0,key:"styles",value:function(){return[p.nA,s.AH`ha-dialog{--vertical-align-dialog:flex-start;--dialog-surface-margin-top:40px}@media all and (max-width:450px),all and (max-height:500px){ha-dialog{--dialog-surface-margin-top:0px}}ha-dialog.yaml-mode{--dialog-content-padding:0}h2{margin:0;font-size:inherit;font-weight:inherit}paper-tabs{--paper-tabs-selection-bar-color:var(--primary-color);color:var(--primary-text-color);text-transform:uppercase;padding:0 20px}mwc-button.warning{margin-right:auto;margin-inline-end:auto;margin-inline-start:initial}ha-circular-progress{display:none}ha-circular-progress[indeterminate]{display:block}.selected_menu_item{color:var(--primary-color)}.hidden{display:none}.error{color:var(--error-color);border-bottom:1px solid var(--error-color)}.preview-badges{display:flex;justify-content:center;margin:12px 16px;flex-wrap:wrap}.incompatible{display:block}@media all and (min-width:600px){ha-dialog{--mdc-dialog-min-width:600px}}`]}}]}}),s.WF);a()}catch(e){a(e)}}))},39223:(e,i,t)=>{t.a(e,(async(e,i)=>{try{var a=t(62659),o=(t(21950),t(26777),t(8339),t(23981),t(40924)),s=t(18791),n=t(77664),r=t(46182),l=e([r]);r=(l.then?(await l)():l)[0];const d={image:{original:!0}};(0,a.A)([(0,s.EM)("hui-view-background-editor")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.wk)()],key:"_config",value:void 0},{kind:"set",key:"config",value:function(e){this._config=e}},{kind:"method",key:"render",value:function(){var e,i;if(!this.hass)return o.s6;const t=null===(e=this._config)||void 0===e?void 0:e.background,a="string"==typeof t?null===(i=t.match(/url\(['"]?([^'"]+)['"]?\)/))||void 0===i?void 0:i[1]:null==t?void 0:t.image;return o.qy` <ha-selector-image .hass="${this.hass}" .label="${this.hass.localize("ui.panel.lovelace.editor.edit_view.background.title")}" .value="${a}" .selector="${d}" @value-changed="${this._backgroundChanged}"></ha-selector-image> `}},{kind:"method",key:"_backgroundChanged",value:function(e){const i=e.detail.value,t={...this._config,background:{..."string"==typeof this._config.background?{}:this._config.background,image:i||void 0}};(0,n.r)(this,"view-config-changed",{config:t})}},{kind:"get",static:!0,key:"styles",value:function(){return o.AH`:host{display:block}`}}]}}),o.WF);i()}catch(e){i(e)}}))},752:(e,i,t)=>{var a=t(62659),o=(t(21950),t(98168),t(8339),t(40924)),s=t(18791),n=t(45081),r=t(77664),l=t(6631),d=(t(23006),t(83882));(0,a.A)([(0,s.EM)("hui-view-editor")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.MZ)({type:Boolean})],key:"isNew",value:()=>!1},{kind:"field",decorators:[(0,s.wk)()],key:"_config",value:void 0},{kind:"field",key:"_suggestedPath",value:()=>!1},{kind:"field",key:"_schema",value:()=>(0,n.A)(((e,i)=>[{name:"title",selector:{text:{}}},{name:"icon",selector:{icon:{}}},{name:"path",selector:{text:{}}},{name:"theme",selector:{theme:{}}},{name:"type",selector:{select:{options:[d.Zy,d.oH,d.YG,d.LQ].map((i=>({value:i,label:e(`ui.panel.lovelace.editor.edit_view.types.${i}`)})))}}},...i===d.LQ?[{name:"max_columns",selector:{number:{min:1,max:10,mode:"slider"}}}]:[],{name:"subview",selector:{boolean:{}}}]))},{kind:"set",key:"config",value:function(e){this._config=e}},{kind:"get",key:"_type",value:function(){return this._config?this._config.panel?d.YG:this._config.type||d.Zy:d.Zy}},{kind:"method",key:"render",value:function(){if(!this.hass)return o.s6;const e=this._schema(this.hass.localize,this._type),i={...this._config,type:this._type};return void 0===i.max_columns&&this._type===d.LQ&&(i.max_columns=4),o.qy` <ha-form .hass="${this.hass}" .data="${i}" .schema="${e}" .computeLabel="${this._computeLabel}" .computeHelper="${this._computeHelper}" @value-changed="${this._valueChanged}"></ha-form> `}},{kind:"method",key:"_valueChanged",value:function(e){const i=e.detail.value;i.type===d.Zy&&delete i.type,i.type!==d.LQ&&delete i.max_columns,!this.isNew||this._suggestedPath||!i.title||this._config.path&&i.path!==(0,l.Y)(this._config.title||"","-")||(i.path=(0,l.Y)(i.title,"-")),(0,r.r)(this,"view-config-changed",{config:i})}},{kind:"field",key:"_computeLabel",value(){return e=>{switch(e.name){case"path":return this.hass.localize("ui.panel.lovelace.editor.card.generic.url");case"type":return this.hass.localize("ui.panel.lovelace.editor.edit_view.type");case"subview":return this.hass.localize("ui.panel.lovelace.editor.edit_view.subview");case"max_columns":return this.hass.localize("ui.panel.lovelace.editor.edit_view.max_columns");default:return this.hass.localize(`ui.panel.lovelace.editor.card.generic.${e.name}`)}}}},{kind:"field",key:"_computeHelper",value(){return e=>{if("subview"===e.name)return this.hass.localize("ui.panel.lovelace.editor.edit_view.subview_helper")}}}]}}),o.WF)},26847:(e,i,t)=>{var a=t(62659),o=t(76504),s=t(80792),n=(t(21950),t(71936),t(14460),t(66274),t(85038),t(98168),t(22836),t(8339),t(23981),t(40924)),r=t(18791),l=t(45081),d=t(77664),c=t(95507),h=(t(42866),t(35978));(0,a.A)([(0,r.EM)("hui-view-visibility-editor")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"set",key:"config",value:function(e){this._config=e,this._visible=void 0===this._config.visible||this._config.visible}},{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_users",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_visible",value:void 0},{kind:"field",key:"_sortedUsers",value(){return(0,l.A)((e=>e.sort(((e,i)=>(0,c.x)(e.name,i.name,this.hass.locale.language)))))}},{kind:"method",key:"firstUpdated",value:function(e){(0,o.A)((0,s.A)(t.prototype),"firstUpdated",this).call(this,e),(0,h.hU)(this.hass).then((e=>{this._users=e.filter((e=>!e.system_generated))}))}},{kind:"method",key:"render",value:function(){return this.hass&&this._users?n.qy` <p> ${this.hass.localize("ui.panel.lovelace.editor.edit_view.visibility.select_users")} </p> ${this._sortedUsers(this._users).map((e=>n.qy` <mwc-list-item graphic="avatar" hasMeta> <ha-user-badge slot="graphic" .hass="${this.hass}" .user="${e}"></ha-user-badge> <span>${e.name}</span> <ha-switch slot="meta" .userId="${e.id}" @change="${this.valChange}" .checked="${this.checkUser(e.id)}"></ha-switch> </mwc-list-item> `))} `:n.s6}},{kind:"method",key:"checkUser",value:function(e){return void 0===this._visible||("boolean"==typeof this._visible?this._visible:this._visible.some((i=>i.user===e)))}},{kind:"method",key:"valChange",value:function(e){const i=e.currentTarget.userId,t=e.currentTarget.checked;let a=[];if("boolean"==typeof this._visible){this._visible&&(a=this._users.map((e=>({user:e.id}))))}else a=[...this._visible];if(!0===t){const e={user:i};a.push(e)}else a=a.filter((e=>e.user!==i));this._visible=a.filter((e=>this._users.some((i=>i.id===e.user)))),(0,d.r)(this,"view-visibility-changed",{visible:this._visible})}},{kind:"get",static:!0,key:"styles",value:function(){return n.AH`:host{display:block}`}}]}}),n.WF)}};
//# sourceMappingURL=33078.-ZOdUvfoa5k.js.map