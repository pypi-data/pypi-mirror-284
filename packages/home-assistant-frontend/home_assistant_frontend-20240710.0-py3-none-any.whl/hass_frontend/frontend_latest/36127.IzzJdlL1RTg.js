export const id=36127;export const ids=[36127,12261];export const modules={12261:(e,t,i)=>{i.r(t);var o=i(62659),a=(i(21950),i(8339),i(40924)),n=i(18791),r=i(69760),s=i(77664);i(12731),i(1683);const l={info:"M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z",warning:"M12,2L1,21H23M12,6L19.53,19H4.47M11,10V14H13V10M11,16V18H13V16",error:"M11,15H13V17H11V15M11,7H13V13H11V7M12,2C6.47,2 2,6.5 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20Z",success:"M20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4C12.76,4 13.5,4.11 14.2,4.31L15.77,2.74C14.61,2.26 13.34,2 12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12M7.91,10.08L6.5,11.5L11,16L21,6L19.59,4.58L11,13.17L7.91,10.08Z"};(0,o.A)([(0,n.EM)("ha-alert")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.MZ)()],key:"title",value:()=>""},{kind:"field",decorators:[(0,n.MZ)({attribute:"alert-type"})],key:"alertType",value:()=>"info"},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"dismissable",value:()=>!1},{kind:"method",key:"render",value:function(){return a.qy` <div class="issue-type ${(0,r.H)({[this.alertType]:!0})}" role="alert"> <div class="icon ${this.title?"":"no-title"}"> <slot name="icon"> <ha-svg-icon .path="${l[this.alertType]}"></ha-svg-icon> </slot> </div> <div class="content"> <div class="main-content"> ${this.title?a.qy`<div class="title">${this.title}</div>`:""} <slot></slot> </div> <div class="action"> <slot name="action"> ${this.dismissable?a.qy`<ha-icon-button @click="${this._dismiss_clicked}" label="Dismiss alert" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}"></ha-icon-button>`:""} </slot> </div> </div> </div> `}},{kind:"method",key:"_dismiss_clicked",value:function(){(0,s.r)(this,"alert-dismissed-clicked")}},{kind:"field",static:!0,key:"styles",value:()=>a.AH`.issue-type{position:relative;padding:8px;display:flex}.issue-type::after{position:absolute;top:0;right:0;bottom:0;left:0;opacity:.12;pointer-events:none;content:"";border-radius:4px}.icon{z-index:1}.icon.no-title{align-self:center}.content{display:flex;justify-content:space-between;align-items:center;width:100%;text-align:var(--float-start)}.action{z-index:1;width:min-content;--mdc-theme-primary:var(--primary-text-color)}.main-content{overflow-wrap:anywhere;word-break:break-word;margin-left:8px;margin-right:0;margin-inline-start:8px;margin-inline-end:0}.title{margin-top:2px;font-weight:700}.action ha-icon-button,.action mwc-button{--mdc-theme-primary:var(--primary-text-color);--mdc-icon-button-size:36px}.issue-type.info>.icon{color:var(--info-color)}.issue-type.info::after{background-color:var(--info-color)}.issue-type.warning>.icon{color:var(--warning-color)}.issue-type.warning::after{background-color:var(--warning-color)}.issue-type.error>.icon{color:var(--error-color)}.issue-type.error::after{background-color:var(--error-color)}.issue-type.success>.icon{color:var(--success-color)}.issue-type.success::after{background-color:var(--success-color)}:host ::slotted(ul){margin:0;padding-inline-start:20px}`}]}}),a.WF)},35641:(e,t,i)=>{i.a(e,(async(e,t)=>{try{var o=i(62659),a=i(76504),n=i(80792),r=(i(21950),i(55888),i(66274),i(84531),i(8339),i(54854)),s=i(66505),l=i(45584),d=i(40924),c=i(18791),h=i(79278),u=i(77664),v=(i(12731),i(39335),i(42398),e([s]));s=(v.then?(await v)():v)[0];const p="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",y="M7,10L12,15L17,10H7Z",m="M7,15L12,10L17,15H7Z";(0,l.SF)("vaadin-combo-box-item",d.AH`:host{padding:0!important}:host([focused]:not([disabled])){background-color:rgba(var(--rgb-primary-text-color,0,0,0),.12)}:host([selected]:not([disabled])){background-color:transparent;color:var(--mdc-theme-primary);--mdc-ripple-color:var(--mdc-theme-primary);--mdc-theme-text-primary-on-background:var(--mdc-theme-primary)}:host([selected]:not([disabled])):before{background-color:var(--mdc-theme-primary);opacity:.12;content:"";position:absolute;top:0;left:0;width:100%;height:100%}:host([selected][focused]:not([disabled])):before{opacity:.24}:host(:hover:not([disabled])){background-color:transparent}[part=content]{width:100%}[part=checkmark]{display:none}`);(0,o.A)([(0,c.EM)("ha-combo-box")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,c.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,c.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,c.MZ)()],key:"value",value:void 0},{kind:"field",decorators:[(0,c.MZ)()],key:"placeholder",value:void 0},{kind:"field",decorators:[(0,c.MZ)()],key:"validationMessage",value:void 0},{kind:"field",decorators:[(0,c.MZ)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,c.MZ)({attribute:"error-message"})],key:"errorMessage",value:void 0},{kind:"field",decorators:[(0,c.MZ)({type:Boolean})],key:"invalid",value:()=>!1},{kind:"field",decorators:[(0,c.MZ)({type:Boolean})],key:"icon",value:()=>!1},{kind:"field",decorators:[(0,c.MZ)({attribute:!1})],key:"items",value:void 0},{kind:"field",decorators:[(0,c.MZ)({attribute:!1})],key:"filteredItems",value:void 0},{kind:"field",decorators:[(0,c.MZ)({attribute:!1})],key:"dataProvider",value:void 0},{kind:"field",decorators:[(0,c.MZ)({attribute:"allow-custom-value",type:Boolean})],key:"allowCustomValue",value:()=>!1},{kind:"field",decorators:[(0,c.MZ)({attribute:"item-value-path"})],key:"itemValuePath",value:()=>"value"},{kind:"field",decorators:[(0,c.MZ)({attribute:"item-label-path"})],key:"itemLabelPath",value:()=>"label"},{kind:"field",decorators:[(0,c.MZ)({attribute:"item-id-path"})],key:"itemIdPath",value:void 0},{kind:"field",decorators:[(0,c.MZ)({attribute:!1})],key:"renderer",value:void 0},{kind:"field",decorators:[(0,c.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,c.MZ)({type:Boolean})],key:"required",value:()=>!1},{kind:"field",decorators:[(0,c.MZ)({type:Boolean,reflect:!0})],key:"opened",value:()=>!1},{kind:"field",decorators:[(0,c.P)("vaadin-combo-box-light",!0)],key:"_comboBox",value:void 0},{kind:"field",decorators:[(0,c.P)("ha-textfield",!0)],key:"_inputElement",value:void 0},{kind:"field",key:"_overlayMutationObserver",value:void 0},{kind:"field",key:"_bodyMutationObserver",value:void 0},{kind:"method",key:"open",value:async function(){var e;await this.updateComplete,null===(e=this._comboBox)||void 0===e||e.open()}},{kind:"method",key:"focus",value:async function(){var e,t;await this.updateComplete,await(null===(e=this._inputElement)||void 0===e?void 0:e.updateComplete),null===(t=this._inputElement)||void 0===t||t.focus()}},{kind:"method",key:"disconnectedCallback",value:function(){(0,a.A)((0,n.A)(i.prototype),"disconnectedCallback",this).call(this),this._overlayMutationObserver&&(this._overlayMutationObserver.disconnect(),this._overlayMutationObserver=void 0),this._bodyMutationObserver&&(this._bodyMutationObserver.disconnect(),this._bodyMutationObserver=void 0)}},{kind:"get",key:"selectedItem",value:function(){return this._comboBox.selectedItem}},{kind:"method",key:"setInputValue",value:function(e){this._comboBox.value=e}},{kind:"method",key:"render",value:function(){var e;return d.qy` <vaadin-combo-box-light .itemValuePath="${this.itemValuePath}" .itemIdPath="${this.itemIdPath}" .itemLabelPath="${this.itemLabelPath}" .items="${this.items}" .value="${this.value||""}" .filteredItems="${this.filteredItems}" .dataProvider="${this.dataProvider}" .allowCustomValue="${this.allowCustomValue}" .disabled="${this.disabled}" .required="${this.required}" ${(0,r.d)(this.renderer||this._defaultRowRenderer)} @opened-changed="${this._openedChanged}" @filter-changed="${this._filterChanged}" @value-changed="${this._valueChanged}" attr-for-value="value"> <ha-textfield label="${(0,h.J)(this.label)}" placeholder="${(0,h.J)(this.placeholder)}" ?disabled="${this.disabled}" ?required="${this.required}" validationMessage="${(0,h.J)(this.validationMessage)}" .errorMessage="${this.errorMessage}" class="input" autocapitalize="none" autocomplete="off" autocorrect="off" input-spellcheck="false" .suffix="${d.qy`<div style="width:28px" role="none presentation"></div>`}" .icon="${this.icon}" .invalid="${this.invalid}" .helper="${this.helper}" helperPersistent> <slot name="icon" slot="leadingIcon"></slot> </ha-textfield> ${this.value?d.qy`<ha-svg-icon role="button" tabindex="-1" aria-label="${(0,h.J)(null===(e=this.hass)||void 0===e?void 0:e.localize("ui.common.clear"))}" class="clear-button" .path="${p}" @click="${this._clearValue}"></ha-svg-icon>`:""} <ha-svg-icon role="button" tabindex="-1" aria-label="${(0,h.J)(this.label)}" aria-expanded="${this.opened?"true":"false"}" class="toggle-button" .path="${this.opened?m:y}" @click="${this._toggleOpen}"></ha-svg-icon> </vaadin-combo-box-light> `}},{kind:"field",key:"_defaultRowRenderer",value(){return e=>d.qy`<ha-list-item> ${this.itemLabelPath?e[this.itemLabelPath]:e} </ha-list-item>`}},{kind:"method",key:"_clearValue",value:function(e){e.stopPropagation(),(0,u.r)(this,"value-changed",{value:void 0})}},{kind:"method",key:"_toggleOpen",value:function(e){var t,i;this.opened?(null===(t=this._comboBox)||void 0===t||t.close(),e.stopPropagation()):null===(i=this._comboBox)||void 0===i||i.inputElement.focus()}},{kind:"method",key:"_openedChanged",value:function(e){e.stopPropagation();const t=e.detail.value;if(setTimeout((()=>{this.opened=t}),0),(0,u.r)(this,"opened-changed",{value:e.detail.value}),t){const e=document.querySelector("vaadin-combo-box-overlay");e&&this._removeInert(e),this._observeBody()}else{var i;null===(i=this._bodyMutationObserver)||void 0===i||i.disconnect(),this._bodyMutationObserver=void 0}}},{kind:"method",key:"_observeBody",value:function(){"MutationObserver"in window&&!this._bodyMutationObserver&&(this._bodyMutationObserver=new MutationObserver((e=>{e.forEach((e=>{e.addedNodes.forEach((e=>{"VAADIN-COMBO-BOX-OVERLAY"===e.nodeName&&this._removeInert(e)})),e.removedNodes.forEach((e=>{var t;"VAADIN-COMBO-BOX-OVERLAY"===e.nodeName&&(null===(t=this._overlayMutationObserver)||void 0===t||t.disconnect(),this._overlayMutationObserver=void 0)}))}))})),this._bodyMutationObserver.observe(document.body,{childList:!0}))}},{kind:"method",key:"_removeInert",value:function(e){var t;if(e.inert)return e.inert=!1,null===(t=this._overlayMutationObserver)||void 0===t||t.disconnect(),void(this._overlayMutationObserver=void 0);"MutationObserver"in window&&!this._overlayMutationObserver&&(this._overlayMutationObserver=new MutationObserver((e=>{e.forEach((e=>{if("inert"===e.attributeName){const i=e.target;var t;if(i.inert)null===(t=this._overlayMutationObserver)||void 0===t||t.disconnect(),this._overlayMutationObserver=void 0,i.inert=!1}}))})),this._overlayMutationObserver.observe(e,{attributes:!0}))}},{kind:"method",key:"_filterChanged",value:function(e){e.stopPropagation(),(0,u.r)(this,"filter-changed",{value:e.detail.value})}},{kind:"method",key:"_valueChanged",value:function(e){e.stopPropagation(),this.allowCustomValue||(this._comboBox._closeOnBlurIsPrevented=!0);const t=e.detail.value;t!==this.value&&(0,u.r)(this,"value-changed",{value:t||void 0})}},{kind:"get",static:!0,key:"styles",value:function(){return d.AH`:host{display:block;width:100%}vaadin-combo-box-light{position:relative;--vaadin-combo-box-overlay-max-height:calc(45vh - 56px)}ha-textfield{width:100%}ha-textfield>ha-icon-button{--mdc-icon-button-size:24px;padding:2px;color:var(--secondary-text-color)}ha-svg-icon{color:var(--input-dropdown-icon-color);position:absolute;cursor:pointer}.toggle-button{right:12px;top:-10px;inset-inline-start:initial;inset-inline-end:12px;direction:var(--direction)}:host([opened]) .toggle-button{color:var(--primary-color)}.clear-button{--mdc-icon-size:20px;top:-7px;right:36px;inset-inline-start:initial;inset-inline-end:36px;direction:var(--direction)}`}}]}}),d.WF);t()}catch(e){t(e)}}))},57225:(e,t,i)=>{i.a(e,(async(e,o)=>{try{i.r(t),i.d(t,{HaIconPicker:()=>f});var a=i(62659),n=(i(53501),i(21950),i(71936),i(14460),i(55888),i(66274),i(85038),i(84531),i(98168),i(22836),i(15445),i(24483),i(13478),i(46355),i(14612),i(53691),i(48455),i(8339),i(40924)),r=i(18791),s=i(45081),l=i(77664),d=i(95866),c=i(35641),h=(i(39335),i(57780),e([c]));c=(h.then?(await h)():h)[0];let u=[],v=!1;const p=async()=>{v=!0;const e=await i.e(25143).then(i.t.bind(i,25143,19));u=e.default.map((e=>({icon:`mdi:${e.name}`,parts:new Set(e.name.split("-")),keywords:e.keywords})));const t=[];Object.keys(d.y).forEach((e=>{t.push(y(e))})),(await Promise.all(t)).forEach((e=>{u.push(...e)}))},y=async e=>{try{const t=d.y[e].getIconList;if("function"!=typeof t)return[];const i=await t();return i.map((t=>{var i;return{icon:`${e}:${t.name}`,parts:new Set(t.name.split("-")),keywords:null!==(i=t.keywords)&&void 0!==i?i:[]}}))}catch(t){return console.warn(`Unable to load icon list for ${e} iconset`),[]}},m=e=>n.qy`<ha-list-item graphic="avatar"> <ha-icon .icon="${e.icon}" slot="graphic"></ha-icon> ${e.icon} </ha-list-item>`;let f=(0,a.A)([(0,r.EM)("ha-icon-picker")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"value",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,r.MZ)()],key:"placeholder",value:void 0},{kind:"field",decorators:[(0,r.MZ)({attribute:"error-message"})],key:"errorMessage",value:void 0},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"required",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"invalid",value:()=>!1},{kind:"method",key:"render",value:function(){return n.qy` <ha-combo-box .hass="${this.hass}" item-value-path="icon" item-label-path="icon" .value="${this._value}" allow-custom-value .dataProvider="${v?this._iconProvider:void 0}" .label="${this.label}" .helper="${this.helper}" .disabled="${this.disabled}" .required="${this.required}" .placeholder="${this.placeholder}" .errorMessage="${this.errorMessage}" .invalid="${this.invalid}" .renderer="${m}" icon @opened-changed="${this._openedChanged}" @value-changed="${this._valueChanged}"> ${this._value||this.placeholder?n.qy` <ha-icon .icon="${this._value||this.placeholder}" slot="icon"> </ha-icon> `:n.qy`<slot slot="icon" name="fallback"></slot>`} </ha-combo-box> `}},{kind:"field",key:"_filterIcons",value:()=>(0,s.A)(((e,t=u)=>{if(!e)return t;const i=[],o=(e,t)=>i.push({icon:e,rank:t});for(const i of t)i.parts.has(e)?o(i.icon,1):i.keywords.includes(e)?o(i.icon,2):i.icon.includes(e)?o(i.icon,3):i.keywords.some((t=>t.includes(e)))&&o(i.icon,4);return 0===i.length&&o(e,0),i.sort(((e,t)=>e.rank-t.rank))}))},{kind:"field",key:"_iconProvider",value(){return(e,t)=>{const i=this._filterIcons(e.filter.toLowerCase(),u),o=e.page*e.pageSize,a=o+e.pageSize;t(i.slice(o,a),i.length)}}},{kind:"method",key:"_openedChanged",value:async function(e){e.detail.value&&!v&&(await p(),this.requestUpdate())}},{kind:"method",key:"_valueChanged",value:function(e){e.stopPropagation(),this._setValue(e.detail.value)}},{kind:"method",key:"_setValue",value:function(e){this.value=e,(0,l.r)(this,"value-changed",{value:this._value},{bubbles:!1,composed:!1})}},{kind:"get",key:"_value",value:function(){return this.value||""}},{kind:"get",static:!0,key:"styles",value:function(){return n.AH`[slot=icon]{color:var(--primary-text-color);position:relative;bottom:2px}[slot=prefix]{margin-right:8px;margin-inline-end:8px;margin-inline-start:initial}`}}]}}),n.WF);o()}catch(e){o(e)}}))},93487:(e,t,i)=>{var o=i(62659),a=(i(21950),i(8339),i(40924)),n=i(18791);(0,o.A)([(0,n.EM)("ha-settings-row")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.MZ)({type:Boolean,reflect:!0})],key:"narrow",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Boolean,attribute:"three-line"})],key:"threeLine",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Boolean,attribute:"wrap-heading",reflect:!0})],key:"wrapHeading",value:()=>!1},{kind:"method",key:"render",value:function(){return a.qy` <div class="prefix-wrap"> <slot name="prefix"></slot> <div class="body" ?two-line="${!this.threeLine}" ?three-line="${this.threeLine}"> <slot name="heading"></slot> <div class="secondary"><slot name="description"></slot></div> </div> </div> <div class="content"><slot></slot></div> `}},{kind:"get",static:!0,key:"styles",value:function(){return a.AH`:host{display:flex;padding:0 16px;align-content:normal;align-self:auto;align-items:center}.body{padding-top:8px;padding-bottom:8px;padding-left:0;padding-inline-start:0;padding-right:16x;padding-inline-end:16px;overflow:hidden;display:var(--layout-vertical_-_display);flex-direction:var(--layout-vertical_-_flex-direction);justify-content:var(--layout-center-justified_-_justify-content);flex:var(--layout-flex_-_flex);flex-basis:var(--layout-flex_-_flex-basis)}.body[three-line]{min-height:var(--paper-item-body-three-line-min-height,88px)}:host(:not([wrap-heading])) body>*{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.body>.secondary{display:block;padding-top:4px;font-family:var(
          --mdc-typography-body2-font-family,
          var(--mdc-typography-font-family, Roboto, sans-serif)
        );-webkit-font-smoothing:antialiased;font-size:var(--mdc-typography-body2-font-size, .875rem);font-weight:var(--mdc-typography-body2-font-weight,400);line-height:normal;color:var(--secondary-text-color)}.body[two-line]{min-height:calc(var(--paper-item-body-two-line-min-height,72px) - 16px);flex:1}.content{display:contents}:host(:not([narrow])) .content{display:var(--settings-row-content-display,flex);justify-content:flex-end;flex:1;padding:16px 0}.content ::slotted(*){width:var(--settings-row-content-width)}:host([narrow]){align-items:normal;flex-direction:column;border-top:1px solid var(--divider-color);padding-bottom:8px}::slotted(ha-switch){padding:16px 0}.secondary{white-space:normal}.prefix-wrap{display:var(--settings-row-prefix-display)}:host([narrow]) .prefix-wrap{display:flex;align-items:center}`}}]}}),a.WF)},32615:(e,t,i)=>{i.a(e,(async(e,o)=>{try{i.r(t);var a=i(62659),n=(i(21950),i(55888),i(8339),i(58068),i(40924)),r=i(18791),s=i(77664),l=(i(12261),i(95439)),d=i(57225),c=(i(93487),i(42398),i(14126)),h=e([d]);d=(h.then?(await h)():h)[0];(0,a.A)([(0,r.EM)("dialog-category-registry-detail")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_name",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_icon",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,r.wk)()],key:"_submitting",value:void 0},{kind:"method",key:"showDialog",value:async function(e){this._params=e,this._error=void 0,this._params.entry?(this._name=this._params.entry.name||"",this._icon=this._params.entry.icon||null):(this._name=this._params.suggestedName||"",this._icon=null),await this.updateComplete}},{kind:"method",key:"closeDialog",value:function(){this._error="",this._params=void 0,(0,s.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){if(!this._params)return n.s6;const e=this._params.entry,t=!this._isNameValid();return n.qy` <ha-dialog open @closed="${this.closeDialog}" .heading="${(0,l.l)(this.hass,e?this.hass.localize("ui.panel.config.category.editor.edit"):this.hass.localize("ui.panel.config.category.editor.create"))}"> <div> ${this._error?n.qy`<ha-alert alert-type="error">${this._error}</ha-alert>`:""} <div class="form"> <ha-textfield .value="${this._name}" @input="${this._nameChanged}" .label="${this.hass.localize("ui.panel.config.category.editor.name")}" .validationMessage="${this.hass.localize("ui.panel.config.category.editor.required_error_msg")}" required dialogInitialFocus></ha-textfield> <ha-icon-picker .hass="${this.hass}" .value="${this._icon}" @value-changed="${this._iconChanged}" .label="${this.hass.localize("ui.panel.config.category.editor.icon")}"></ha-icon-picker> </div> </div> <mwc-button slot="secondaryAction" @click="${this.closeDialog}"> ${this.hass.localize("ui.common.cancel")} </mwc-button> <mwc-button slot="primaryAction" @click="${this._updateEntry}" .disabled="${t||this._submitting}"> ${e?this.hass.localize("ui.common.save"):this.hass.localize("ui.common.add")} </mwc-button> </ha-dialog> `}},{kind:"method",key:"_isNameValid",value:function(){return""!==this._name.trim()}},{kind:"method",key:"_nameChanged",value:function(e){this._error=void 0,this._name=e.target.value}},{kind:"method",key:"_iconChanged",value:function(e){this._error=void 0,this._icon=e.detail.value}},{kind:"method",key:"_updateEntry",value:async function(){const e=!this._params.entry;let t;this._submitting=!0;try{const i={name:this._name.trim(),icon:this._icon||(e?void 0:null)};t=e?await this._params.createEntry(i):await this._params.updateEntry(i),this.closeDialog()}catch(e){this._error=e.message||this.hass.localize("ui.panel.config.category.editor.unknown_error")}finally{this._submitting=!1}return t}},{kind:"get",static:!0,key:"styles",value:function(){return[c.nA,n.AH`ha-icon-picker,ha-textfield{display:block;margin-bottom:16px}`]}}]}}),n.WF);o()}catch(e){o(e)}}))},79372:(e,t,i)=>{var o=i(73155),a=i(33817),n=i(3429),r=i(75077);e.exports=function(e,t){t&&"string"==typeof e||a(e);var i=r(e);return n(a(void 0!==i?o(i,e):e))}},18684:(e,t,i)=>{var o=i(87568),a=i(42509),n=i(30356),r=i(51607),s=i(95124),l=i(79635);o({target:"Array",proto:!0},{flatMap:function(e){var t,i=r(this),o=s(i);return n(e),(t=l(i,0)).length=a(t,i,i,o,0,1,e,arguments.length>1?arguments[1]:void 0),t}})},74991:(e,t,i)=>{i(33523)("flatMap")},69704:(e,t,i)=>{var o=i(87568),a=i(73155),n=i(30356),r=i(33817),s=i(3429),l=i(79372),d=i(23408),c=i(44933),h=i(89385),u=d((function(){for(var e,t,i=this.iterator,o=this.mapper;;){if(t=this.inner)try{if(!(e=r(a(t.next,t.iterator))).done)return e.value;this.inner=null}catch(e){c(i,"throw",e)}if(e=r(a(this.next,i)),this.done=!!e.done)return;try{this.inner=l(o(e.value,this.counter++),!1)}catch(e){c(i,"throw",e)}}}));o({target:"Iterator",proto:!0,real:!0,forced:h},{flatMap:function(e){return r(this),n(e),new u(s(this),{mapper:e,inner:null})}})}};
//# sourceMappingURL=36127.IzzJdlL1RTg.js.map