export const id=82635;export const ids=[82635];export const modules={52008:(e,i,t)=>{t.d(i,{X:()=>o});t(21950),t(55888),t(8339);var a=t(77664);const o=(e,i)=>{(0,a.r)(e,"show-dialog",{dialogTag:"hui-dialog-select-view",dialogImport:()=>Promise.all([t.e(22658),t.e(50988),t.e(32503),t.e(88436),t.e(64351)]).then(t.bind(t,64351)),dialogParams:i})}},82635:(e,i,t)=>{t.r(i);t(32154);var a=t(62659),o=(t(21950),t(55888),t(8339),t(58068),t(92518)),s=t(40924),l=t(18791),c=t(24930),n=t(77664),d=(t(59151),t(12731),t(39335),t(79861)),r=t(47387),h=t(98876),p=t(14126),v=t(9742),u=t(40068),g=t(62679),f=t(44497),k=t(67549),m=t(52008),_=t(83882);(0,a.A)([(0,l.EM)("hui-card-options")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,l.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,l.MZ)({attribute:!1})],key:"lovelace",value:void 0},{kind:"field",decorators:[(0,l.MZ)({type:Array})],key:"path",value:void 0},{kind:"field",decorators:[(0,l.gZ)()],key:"_assignedNodes",value:void 0},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"hidePosition",value:()=>!1},{kind:"field",decorators:[(0,c.I)({key:"lovelaceClipboard",state:!1,subscribe:!1,storage:"sessionStorage"})],key:"_clipboard",value:void 0},{kind:"method",key:"getCardSize",value:function(){return this._assignedNodes?(0,u.Z)(this._assignedNodes[0]):1}},{kind:"method",key:"updated",value:function(e){if(!e.has("path")||!this.path)return;const{viewIndex:i}=(0,k.gO)(this.path);this.classList.toggle("panel",this.lovelace.config.views[i].panel)}},{kind:"get",key:"_cards",value:function(){const e=(0,k.S2)(this.path);return(0,k.MJ)(this.lovelace.config,e)}},{kind:"method",key:"render",value:function(){const{cardIndex:e}=(0,k.gO)(this.path);return s.qy` <div class="card"><slot></slot></div> <ha-card> <div class="card-actions"> <mwc-button @click="${this._editCard}">${this.hass.localize("ui.panel.lovelace.editor.edit_card.edit")}</mwc-button> <div class="right"> <slot name="buttons"></slot> ${this.hidePosition?s.s6:s.qy` <ha-icon-button .label="${this.hass.localize("ui.panel.lovelace.editor.edit_card.decrease_position")}" .path="${"M19,13H5V11H19V13Z"}" class="move-arrow" @click="${this._decreaseCardPosiion}" ?disabled="${0===e}"></ha-icon-button> <ha-icon-button @click="${this._changeCardPosition}" .label="${this.hass.localize("ui.panel.lovelace.editor.edit_card.change_position")}"> <div class="position-badge">${e+1}</div> </ha-icon-button> <ha-icon-button .label="${this.hass.localize("ui.panel.lovelace.editor.edit_card.increase_position")}" .path="${"M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z"}" class="move-arrow" @click="${this._increaseCardPosition}" .disabled="${this._cards.length===e+1}"></ha-icon-button> `} <ha-button-menu @action="${this._handleAction}"> <ha-icon-button slot="trigger" .label="${this.hass.localize("ui.panel.lovelace.editor.edit_card.options")}" .path="${"M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z"}"></ha-icon-button> <ha-list-item graphic="icon"> <ha-svg-icon slot="graphic" .path="${"M14 2H6C4.9 2 4 2.9 4 4V20C4 20.41 4.12 20.8 4.34 21.12C4.41 21.23 4.5 21.33 4.59 21.41C4.95 21.78 5.45 22 6 22H13.53C13 21.42 12.61 20.75 12.35 20H6V4H13V9H18V12C18.7 12 19.37 12.12 20 12.34V8L14 2M18 23L23 18.5L20 15.8L18 14V17H14V20H18V23Z"}"></ha-svg-icon> ${this.hass.localize("ui.panel.lovelace.editor.edit_card.move")} </ha-list-item> <ha-list-item graphic="icon"> <ha-svg-icon slot="graphic" .path="${"M11,17H4A2,2 0 0,1 2,15V3A2,2 0 0,1 4,1H16V3H4V15H11V13L15,16L11,19V17M19,21V7H8V13H6V7A2,2 0 0,1 8,5H19A2,2 0 0,1 21,7V21A2,2 0 0,1 19,23H8A2,2 0 0,1 6,21V19H8V21H19Z"}"></ha-svg-icon> ${this.hass.localize("ui.panel.lovelace.editor.edit_card.duplicate")} </ha-list-item> <ha-list-item graphic="icon"> <ha-svg-icon slot="graphic" .path="${"M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z"}"></ha-svg-icon> ${this.hass.localize("ui.panel.lovelace.editor.edit_card.copy")} </ha-list-item> <ha-list-item graphic="icon"> <ha-svg-icon slot="graphic" .path="${"M19,3L13,9L15,11L22,4V3M12,12.5A0.5,0.5 0 0,1 11.5,12A0.5,0.5 0 0,1 12,11.5A0.5,0.5 0 0,1 12.5,12A0.5,0.5 0 0,1 12,12.5M6,20A2,2 0 0,1 4,18C4,16.89 4.9,16 6,16A2,2 0 0,1 8,18C8,19.11 7.1,20 6,20M6,8A2,2 0 0,1 4,6C4,4.89 4.9,4 6,4A2,2 0 0,1 8,6C8,7.11 7.1,8 6,8M9.64,7.64C9.87,7.14 10,6.59 10,6A4,4 0 0,0 6,2A4,4 0 0,0 2,6A4,4 0 0,0 6,10C6.59,10 7.14,9.87 7.64,9.64L10,12L7.64,14.36C7.14,14.13 6.59,14 6,14A4,4 0 0,0 2,18A4,4 0 0,0 6,22A4,4 0 0,0 10,18C10,17.41 9.87,16.86 9.64,16.36L12,14L19,21H22V20L9.64,7.64Z"}"></ha-svg-icon> ${this.hass.localize("ui.panel.lovelace.editor.edit_card.cut")} </ha-list-item> <li divider role="separator"></li> <ha-list-item class="warning" graphic="icon"> <ha-svg-icon class="warning" slot="graphic" .path="${"M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"}"></ha-svg-icon> ${this.hass.localize("ui.panel.lovelace.editor.edit_card.delete")} </ha-list-item> </ha-button-menu> </div> </div> </ha-card> `}},{kind:"get",static:!0,key:"styles",value:function(){return[p.RF,s.AH`:host(:hover){outline:2px solid var(--primary-color)}:host(:not(.panel)) ::slotted(*){display:block}:host(.panel) .card{height:calc(100% - 59px)}ha-card{border-top-right-radius:0;border-top-left-radius:0}.card-actions{display:flex;justify-content:space-between;align-items:center}.right{display:flex;align-items:center}.position-badge{display:block;width:24px;line-height:24px;box-sizing:border-box;border-radius:50%;font-weight:500;text-align:center;font-size:14px;background-color:var(--app-header-edit-background-color,#455a64);color:var(--app-header-edit-text-color,#fff)}ha-icon-button{color:var(--primary-text-color)}ha-icon-button.move-arrow[disabled]{color:var(--disabled-text-color)}ha-list-item{cursor:pointer;white-space:nowrap}`]}},{kind:"method",key:"_handleAction",value:function(e){switch(e.detail.index){case 0:this._moveCard();break;case 1:this._duplicateCard();break;case 2:this._copyCard();break;case 3:this._cutCard();break;case 4:this._deleteCard(!0)}}},{kind:"method",key:"_duplicateCard",value:function(){const{cardIndex:e}=(0,k.gO)(this.path),i=(0,k.S2)(this.path),t=this._cards[e];(0,g.O)(this,{lovelaceConfig:this.lovelace.config,saveConfig:this.lovelace.saveConfig,path:i,cardConfig:t})}},{kind:"method",key:"_editCard",value:function(){(0,n.r)(this,"ll-edit-card",{path:this.path})}},{kind:"method",key:"_cutCard",value:function(){this._copyCard(),this._deleteCard(!1)}},{kind:"method",key:"_copyCard",value:function(){const{cardIndex:e}=(0,k.gO)(this.path),i=this._cards[e];this._clipboard=(0,o.A)(i)}},{kind:"method",key:"_decreaseCardPosiion",value:function(){const e=this.lovelace,i=this.path,{cardIndex:t}=(0,k.gO)(i);e.saveConfig((0,f.d6)(e.config,i,t-1))}},{kind:"method",key:"_increaseCardPosition",value:function(){const e=this.lovelace,i=this.path,{cardIndex:t}=(0,k.gO)(i);e.saveConfig((0,f.d6)(e.config,i,t+1))}},{kind:"method",key:"_changeCardPosition",value:async function(){const e=this.lovelace,i=this.path,{cardIndex:t}=(0,k.gO)(i),a=await(0,h.showPromptDialog)(this,{title:this.hass.localize("ui.panel.lovelace.editor.change_position.title"),text:this.hass.localize("ui.panel.lovelace.editor.change_position.text"),inputType:"number",inputMin:"1",placeholder:String(t+1)});if(!a)return;const o=parseInt(a);if(isNaN(o))return;const s=o-1;e.saveConfig((0,f.d6)(e.config,i,s))}},{kind:"method",key:"_moveCard",value:function(){(0,m.X)(this,{lovelaceConfig:this.lovelace.config,urlPath:this.lovelace.urlPath,allowDashboardChange:!0,header:this.hass.localize("ui.panel.lovelace.editor.move_card.header"),viewSelectedCallback:async(e,i,t)=>{const a=i.views[t];if((0,r.R)(a)||a.type!==_.LQ){if(e===this.lovelace.urlPath)return this.lovelace.saveConfig((0,f.Ei)(this.lovelace.config,this.path,[t])),void(0,v.f)(this,this.hass);try{const{cardIndex:a}=(0,k.gO)(this.path);await(0,d.ql)(this.hass,e,(0,f.gm)(i,[t],this._cards[a])),this.lovelace.saveConfig((0,f.GO)(this.lovelace.config,this.path)),(0,v.f)(this,this.hass)}catch(e){(0,h.showAlertDialog)(this,{text:`Moving failed: ${e.message}`})}}else(0,h.showAlertDialog)(this,{title:this.hass.localize("ui.panel.lovelace.editor.move_card.error_title"),text:this.hass.localize("ui.panel.lovelace.editor.move_card.error_text_section"),warning:!0})}})}},{kind:"method",key:"_deleteCard",value:function(e){(0,n.r)(this,"ll-delete-card",{path:this.path,confirm:e})}}]}}),s.WF);var b=t(43055),C=t(22360);(0,b.a)(),(0,C.d)(),(0,g.S)()},9742:(e,i,t)=>{t.d(i,{f:()=>o});var a=t(75610);const o=(e,i)=>(0,a.P)(e,{message:i.localize("ui.common.successfully_saved")})}};
//# sourceMappingURL=82635.Rll6qOFi5rs.js.map