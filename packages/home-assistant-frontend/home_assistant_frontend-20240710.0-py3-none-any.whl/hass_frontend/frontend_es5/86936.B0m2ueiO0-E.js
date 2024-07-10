"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[86936],{86936:function(e,i,t){t.r(i);var s,a,n,r,o,c,l=t(6238),h=t(94881),d=t(1781),u=t(36683),v=t(89231),p=t(29864),f=t(83647),g=t(8364),m=(t(77052),t(34069),t(40924)),_=t(196),w=t(77664),k=(t(4596),t(95439)),A=t(4940),y=t(14126);(0,g.A)([(0,_.EM)("dialog-matter-reinterview-node")],(function(e,i){var t,g,x=function(i){function t(){var i;(0,v.A)(this,t);for(var s=arguments.length,a=new Array(s),n=0;n<s;n++)a[n]=arguments[n];return i=(0,p.A)(this,t,[].concat(a)),e(i),i}return(0,f.A)(t,i),(0,u.A)(t)}(i);return{F:x,d:[{kind:"field",decorators:[(0,_.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,_.wk)()],key:"device_id",value:void 0},{kind:"field",decorators:[(0,_.wk)()],key:"_status",value:void 0},{kind:"method",key:"showDialog",value:(g=(0,d.A)((0,h.A)().mark((function e(i){return(0,h.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:this.device_id=i.device_id;case 1:case"end":return e.stop()}}),e,this)}))),function(e){return g.apply(this,arguments)})},{kind:"method",key:"render",value:function(){return this.device_id?(0,m.qy)(s||(s=(0,l.A)([' <ha-dialog open @closed="','" .heading="','"> '," </ha-dialog> "])),this.closeDialog,(0,k.l)(this.hass,this.hass.localize("ui.panel.config.matter.reinterview_node.title")),this._status?"started"===this._status?(0,m.qy)(n||(n=(0,l.A)([' <div class="flex-container"> <ha-circular-progress indeterminate></ha-circular-progress> <div class="status"> <p> <b> '," </b> </p> <p> ",' </p> </div> </div> <mwc-button slot="primaryAction" @click="','"> '," </mwc-button> "])),this.hass.localize("ui.panel.config.matter.reinterview_node.in_progress"),this.hass.localize("ui.panel.config.matter.reinterview_node.run_in_background"),this.closeDialog,this.hass.localize("ui.common.close")):"failed"===this._status?(0,m.qy)(r||(r=(0,l.A)([' <div class="flex-container"> <ha-svg-icon .path="','" class="failed"></ha-svg-icon> <div class="status"> <p> ',' </p> </div> </div> <mwc-button slot="primaryAction" @click="','"> '," </mwc-button> "])),"M12,2C17.53,2 22,6.47 22,12C22,17.53 17.53,22 12,22C6.47,22 2,17.53 2,12C2,6.47 6.47,2 12,2M15.59,7L12,10.59L8.41,7L7,8.41L10.59,12L7,15.59L8.41,17L12,13.41L15.59,17L17,15.59L13.41,12L17,8.41L15.59,7Z",this.hass.localize("ui.panel.config.matter.reinterview_node.interview_failed"),this.closeDialog,this.hass.localize("ui.common.close")):"finished"===this._status?(0,m.qy)(o||(o=(0,l.A)([' <div class="flex-container"> <ha-svg-icon .path="','" class="success"></ha-svg-icon> <div class="status"> <p> ',' </p> </div> </div> <mwc-button slot="primaryAction" @click="','"> '," </mwc-button> "])),"M12 2C6.5 2 2 6.5 2 12S6.5 22 12 22 22 17.5 22 12 17.5 2 12 2M10 17L5 12L6.41 10.59L10 14.17L17.59 6.58L19 8L10 17Z",this.hass.localize("ui.panel.config.matter.reinterview_node.interview_complete"),this.closeDialog,this.hass.localize("ui.common.close")):m.s6:(0,m.qy)(a||(a=(0,l.A)([" <p> "," </p> <p> <em> ",' </em> </p> <mwc-button slot="primaryAction" @click="','"> '," </mwc-button> "])),this.hass.localize("ui.panel.config.matter.reinterview_node.introduction"),this.hass.localize("ui.panel.config.matter.reinterview_node.battery_device_warning"),this._startReinterview,this.hass.localize("ui.panel.config.matter.reinterview_node.start_reinterview"))):m.s6}},{kind:"method",key:"_startReinterview",value:(t=(0,d.A)((0,h.A)().mark((function e(){return(0,h.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(this.hass){e.next=2;break}return e.abrupt("return");case 2:return this._status="started",e.prev=3,e.next=6,(0,A.JW)(this.hass,this.device_id);case 6:this._status="finished",e.next=12;break;case 9:e.prev=9,e.t0=e.catch(3),this._status="failed";case 12:case"end":return e.stop()}}),e,this,[[3,9]])}))),function(){return t.apply(this,arguments)})},{kind:"method",key:"closeDialog",value:function(){this.device_id=void 0,this._status=void 0,(0,w.r)(this,"dialog-closed",{dialog:this.localName})}},{kind:"get",static:!0,key:"styles",value:function(){return[y.nA,(0,m.AH)(c||(c=(0,l.A)([".success{color:var(--success-color)}.failed{color:var(--error-color)}.flex-container{display:flex;align-items:center}.stages{margin-top:16px}.stage ha-svg-icon{width:16px;height:16px}.stage{padding:8px}ha-svg-icon{width:68px;height:48px}.flex-container ha-circular-progress,.flex-container ha-svg-icon{margin-right:20px}"])))]}}]}}),m.WF)}}]);
//# sourceMappingURL=86936.B0m2ueiO0-E.js.map