/*! For license information please see 77598.Zib7piAMgVw.js.LICENSE.txt */
export const id=77598;export const ids=[77598];export const modules={91619:(e,t,o)=>{o.d(t,{$:()=>v});o(21950),o(8339);var i=o(76513),r=o(54788),a=o(18791),s=o(71086),d=o(86029),n=o(69303),l=o(40924),c=o(69760);const h=d.QQ?{passive:!0}:void 0;class u extends s.O{constructor(){super(...arguments),this.centerTitle=!1,this.handleTargetScroll=()=>{this.mdcFoundation.handleTargetScroll()},this.handleNavigationClick=()=>{this.mdcFoundation.handleNavigationClick()}}get scrollTarget(){return this._scrollTarget||window}set scrollTarget(e){this.unregisterScrollListener();const t=this.scrollTarget;this._scrollTarget=e,this.updateRootPosition(),this.requestUpdate("scrollTarget",t),this.registerScrollListener()}updateRootPosition(){if(this.mdcRoot){const e=this.scrollTarget===window;this.mdcRoot.style.position=e?"":"absolute"}}render(){let e=l.qy`<span class="mdc-top-app-bar__title"><slot name="title"></slot></span>`;return this.centerTitle&&(e=l.qy`<section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-center">${e}</section>`),l.qy` <header class="mdc-top-app-bar ${(0,c.H)(this.barClasses())}"> <div class="mdc-top-app-bar__row"> <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start" id="navigation"> <slot name="navigationIcon" @click="${this.handleNavigationClick}"></slot> ${this.centerTitle?null:e} </section> ${this.centerTitle?e:null} <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end" id="actions" role="toolbar"> <slot name="actionItems"></slot> </section> </div> </header> <div class="${(0,c.H)(this.contentClasses())}"> <slot></slot> </div> `}createAdapter(){return Object.assign(Object.assign({},(0,s.i)(this.mdcRoot)),{setStyle:(e,t)=>this.mdcRoot.style.setProperty(e,t),getTopAppBarHeight:()=>this.mdcRoot.clientHeight,notifyNavigationIconClicked:()=>{this.dispatchEvent(new Event(n.P$.NAVIGATION_EVENT,{bubbles:!0,cancelable:!0}))},getViewportScrollY:()=>this.scrollTarget instanceof Window?this.scrollTarget.pageYOffset:this.scrollTarget.scrollTop,getTotalActionItems:()=>this._actionItemsSlot.assignedNodes({flatten:!0}).length})}registerListeners(){this.registerScrollListener()}unregisterListeners(){this.unregisterScrollListener()}registerScrollListener(){this.scrollTarget.addEventListener("scroll",this.handleTargetScroll,h)}unregisterScrollListener(){this.scrollTarget.removeEventListener("scroll",this.handleTargetScroll)}firstUpdated(){super.firstUpdated(),this.updateRootPosition(),this.registerListeners()}disconnectedCallback(){super.disconnectedCallback(),this.unregisterListeners()}}(0,i.__decorate)([(0,a.P)(".mdc-top-app-bar")],u.prototype,"mdcRoot",void 0),(0,i.__decorate)([(0,a.P)('slot[name="actionItems"]')],u.prototype,"_actionItemsSlot",void 0),(0,i.__decorate)([(0,a.MZ)({type:Boolean})],u.prototype,"centerTitle",void 0),(0,i.__decorate)([(0,a.MZ)({type:Object})],u.prototype,"scrollTarget",null);class p extends u{constructor(){super(...arguments),this.mdcFoundationClass=r.A,this.prominent=!1,this.dense=!1,this.handleResize=()=>{this.mdcFoundation.handleWindowResize()}}barClasses(){return{"mdc-top-app-bar--dense":this.dense,"mdc-top-app-bar--prominent":this.prominent,"center-title":this.centerTitle}}contentClasses(){return{"mdc-top-app-bar--fixed-adjust":!this.dense&&!this.prominent,"mdc-top-app-bar--dense-fixed-adjust":this.dense&&!this.prominent,"mdc-top-app-bar--prominent-fixed-adjust":!this.dense&&this.prominent,"mdc-top-app-bar--dense-prominent-fixed-adjust":this.dense&&this.prominent}}registerListeners(){super.registerListeners(),window.addEventListener("resize",this.handleResize,h)}unregisterListeners(){super.unregisterListeners(),window.removeEventListener("resize",this.handleResize)}}(0,i.__decorate)([(0,a.MZ)({type:Boolean,reflect:!0})],p.prototype,"prominent",void 0),(0,i.__decorate)([(0,a.MZ)({type:Boolean,reflect:!0})],p.prototype,"dense",void 0);var m=o(70750);class v extends p{constructor(){super(...arguments),this.mdcFoundationClass=m.A}barClasses(){return Object.assign(Object.assign({},super.barClasses()),{"mdc-top-app-bar--fixed":!0})}registerListeners(){this.scrollTarget.addEventListener("scroll",this.handleTargetScroll,h)}unregisterListeners(){this.scrollTarget.removeEventListener("scroll",this.handleTargetScroll)}}},26250:(e,t,o)=>{var i=o(62659),r=o(76504),a=o(80792),s=(o(27934),o(21950),o(71936),o(55888),o(98168),o(8339),o(40924)),d=o(18791),n=o(45081),l=o(77664),c=o(48962);o(57780);const h={key:"Mod-s",run:e=>((0,l.r)(e.dom,"editor-save"),!0)},u=e=>{const t=document.createElement("ha-icon");return t.icon=e.label,t};(0,i.A)([(0,d.EM)("ha-code-editor")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",key:"codemirror",value:void 0},{kind:"field",decorators:[(0,d.MZ)()],key:"mode",value:()=>"yaml"},{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[(0,d.MZ)({type:Boolean})],key:"autofocus",value:()=>!1},{kind:"field",decorators:[(0,d.MZ)({type:Boolean})],key:"readOnly",value:()=>!1},{kind:"field",decorators:[(0,d.MZ)({type:Boolean})],key:"linewrap",value:()=>!1},{kind:"field",decorators:[(0,d.MZ)({type:Boolean,attribute:"autocomplete-entities"})],key:"autocompleteEntities",value:()=>!1},{kind:"field",decorators:[(0,d.MZ)({type:Boolean,attribute:"autocomplete-icons"})],key:"autocompleteIcons",value:()=>!1},{kind:"field",decorators:[(0,d.MZ)({type:Boolean})],key:"error",value:()=>!1},{kind:"field",decorators:[(0,d.wk)()],key:"_value",value:()=>""},{kind:"field",key:"_loadedCodeMirror",value:void 0},{kind:"field",key:"_iconList",value:void 0},{kind:"set",key:"value",value:function(e){this._value=e}},{kind:"get",key:"value",value:function(){return this.codemirror?this.codemirror.state.doc.toString():this._value}},{kind:"get",key:"hasComments",value:function(){if(!this.codemirror||!this._loadedCodeMirror)return!1;const e=this._loadedCodeMirror.highlightingFor(this.codemirror.state,[this._loadedCodeMirror.tags.comment]);return!!this.renderRoot.querySelector(`span.${e}`)}},{kind:"method",key:"connectedCallback",value:function(){(0,r.A)((0,a.A)(i.prototype),"connectedCallback",this).call(this),this.hasUpdated&&this.requestUpdate(),this.addEventListener("keydown",c.d),this.codemirror&&!1!==this.autofocus&&this.codemirror.focus()}},{kind:"method",key:"disconnectedCallback",value:function(){(0,r.A)((0,a.A)(i.prototype),"disconnectedCallback",this).call(this),this.removeEventListener("keydown",c.d),this.updateComplete.then((()=>{this.codemirror.destroy(),delete this.codemirror}))}},{kind:"method",key:"scheduleUpdate",value:async function(){var e;null!==(e=this._loadedCodeMirror)&&void 0!==e||(this._loadedCodeMirror=await Promise.all([o.e(51859),o.e(380),o.e(24187),o.e(79881)]).then(o.bind(o,46054))),(0,r.A)((0,a.A)(i.prototype),"scheduleUpdate",this).call(this)}},{kind:"method",key:"update",value:function(e){if((0,r.A)((0,a.A)(i.prototype),"update",this).call(this,e),!this.codemirror)return void this._createCodeMirror();const t=[];e.has("mode")&&t.push({effects:this._loadedCodeMirror.langCompartment.reconfigure(this._mode)}),e.has("readOnly")&&t.push({effects:this._loadedCodeMirror.readonlyCompartment.reconfigure(this._loadedCodeMirror.EditorView.editable.of(!this.readOnly))}),e.has("linewrap")&&t.push({effects:this._loadedCodeMirror.linewrapCompartment.reconfigure(this.linewrap?this._loadedCodeMirror.EditorView.lineWrapping:[])}),e.has("_value")&&this._value!==this.value&&t.push({changes:{from:0,to:this.codemirror.state.doc.length,insert:this._value}}),t.length>0&&this.codemirror.dispatch(...t),e.has("error")&&this.classList.toggle("error-state",this.error)}},{kind:"get",key:"_mode",value:function(){return this._loadedCodeMirror.langs[this.mode]}},{kind:"method",key:"_createCodeMirror",value:function(){if(!this._loadedCodeMirror)throw new Error("Cannot create editor before CodeMirror is loaded");const e=[this._loadedCodeMirror.lineNumbers(),this._loadedCodeMirror.history(),this._loadedCodeMirror.drawSelection(),this._loadedCodeMirror.EditorState.allowMultipleSelections.of(!0),this._loadedCodeMirror.rectangularSelection(),this._loadedCodeMirror.crosshairCursor(),this._loadedCodeMirror.highlightSelectionMatches(),this._loadedCodeMirror.highlightActiveLine(),this._loadedCodeMirror.keymap.of([...this._loadedCodeMirror.defaultKeymap,...this._loadedCodeMirror.searchKeymap,...this._loadedCodeMirror.historyKeymap,...this._loadedCodeMirror.tabKeyBindings,h]),this._loadedCodeMirror.langCompartment.of(this._mode),this._loadedCodeMirror.haTheme,this._loadedCodeMirror.haSyntaxHighlighting,this._loadedCodeMirror.readonlyCompartment.of(this._loadedCodeMirror.EditorView.editable.of(!this.readOnly)),this._loadedCodeMirror.linewrapCompartment.of(this.linewrap?this._loadedCodeMirror.EditorView.lineWrapping:[]),this._loadedCodeMirror.EditorView.updateListener.of(this._onUpdate)];if(!this.readOnly){const t=[];this.autocompleteEntities&&this.hass&&t.push(this._entityCompletions.bind(this)),this.autocompleteIcons&&t.push(this._mdiCompletions.bind(this)),t.length>0&&e.push(this._loadedCodeMirror.autocompletion({override:t,maxRenderedOptions:10}))}this.codemirror=new this._loadedCodeMirror.EditorView({state:this._loadedCodeMirror.EditorState.create({doc:this._value,extensions:e}),parent:this.renderRoot})}},{kind:"field",key:"_getStates",value:()=>(0,n.A)((e=>{if(!e)return[];return Object.keys(e).map((t=>({type:"variable",label:t,detail:e[t].attributes.friendly_name,info:`State: ${e[t].state}`})))}))},{kind:"method",key:"_entityCompletions",value:function(e){const t=e.matchBefore(/[a-z_]{3,}\.\w*/);if(!t||t.from===t.to&&!e.explicit)return null;const o=this._getStates(this.hass.states);return o&&o.length?{from:Number(t.from),options:o,validFor:/^[a-z_]{3,}\.\w*$/}:null}},{kind:"field",key:"_getIconItems",value(){return async()=>{if(!this._iconList){let e;e=(await o.e(25143).then(o.t.bind(o,25143,19))).default,this._iconList=e.map((e=>({type:"variable",label:`mdi:${e.name}`,detail:e.keywords.join(", "),info:u})))}return this._iconList}}},{kind:"method",key:"_mdiCompletions",value:async function(e){const t=e.matchBefore(/mdi:\S*/);if(!t||t.from===t.to&&!e.explicit)return null;const o=await this._getIconItems();return{from:Number(t.from),options:o,validFor:/^mdi:\S*$/}}},{kind:"field",key:"_onUpdate",value(){return e=>{e.docChanged&&(this._value=e.state.doc.toString(),(0,l.r)(this,"value-changed",{value:this._value}))}}},{kind:"get",static:!0,key:"styles",value:function(){return s.AH`:host(.error-state) .cm-gutters{border-color:var(--error-state-color,red)}`}}]}}),s.mN)},95273:(e,t,o)=>{var i=o(62659),r=(o(21950),o(8339),o(91619)),a=o(80346),s=o(40924),d=o(18791);(0,i.A)([(0,d.EM)("ha-top-app-bar-fixed")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",static:!0,key:"styles",value:()=>[a.R,s.AH`.mdc-top-app-bar__row{height:var(--header-height);border-bottom:var(--app-header-border-bottom)}.mdc-top-app-bar--fixed-adjust{padding-top:var(--header-height)}.mdc-top-app-bar{--mdc-typography-headline6-font-weight:400;color:var(--app-header-text-color,var(--mdc-theme-on-primary,#fff));background-color:var(--app-header-background-color,var(--mdc-theme-primary))}.mdc-top-app-bar__title{padding-inline-start:20px;padding-inline-end:initial}`]}]}}),r.$)},77598:(e,t,o)=>{o.a(e,(async(e,i)=>{try{o.r(t);var r=o(62659),a=o(76504),s=o(80792),d=(o(21950),o(55888),o(8339),o(380)),n=(o(58068),o(47420)),l=o(40924),c=o(18791),h=o(69760),u=o(63428),p=o(61314),m=(o(4596),o(26250),o(12731),o(98876)),v=o(14126),g=o(75610),_=(o(95273),o(79861)),f=e([d]);d=(f.then?(await f)():f)[0];const y="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",k=(0,u.NW)({title:(0,u.lq)((0,u.Yj)()),views:(0,u.YO)((0,u.Ik)())}),b=(0,u.NW)({strategy:(0,u.NW)({type:(0,u.Yj)()})});(0,r.A)([(0,c.EM)("hui-editor")],(function(e,t){class o extends t{constructor(...t){super(...t),e(this)}}return{F:o,d:[{kind:"field",decorators:[(0,c.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,c.MZ)({attribute:!1})],key:"lovelace",value:void 0},{kind:"field",decorators:[(0,c.MZ)({attribute:!1})],key:"closeEditor",value:void 0},{kind:"field",decorators:[(0,c.wk)()],key:"_saving",value:void 0},{kind:"field",decorators:[(0,c.wk)()],key:"_changed",value:void 0},{kind:"method",key:"render",value:function(){return l.qy` <ha-top-app-bar-fixed> <ha-icon-button slot="navigationIcon" .path="${y}" @click="${this._closeEditor}" .label="${this.hass.localize("ui.common.close")}"></ha-icon-button> <div slot="title"> ${this.hass.localize("ui.panel.lovelace.editor.raw_editor.header")} </div> <div slot="actionItems" class="save-button ${(0,h.H)({saved:!1===this._saving||!0===this._changed})}"> ${this._changed?this.hass.localize("ui.panel.lovelace.editor.raw_editor.unsaved_changes"):this.hass.localize("ui.panel.lovelace.editor.raw_editor.saved")} </div> <mwc-button raised slot="actionItems" @click="${this._handleSave}" .disabled="${!this._changed}">${this.hass.localize("ui.panel.lovelace.editor.raw_editor.save")}</mwc-button> <div class="content"> <ha-code-editor mode="yaml" autofocus autocomplete-entities autocomplete-icons .hass="${this.hass}" @value-changed="${this._yamlChanged}" @editor-save="${this._handleSave}" dir="ltr"> </ha-code-editor> </div> </ha-top-app-bar-fixed> `}},{kind:"method",key:"firstUpdated",value:function(e){(0,a.A)((0,s.A)(o.prototype),"firstUpdated",this).call(this,e),this.yamlEditor.value=(0,n.dump)(this.lovelace.rawConfig)}},{kind:"method",key:"updated",value:function(e){const t=e.get("lovelace");!this._saving&&t&&this.lovelace&&t.rawConfig!==this.lovelace.rawConfig&&!(0,p.b)(t.rawConfig,this.lovelace.rawConfig)&&(0,g.P)(this,{message:this.hass.localize("ui.panel.lovelace.editor.raw_editor.lovelace_changed"),action:{action:()=>{this.yamlEditor.value=(0,n.dump)(this.lovelace.rawConfig)},text:this.hass.localize("ui.panel.lovelace.editor.raw_editor.reload")},duration:-1,dismissable:!1})}},{kind:"get",static:!0,key:"styles",value:function(){return[v.RF,l.AH`:host{--code-mirror-height:100%;--app-header-background-color:var(
            --app-header-edit-background-color,
            #455a64
          );--app-header-text-color:var(--app-header-edit-text-color, #fff)}mwc-button[disabled]{background-color:var(--mdc-theme-on-primary);border-radius:4px}.content{height:calc(100vh - var(--header-height))}.comments{font-size:16px}.save-button{opacity:0;font-size:14px;padding:0px 10px}.saved{opacity:1}`]}},{kind:"method",key:"_yamlChanged",value:function(){this._changed=(0,d.mk)(this.yamlEditor.codemirror.state)>0,this._changed&&!window.onbeforeunload?window.onbeforeunload=()=>!0:!this._changed&&window.onbeforeunload&&(window.onbeforeunload=null)}},{kind:"method",key:"_closeEditor",value:async function(){this._changed&&!await(0,m.showConfirmationDialog)(this,{text:this.hass.localize("ui.panel.lovelace.editor.raw_editor.confirm_unsaved_changes"),dismissText:this.hass.localize("ui.common.stay"),confirmText:this.hass.localize("ui.common.leave")})||(window.onbeforeunload=null,this.closeEditor&&this.closeEditor())}},{kind:"method",key:"_removeConfig",value:async function(){try{await this.lovelace.deleteConfig()}catch(e){(0,m.showAlertDialog)(this,{text:this.hass.localize("ui.panel.lovelace.editor.raw_editor.error_remove",{error:e})})}window.onbeforeunload=null,this.closeEditor&&this.closeEditor()}},{kind:"method",key:"_handleSave",value:async function(){this._saving=!0;const e=this.yamlEditor.value;if(!e)return void(0,m.showConfirmationDialog)(this,{title:this.hass.localize("ui.panel.lovelace.editor.raw_editor.confirm_remove_config_title"),text:this.hass.localize("ui.panel.lovelace.editor.raw_editor.confirm_remove_config_text"),confirmText:this.hass.localize("ui.common.remove"),dismissText:this.hass.localize("ui.common.cancel"),confirm:()=>this._removeConfig()});if(this.yamlEditor.hasComments&&!confirm(this.hass.localize("ui.panel.lovelace.editor.raw_editor.confirm_unsaved_comments")))return;let t;try{t=(0,n.load)(e)}catch(e){return(0,m.showAlertDialog)(this,{text:this.hass.localize("ui.panel.lovelace.editor.raw_editor.error_parse_yaml",{error:e})}),void(this._saving=!1)}try{(0,_.Wu)(t)?(0,u.vA)(t,b):(0,u.vA)(t,k)}catch(e){return void(0,m.showAlertDialog)(this,{text:this.hass.localize("ui.panel.lovelace.editor.raw_editor.error_invalid_config",{error:e})})}t.resources&&(0,m.showAlertDialog)(this,{text:this.hass.localize("ui.panel.lovelace.editor.raw_editor.resources_moved")});try{await this.lovelace.saveConfig(t)}catch(e){(0,m.showAlertDialog)(this,{text:this.hass.localize("ui.panel.lovelace.editor.raw_editor.error_save_yaml",{error:e})})}window.onbeforeunload=null,this._changed=!1,this._saving=!1}},{kind:"get",key:"yamlEditor",value:function(){return this.shadowRoot.querySelector("ha-code-editor")}}]}}),l.WF);i()}catch(e){i(e)}}))}};
//# sourceMappingURL=77598.Zib7piAMgVw.js.map