export const id=61208;export const ids=[61208];export const modules={36471:(t,e,i)=>{i.d(e,{_:()=>s});i(27934),i(21950),i(66274),i(84531),i(8339);var n=i(40924),o=i(3358);const s=(0,o.u$)(class extends o.WL{constructor(t){if(super(t),this._element=void 0,t.type!==o.OA.CHILD)throw new Error("dynamicElementDirective can only be used in content bindings")}update(t,[e,i]){return this._element&&this._element.localName===e?(i&&Object.entries(i).forEach((([t,e])=>{this._element[t]=e})),n.c0):this.render(e,i)}render(t,e){return this._element=document.createElement(t),e&&Object.entries(e).forEach((([t,e])=>{this._element[t]=e})),this._element}})},17876:(t,e,i)=>{i.d(e,{L:()=>o,z:()=>s});var n=i(1751);const o=["input_boolean","input_button","input_text","input_number","input_datetime","input_select","counter","timer","schedule"],s=(0,n.g)(o)},53461:(t,e,i)=>{i.r(e),i.d(e,{HuiSelectOptionsCardFeatureEditor:()=>l});var n=i(62659),o=(i(21950),i(98168),i(8339),i(40924)),s=i(18791),r=i(45081),a=i(77664);i(23006);let l=(0,n.A)([(0,s.EM)("hui-select-options-card-feature-editor")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"context",value:void 0},{kind:"field",decorators:[(0,s.wk)()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(t){this._config=t}},{kind:"field",key:"_schema",value:()=>(0,r.A)(((t,e,i)=>{var n;return[{name:"customize_options",selector:{boolean:{}}},...i?[{name:"options",selector:{select:{multiple:!0,reorder:!0,options:(null==e||null===(n=e.attributes.options)||void 0===n?void 0:n.map((i=>({value:i,label:t(e,i)}))))||[]}}}]:[]]}))},{kind:"method",key:"render",value:function(){var t,e;if(!this.hass||!this._config)return o.s6;const i=null!==(t=this.context)&&void 0!==t&&t.entity_id?this.hass.states[null===(e=this.context)||void 0===e?void 0:e.entity_id]:void 0,n={...this._config,customize_options:void 0!==this._config.options},s=this._schema(this.hass.formatEntityState,i,n.customize_options);return o.qy` <ha-form .hass="${this.hass}" .data="${n}" .schema="${s}" .computeLabel="${this._computeLabelCallback}" @value-changed="${this._valueChanged}"></ha-form> `}},{kind:"method",key:"_valueChanged",value:function(t){var e,i;const{customize_options:n,...o}=t.detail.value,s=null!==(e=this.context)&&void 0!==e&&e.entity_id?this.hass.states[null===(i=this.context)||void 0===i?void 0:i.entity_id]:void 0;n&&!o.options&&(o.options=(null==s?void 0:s.attributes.options)||[]),!n&&o.options&&delete o.options,(0,a.r)(this,"config-changed",{config:o})}},{kind:"field",key:"_computeLabelCallback",value(){return t=>{switch(t.name){case"options":case"customize_options":return this.hass.localize(`ui.panel.lovelace.editor.features.types.select-options.${t.name}`);default:return""}}}}]}}),o.WF)},79372:(t,e,i)=>{var n=i(73155),o=i(33817),s=i(3429),r=i(75077);t.exports=function(t,e){e&&"string"==typeof t||o(t);var i=r(t);return s(o(void 0!==i?n(i,t):t))}},18684:(t,e,i)=>{var n=i(87568),o=i(42509),s=i(30356),r=i(51607),a=i(95124),l=i(79635);n({target:"Array",proto:!0},{flatMap:function(t){var e,i=r(this),n=a(i);return s(t),(e=l(i,0)).length=o(e,i,i,n,0,1,t,arguments.length>1?arguments[1]:void 0),e}})},74991:(t,e,i)=>{i(33523)("flatMap")},69704:(t,e,i)=>{var n=i(87568),o=i(73155),s=i(30356),r=i(33817),a=i(3429),l=i(79372),u=i(23408),c=i(44933),d=i(89385),h=u((function(){for(var t,e,i=this.iterator,n=this.mapper;;){if(e=this.inner)try{if(!(t=r(o(e.next,e.iterator))).done)return t.value;this.inner=null}catch(t){c(i,"throw",t)}if(t=r(o(this.next,i)),this.done=!!t.done)return;try{this.inner=l(n(t.value,this.counter++),!1)}catch(t){c(i,"throw",t)}}}));n({target:"Iterator",proto:!0,real:!0,forced:d},{flatMap:function(t){return r(this),s(t),new h(a(this),{mapper:t,inner:null})}})}};
//# sourceMappingURL=61208.-p0DL0OCJHw.js.map