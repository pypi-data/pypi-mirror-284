"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[28464],{28464:function(e,a,i){i.r(a),i.d(a,{PanelView:function(){return _}});var t,r,d,n,o=i(6238),l=i(36683),s=i(89231),c=i(29864),h=i(83647),u=i(8364),v=i(76504),f=i(80792),k=(i(77052),i(21950),i(650),i(68113),i(55888),i(56262),i(8339),i(40924)),p=i(196),b=i(69760),y=i(77664),g=i(12249),w=!1,_=(0,u.A)(null,(function(e,a){var u=function(a){function i(){var a;(0,s.A)(this,i);for(var t=arguments.length,r=new Array(t),d=0;d<t;d++)r[d]=arguments[d];return a=(0,c.A)(this,i,[].concat(r)),e(a),a}return(0,h.A)(i,a),(0,l.A)(i)}(a);return{F:u,d:[{kind:"field",decorators:[(0,p.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,p.MZ)({attribute:!1})],key:"lovelace",value:void 0},{kind:"field",decorators:[(0,p.MZ)({type:Number})],key:"index",value:void 0},{kind:"field",decorators:[(0,p.MZ)({type:Boolean})],key:"isStrategy",value:function(){return!1}},{kind:"field",decorators:[(0,p.MZ)({attribute:!1})],key:"cards",value:function(){return[]}},{kind:"field",decorators:[(0,p.wk)()],key:"_card",value:void 0},{kind:"method",key:"setConfig",value:function(e){}},{kind:"method",key:"willUpdate",value:function(e){var a,t,r;if((0,v.A)((0,f.A)(u.prototype),"willUpdate",this).call(this,e),null!==(a=this.lovelace)&&void 0!==a&&a.editMode&&!w&&(w=!0,i.e(82635).then(i.bind(i,82635))),e.has("cards")&&this._createCard(),e.has("lovelace")){var d=e.get("lovelace");(!e.has("cards")&&(null==d?void 0:d.config)!==(null===(t=this.lovelace)||void 0===t?void 0:t.config)||d&&(null==d?void 0:d.editMode)!==(null===(r=this.lovelace)||void 0===r?void 0:r.editMode))&&this._createCard()}}},{kind:"method",key:"render",value:function(){var e;return(0,k.qy)(t||(t=(0,o.A)([" "," "," "," "])),this.cards.length>1?(0,k.qy)(r||(r=(0,o.A)(["<hui-warning> "," </hui-warning>"])),this.hass.localize("ui.panel.lovelace.editor.view.panel_mode.warning_multiple_cards")):"",this._card,null!==(e=this.lovelace)&&void 0!==e&&e.editMode&&0===this.cards.length?(0,k.qy)(d||(d=(0,o.A)([' <ha-fab .label="','" extended @click="','" class="','"> <ha-svg-icon slot="icon" .path="','"></ha-svg-icon> </ha-fab> '])),this.hass.localize("ui.panel.lovelace.editor.edit_card.add"),this._addCard,(0,b.H)({rtl:(0,g.qC)(this.hass)}),"M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z"):"")}},{kind:"method",key:"_addCard",value:function(){(0,y.r)(this,"ll-create-card")}},{kind:"method",key:"_createCard",value:function(){var e;if(0!==this.cards.length){var a=this.cards[0];if(a.isPanel=!0,this.isStrategy||null===(e=this.lovelace)||void 0===e||!e.editMode)return a.preview=!1,void(this._card=a);var i=document.createElement("hui-card-options");i.hass=this.hass,i.lovelace=this.lovelace,i.path=[this.index,0],i.hidePosition=!0,a.preview=!0,i.appendChild(a),this._card=i}else this._card=void 0}},{kind:"get",static:!0,key:"styles",value:function(){return(0,k.AH)(n||(n=(0,o.A)([":host{display:block;height:100%;--restore-card-border-radius:var(--ha-card-border-radius, 12px);--restore-card-border-width:var(--ha-card-border-width, 1px);--restore-card-box-shadow:var(--ha-card-box-shadow, none)}*{--ha-card-border-radius:0;--ha-card-border-width:0;--ha-card-box-shadow:none}ha-fab{position:fixed;right:calc(16px + env(safe-area-inset-right));bottom:calc(16px + env(safe-area-inset-bottom));z-index:1;float:var(--float-end);inset-inline-end:calc(16px + env(safe-area-inset-right));inset-inline-start:initial}"])))}}]}}),k.WF);customElements.define("hui-panel-view",_)}}]);
//# sourceMappingURL=28464.6JmtTO_Cnq4.js.map