export const id=19915;export const ids=[19915];export const modules={19915:(t,i,e)=>{e.a(t,(async(t,s)=>{try{e.r(i);var n=e(62659),o=(e(27934),e(21950),e(66274),e(22836),e(8339),e(40924)),a=e(18791),r=e(7383),h=e(47038),u=(e(78337),e(15821)),c=e(21242),d=e(76158),g=t([c]);c=(g.then?(await g)():g)[0];(0,n.A)([(0,a.EM)("hui-group-entity-row")],(function(t,i){return{F:class extends i{constructor(...i){super(...i),t(this)}},d:[{kind:"field",decorators:[(0,a.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_config",value:void 0},{kind:"method",key:"_computeCanToggle",value:function(t,i){return i.some((i=>{const e=(0,h.m)(i);var s;return"group"===e?this._computeCanToggle(t,null===(s=this.hass)||void 0===s?void 0:s.states[i].attributes.entity_id):r.FD.has(e)}))}},{kind:"method",key:"setConfig",value:function(t){if(!t)throw new Error("Invalid configuration");this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return(0,u.LX)(this,t)}},{kind:"method",key:"render",value:function(){if(!this._config||!this.hass)return o.s6;const t=this.hass.states[this._config.entity];return t?o.qy` <hui-generic-entity-row .hass="${this.hass}" .config="${this._config}"> ${this._computeCanToggle(this.hass,t.attributes.entity_id)?o.qy` <ha-entity-toggle .hass="${this.hass}" .stateObj="${t}"></ha-entity-toggle> `:o.qy` <div class="text-content"> ${this.hass.formatEntityState(t)} </div> `} </hui-generic-entity-row> `:o.qy` <hui-warning> ${(0,d.j)(this.hass,this._config.entity)} </hui-warning> `}}]}}),o.WF);s()}catch(t){s(t)}}))}};
//# sourceMappingURL=19915.QEbds7lUu5o.js.map