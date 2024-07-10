export const id=70120;export const ids=[70120,81998,12261,23141,59617];export const modules={33315:(t,e,o)=>{o.d(e,{a:()=>a});const i=(0,o(81053).n)((t=>{history.replaceState({scrollPosition:t},"")}),300),a=t=>e=>({kind:"method",placement:"prototype",key:e.key,descriptor:{set(t){i(t),this[`__${String(e.key)}`]=t},get(){var t;return this[`__${String(e.key)}`]||(null===(t=history.state)||void 0===t?void 0:t.scrollPosition)},enumerable:!0,configurable:!0},finisher(o){const i=o.prototype.connectedCallback;o.prototype.connectedCallback=function(){i.call(this);const o=this[e.key];o&&this.updateComplete.then((()=>{const e=this.renderRoot.querySelector(t);e&&setTimeout((()=>{e.scrollTop=o}),0)}))}}})},81053:(t,e,o)=>{o.d(e,{n:()=>i});o(21950),o(8339);const i=(t,e,o=!0,i=!0)=>{let a,r=0;const n=(...n)=>{const s=()=>{r=!1===o?0:Date.now(),a=void 0,t(...n)},l=Date.now();r||!1!==o||(r=l);const c=e-(l-r);c<=0||c>e?(a&&(clearTimeout(a),a=void 0),r=l,t(...n)):a||!1===i||(a=window.setTimeout(s,c))};return n.cancel=()=>{clearTimeout(a),a=void 0,r=0},n}},12261:(t,e,o)=>{o.r(e);var i=o(62659),a=(o(21950),o(8339),o(40924)),r=o(18791),n=o(69760),s=o(77664);o(12731),o(1683);const l={info:"M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z",warning:"M12,2L1,21H23M12,6L19.53,19H4.47M11,10V14H13V10M11,16V18H13V16",error:"M11,15H13V17H11V15M11,7H13V13H11V7M12,2C6.47,2 2,6.5 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20Z",success:"M20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4C12.76,4 13.5,4.11 14.2,4.31L15.77,2.74C14.61,2.26 13.34,2 12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12M7.91,10.08L6.5,11.5L11,16L21,6L19.59,4.58L11,13.17L7.91,10.08Z"};(0,i.A)([(0,r.EM)("ha-alert")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,r.MZ)()],key:"title",value:()=>""},{kind:"field",decorators:[(0,r.MZ)({attribute:"alert-type"})],key:"alertType",value:()=>"info"},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"dismissable",value:()=>!1},{kind:"method",key:"render",value:function(){return a.qy` <div class="issue-type ${(0,n.H)({[this.alertType]:!0})}" role="alert"> <div class="icon ${this.title?"":"no-title"}"> <slot name="icon"> <ha-svg-icon .path="${l[this.alertType]}"></ha-svg-icon> </slot> </div> <div class="content"> <div class="main-content"> ${this.title?a.qy`<div class="title">${this.title}</div>`:""} <slot></slot> </div> <div class="action"> <slot name="action"> ${this.dismissable?a.qy`<ha-icon-button @click="${this._dismiss_clicked}" label="Dismiss alert" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}"></ha-icon-button>`:""} </slot> </div> </div> </div> `}},{kind:"method",key:"_dismiss_clicked",value:function(){(0,s.r)(this,"alert-dismissed-clicked")}},{kind:"field",static:!0,key:"styles",value:()=>a.AH`.issue-type{position:relative;padding:8px;display:flex}.issue-type::after{position:absolute;top:0;right:0;bottom:0;left:0;opacity:.12;pointer-events:none;content:"";border-radius:4px}.icon{z-index:1}.icon.no-title{align-self:center}.content{display:flex;justify-content:space-between;align-items:center;width:100%;text-align:var(--float-start)}.action{z-index:1;width:min-content;--mdc-theme-primary:var(--primary-text-color)}.main-content{overflow-wrap:anywhere;word-break:break-word;margin-left:8px;margin-right:0;margin-inline-start:8px;margin-inline-end:0}.title{margin-top:2px;font-weight:700}.action ha-icon-button,.action mwc-button{--mdc-theme-primary:var(--primary-text-color);--mdc-icon-button-size:36px}.issue-type.info>.icon{color:var(--info-color)}.issue-type.info::after{background-color:var(--info-color)}.issue-type.warning>.icon{color:var(--warning-color)}.issue-type.warning::after{background-color:var(--warning-color)}.issue-type.error>.icon{color:var(--error-color)}.issue-type.error::after{background-color:var(--error-color)}.issue-type.success>.icon{color:var(--success-color)}.issue-type.success::after{background-color:var(--success-color)}:host ::slotted(ul){margin:0;padding-inline-start:20px}`}]}}),a.WF)},23141:(t,e,o)=>{o.r(e),o.d(e,{HaIconButtonArrowPrev:()=>s});var i=o(62659),a=(o(21950),o(8339),o(40924)),r=o(18791),n=o(51150);o(12731);let s=(0,i.A)([(0,r.EM)("ha-icon-button-arrow-prev")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_icon",value:()=>"rtl"===n.G.document.dir?"M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z":"M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"},{kind:"method",key:"render",value:function(){var t;return a.qy` <ha-icon-button .disabled="${this.disabled}" .label="${this.label||(null===(t=this.hass)||void 0===t?void 0:t.localize("ui.common.back"))||"Back"}" .path="${this._icon}"></ha-icon-button> `}}]}}),a.WF)},12731:(t,e,o)=>{o.r(e),o.d(e,{HaIconButton:()=>s});var i=o(62659),a=(o(21950),o(8339),o(25413),o(40924)),r=o(18791),n=o(79278);o(1683);let s=(0,i.A)([(0,r.EM)("ha-icon-button")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,r.MZ)({type:Boolean,reflect:!0})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:String})],key:"path",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:String})],key:"label",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:String,attribute:"aria-haspopup"})],key:"ariaHasPopup",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"hideTitle",value:()=>!1},{kind:"field",decorators:[(0,r.P)("mwc-icon-button",!0)],key:"_button",value:void 0},{kind:"method",key:"focus",value:function(){var t;null===(t=this._button)||void 0===t||t.focus()}},{kind:"field",static:!0,key:"shadowRootOptions",value:()=>({mode:"open",delegatesFocus:!0})},{kind:"method",key:"render",value:function(){return a.qy` <mwc-icon-button aria-label="${(0,n.J)(this.label)}" title="${(0,n.J)(this.hideTitle?void 0:this.label)}" aria-haspopup="${(0,n.J)(this.ariaHasPopup)}" .disabled="${this.disabled}"> ${this.path?a.qy`<ha-svg-icon .path="${this.path}"></ha-svg-icon>`:a.qy`<slot></slot>`} </mwc-icon-button> `}},{kind:"get",static:!0,key:"styles",value:function(){return a.AH`:host{display:inline-block;outline:0}:host([disabled]){pointer-events:none}mwc-icon-button{--mdc-theme-on-primary:currentColor;--mdc-theme-text-disabled-on-light:var(--disabled-text-color)}`}}]}}),a.WF)},78361:(t,e,o)=>{var i=o(62659),a=o(76504),r=o(80792),n=(o(27934),o(21950),o(8339),o(40924)),s=o(18791),l=o(77664),c=o(82188);o(12731);(0,i.A)([(0,s.EM)("ha-menu-button")],(function(t,e){class o extends e{constructor(...e){super(...e),t(this)}}return{F:o,d:[{kind:"field",decorators:[(0,s.MZ)({type:Boolean})],key:"hassio",value:()=>!1},{kind:"field",decorators:[(0,s.MZ)({type:Boolean})],key:"narrow",value:()=>!1},{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.wk)()],key:"_hasNotifications",value:()=>!1},{kind:"field",decorators:[(0,s.wk)()],key:"_show",value:()=>!1},{kind:"field",key:"_alwaysVisible",value:()=>!1},{kind:"field",key:"_attachNotifOnConnect",value:()=>!1},{kind:"field",key:"_unsubNotifications",value:void 0},{kind:"method",key:"connectedCallback",value:function(){(0,a.A)((0,r.A)(o.prototype),"connectedCallback",this).call(this),this._attachNotifOnConnect&&(this._attachNotifOnConnect=!1,this._subscribeNotifications())}},{kind:"method",key:"disconnectedCallback",value:function(){(0,a.A)((0,r.A)(o.prototype),"disconnectedCallback",this).call(this),this._unsubNotifications&&(this._attachNotifOnConnect=!0,this._unsubNotifications(),this._unsubNotifications=void 0)}},{kind:"method",key:"render",value:function(){if(!this._show)return n.s6;const t=this._hasNotifications&&(this.narrow||"always_hidden"===this.hass.dockedSidebar);return n.qy` <ha-icon-button .label="${this.hass.localize("ui.sidebar.sidebar_toggle")}" .path="${"M3,6H21V8H3V6M3,11H21V13H3V11M3,16H21V18H3V16Z"}" @click="${this._toggleMenu}"></ha-icon-button> ${t?n.qy`<div class="dot"></div>`:""} `}},{kind:"method",key:"firstUpdated",value:function(t){(0,a.A)((0,r.A)(o.prototype),"firstUpdated",this).call(this,t),this.hassio&&(this._alwaysVisible=(Number(window.parent.frontendVersion)||0)<20190710)}},{kind:"method",key:"willUpdate",value:function(t){if((0,a.A)((0,r.A)(o.prototype),"willUpdate",this).call(this,t),!t.has("narrow")&&!t.has("hass"))return;const e=t.has("hass")?t.get("hass"):this.hass,i=(t.has("narrow")?t.get("narrow"):this.narrow)||"always_hidden"===(null==e?void 0:e.dockedSidebar),n=this.narrow||"always_hidden"===this.hass.dockedSidebar;this.hasUpdated&&i===n||(this._show=n||this._alwaysVisible,n?this._subscribeNotifications():this._unsubNotifications&&(this._unsubNotifications(),this._unsubNotifications=void 0))}},{kind:"method",key:"_subscribeNotifications",value:function(){if(this._unsubNotifications)throw new Error("Already subscribed");this._unsubNotifications=(0,c.V)(this.hass.connection,(t=>{this._hasNotifications=t.length>0}))}},{kind:"method",key:"_toggleMenu",value:function(){(0,l.r)(this,"hass-toggle-menu")}},{kind:"get",static:!0,key:"styles",value:function(){return n.AH`:host{position:relative}.dot{pointer-events:none;position:absolute;background-color:var(--accent-color);width:12px;height:12px;top:9px;right:7px;inset-inline-end:7px;inset-inline-start:initial;border-radius:50%;border:2px solid var(--app-header-background-color)}`}}]}}),n.WF)},1683:(t,e,o)=>{o.r(e),o.d(e,{HaSvgIcon:()=>n});var i=o(62659),a=(o(21950),o(8339),o(40924)),r=o(18791);let n=(0,i.A)([(0,r.EM)("ha-svg-icon")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,r.MZ)()],key:"path",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"secondaryPath",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"viewBox",value:void 0},{kind:"method",key:"render",value:function(){return a.JW` <svg viewBox="${this.viewBox||"0 0 24 24"}" preserveAspectRatio="xMidYMid meet" focusable="false" role="img" aria-hidden="true"> <g> ${this.path?a.JW`<path class="primary-path" d="${this.path}"></path>`:a.s6} ${this.secondaryPath?a.JW`<path class="secondary-path" d="${this.secondaryPath}"></path>`:a.s6} </g> </svg>`}},{kind:"get",static:!0,key:"styles",value:function(){return a.AH`:host{display:var(--ha-icon-display,inline-flex);align-items:center;justify-content:center;position:relative;vertical-align:middle;fill:var(--icon-primary-color,currentcolor);width:var(--mdc-icon-size,24px);height:var(--mdc-icon-size,24px)}svg{width:100%;height:100%;pointer-events:none;display:block}path.primary-path{opacity:var(--icon-primary-opactity, 1)}path.secondary-path{fill:var(--icon-secondary-color,currentcolor);opacity:var(--icon-secondary-opactity, .5)}`}}]}}),a.WF)},82188:(t,e,o)=>{o.d(e,{V:()=>i});o(21950),o(8339);const i=(t,e)=>{const o=new a,i=t.subscribeMessage((t=>e(o.processMessage(t))),{type:"persistent_notification/subscribe"});return()=>{i.then((t=>null==t?void 0:t()))}};class a{constructor(){this.notifications=void 0,this.notifications={}}processMessage(t){if("removed"===t.type)for(const e of Object.keys(t.notifications))delete this.notifications[e];else this.notifications={...this.notifications,...t.notifications};return Object.values(this.notifications)}}},59617:(t,e,o)=>{o.r(e);var i=o(62659),a=(o(21950),o(8339),o(58068),o(40924)),r=o(18791);o(23141),o(78361),o(12261);(0,i.A)([(0,r.EM)("hass-error-screen")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"toolbar",value:()=>!0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"rootnav",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"narrow",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)()],key:"error",value:void 0},{kind:"method",key:"render",value:function(){var t,e;return a.qy` ${this.toolbar?a.qy`<div class="toolbar"> ${this.rootnav||null!==(t=history.state)&&void 0!==t&&t.root?a.qy` <ha-menu-button .hass="${this.hass}" .narrow="${this.narrow}"></ha-menu-button> `:a.qy` <ha-icon-button-arrow-prev .hass="${this.hass}" @click="${this._handleBack}"></ha-icon-button-arrow-prev> `} </div>`:""} <div class="content"> <ha-alert alert-type="error">${this.error}</ha-alert> <slot> <mwc-button @click="${this._handleBack}"> ${null===(e=this.hass)||void 0===e?void 0:e.localize("ui.common.back")} </mwc-button> </slot> </div> `}},{kind:"method",key:"_handleBack",value:function(){history.back()}},{kind:"get",static:!0,key:"styles",value:function(){return[a.AH`:host{display:block;height:100%;background-color:var(--primary-background-color)}.toolbar{display:flex;align-items:center;font-size:20px;height:var(--header-height);padding:8px 12px;pointer-events:none;background-color:var(--app-header-background-color);font-weight:400;color:var(--app-header-text-color,#fff);border-bottom:var(--app-header-border-bottom,none);box-sizing:border-box}@media (max-width:599px){.toolbar{padding:4px}}ha-icon-button-arrow-prev{pointer-events:auto}.content{color:var(--primary-text-color);height:calc(100% - var(--header-height));display:flex;padding:16px;align-items:center;justify-content:center;flex-direction:column;box-sizing:border-box}a{color:var(--primary-color)}ha-alert{margin-bottom:16px}`]}}]}}),a.WF)},52287:(t,e,o)=>{var i=o(62659),a=(o(21950),o(8339),o(40924)),r=o(18791),n=o(33315),s=(o(23141),o(78361),o(14126));(0,i.A)([(0,r.EM)("hass-subpage")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"header",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean,attribute:"main-page"})],key:"mainPage",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:String,attribute:"back-path"})],key:"backPath",value:void 0},{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"backCallback",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean,reflect:!0})],key:"narrow",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"supervisor",value:()=>!1},{kind:"field",decorators:[(0,n.a)(".content")],key:"_savedScrollPos",value:void 0},{kind:"method",key:"render",value:function(){var t;return a.qy` <div class="toolbar"> ${this.mainPage||null!==(t=history.state)&&void 0!==t&&t.root?a.qy` <ha-menu-button .hassio="${this.supervisor}" .hass="${this.hass}" .narrow="${this.narrow}"></ha-menu-button> `:this.backPath?a.qy` <a href="${this.backPath}"> <ha-icon-button-arrow-prev .hass="${this.hass}"></ha-icon-button-arrow-prev> </a> `:a.qy` <ha-icon-button-arrow-prev .hass="${this.hass}" @click="${this._backTapped}"></ha-icon-button-arrow-prev> `} <div class="main-title"><slot name="header">${this.header}</slot></div> <slot name="toolbar-icon"></slot> </div> <div class="content ha-scrollbar" @scroll="${this._saveScrollPos}"> <slot></slot> </div> <div id="fab"> <slot name="fab"></slot> </div> `}},{kind:"method",decorators:[(0,r.Ls)({passive:!0})],key:"_saveScrollPos",value:function(t){this._savedScrollPos=t.target.scrollTop}},{kind:"method",key:"_backTapped",value:function(){this.backCallback?this.backCallback():history.back()}},{kind:"get",static:!0,key:"styles",value:function(){return[s.dp,a.AH`:host{display:block;height:100%;background-color:var(--primary-background-color);overflow:hidden;position:relative}:host([narrow]){width:100%;position:fixed}.toolbar{display:flex;align-items:center;font-size:20px;height:var(--header-height);padding:8px 12px;background-color:var(--app-header-background-color);font-weight:400;color:var(--app-header-text-color,#fff);border-bottom:var(--app-header-border-bottom,none);box-sizing:border-box}@media (max-width:599px){.toolbar{padding:4px}}.toolbar a{color:var(--sidebar-text-color);text-decoration:none}::slotted([slot=toolbar-icon]),ha-icon-button-arrow-prev,ha-menu-button{pointer-events:auto;color:var(--sidebar-icon-color)}.main-title{margin:var(--margin-title);line-height:20px;flex-grow:1}.content{position:relative;width:100%;height:calc(100% - 1px - var(--header-height));overflow-y:auto;overflow:auto;-webkit-overflow-scrolling:touch}#fab{position:absolute;right:calc(16px + env(safe-area-inset-right));inset-inline-end:calc(16px + env(safe-area-inset-right));inset-inline-start:initial;bottom:calc(16px + env(safe-area-inset-bottom));z-index:1;display:flex;flex-wrap:wrap;justify-content:flex-end;gap:8px}:host([narrow]) #fab.tabs{bottom:calc(84px + env(safe-area-inset-bottom))}#fab[is-wide]{bottom:24px;right:24px;inset-inline-end:24px;inset-inline-start:initial}`]}}]}}),a.WF)},70120:(t,e,o)=>{o.r(e);var i=o(62659),a=(o(21950),o(8339),o(29734),o(72134),o(7146),o(97157),o(56648),o(72435),o(40924)),r=o(18791),n=o(79278),s=(o(59617),o(52287),o(74541));(0,i.A)([(0,r.EM)("ha-panel-iframe")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"narrow",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"panel",value:void 0},{kind:"method",key:"render",value:function(){return"https:"===location.protocol&&"https:"!==new URL(this.panel.config.url,location.toString()).protocol?a.qy` <hass-error-screen .hass="${this.hass}" .narrow="${this.narrow}" error="Unable to load iframes that load websites over http:// if Home Assistant is served over https://." rootnav></hass-error-screen> `:a.qy` <hass-subpage .hass="${this.hass}" .narrow="${this.narrow}" .header="${this.panel.title}" main-page> <iframe title="${(0,n.J)(null===this.panel.title?void 0:this.panel.title)}" src="${this.panel.config.url}" .sandbox="${s.D}" allow="fullscreen"></iframe> </hass-subpage> `}},{kind:"field",static:!0,key:"styles",value:()=>a.AH`iframe{border:0;width:100%;position:absolute;height:100%;background-color:var(--primary-background-color)}`}]}}),a.WF)},14126:(t,e,o)=>{o.d(e,{RF:()=>r,dp:()=>s,nA:()=>n,og:()=>a});var i=o(40924);const a=i.AH`button.link{background:0 0;color:inherit;border:none;padding:0;font:inherit;text-align:left;text-decoration:underline;cursor:pointer;outline:0}`,r=i.AH`:host{font-family:var(--paper-font-body1_-_font-family);-webkit-font-smoothing:var(--paper-font-body1_-_-webkit-font-smoothing);font-size:var(--paper-font-body1_-_font-size);font-weight:var(--paper-font-body1_-_font-weight);line-height:var(--paper-font-body1_-_line-height)}app-header div[sticky]{height:48px}app-toolbar [main-title]{margin-left:20px;margin-inline-start:20px;margin-inline-end:initial}h1{font-family:var(--paper-font-headline_-_font-family);-webkit-font-smoothing:var(--paper-font-headline_-_-webkit-font-smoothing);white-space:var(--paper-font-headline_-_white-space);overflow:var(--paper-font-headline_-_overflow);text-overflow:var(--paper-font-headline_-_text-overflow);font-size:var(--paper-font-headline_-_font-size);font-weight:var(--paper-font-headline_-_font-weight);line-height:var(--paper-font-headline_-_line-height)}h2{font-family:var(--paper-font-title_-_font-family);-webkit-font-smoothing:var(--paper-font-title_-_-webkit-font-smoothing);white-space:var(--paper-font-title_-_white-space);overflow:var(--paper-font-title_-_overflow);text-overflow:var(--paper-font-title_-_text-overflow);font-size:var(--paper-font-title_-_font-size);font-weight:var(--paper-font-title_-_font-weight);line-height:var(--paper-font-title_-_line-height)}h3{font-family:var(--paper-font-subhead_-_font-family);-webkit-font-smoothing:var(--paper-font-subhead_-_-webkit-font-smoothing);white-space:var(--paper-font-subhead_-_white-space);overflow:var(--paper-font-subhead_-_overflow);text-overflow:var(--paper-font-subhead_-_text-overflow);font-size:var(--paper-font-subhead_-_font-size);font-weight:var(--paper-font-subhead_-_font-weight);line-height:var(--paper-font-subhead_-_line-height)}a{color:var(--primary-color)}.secondary{color:var(--secondary-text-color)}.error{color:var(--error-color)}.warning{color:var(--error-color)}ha-button.warning,mwc-button.warning{--mdc-theme-primary:var(--error-color)}${a} .card-actions a{text-decoration:none}.card-actions .warning{--mdc-theme-primary:var(--error-color)}.layout.horizontal,.layout.vertical{display:flex}.layout.inline{display:inline-flex}.layout.horizontal{flex-direction:row}.layout.vertical{flex-direction:column}.layout.wrap{flex-wrap:wrap}.layout.no-wrap{flex-wrap:nowrap}.layout.center,.layout.center-center{align-items:center}.layout.bottom{align-items:flex-end}.layout.center-center,.layout.center-justified{justify-content:center}.flex{flex:1;flex-basis:0.000000001px}.flex-auto{flex:1 1 auto}.flex-none{flex:none}.layout.justified{justify-content:space-between}`,n=i.AH`ha-dialog{--mdc-dialog-min-width:400px;--mdc-dialog-max-width:600px;--mdc-dialog-max-width:min(600px, 95vw);--justify-action-buttons:space-between}ha-dialog .form{color:var(--primary-text-color)}a{color:var(--primary-color)}@media all and (max-width:450px),all and (max-height:500px){ha-dialog{--mdc-dialog-min-width:calc(
        100vw - env(safe-area-inset-right) - env(safe-area-inset-left)
      );--mdc-dialog-max-width:calc(
        100vw - env(safe-area-inset-right) - env(safe-area-inset-left)
      );--mdc-dialog-min-height:100%;--mdc-dialog-max-height:100%;--vertical-align-dialog:flex-end;--ha-dialog-border-radius:0}}ha-button.warning,mwc-button.warning{--mdc-theme-primary:var(--error-color)}.error{color:var(--error-color)}`,s=i.AH`.ha-scrollbar::-webkit-scrollbar{width:.4rem;height:.4rem}.ha-scrollbar::-webkit-scrollbar-thumb{-webkit-border-radius:4px;border-radius:4px;background:var(--scrollbar-thumb-color)}.ha-scrollbar{overflow-y:auto;scrollbar-color:var(--scrollbar-thumb-color) transparent;scrollbar-width:thin}`;i.AH`body{background-color:var(--primary-background-color);color:var(--primary-text-color);height:calc(100vh - 32px);width:100vw}`},74541:(t,e,o)=>{o.d(e,{D:()=>i});const i="allow-forms allow-popups allow-pointer-lock allow-same-origin allow-scripts allow-modals allow-downloads"}};
//# sourceMappingURL=70120.0wkw840J7Cg.js.map