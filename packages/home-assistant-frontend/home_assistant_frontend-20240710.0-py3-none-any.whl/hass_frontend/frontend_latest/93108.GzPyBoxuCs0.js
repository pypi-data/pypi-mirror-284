export const id=93108;export const ids=[93108];export const modules={36471:(e,t,a)=>{a.d(t,{_:()=>o});a(27934),a(21950),a(66274),a(84531),a(8339);var i=a(40924),n=a(3358);const o=(0,n.u$)(class extends n.WL{constructor(e){if(super(e),this._element=void 0,e.type!==n.OA.CHILD)throw new Error("dynamicElementDirective can only be used in content bindings")}update(e,[t,a]){return this._element&&this._element.localName===t?(a&&Object.entries(a).forEach((([e,t])=>{this._element[e]=t})),i.c0):this.render(t,a)}render(e,t){return this._element=document.createElement(e),t&&Object.entries(t).forEach((([e,t])=>{this._element[e]=t})),this._element}})},17876:(e,t,a)=>{a.d(t,{L:()=>n,z:()=>o});var i=a(1751);const n=["input_boolean","input_button","input_text","input_number","input_datetime","input_select","counter","timer","schedule"],o=(0,i.g)(n)},66339:(e,t,a)=>{a.r(t),a.d(t,{HuiStatisticCardEditor:()=>v});var i=a(62659),n=(a(53501),a(21950),a(55888),a(66274),a(84531),a(98168),a(8339),a(40924)),o=a(18791),r=a(45081),s=a(63428),l=a(77664),c=a(61314),d=(a(23006),a(74959)),h=a(7214),u=a(2977);const p=(0,s.kp)(u.H,(0,s.Ik)({entity:(0,s.lq)((0,s.Yj)()),name:(0,s.lq)((0,s.Yj)()),icon:(0,s.lq)((0,s.Yj)()),unit:(0,s.lq)((0,s.Yj)()),stat_type:(0,s.lq)((0,s.Yj)()),period:(0,s.lq)((0,s.bz)()),theme:(0,s.lq)((0,s.Yj)()),footer:(0,s.lq)(h.zb)})),m=["mean","min","max","change"],_={mean:"mean",min:"min",max:"max",change:"sum"},f={today:{calendar:{period:"day"}},yesterday:{calendar:{period:"day",offset:-1}},this_week:{calendar:{period:"week"}},last_week:{calendar:{period:"week",offset:-1}},this_month:{calendar:{period:"month"}},last_month:{calendar:{period:"month",offset:-1}},this_year:{calendar:{period:"year"}},last_year:{calendar:{period:"year",offset:-1}}};let v=(0,i.A)([(0,o.EM)("hui-statistic-card-editor")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.wk)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,o.wk)()],key:"_metadata",value:void 0},{kind:"method",key:"setConfig",value:function(e){(0,s.vA)(e,p),this._config=e,this._fetchMetadata()}},{kind:"method",key:"firstUpdated",value:function(){this._fetchMetadata().then((()=>{var e,t,a;null!==(e=this._config)&&void 0!==e&&e.stat_type||null===(t=this._config)||void 0===t||!t.entity||(0,l.r)(this,"config-changed",{config:{...this._config,stat_type:null!==(a=this._metadata)&&void 0!==a&&a.has_sum?"change":"mean"}})}))}},{kind:"field",key:"_data",value:()=>(0,r.A)((e=>{if(!e||!e.period)return e;for(const[t,a]of Object.entries(f))if((0,c.b)(a,e.period))return{...e,period:t};return e}))},{kind:"field",key:"_schema",value:()=>(0,r.A)(((e,t,a)=>[{name:"entity",required:!0,selector:{statistic:{}}},{name:"stat_type",required:!0,selector:{select:{multiple:!1,options:m.map((e=>({value:e,label:t(`ui.panel.lovelace.editor.card.statistic.stat_type_labels.${e}`),disabled:!a||!(0,d.nN)(a,_[e])})))}}},{name:"period",required:!0,selector:e&&Object.keys(f).includes(e)?{select:{multiple:!1,options:Object.keys(f).map((e=>({value:e,label:t(`ui.panel.lovelace.editor.card.statistic.periods.${e}`)||e})))}}:{object:{}}},{type:"grid",name:"",schema:[{name:"name",selector:{text:{}}},{name:"icon",selector:{icon:{}},context:{icon_entity:"entity"}},{name:"unit",selector:{text:{}}},{name:"theme",selector:{theme:{}}}]}]))},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return n.s6;const e=this._data(this._config),t=this._schema("string"==typeof e.period?e.period:void 0,this.hass.localize,this._metadata);return n.qy` <ha-form .hass="${this.hass}" .data="${e}" .schema="${t}" .computeLabel="${this._computeLabelCallback}" @value-changed="${this._valueChanged}"></ha-form> `}},{kind:"method",key:"_fetchMetadata",value:async function(){this.hass&&this._config&&(this._metadata=(await(0,d.Wr)(this.hass,[this._config.entity]))[0])}},{kind:"method",key:"_valueChanged",value:async function(e){var t;const a={...e.detail.value};if(Object.keys(a).forEach((e=>""===a[e]&&delete a[e])),"string"==typeof a.period){const e=f[a.period];e&&(a.period=e)}if(a.stat_type&&a.entity&&a.entity!==(null===(t=this._metadata)||void 0===t?void 0:t.statistic_id)){var i;const e=null===(i=await(0,d.Wr)(this.hass,[a.entity]))||void 0===i?void 0:i[0];e&&!e.has_sum&&"change"===a.stat_type&&(a.stat_type="mean"),e&&!e.has_mean&&"change"!==a.stat_type&&(a.stat_type="change")}if(!a.stat_type&&a.entity){var n;const e=null===(n=await(0,d.Wr)(this.hass,[a.entity]))||void 0===n?void 0:n[0];a.stat_type=null!=e&&e.has_sum?"change":"mean"}(0,l.r)(this,"config-changed",{config:a})}},{kind:"field",key:"_computeLabelCallback",value(){return e=>"period"===e.name?this.hass.localize("ui.panel.lovelace.editor.card.statistic.period"):"theme"===e.name?`${this.hass.localize("ui.panel.lovelace.editor.card.generic.theme")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})`:this.hass.localize(`ui.panel.lovelace.editor.card.generic.${e.name}`)}}]}}),n.WF)},54293:(e,t,a)=>{a.d(t,{k:()=>h});var i=a(63428);const n=(0,i.Ik)({user:(0,i.Yj)()}),o=(0,i.KC)([(0,i.zM)(),(0,i.Ik)({text:(0,i.lq)((0,i.Yj)()),excemptions:(0,i.lq)((0,i.YO)(n))})]),r=(0,i.Ik)({action:(0,i.eu)("url"),url_path:(0,i.Yj)(),confirmation:(0,i.lq)(o)}),s=(0,i.Ik)({action:(0,i.eu)("call-service"),service:(0,i.Yj)(),service_data:(0,i.lq)((0,i.Ik)()),data:(0,i.lq)((0,i.Ik)()),target:(0,i.lq)((0,i.Ik)({entity_id:(0,i.lq)((0,i.KC)([(0,i.Yj)(),(0,i.YO)((0,i.Yj)())])),device_id:(0,i.lq)((0,i.KC)([(0,i.Yj)(),(0,i.YO)((0,i.Yj)())])),area_id:(0,i.lq)((0,i.KC)([(0,i.Yj)(),(0,i.YO)((0,i.Yj)())]))})),confirmation:(0,i.lq)(o)}),l=(0,i.Ik)({action:(0,i.eu)("navigate"),navigation_path:(0,i.Yj)(),navigation_replace:(0,i.lq)((0,i.zM)()),confirmation:(0,i.lq)(o)}),c=(0,i.NW)({action:(0,i.eu)("assist"),pipeline_id:(0,i.lq)((0,i.Yj)()),start_listening:(0,i.lq)((0,i.zM)())}),d=(0,i.Ik)({action:(0,i.vP)(["none","toggle","more-info","call-service","url","navigate","assist"]),confirmation:(0,i.lq)(o)}),h=(0,i.OR)((e=>{if(e&&"object"==typeof e&&"action"in e)switch(e.action){case"call-service":return s;case"navigate":return l;case"url":return r;case"assist":return c}return d}))},2977:(e,t,a)=>{a.d(t,{H:()=>n});var i=a(63428);const n=(0,i.Ik)({type:(0,i.Yj)(),view_layout:(0,i.bz)(),layout_options:(0,i.bz)(),visibility:(0,i.bz)()})},63775:(e,t,a)=>{a.d(t,{J:()=>o});var i=a(63428),n=a(54293);const o=(0,i.Ik)({entity:(0,i.Yj)(),name:(0,i.lq)((0,i.Yj)()),icon:(0,i.lq)((0,i.Yj)()),image:(0,i.lq)((0,i.Yj)()),show_name:(0,i.lq)((0,i.zM)()),show_icon:(0,i.lq)((0,i.zM)()),tap_action:(0,i.lq)(n.k),hold_action:(0,i.lq)(n.k),double_tap_action:(0,i.lq)(n.k)})},7214:(e,t,a)=>{a.d(t,{oe:()=>l,zb:()=>c});var i=a(63428),n=a(54293),o=a(63775);const r=(0,i.Ik)({type:(0,i.Yj)(),image:(0,i.Yj)(),tap_action:(0,i.lq)(n.k),hold_action:(0,i.lq)(n.k),double_tap_action:(0,i.lq)(n.k),alt_text:(0,i.lq)((0,i.Yj)())}),s=(0,i.Ik)({type:(0,i.Yj)(),entities:(0,i.YO)(o.J)}),l=(0,i.Ik)({type:(0,i.Yj)(),entity:(0,i.Yj)(),detail:(0,i.lq)((0,i.ai)()),hours_to_show:(0,i.lq)((0,i.ai)())}),c=(0,i.OR)((e=>{if(e&&"object"==typeof e&&"type"in e)switch(e.type){case"buttons":return s;case"graph":return l;case"picture":return r}return(0,i.KC)([s,l,r])}))},79372:(e,t,a)=>{var i=a(73155),n=a(33817),o=a(3429),r=a(75077);e.exports=function(e,t){t&&"string"==typeof e||n(e);var a=r(e);return o(n(void 0!==a?i(a,e):e))}},18684:(e,t,a)=>{var i=a(87568),n=a(42509),o=a(30356),r=a(51607),s=a(95124),l=a(79635);i({target:"Array",proto:!0},{flatMap:function(e){var t,a=r(this),i=s(a);return o(e),(t=l(a,0)).length=n(t,a,a,i,0,1,e,arguments.length>1?arguments[1]:void 0),t}})},74991:(e,t,a)=>{a(33523)("flatMap")},69704:(e,t,a)=>{var i=a(87568),n=a(73155),o=a(30356),r=a(33817),s=a(3429),l=a(79372),c=a(23408),d=a(44933),h=a(89385),u=c((function(){for(var e,t,a=this.iterator,i=this.mapper;;){if(t=this.inner)try{if(!(e=r(n(t.next,t.iterator))).done)return e.value;this.inner=null}catch(e){d(a,"throw",e)}if(e=r(n(this.next,a)),this.done=!!e.done)return;try{this.inner=l(i(e.value,this.counter++),!1)}catch(e){d(a,"throw",e)}}}));i({target:"Iterator",proto:!0,real:!0,forced:h},{flatMap:function(e){return r(this),o(e),new u(s(this),{mapper:e,inner:null})}})}};
//# sourceMappingURL=93108.GzPyBoxuCs0.js.map