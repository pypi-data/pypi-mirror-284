export const id=68227;export const ids=[68227];export const modules={15696:(e,t,i)=>{i.d(t,{j:()=>a});const a=["relative","total","date","time","datetime"]},68227:(e,t,i)=>{i.a(e,(async(e,a)=>{try{i.r(t),i.d(t,{HuiGlanceCardEditor:()=>v});var n=i(62659),o=(i(21950),i(8339),i(40924)),s=i(18791),l=i(63428),c=i(77664),r=(i(23006),i(90353)),d=i(12851),h=i(2977),u=i(30322),m=e([r]);r=(m.then?(await m)():m)[0];const _=(0,l.kp)(h.H,(0,l.Ik)({title:(0,l.lq)((0,l.KC)([(0,l.Yj)(),(0,l.ai)()])),theme:(0,l.lq)((0,l.Yj)()),columns:(0,l.lq)((0,l.ai)()),show_name:(0,l.lq)((0,l.zM)()),show_state:(0,l.lq)((0,l.zM)()),show_icon:(0,l.lq)((0,l.zM)()),state_color:(0,l.lq)((0,l.zM)()),entities:(0,l.YO)(u.l)})),g=[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"columns",selector:{number:{min:1,mode:"box"}}},{name:"theme",selector:{theme:{}}}]},{name:"",type:"grid",column_min_width:"100px",schema:[{name:"show_name",selector:{boolean:{}}},{name:"show_icon",selector:{boolean:{}}},{name:"show_state",selector:{boolean:{}}}]},{name:"state_color",selector:{boolean:{}}}];let v=(0,n.A)([(0,s.EM)("hui-glance-card-editor")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,s.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.wk)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,s.wk)()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function(e){(0,l.vA)(e,_),this._config=e,this._configEntities=(0,d._)(e.entities)}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return o.s6;const e={show_name:!0,show_icon:!0,show_state:!0,...this._config};return o.qy` <ha-form .hass="${this.hass}" .data="${e}" .schema="${g}" .computeLabel="${this._computeLabelCallback}" @value-changed="${this._valueChanged}"></ha-form> <hui-entity-editor .hass="${this.hass}" .entities="${this._configEntities}" @entities-changed="${this._entitiesChanged}"></hui-entity-editor> `}},{kind:"method",key:"_valueChanged",value:function(e){const t=e.detail.value;(0,c.r)(this,"config-changed",{config:t})}},{kind:"method",key:"_entitiesChanged",value:function(e){let t=this._config;t={...t,entities:e.detail.entities},this._configEntities=(0,d._)(this._config.entities),(0,c.r)(this,"config-changed",{config:t})}},{kind:"field",key:"_computeLabelCallback",value(){return e=>{switch(e.name){case"theme":return`${this.hass.localize("ui.panel.lovelace.editor.card.generic.theme")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})`;case"columns":return this.hass.localize(`ui.panel.lovelace.editor.card.glance.${e.name}`);default:return this.hass.localize(`ui.panel.lovelace.editor.card.generic.${e.name}`)}}}}]}}),o.WF);a()}catch(e){a(e)}}))},54293:(e,t,i)=>{i.d(t,{k:()=>h});var a=i(63428);const n=(0,a.Ik)({user:(0,a.Yj)()}),o=(0,a.KC)([(0,a.zM)(),(0,a.Ik)({text:(0,a.lq)((0,a.Yj)()),excemptions:(0,a.lq)((0,a.YO)(n))})]),s=(0,a.Ik)({action:(0,a.eu)("url"),url_path:(0,a.Yj)(),confirmation:(0,a.lq)(o)}),l=(0,a.Ik)({action:(0,a.eu)("call-service"),service:(0,a.Yj)(),service_data:(0,a.lq)((0,a.Ik)()),data:(0,a.lq)((0,a.Ik)()),target:(0,a.lq)((0,a.Ik)({entity_id:(0,a.lq)((0,a.KC)([(0,a.Yj)(),(0,a.YO)((0,a.Yj)())])),device_id:(0,a.lq)((0,a.KC)([(0,a.Yj)(),(0,a.YO)((0,a.Yj)())])),area_id:(0,a.lq)((0,a.KC)([(0,a.Yj)(),(0,a.YO)((0,a.Yj)())]))})),confirmation:(0,a.lq)(o)}),c=(0,a.Ik)({action:(0,a.eu)("navigate"),navigation_path:(0,a.Yj)(),navigation_replace:(0,a.lq)((0,a.zM)()),confirmation:(0,a.lq)(o)}),r=(0,a.NW)({action:(0,a.eu)("assist"),pipeline_id:(0,a.lq)((0,a.Yj)()),start_listening:(0,a.lq)((0,a.zM)())}),d=(0,a.Ik)({action:(0,a.vP)(["none","toggle","more-info","call-service","url","navigate","assist"]),confirmation:(0,a.lq)(o)}),h=(0,a.OR)((e=>{if(e&&"object"==typeof e&&"action"in e)switch(e.action){case"call-service":return l;case"navigate":return c;case"url":return s;case"assist":return r}return d}))},2977:(e,t,i)=>{i.d(t,{H:()=>n});var a=i(63428);const n=(0,a.Ik)({type:(0,a.Yj)(),view_layout:(0,a.bz)(),layout_options:(0,a.bz)(),visibility:(0,a.bz)()})},30322:(e,t,i)=>{i.d(t,{l:()=>s});var a=i(63428),n=i(15696),o=i(54293);const s=(0,a.KC)([(0,a.Ik)({entity:(0,a.Yj)(),name:(0,a.lq)((0,a.Yj)()),icon:(0,a.lq)((0,a.Yj)()),image:(0,a.lq)((0,a.Yj)()),secondary_info:(0,a.lq)((0,a.Yj)()),format:(0,a.lq)((0,a.vP)(n.j)),state_color:(0,a.lq)((0,a.zM)()),tap_action:(0,a.lq)(o.k),hold_action:(0,a.lq)(o.k),double_tap_action:(0,a.lq)(o.k)}),(0,a.Yj)()])}};
//# sourceMappingURL=68227.FP_oupDG2W0.js.map