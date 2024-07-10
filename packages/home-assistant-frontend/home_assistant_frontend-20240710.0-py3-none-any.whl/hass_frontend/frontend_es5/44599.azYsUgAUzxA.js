"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[44599,74808],{68286:function(e,t,i){function n(e){return void 0===e||Array.isArray(e)?e:[e]}i.d(t,{e:function(){return n}})},1751:function(e,t,i){i.d(t,{g:function(){return n}});i(53501),i(34517);var n=function(e){return function(t,i){return e.includes(t,i)}}},68704:function(e,t,i){var n=i(1781).A,a=i(94881).A;i.a(e,function(){var e=n(a().mark((function e(t,n){var r,o,s,l,d,c,u,h,v,f,p,m,y,k,g,_,b,x,A,w,M,C,O,L,Z,E,I,B,P,F,V,z,H,q,R;return a().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(e.prev=0,r=i(94881),o=i(1781),s=i(6238),l=i(36683),d=i(89231),c=i(29864),u=i(83647),h=i(8364),v=i(77052),f=i(69466),p=i(53501),m=i(71936),y=i(14460),k=i(848),g=i(68113),_=i(34517),b=i(66274),x=i(85038),A=i(84531),w=i(34290),M=i(40924),C=i(196),O=i(45081),L=i(68286),Z=i(77664),E=i(95507),I=i(74959),B=i(92483),P=i(35641),i(1683),i(37482),F=i(38696),!(V=t([P])).then){e.next=53;break}return e.next=49,V;case 49:e.t1=e.sent,e.t0=(0,e.t1)(),e.next=54;break;case 53:e.t0=V;case 54:P=e.t0[0],(0,h.A)([(0,C.EM)("ha-statistic-picker")],(function(e,t){var i,n=function(t){function i(){var t;(0,d.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return t=(0,c.A)(this,i,[].concat(a)),e(t),t}return(0,u.A)(i,t),(0,l.A)(i)}(t);return{F:n,d:[{kind:"field",decorators:[(0,C.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,C.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,C.MZ)()],key:"value",value:void 0},{kind:"field",decorators:[(0,C.MZ)({attribute:"statistic-types"})],key:"statisticTypes",value:void 0},{kind:"field",decorators:[(0,C.MZ)({type:Boolean,attribute:"allow-custom-entity"})],key:"allowCustomEntity",value:void 0},{kind:"field",decorators:[(0,C.MZ)({type:Array})],key:"statisticIds",value:void 0},{kind:"field",decorators:[(0,C.MZ)({type:Boolean})],key:"disabled",value:function(){return!1}},{kind:"field",decorators:[(0,C.MZ)({type:Array,attribute:"include-statistics-unit-of-measurement"})],key:"includeStatisticsUnitOfMeasurement",value:void 0},{kind:"field",decorators:[(0,C.MZ)({attribute:"include-unit-class"})],key:"includeUnitClass",value:void 0},{kind:"field",decorators:[(0,C.MZ)({attribute:"include-device-class"})],key:"includeDeviceClass",value:void 0},{kind:"field",decorators:[(0,C.MZ)({type:Boolean,attribute:"entities-only"})],key:"entitiesOnly",value:function(){return!1}},{kind:"field",decorators:[(0,C.MZ)({type:Array,attribute:"exclude-statistics"})],key:"excludeStatistics",value:void 0},{kind:"field",decorators:[(0,C.MZ)()],key:"helpMissingEntityUrl",value:function(){return"/more-info/statistics/"}},{kind:"field",decorators:[(0,C.wk)()],key:"_opened",value:void 0},{kind:"field",decorators:[(0,C.P)("ha-combo-box",!0)],key:"comboBox",value:void 0},{kind:"field",key:"_init",value:function(){return!1}},{kind:"field",key:"_statistics",value:function(){return[]}},{kind:"field",decorators:[(0,C.wk)()],key:"_filteredItems",value:function(){}},{kind:"field",key:"_rowRenderer",value:function(){var e=this;return function(t){return(0,M.qy)(z||(z=(0,s.A)(['<mwc-list-item graphic="avatar" twoline> '," <span>",'</span> <span slot="secondary">',"</span> </mwc-list-item>"])),t.state?(0,M.qy)(H||(H=(0,s.A)(['<state-badge slot="graphic" .stateObj="','" .hass="','"></state-badge>'])),t.state,e.hass):"",t.name,""===t.id||"__missing"===t.id?(0,M.qy)(q||(q=(0,s.A)(['<a target="_blank" rel="noopener noreferrer" href="','">',"</a>"])),(0,B.o)(e.hass,e.helpMissingEntityUrl),e.hass.localize("ui.components.statistic-picker.learn_more")):t.id)}}},{kind:"field",key:"_getStatistics",value:function(){var e=this;return(0,O.A)((function(t,i,n,a,r,o,s){if(!t.length)return[{id:"",name:e.hass.localize("ui.components.statistic-picker.no_statistics"),strings:[]}];if(i){var l=(0,L.e)(i);t=t.filter((function(e){return l.includes(e.statistics_unit_of_measurement)}))}if(n){var d=(0,L.e)(n);t=t.filter((function(e){return d.includes(e.unit_class)}))}if(a){var c=(0,L.e)(a);t=t.filter((function(t){var i=e.hass.states[t.statistic_id];return!i||c.includes(i.attributes.device_class||"")}))}var u=[];return t.forEach((function(t){if(!o||t.statistic_id===s||!o.includes(t.statistic_id)){var i=e.hass.states[t.statistic_id];if(i){var n=t.statistic_id,a=(0,I.$O)(e.hass,t.statistic_id,t);u.push({id:n,name:a,state:i,strings:[n,a]})}else if(!r){var l=t.statistic_id,d=(0,I.$O)(e.hass,t.statistic_id,t);u.push({id:l,name:d,strings:[l,d]})}}})),u.length?(u.length>1&&u.sort((function(t,i){return(0,E.x)(t.name||"",i.name||"",e.hass.locale.language)})),u.push({id:"__missing",name:e.hass.localize("ui.components.statistic-picker.missing_entity"),strings:[]}),u):[{id:"",name:e.hass.localize("ui.components.statistic-picker.no_match"),strings:[]}]}))}},{kind:"method",key:"open",value:function(){var e;null===(e=this.comboBox)||void 0===e||e.open()}},{kind:"method",key:"focus",value:function(){var e;null===(e=this.comboBox)||void 0===e||e.focus()}},{kind:"method",key:"willUpdate",value:function(e){var t=this;(!this.hasUpdated&&!this.statisticIds||e.has("statisticTypes"))&&this._getStatisticIds(),(!this._init&&this.statisticIds||e.has("_opened")&&this._opened)&&(this._init=!0,this.hasUpdated?this._statistics=this._getStatistics(this.statisticIds,this.includeStatisticsUnitOfMeasurement,this.includeUnitClass,this.includeDeviceClass,this.entitiesOnly,this.excludeStatistics,this.value):this.updateComplete.then((function(){t._statistics=t._getStatistics(t.statisticIds,t.includeStatisticsUnitOfMeasurement,t.includeUnitClass,t.includeDeviceClass,t.entitiesOnly,t.excludeStatistics,t.value)})))}},{kind:"method",key:"render",value:function(){var e;return 0===this._statistics.length?M.s6:(0,M.qy)(R||(R=(0,s.A)([' <ha-combo-box .hass="','" .label="','" .value="','" .renderer="','" .disabled="','" .allowCustomValue="','" .items="','" .filteredItems="','" item-value-path="id" item-id-path="id" item-label-path="name" @opened-changed="','" @value-changed="','" @filter-changed="','"></ha-combo-box> '])),this.hass,void 0===this.label&&this.hass?this.hass.localize("ui.components.statistic-picker.statistic"):this.label,this._value,this._rowRenderer,this.disabled,this.allowCustomEntity,this._statistics,null!==(e=this._filteredItems)&&void 0!==e?e:this._statistics,this._openedChanged,this._statisticChanged,this._filterChanged)}},{kind:"method",key:"_getStatisticIds",value:(i=(0,o.A)((0,r.A)().mark((function e(){return(0,r.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,(0,I.p3)(this.hass,this.statisticTypes);case 2:this.statisticIds=e.sent;case 3:case"end":return e.stop()}}),e,this)}))),function(){return i.apply(this,arguments)})},{kind:"get",key:"_value",value:function(){return this.value||""}},{kind:"method",key:"_statisticChanged",value:function(e){e.stopPropagation();var t=e.detail.value;"__missing"===t&&(t=""),t!==this._value&&this._setValue(t)}},{kind:"method",key:"_openedChanged",value:function(e){this._opened=e.detail.value}},{kind:"method",key:"_filterChanged",value:function(e){var t=e.detail.value.toLowerCase();this._filteredItems=t.length?(0,F.H)(t,this._statistics):void 0}},{kind:"method",key:"_setValue",value:function(e){var t=this;this.value=e,setTimeout((function(){(0,Z.r)(t,"value-changed",{value:e}),(0,Z.r)(t,"change")}),0)}}]}}),M.WF),n(),e.next=62;break;case 59:e.prev=59,e.t2=e.catch(0),n(e.t2);case 62:case"end":return e.stop()}}),e,null,[[0,59]])})));return function(t,i){return e.apply(this,arguments)}}())},61674:function(e,t,i){var n,a=i(6238),r=i(36683),o=i(89231),s=i(29864),l=i(83647),d=i(8364),c=(i(77052),i(51497)),u=i(48678),h=i(40924),v=i(196);(0,d.A)([(0,v.EM)("ha-checkbox")],(function(e,t){var i=function(t){function i(){var t;(0,o.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return t=(0,s.A)(this,i,[].concat(a)),e(t),t}return(0,l.A)(i,t),(0,r.A)(i)}(t);return{F:i,d:[{kind:"field",static:!0,key:"styles",value:function(){return[u.R,(0,h.AH)(n||(n=(0,a.A)([":host{--mdc-theme-secondary:var(--primary-color)}"])))]}}]}}),c.L)},35641:function(e,t,i){var n=i(1781).A,a=i(94881).A;i.a(e,function(){var e=n(a().mark((function e(t,n){var r,o,s,l,d,c,u,h,v,f,p,m,y,k,g,_,b,x,A,w,M,C,O,L,Z,E,I,B,P;return a().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(e.prev=0,r=i(94881),o=i(1781),s=i(36683),l=i(89231),d=i(29864),c=i(83647),u=i(8364),h=i(76504),v=i(80792),f=i(6238),p=i(77052),m=i(68113),y=i(66274),k=i(84531),g=i(34290),_=i(54854),b=i(66505),x=i(45584),A=i(40924),w=i(196),M=i(79278),C=i(77664),i(12731),i(39335),i(42398),!(O=t([b])).then){e.next=39;break}return e.next=35,O;case 35:e.t1=e.sent,e.t0=(0,e.t1)(),e.next=40;break;case 39:e.t0=O;case 40:b=e.t0[0],(0,x.SF)("vaadin-combo-box-item",(0,A.AH)(L||(L=(0,f.A)([':host{padding:0!important}:host([focused]:not([disabled])){background-color:rgba(var(--rgb-primary-text-color,0,0,0),.12)}:host([selected]:not([disabled])){background-color:transparent;color:var(--mdc-theme-primary);--mdc-ripple-color:var(--mdc-theme-primary);--mdc-theme-text-primary-on-background:var(--mdc-theme-primary)}:host([selected]:not([disabled])):before{background-color:var(--mdc-theme-primary);opacity:.12;content:"";position:absolute;top:0;left:0;width:100%;height:100%}:host([selected][focused]:not([disabled])):before{opacity:.24}:host(:hover:not([disabled])){background-color:transparent}[part=content]{width:100%}[part=checkmark]{display:none}'])))),(0,u.A)([(0,w.EM)("ha-combo-box")],(function(e,t){var i,n,a=function(t){function i(){var t;(0,l.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return t=(0,d.A)(this,i,[].concat(a)),e(t),t}return(0,c.A)(i,t),(0,s.A)(i)}(t);return{F:a,d:[{kind:"field",decorators:[(0,w.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,w.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,w.MZ)()],key:"value",value:void 0},{kind:"field",decorators:[(0,w.MZ)()],key:"placeholder",value:void 0},{kind:"field",decorators:[(0,w.MZ)()],key:"validationMessage",value:void 0},{kind:"field",decorators:[(0,w.MZ)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,w.MZ)({attribute:"error-message"})],key:"errorMessage",value:void 0},{kind:"field",decorators:[(0,w.MZ)({type:Boolean})],key:"invalid",value:function(){return!1}},{kind:"field",decorators:[(0,w.MZ)({type:Boolean})],key:"icon",value:function(){return!1}},{kind:"field",decorators:[(0,w.MZ)({attribute:!1})],key:"items",value:void 0},{kind:"field",decorators:[(0,w.MZ)({attribute:!1})],key:"filteredItems",value:void 0},{kind:"field",decorators:[(0,w.MZ)({attribute:!1})],key:"dataProvider",value:void 0},{kind:"field",decorators:[(0,w.MZ)({attribute:"allow-custom-value",type:Boolean})],key:"allowCustomValue",value:function(){return!1}},{kind:"field",decorators:[(0,w.MZ)({attribute:"item-value-path"})],key:"itemValuePath",value:function(){return"value"}},{kind:"field",decorators:[(0,w.MZ)({attribute:"item-label-path"})],key:"itemLabelPath",value:function(){return"label"}},{kind:"field",decorators:[(0,w.MZ)({attribute:"item-id-path"})],key:"itemIdPath",value:void 0},{kind:"field",decorators:[(0,w.MZ)({attribute:!1})],key:"renderer",value:void 0},{kind:"field",decorators:[(0,w.MZ)({type:Boolean})],key:"disabled",value:function(){return!1}},{kind:"field",decorators:[(0,w.MZ)({type:Boolean})],key:"required",value:function(){return!1}},{kind:"field",decorators:[(0,w.MZ)({type:Boolean,reflect:!0})],key:"opened",value:function(){return!1}},{kind:"field",decorators:[(0,w.P)("vaadin-combo-box-light",!0)],key:"_comboBox",value:void 0},{kind:"field",decorators:[(0,w.P)("ha-textfield",!0)],key:"_inputElement",value:void 0},{kind:"field",key:"_overlayMutationObserver",value:void 0},{kind:"field",key:"_bodyMutationObserver",value:void 0},{kind:"method",key:"open",value:(n=(0,o.A)((0,r.A)().mark((function e(){var t;return(0,r.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.updateComplete;case 2:null===(t=this._comboBox)||void 0===t||t.open();case 3:case"end":return e.stop()}}),e,this)}))),function(){return n.apply(this,arguments)})},{kind:"method",key:"focus",value:(i=(0,o.A)((0,r.A)().mark((function e(){var t,i;return(0,r.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.updateComplete;case 2:return e.next=4,null===(t=this._inputElement)||void 0===t?void 0:t.updateComplete;case 4:null===(i=this._inputElement)||void 0===i||i.focus();case 5:case"end":return e.stop()}}),e,this)}))),function(){return i.apply(this,arguments)})},{kind:"method",key:"disconnectedCallback",value:function(){(0,h.A)((0,v.A)(a.prototype),"disconnectedCallback",this).call(this),this._overlayMutationObserver&&(this._overlayMutationObserver.disconnect(),this._overlayMutationObserver=void 0),this._bodyMutationObserver&&(this._bodyMutationObserver.disconnect(),this._bodyMutationObserver=void 0)}},{kind:"get",key:"selectedItem",value:function(){return this._comboBox.selectedItem}},{kind:"method",key:"setInputValue",value:function(e){this._comboBox.value=e}},{kind:"method",key:"render",value:function(){var e;return(0,A.qy)(Z||(Z=(0,f.A)([' <vaadin-combo-box-light .itemValuePath="','" .itemIdPath="','" .itemLabelPath="','" .items="','" .value="','" .filteredItems="','" .dataProvider="','" .allowCustomValue="','" .disabled="','" .required="','" ',' @opened-changed="','" @filter-changed="','" @value-changed="','" attr-for-value="value"> <ha-textfield label="','" placeholder="','" ?disabled="','" ?required="','" validationMessage="','" .errorMessage="','" class="input" autocapitalize="none" autocomplete="off" autocorrect="off" input-spellcheck="false" .suffix="','" .icon="','" .invalid="','" .helper="','" helperPersistent> <slot name="icon" slot="leadingIcon"></slot> </ha-textfield> ',' <ha-svg-icon role="button" tabindex="-1" aria-label="','" aria-expanded="','" class="toggle-button" .path="','" @click="','"></ha-svg-icon> </vaadin-combo-box-light> '])),this.itemValuePath,this.itemIdPath,this.itemLabelPath,this.items,this.value||"",this.filteredItems,this.dataProvider,this.allowCustomValue,this.disabled,this.required,(0,_.d)(this.renderer||this._defaultRowRenderer),this._openedChanged,this._filterChanged,this._valueChanged,(0,M.J)(this.label),(0,M.J)(this.placeholder),this.disabled,this.required,(0,M.J)(this.validationMessage),this.errorMessage,(0,A.qy)(E||(E=(0,f.A)(['<div style="width:28px" role="none presentation"></div>']))),this.icon,this.invalid,this.helper,this.value?(0,A.qy)(I||(I=(0,f.A)(['<ha-svg-icon role="button" tabindex="-1" aria-label="','" class="clear-button" .path="','" @click="','"></ha-svg-icon>'])),(0,M.J)(null===(e=this.hass)||void 0===e?void 0:e.localize("ui.common.clear")),"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",this._clearValue):"",(0,M.J)(this.label),this.opened?"true":"false",this.opened?"M7,15L12,10L17,15H7Z":"M7,10L12,15L17,10H7Z",this._toggleOpen)}},{kind:"field",key:"_defaultRowRenderer",value:function(){var e=this;return function(t){return(0,A.qy)(B||(B=(0,f.A)(["<ha-list-item> "," </ha-list-item>"])),e.itemLabelPath?t[e.itemLabelPath]:t)}}},{kind:"method",key:"_clearValue",value:function(e){e.stopPropagation(),(0,C.r)(this,"value-changed",{value:void 0})}},{kind:"method",key:"_toggleOpen",value:function(e){var t,i;this.opened?(null===(t=this._comboBox)||void 0===t||t.close(),e.stopPropagation()):null===(i=this._comboBox)||void 0===i||i.inputElement.focus()}},{kind:"method",key:"_openedChanged",value:function(e){var t=this;e.stopPropagation();var i=e.detail.value;if(setTimeout((function(){t.opened=i}),0),(0,C.r)(this,"opened-changed",{value:e.detail.value}),i){var n=document.querySelector("vaadin-combo-box-overlay");n&&this._removeInert(n),this._observeBody()}else{var a;null===(a=this._bodyMutationObserver)||void 0===a||a.disconnect(),this._bodyMutationObserver=void 0}}},{kind:"method",key:"_observeBody",value:function(){var e=this;"MutationObserver"in window&&!this._bodyMutationObserver&&(this._bodyMutationObserver=new MutationObserver((function(t){t.forEach((function(t){t.addedNodes.forEach((function(t){"VAADIN-COMBO-BOX-OVERLAY"===t.nodeName&&e._removeInert(t)})),t.removedNodes.forEach((function(t){var i;"VAADIN-COMBO-BOX-OVERLAY"===t.nodeName&&(null===(i=e._overlayMutationObserver)||void 0===i||i.disconnect(),e._overlayMutationObserver=void 0)}))}))})),this._bodyMutationObserver.observe(document.body,{childList:!0}))}},{kind:"method",key:"_removeInert",value:function(e){var t,i=this;if(e.inert)return e.inert=!1,null===(t=this._overlayMutationObserver)||void 0===t||t.disconnect(),void(this._overlayMutationObserver=void 0);"MutationObserver"in window&&!this._overlayMutationObserver&&(this._overlayMutationObserver=new MutationObserver((function(e){e.forEach((function(e){if("inert"===e.attributeName){var t,n=e.target;if(n.inert)null===(t=i._overlayMutationObserver)||void 0===t||t.disconnect(),i._overlayMutationObserver=void 0,n.inert=!1}}))})),this._overlayMutationObserver.observe(e,{attributes:!0}))}},{kind:"method",key:"_filterChanged",value:function(e){e.stopPropagation(),(0,C.r)(this,"filter-changed",{value:e.detail.value})}},{kind:"method",key:"_valueChanged",value:function(e){e.stopPropagation(),this.allowCustomValue||(this._comboBox._closeOnBlurIsPrevented=!0);var t=e.detail.value;t!==this.value&&(0,C.r)(this,"value-changed",{value:t||void 0})}},{kind:"get",static:!0,key:"styles",value:function(){return(0,A.AH)(P||(P=(0,f.A)([":host{display:block;width:100%}vaadin-combo-box-light{position:relative;--vaadin-combo-box-overlay-max-height:calc(45vh - 56px)}ha-textfield{width:100%}ha-textfield>ha-icon-button{--mdc-icon-button-size:24px;padding:2px;color:var(--secondary-text-color)}ha-svg-icon{color:var(--input-dropdown-icon-color);position:absolute;cursor:pointer}.toggle-button{right:12px;top:-10px;inset-inline-start:initial;inset-inline-end:12px;direction:var(--direction)}:host([opened]) .toggle-button{color:var(--primary-color)}.clear-button{--mdc-icon-size:20px;top:-7px;right:36px;inset-inline-start:initial;inset-inline-end:36px;direction:var(--direction)}"])))}}]}}),A.WF),n(),e.next=52;break;case 49:e.prev=49,e.t2=e.catch(0),n(e.t2);case 52:case"end":return e.stop()}}),e,null,[[0,49]])})));return function(t,i){return e.apply(this,arguments)}}())},83357:function(e,t,i){var n,a,r=i(6238),o=i(36683),s=i(89231),l=i(29864),d=i(83647),c=i(8364),u=(i(77052),i(80487)),h=i(4258),v=i(40924),f=i(196),p=i(69760),m=i(77664);(0,c.A)([(0,f.EM)("ha-formfield")],(function(e,t){var i=function(t){function i(){var t;(0,s.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return t=(0,l.A)(this,i,[].concat(a)),e(t),t}return(0,d.A)(i,t),(0,o.A)(i)}(t);return{F:i,d:[{kind:"field",decorators:[(0,f.MZ)({type:Boolean,reflect:!0})],key:"disabled",value:function(){return!1}},{kind:"method",key:"render",value:function(){var e={"mdc-form-field--align-end":this.alignEnd,"mdc-form-field--space-between":this.spaceBetween,"mdc-form-field--nowrap":this.nowrap};return(0,v.qy)(n||(n=(0,r.A)([' <div class="mdc-form-field ','"> <slot></slot> <label class="mdc-label" @click="','"><slot name="label">',"</slot></label> </div>"])),(0,p.H)(e),this._labelClick,this.label)}},{kind:"method",key:"_labelClick",value:function(){var e=this.input;if(e&&(e.focus(),!e.disabled))switch(e.tagName){case"HA-CHECKBOX":e.checked=!e.checked,(0,m.r)(e,"change");break;case"HA-RADIO":e.checked=!0,(0,m.r)(e,"change");break;default:e.click()}}},{kind:"field",static:!0,key:"styles",value:function(){return[h.R,(0,v.AH)(a||(a=(0,r.A)([":host(:not([alignEnd])) ::slotted(ha-switch){margin-right:10px;margin-inline-end:10px;margin-inline-start:inline}.mdc-form-field{align-items:var(--ha-formfield-align-items,center)}.mdc-form-field>label{direction:var(--direction);margin-inline-start:0;margin-inline-end:auto;padding-inline-start:4px;padding-inline-end:0}:host([disabled]) label{color:var(--disabled-text-color)}"])))]}}]}}),u.M)},39335:function(e,t,i){i.d(t,{$:function(){return k}});var n,a,r,o=i(6238),s=i(36683),l=i(89231),d=i(29864),c=i(83647),u=i(8364),h=i(76504),v=i(80792),f=(i(77052),i(46175)),p=i(45592),m=i(40924),y=i(196),k=(0,u.A)([(0,y.EM)("ha-list-item")],(function(e,t){var i=function(t){function i(){var t;(0,l.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return t=(0,d.A)(this,i,[].concat(a)),e(t),t}return(0,c.A)(i,t),(0,s.A)(i)}(t);return{F:i,d:[{kind:"method",key:"renderRipple",value:function(){return this.noninteractive?"":(0,h.A)((0,v.A)(i.prototype),"renderRipple",this).call(this)}},{kind:"get",static:!0,key:"styles",value:function(){return[p.R,(0,m.AH)(n||(n=(0,o.A)([":host{padding-left:var(--mdc-list-side-padding-left,var(--mdc-list-side-padding,20px));padding-inline-start:var(--mdc-list-side-padding-left,var(--mdc-list-side-padding,20px));padding-right:var(--mdc-list-side-padding-right,var(--mdc-list-side-padding,20px));padding-inline-end:var(--mdc-list-side-padding-right,var(--mdc-list-side-padding,20px))}:host([graphic=avatar]:not([twoLine])),:host([graphic=icon]:not([twoLine])){height:48px}span.material-icons:first-of-type{margin-inline-start:0px!important;margin-inline-end:var(--mdc-list-item-graphic-margin,16px)!important;direction:var(--direction)!important}span.material-icons:last-of-type{margin-inline-start:auto!important;margin-inline-end:0px!important;direction:var(--direction)!important}.mdc-deprecated-list-item__meta{display:var(--mdc-list-item-meta-display);align-items:center;flex-shrink:0}:host([graphic=icon]:not([twoline])) .mdc-deprecated-list-item__graphic{margin-inline-end:var(--mdc-list-item-graphic-margin,20px)!important}:host([multiline-secondary]){height:auto}:host([multiline-secondary]) .mdc-deprecated-list-item__text{padding:8px 0}:host([multiline-secondary]) .mdc-deprecated-list-item__secondary-text{text-overflow:initial;white-space:normal;overflow:auto;display:inline-block;margin-top:10px}:host([multiline-secondary]) .mdc-deprecated-list-item__primary-text{margin-top:10px}:host([multiline-secondary]) .mdc-deprecated-list-item__secondary-text::before{display:none}:host([multiline-secondary]) .mdc-deprecated-list-item__primary-text::before{display:none}:host([disabled]){color:var(--disabled-text-color)}:host([noninteractive]){pointer-events:unset}"]))),"rtl"===document.dir?(0,m.AH)(a||(a=(0,o.A)(["span.material-icons:first-of-type,span.material-icons:last-of-type{direction:rtl!important;--direction:rtl}"]))):(0,m.AH)(r||(r=(0,o.A)([""])))]}}]}}),f.J)},28452:function(e,t,i){var n,a=i(6238),r=i(36683),o=i(89231),s=i(29864),l=i(83647),d=i(8364),c=(i(77052),i(8463)),u=i(14414),h=i(40924),v=i(196);(0,d.A)([(0,v.EM)("ha-radio")],(function(e,t){var i=function(t){function i(){var t;(0,o.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return t=(0,s.A)(this,i,[].concat(a)),e(t),t}return(0,l.A)(i,t),(0,r.A)(i)}(t);return{F:i,d:[{kind:"field",static:!0,key:"styles",value:function(){return[u.R,(0,h.AH)(n||(n=(0,a.A)([":host{--mdc-theme-secondary:var(--primary-color)}"])))]}}]}}),c.F)},83378:function(e,t,i){i.d(t,{HV:function(){return r},Hh:function(){return a},KF:function(){return o},g0:function(){return d},s7:function(){return s}});var n=i(1751),a="unavailable",r="unknown",o="off",s=[a,r],l=[a,r,o],d=(0,n.g)(s);(0,n.g)(l)},64433:function(e,t,i){var n=i(1781).A,a=i(94881).A;i.a(e,function(){var e=n(a().mark((function e(n,r){var o,s,l,d,c,u,h,v,f,p,m,y,k,g,_,b,x,A,w,M,C,O,L,Z,E,I,B,P,F,V,z,H,q,R,S,U,D,N,T,j,J,W,X;return a().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(e.prev=0,i.r(t),i.d(t,{DialogEnergySolarSettings:function(){return X}}),o=i(6238),s=i(94881),l=i(1781),d=i(36683),c=i(89231),u=i(29864),h=i(83647),v=i(8364),f=i(77052),p=i(69466),m=i(53501),y=i(75658),k=i(53156),g=i(36724),_=i(71936),b=i(60060),x=i(43859),A=i(68113),w=i(34517),M=i(66274),C=i(85038),O=i(98168),i(34069),L=i(40924),Z=i(196),E=i(77664),I=i(68704),i(61674),i(95439),i(83357),i(28452),B=i(60280),P=i(41525),F=i(96951),V=i(9452),z=i(14126),H=i(5203),!(q=n([I,P])).then){e.next=62;break}return e.next=58,q;case 58:e.t1=e.sent,e.t0=(0,e.t1)(),e.next=63;break;case 62:e.t0=q;case 63:R=e.t0,I=R[0],P=R[1],W=["energy"],X=(0,v.A)([(0,Z.EM)("dialog-energy-solar-settings")],(function(e,t){var i,n,a,r=function(t){function i(){var t;(0,c.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return t=(0,u.A)(this,i,[].concat(a)),e(t),t}return(0,h.A)(i,t),(0,d.A)(i)}(t);return{F:r,d:[{kind:"field",decorators:[(0,Z.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,Z.wk)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,Z.wk)()],key:"_source",value:void 0},{kind:"field",decorators:[(0,Z.wk)()],key:"_configEntries",value:void 0},{kind:"field",decorators:[(0,Z.wk)()],key:"_forecast",value:void 0},{kind:"field",decorators:[(0,Z.wk)()],key:"_energy_units",value:void 0},{kind:"field",decorators:[(0,Z.wk)()],key:"_error",value:void 0},{kind:"field",key:"_excludeList",value:void 0},{kind:"method",key:"showDialog",value:(a=(0,l.A)((0,s.A)().mark((function e(t){var i=this;return(0,s.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return this._params=t,this._fetchSolarForecastConfigEntries(),this._source=t.source?Object.assign({},t.source):(0,P.Q4)(),this._forecast=null!==this._source.config_entry_solar_forecast,e.next=6,(0,F.j4)(this.hass,"energy");case 6:this._energy_units=e.sent.units,this._excludeList=this._params.solar_sources.map((function(e){return e.stat_energy_from})).filter((function(e){var t;return e!==(null===(t=i._source)||void 0===t?void 0:t.stat_energy_from)}));case 8:case"end":return e.stop()}}),e,this)}))),function(e){return a.apply(this,arguments)})},{kind:"method",key:"closeDialog",value:function(){this._params=void 0,this._source=void 0,this._error=void 0,this._excludeList=void 0,(0,E.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){var e,t,i=this;if(!this._params||!this._source)return L.s6;var n=(null===(e=this._energy_units)||void 0===e?void 0:e.join(", "))||"";return(0,L.qy)(S||(S=(0,o.A)([' <ha-dialog open .heading="','" @closed="','"> '," <div> ",' </div> <ha-statistic-picker .hass="','" .helpMissingEntityUrl="','" .includeUnitClass="','" .value="','" .label="','" .excludeStatistics="','" @value-changed="','" dialogInitialFocus></ha-statistic-picker> <h3> '," </h3> <p> ",' </p> <ha-formfield label="','"> <ha-radio value="false" name="forecast" .checked="','" @change="','"></ha-radio> </ha-formfield> <ha-formfield label="','"> <ha-radio value="true" name="forecast" .checked="','" @change="','"></ha-radio> </ha-formfield> ',' <mwc-button @click="','" slot="secondaryAction"> ',' </mwc-button> <mwc-button @click="','" .disabled="','" slot="primaryAction"> '," </mwc-button> </ha-dialog> "])),(0,L.qy)(U||(U=(0,o.A)(['<ha-svg-icon .path="','" style="--mdc-icon-size:32px"></ha-svg-icon> ',""])),"M11.45,2V5.55L15,3.77L11.45,2M10.45,8L8,10.46L11.75,11.71L10.45,8M2,11.45L3.77,15L5.55,11.45H2M10,2H2V10C2.57,10.17 3.17,10.25 3.77,10.25C7.35,10.26 10.26,7.35 10.27,3.75C10.26,3.16 10.17,2.57 10,2M17,22V16H14L19,7V13H22L17,22Z",this.hass.localize("ui.panel.config.energy.solar.dialog.header")),this.closeDialog,this._error?(0,L.qy)(D||(D=(0,o.A)(['<p class="error">',"</p>"])),this._error):"",this.hass.localize("ui.panel.config.energy.solar.dialog.entity_para",{unit:n}),this.hass,P.X4,W,this._source.stat_energy_from,this.hass.localize("ui.panel.config.energy.solar.dialog.solar_production_energy"),this._excludeList,this._statisticChanged,this.hass.localize("ui.panel.config.energy.solar.dialog.solar_production_forecast"),this.hass.localize("ui.panel.config.energy.solar.dialog.solar_production_forecast_description"),this.hass.localize("ui.panel.config.energy.solar.dialog.dont_forecast_production"),!this._forecast,this._handleForecastChanged,this.hass.localize("ui.panel.config.energy.solar.dialog.forecast_production"),this._forecast,this._handleForecastChanged,this._forecast?(0,L.qy)(N||(N=(0,o.A)(['<div class="forecast-options"> ',' <mwc-button @click="','"> '," </mwc-button> </div>"])),null===(t=this._configEntries)||void 0===t?void 0:t.map((function(e){var t,n;return(0,L.qy)(T||(T=(0,o.A)(['<ha-formfield .label="','"> <ha-checkbox .entry="','" @change="','" .checked="','"> </ha-checkbox> </ha-formfield>'])),(0,L.qy)(j||(j=(0,o.A)(['<div style="display:flex;align-items:center"> <img alt="" crossorigin="anonymous" referrerpolicy="no-referrer" style="height:24px;margin-right:16px;margin-inline-end:16px;margin-inline-start:initial" src="','">'," </div>"])),(0,H.MR)({domain:e.domain,type:"icon",darkOptimized:null===(t=i.hass.themes)||void 0===t?void 0:t.darkMode}),e.title),e,i._forecastCheckChanged,null===(n=i._source)||void 0===n||null===(n=n.config_entry_solar_forecast)||void 0===n?void 0:n.includes(e.entry_id))})),this._addForecast,this.hass.localize("ui.panel.config.energy.solar.dialog.add_forecast")):"",this.closeDialog,this.hass.localize("ui.common.cancel"),this._save,!this._source.stat_energy_from,this.hass.localize("ui.common.save"))}},{kind:"method",key:"_fetchSolarForecastConfigEntries",value:(n=(0,l.A)((0,s.A)().mark((function e(){var t;return(0,s.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(0!==(t=this._params.info.solar_forecast_domains).length){e.next=5;break}e.t0=[],e.next=15;break;case 5:if(1!==t.length){e.next=11;break}return e.next=8,(0,B.VN)(this.hass,{type:["service"],domain:t[0]});case 8:e.t1=e.sent,e.next=14;break;case 11:return e.next=13,(0,B.VN)(this.hass,{type:["service"]});case 13:e.t1=e.sent.filter((function(e){return t.includes(e.domain)}));case 14:e.t0=e.t1;case 15:this._configEntries=e.t0;case 16:case"end":return e.stop()}}),e,this)}))),function(){return n.apply(this,arguments)})},{kind:"method",key:"_handleForecastChanged",value:function(e){var t=e.currentTarget;this._forecast="true"===t.value}},{kind:"method",key:"_forecastCheckChanged",value:function(e){var t=e.currentTarget,i=t.entry;t.checked?(null===this._source.config_entry_solar_forecast&&(this._source.config_entry_solar_forecast=[]),this._source.config_entry_solar_forecast.push(i.entry_id)):this._source.config_entry_solar_forecast.splice(this._source.config_entry_solar_forecast.indexOf(i.entry_id),1)}},{kind:"method",key:"_addForecast",value:function(){var e=this;(0,V.W)(this,{startFlowHandler:"forecast_solar",dialogClosedCallback:function(t){t.entryId&&(null===e._source.config_entry_solar_forecast&&(e._source.config_entry_solar_forecast=[]),e._source.config_entry_solar_forecast.push(t.entryId),e._fetchSolarForecastConfigEntries())}})}},{kind:"method",key:"_statisticChanged",value:function(e){this._source=Object.assign(Object.assign({},this._source),{},{stat_energy_from:e.detail.value})}},{kind:"method",key:"_save",value:(i=(0,l.A)((0,s.A)().mark((function e(){return(0,s.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,this._forecast||(this._source.config_entry_solar_forecast=null),e.next=4,this._params.saveCallback(this._source);case 4:this.closeDialog(),e.next=10;break;case 7:e.prev=7,e.t0=e.catch(0),this._error=e.t0.message;case 10:case"end":return e.stop()}}),e,this,[[0,7]])}))),function(){return i.apply(this,arguments)})},{kind:"get",static:!0,key:"styles",value:function(){return[z.RF,z.nA,(0,L.AH)(J||(J=(0,o.A)(["ha-dialog{--mdc-dialog-max-width:430px}img{height:24px;margin-right:16px;margin-inline-end:16px;margin-inline-start:initial}ha-formfield{display:block}ha-statistic-picker{width:100%}.forecast-options{padding-left:32px;padding-inline-start:32px;padding-inline-end:initial}.forecast-options mwc-button{padding-left:8px;padding-inline-start:8px;padding-inline-end:initial}"])))]}}]}}),L.WF),r(),e.next=75;break;case 72:e.prev=72,e.t2=e.catch(0),r(e.t2);case 75:case"end":return e.stop()}}),e,null,[[0,72]])})));return function(t,i){return e.apply(this,arguments)}}())},74808:function(e,t,i){var n=i(1781).A,a=i(94881).A;i.a(e,function(){var e=n(a().mark((function e(t,n){var r,o,s,l,d;return a().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(e.prev=0,r=i(21950),o=i(68113),s=i(55888),l=i(56262),d=i(8339),"function"==typeof window.ResizeObserver){e.next=15;break}return e.next=14,i.e(76071).then(i.bind(i,76071));case 14:window.ResizeObserver=e.sent.default;case 15:n(),e.next=21;break;case 18:e.prev=18,e.t0=e.catch(0),n(e.t0);case 21:case"end":return e.stop()}}),e,null,[[0,18]])})));return function(t,i){return e.apply(this,arguments)}}(),1)}}]);
//# sourceMappingURL=44599.azYsUgAUzxA.js.map