(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[50320],{24930:function(e,t,i){"use strict";i.d(t,{I:function(){return s}});var n=i(89231),o=i(36683),a=(i(75658),i(71936),i(60060),i(59092),i(43859),i(1158),i(68113),i(66274),i(84531),i(32877),i(34290),function(){return(0,o.A)((function e(){var t=this,i=arguments.length>0&&void 0!==arguments[0]?arguments[0]:window.localStorage;(0,n.A)(this,e),this.storage=void 0,this._storage={},this._listeners={},this.storage=i,i===window.localStorage&&window.addEventListener("storage",(function(e){e.key&&t.hasKey(e.key)&&(t._storage[e.key]=e.newValue?JSON.parse(e.newValue):e.newValue,t._listeners[e.key]&&t._listeners[e.key].forEach((function(i){return i(e.oldValue?JSON.parse(e.oldValue):e.oldValue,t._storage[e.key])})))}))}),[{key:"addFromStorage",value:function(e){if(!this._storage[e]){var t=this.storage.getItem(e);t&&(this._storage[e]=JSON.parse(t))}}},{key:"subscribeChanges",value:function(e,t){var i=this;return this._listeners[e]?this._listeners[e].push(t):this._listeners[e]=[t],function(){i.unsubscribeChanges(e,t)}}},{key:"unsubscribeChanges",value:function(e,t){if(e in this._listeners){var i=this._listeners[e].indexOf(t);-1!==i&&this._listeners[e].splice(i,1)}}},{key:"hasKey",value:function(e){return e in this._storage}},{key:"getValue",value:function(e){return this._storage[e]}},{key:"setValue",value:function(e,t){var i=this._storage[e];this._storage[e]=t;try{void 0===t?this.storage.removeItem(e):this.storage.setItem(e,JSON.stringify(t))}catch(n){}finally{this._listeners[e]&&this._listeners[e].forEach((function(e){return e(i,t)}))}}}])}()),r={},s=function(e){return function(t){var i,n=e.storage||"localStorage";n&&n in r?i=r[n]:(i=new a(window[n]),r[n]=i);var o=String(t.key),s=e.key||String(t.key),d=t.initializer?t.initializer():void 0;i.addFromStorage(s);var l=!1!==e.subscribe?function(e){return i.subscribeChanges(s,(function(i,n){e.requestUpdate(t.key,i)}))}:void 0,c=function(){return i.hasKey(s)?e.deserializer?e.deserializer(i.getValue(s)):i.getValue(s):d};return{kind:"method",placement:"prototype",key:t.key,descriptor:{set:function(n){!function(n,o){var a;e.state&&(a=c()),i.setValue(s,e.serializer?e.serializer(o):o),e.state&&n.requestUpdate(t.key,a)}(this,n)},get:function(){return c()},enumerable:!0,configurable:!0},finisher:function(i){if(e.state&&e.subscribe){var n=i.prototype.connectedCallback,a=i.prototype.disconnectedCallback;i.prototype.connectedCallback=function(){n.call(this),this["__unbsubLocalStorage".concat(o)]=null==l?void 0:l(this)},i.prototype.disconnectedCallback=function(){var e;a.call(this),null===(e=this["__unbsubLocalStorage".concat(o)])||void 0===e||e.call(this),this["__unbsubLocalStorage".concat(o)]=void 0}}e.state&&i.createProperty(t.key,Object.assign({noAccessor:!0},e.stateOptions))}}}}},59151:function(e,t,i){"use strict";var n,o,a=i(6238),r=i(36683),s=i(89231),d=i(29864),l=i(83647),c=i(8364),u=i(76504),h=i(80792),p=(i(77052),i(650),i(68113),i(58177),i(42416),i(66274),i(84531),i(34290),i(27350),i(40924)),v=i(196),g=i(51150),f=i(25465);(0,c.A)([(0,v.EM)("ha-button-menu")],(function(e,t){var i=function(t){function i(){var t;(0,s.A)(this,i);for(var n=arguments.length,o=new Array(n),a=0;a<n;a++)o[a]=arguments[a];return t=(0,d.A)(this,i,[].concat(o)),e(t),t}return(0,l.A)(i,t),(0,r.A)(i)}(t);return{F:i,d:[{kind:"field",key:f.Xr,value:void 0},{kind:"field",decorators:[(0,v.MZ)()],key:"corner",value:function(){return"BOTTOM_START"}},{kind:"field",decorators:[(0,v.MZ)()],key:"menuCorner",value:function(){return"START"}},{kind:"field",decorators:[(0,v.MZ)({type:Number})],key:"x",value:function(){return null}},{kind:"field",decorators:[(0,v.MZ)({type:Number})],key:"y",value:function(){return null}},{kind:"field",decorators:[(0,v.MZ)({type:Boolean})],key:"multi",value:function(){return!1}},{kind:"field",decorators:[(0,v.MZ)({type:Boolean})],key:"activatable",value:function(){return!1}},{kind:"field",decorators:[(0,v.MZ)({type:Boolean})],key:"disabled",value:function(){return!1}},{kind:"field",decorators:[(0,v.MZ)({type:Boolean})],key:"fixed",value:function(){return!1}},{kind:"field",decorators:[(0,v.MZ)({type:Boolean,attribute:"no-anchor"})],key:"noAnchor",value:function(){return!1}},{kind:"field",decorators:[(0,v.P)("mwc-menu",!0)],key:"_menu",value:void 0},{kind:"get",key:"items",value:function(){var e;return null===(e=this._menu)||void 0===e?void 0:e.items}},{kind:"get",key:"selected",value:function(){var e;return null===(e=this._menu)||void 0===e?void 0:e.selected}},{kind:"method",key:"focus",value:function(){var e,t;null!==(e=this._menu)&&void 0!==e&&e.open?this._menu.focusItemAtIndex(0):null===(t=this._triggerButton)||void 0===t||t.focus()}},{kind:"method",key:"render",value:function(){return(0,p.qy)(n||(n=(0,a.A)([' <div @click="','"> <slot name="trigger" @slotchange="','"></slot> </div> <mwc-menu .corner="','" .menuCorner="','" .fixed="','" .multi="','" .activatable="','" .y="','" .x="','"> <slot></slot> </mwc-menu> '])),this._handleClick,this._setTriggerAria,this.corner,this.menuCorner,this.fixed,this.multi,this.activatable,this.y,this.x)}},{kind:"method",key:"firstUpdated",value:function(e){var t=this;(0,u.A)((0,h.A)(i.prototype),"firstUpdated",this).call(this,e),"rtl"===g.G.document.dir&&this.updateComplete.then((function(){t.querySelectorAll("mwc-list-item").forEach((function(e){var t=document.createElement("style");t.innerHTML="span.material-icons:first-of-type { margin-left: var(--mdc-list-item-graphic-margin, 32px) !important; margin-right: 0px !important;}",e.shadowRoot.appendChild(t)}))}))}},{kind:"method",key:"_handleClick",value:function(){this.disabled||(this._menu.anchor=this.noAnchor?null:this,this._menu.show())}},{kind:"get",key:"_triggerButton",value:function(){return this.querySelector('ha-icon-button[slot="trigger"], mwc-button[slot="trigger"]')}},{kind:"method",key:"_setTriggerAria",value:function(){this._triggerButton&&(this._triggerButton.ariaHasPopup="menu")}},{kind:"get",static:!0,key:"styles",value:function(){return(0,p.AH)(o||(o=(0,a.A)([":host{display:inline-block;position:relative}::slotted([disabled]){color:var(--disabled-text-color)}"])))}}]}}),p.WF)},25285:function(e,t,i){"use strict";var n,o,a=i(6238),r=i(36683),s=i(89231),d=i(29864),l=i(83647),c=i(8364),u=(i(77052),i(40924)),h=i(196);(0,c.A)([(0,h.EM)("ha-dialog-header")],(function(e,t){var i=function(t){function i(){var t;(0,s.A)(this,i);for(var n=arguments.length,o=new Array(n),a=0;a<n;a++)o[a]=arguments[a];return t=(0,d.A)(this,i,[].concat(o)),e(t),t}return(0,l.A)(i,t),(0,r.A)(i)}(t);return{F:i,d:[{kind:"method",key:"render",value:function(){return(0,u.qy)(n||(n=(0,a.A)([' <header class="header"> <div class="header-bar"> <section class="header-navigation-icon"> <slot name="navigationIcon"></slot> </section> <section class="header-title"> <slot name="title"></slot> </section> <section class="header-action-items"> <slot name="actionItems"></slot> </section> </div> <slot></slot> </header> '])))}},{kind:"get",static:!0,key:"styles",value:function(){return[(0,u.AH)(o||(o=(0,a.A)([":host{display:block}:host([show-border]){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.header-bar{display:flex;flex-direction:row;align-items:flex-start;padding:4px;box-sizing:border-box}.header-title{flex:1;font-size:22px;line-height:28px;font-weight:400;padding:10px 4px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}@media all and (min-width:450px) and (min-height:500px){.header-bar{padding:12px}}.header-navigation-icon{flex:none;min-width:8px;height:100%;display:flex;flex-direction:row}.header-action-items{flex:none;min-width:8px;height:100%;display:flex;flex-direction:row}"])))]}}]}}),u.WF)},95439:function(e,t,i){"use strict";i.d(t,{l:function(){return k}});var n,o,a,r=i(36683),s=i(89231),d=i(29864),l=i(83647),c=i(8364),u=i(76504),h=i(80792),p=i(6238),v=(i(86176),i(77052),i(53156),i(12387)),g=i(52280),f=i(40924),m=i(196),_=i(25465),y=(i(12731),["button","ha-list-item"]),k=function(e,t){var i;return(0,f.qy)(n||(n=(0,p.A)([' <div class="header_title"> <span>','</span> <ha-icon-button .label="','" .path="','" dialogAction="close" class="header_button"></ha-icon-button> </div> '])),t,null!==(i=null==e?void 0:e.localize("ui.dialogs.generic.close"))&&void 0!==i?i:"Close","M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z")};(0,c.A)([(0,m.EM)("ha-dialog")],(function(e,t){var i=function(t){function i(){var t;(0,s.A)(this,i);for(var n=arguments.length,o=new Array(n),a=0;a<n;a++)o[a]=arguments[a];return t=(0,d.A)(this,i,[].concat(o)),e(t),t}return(0,l.A)(i,t),(0,r.A)(i)}(t);return{F:i,d:[{kind:"field",key:_.Xr,value:void 0},{kind:"method",key:"scrollToPos",value:function(e,t){var i;null===(i=this.contentElement)||void 0===i||i.scrollTo(e,t)}},{kind:"method",key:"renderHeading",value:function(){return(0,f.qy)(o||(o=(0,p.A)(['<slot name="heading"> '," </slot>"])),(0,u.A)((0,h.A)(i.prototype),"renderHeading",this).call(this))}},{kind:"method",key:"firstUpdated",value:function(){var e;(0,u.A)((0,h.A)(i.prototype),"firstUpdated",this).call(this),this.suppressDefaultPressSelector=[this.suppressDefaultPressSelector,y].join(", "),this._updateScrolledAttribute(),null===(e=this.contentElement)||void 0===e||e.addEventListener("scroll",this._onScroll,{passive:!0})}},{kind:"method",key:"disconnectedCallback",value:function(){(0,u.A)((0,h.A)(i.prototype),"disconnectedCallback",this).call(this),this.contentElement.removeEventListener("scroll",this._onScroll)}},{kind:"field",key:"_onScroll",value:function(){var e=this;return function(){e._updateScrolledAttribute()}}},{kind:"method",key:"_updateScrolledAttribute",value:function(){this.contentElement&&this.toggleAttribute("scrolled",0!==this.contentElement.scrollTop)}},{kind:"field",static:!0,key:"styles",value:function(){return[g.R,(0,f.AH)(a||(a=(0,p.A)([":host([scrolled]) ::slotted(ha-dialog-header){border-bottom:1px solid var(--mdc-dialog-scroll-divider-color,rgba(0,0,0,.12))}.mdc-dialog{--mdc-dialog-scroll-divider-color:var(\n          --dialog-scroll-divider-color,\n          var(--divider-color)\n        );z-index:var(--dialog-z-index,8);-webkit-backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));backdrop-filter:var(--ha-dialog-scrim-backdrop-filter,var(--dialog-backdrop-filter,none));--mdc-dialog-box-shadow:var(--dialog-box-shadow, none);--mdc-typography-headline6-font-weight:400;--mdc-typography-headline6-font-size:1.574rem}.mdc-dialog__actions{justify-content:var(--justify-action-buttons,flex-end);padding-bottom:max(env(safe-area-inset-bottom),24px)}.mdc-dialog__actions span:first-child{flex:var(--secondary-action-button-flex,unset)}.mdc-dialog__actions span:nth-child(2){flex:var(--primary-action-button-flex,unset)}.mdc-dialog__container{align-items:var(--vertical-align-dialog,center)}.mdc-dialog__title{padding:24px 24px 0 24px}.mdc-dialog__actions{padding:12px 24px 12px 24px}.mdc-dialog__title::before{content:unset}.mdc-dialog .mdc-dialog__content{position:var(--dialog-content-position,relative);padding:var(--dialog-content-padding,24px)}:host([hideactions]) .mdc-dialog .mdc-dialog__content{padding-bottom:max(var(--dialog-content-padding,24px),env(safe-area-inset-bottom))}.mdc-dialog .mdc-dialog__surface{position:var(--dialog-surface-position,relative);top:var(--dialog-surface-top);margin-top:var(--dialog-surface-margin-top);min-height:var(--mdc-dialog-min-height,auto);border-radius:var(--ha-dialog-border-radius,28px);-webkit-backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);backdrop-filter:var(--ha-dialog-surface-backdrop-filter,none);background:var(--ha-dialog-surface-background,var(--mdc-theme-surface,#fff))}:host([flexContent]) .mdc-dialog .mdc-dialog__content{display:flex;flex-direction:column}.header_title{position:relative;padding-right:40px;padding-inline-end:40px;padding-inline-start:initial;direction:var(--direction)}.header_title span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block}.header_button{position:absolute;right:-12px;top:-12px;text-decoration:none;color:inherit;inset-inline-start:initial;inset-inline-end:-12px;direction:var(--direction)}.dialog-actions{inset-inline-start:initial!important;inset-inline-end:0px!important;direction:var(--direction)}"])))]}}]}}),v.u)},96249:function(e,t,i){"use strict";i.r(t),i.d(t,{HaVoiceCommandDialog:function(){return H}});var n,o,a,r,s,d,l,c,u,h,p,v,g=i(66123),f=i(61780),m=i(6238),_=i(94881),y=i(1781),k=i(36683),b=i(89231),x=i(29864),A=i(83647),w=i(8364),L=i(76504),M=i(80792),S=(i(77052),i(21950),i(36724),i(71936),i(52107),i(75191),i(55974),i(61842),i(848),i(68113),i(64148),i(92321),i(69099),i(18862),i(2068),i(2456),i(80274),i(4533),i(11064),i(69881),i(11417),i(52716),i(77056),i(82206),i(8225),i(43917),i(24463),i(67642),i(17265),i(11833),i(1618),i(43273),i(63527),i(74525),i(17695),i(82499),i(71296),i(64347),i(20661),i(69330),i(70038),i(49799),i(98168),i(34069),i(40924)),C=i(196),I=i(24930),B=i(77664),z=i(48962),q=(i(99535),i(59151),i(95439),i(25285),i(12731),i(39335),i(42398),i(7615)),E=i(14126),P=i(35126),U=i(92483),V=i(98876),H=(0,w.A)([(0,C.EM)("ha-voice-command-dialog")],(function(e,t){var i,w,H,T,Z,R,N,D,F=function(t){function i(){var t;(0,b.A)(this,i);for(var n=arguments.length,o=new Array(n),a=0;a<n;a++)o[a]=arguments[a];return t=(0,x.A)(this,i,[].concat(o)),e(t),t}return(0,A.A)(i,t),(0,k.A)(i)}(t);return{F:F,d:[{kind:"field",decorators:[(0,C.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,C.wk)()],key:"_conversation",value:void 0},{kind:"field",decorators:[(0,C.wk)()],key:"_opened",value:function(){return!1}},{kind:"field",decorators:[(0,I.I)({key:"AssistPipelineId",state:!0,subscribe:!1})],key:"_pipelineId",value:void 0},{kind:"field",decorators:[(0,C.wk)()],key:"_pipeline",value:void 0},{kind:"field",decorators:[(0,C.wk)()],key:"_showSendButton",value:function(){return!1}},{kind:"field",decorators:[(0,C.wk)()],key:"_pipelines",value:void 0},{kind:"field",decorators:[(0,C.wk)()],key:"_preferredPipeline",value:void 0},{kind:"field",decorators:[(0,C.P)("#scroll-container")],key:"_scrollContainer",value:void 0},{kind:"field",decorators:[(0,C.P)("#message-input")],key:"_messageInput",value:void 0},{kind:"field",key:"_conversationId",value:function(){return null}},{kind:"field",key:"_audioRecorder",value:void 0},{kind:"field",key:"_audioBuffer",value:void 0},{kind:"field",key:"_audio",value:void 0},{kind:"field",key:"_stt_binary_handler_id",value:void 0},{kind:"field",key:"_pipelinePromise",value:void 0},{kind:"method",key:"showDialog",value:(D=(0,y.A)((0,_.A)().mark((function e(t){var i;return(0,_.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if("last_used"!==t.pipeline_id){e.next=3;break}e.next=10;break;case 3:if("preferred"!==t.pipeline_id){e.next=9;break}return e.next=6,this._loadPipelines();case 6:this._pipelineId=this._preferredPipeline,e.next=10;break;case 9:this._pipelineId=t.pipeline_id;case 10:return this._conversation=[{who:"hass",text:this.hass.localize("ui.dialogs.voice_command.how_can_i_help")}],this._opened=!0,e.next=14,this.updateComplete;case 14:return this._scrollMessagesBottom(),e.next=17,this._pipelinePromise;case 17:null!=t&&t.start_listening&&null!==(i=this._pipeline)&&void 0!==i&&i.stt_engine&&P.N.isSupported&&this._toggleListening();case 18:case"end":return e.stop()}}),e,this)}))),function(e){return D.apply(this,arguments)})},{kind:"method",key:"closeDialog",value:(N=(0,y.A)((0,_.A)().mark((function e(){var t,i;return(0,_.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:this._opened=!1,this._pipeline=void 0,this._pipelines=void 0,this._conversation=void 0,this._conversationId=null,null===(t=this._audioRecorder)||void 0===t||t.close(),this._audioRecorder=void 0,null===(i=this._audio)||void 0===i||i.pause(),(0,B.r)(this,"dialog-closed",{dialog:this.localName});case 9:case"end":return e.stop()}}),e,this)}))),function(){return N.apply(this,arguments)})},{kind:"method",key:"render",value:function(){var e,t,i,h,p,v=this;if(!this._opened)return S.s6;var g=P.N.isSupported,f=null===(e=this._pipeline)||void 0===e?void 0:e.stt_engine;return(0,S.qy)(n||(n=(0,m.A)([' <ha-dialog open @closed="','" .heading="','" flexContent> <ha-dialog-header slot="heading"> <ha-icon-button slot="navigationIcon" dialogAction="cancel" .label="','" .path="','"></ha-icon-button> <div slot="title"> ',' <ha-button-menu @opened="','" @closed="','" activatable fixed> <ha-button slot="trigger"> ',' <ha-svg-icon slot="trailingIcon" .path="','"></ha-svg-icon> </ha-button> '," ",' </ha-button-menu> </div> <a href="','" slot="actionItems" target="_blank" rel="noopener noreferer"> <ha-icon-button .label="','" .path="','"></ha-icon-button> </a> </ha-dialog-header> <div class="messages"> <div class="messages-container" id="scroll-container"> ',' </div> </div> <div class="input" slot="primaryAction"> <ha-textfield id="message-input" @keyup="','" @input="','" .label="','" dialogInitialFocus iconTrailing> <span slot="trailingIcon"> '," </span> </ha-textfield> </div> </ha-dialog> "])),this.closeDialog,this.hass.localize("ui.dialogs.voice_command.title"),this.hass.localize("ui.common.close"),"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",this.hass.localize("ui.dialogs.voice_command.title"),this._loadPipelines,z.d,null===(t=this._pipeline)||void 0===t?void 0:t.name,"M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z",null===(i=this._pipelines)||void 0===i?void 0:i.map((function(e){return(0,S.qy)(o||(o=(0,m.A)(['<ha-list-item ?selected="','" .pipeline="','" @click="','" .hasMeta="','"> ',""," </ha-list-item>"])),e.id===v._pipelineId||!v._pipelineId&&e.id===v._preferredPipeline,e.id,v._selectPipeline,e.id===v._preferredPipeline,e.name,e.id===v._preferredPipeline?(0,S.qy)(a||(a=(0,m.A)([' <ha-svg-icon slot="meta" .path="','"></ha-svg-icon> '])),"M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z"):S.s6)})),null!==(h=this.hass.user)&&void 0!==h&&h.is_admin?(0,S.qy)(r||(r=(0,m.A)(['<li divider role="separator"></li> <a href="/config/voice-assistants/assistants"><ha-list-item @click="','">',"</ha-list-item></a>"])),this.closeDialog,this.hass.localize("ui.dialogs.voice_command.manage_assistants")):S.s6,(0,U.o)(this.hass,"/docs/assist/"),this.hass.localize("ui.common.help"),"M11,18H13V16H11V18M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,6A4,4 0 0,0 8,10H10A2,2 0 0,1 12,8A2,2 0 0,1 14,10C14,12 11,11.75 11,15H13C13,12.75 16,12.5 16,10A4,4 0 0,0 12,6Z",this._conversation.map((function(e){return(0,S.qy)(s||(s=(0,m.A)([' <div class="','">',"</div> "])),v._computeMessageClasses(e),e.text)})),this._handleKeyUp,this._handleInput,this.hass.localize("ui.dialogs.voice_command.input_label"),this._showSendButton||!f?(0,S.qy)(d||(d=(0,m.A)([' <ha-icon-button class="listening-icon" .path="','" @click="','" .label="','"> </ha-icon-button> '])),"M2,21L23,12L2,3V10L17,12L2,14V21Z",this._handleSendMessage,this.hass.localize("ui.dialogs.voice_command.send_text")):(0,S.qy)(l||(l=(0,m.A)([" ",' <div class="listening-icon"> <ha-icon-button .path="','" @click="','" .label="','"> </ha-icon-button> '," </div> "])),null!==(p=this._audioRecorder)&&void 0!==p&&p.active?(0,S.qy)(c||(c=(0,m.A)([' <div class="bouncer"> <div class="double-bounce1"></div> <div class="double-bounce2"></div> </div> ']))):S.s6,"M12,2A3,3 0 0,1 15,5V11A3,3 0 0,1 12,14A3,3 0 0,1 9,11V5A3,3 0 0,1 12,2M19,11C19,14.53 16.39,17.44 13,17.93V21H11V17.93C7.61,17.44 5,14.53 5,11H7A5,5 0 0,0 12,16A5,5 0 0,0 17,11H19Z",this._handleListeningButton,this.hass.localize("ui.dialogs.voice_command.start_listening"),g?null:(0,S.qy)(u||(u=(0,m.A)([' <ha-svg-icon .path="','" class="unsupported"></ha-svg-icon> '])),"M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z")))}},{kind:"method",key:"willUpdate",value:function(e){(e.has("_pipelineId")||e.has("_opened")&&!0===this._opened)&&this._getPipeline()}},{kind:"method",key:"_getPipeline",value:(R=(0,y.A)((0,_.A)().mark((function e(){return(0,_.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,this._pipelinePromise=(0,q.mp)(this.hass,this._pipelineId),e.next=4,this._pipelinePromise;case 4:this._pipeline=e.sent,e.next=10;break;case 7:e.prev=7,e.t0=e.catch(0),"not_found"===e.t0.code&&(this._pipelineId=void 0);case 10:case"end":return e.stop()}}),e,this,[[0,7]])}))),function(){return R.apply(this,arguments)})},{kind:"method",key:"_loadPipelines",value:(Z=(0,y.A)((0,_.A)().mark((function e(){var t,i,n;return(0,_.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!this._pipelines){e.next=2;break}return e.abrupt("return");case 2:return e.next=4,(0,q.nx)(this.hass);case 4:t=e.sent,i=t.pipelines,n=t.preferred_pipeline,this._pipelines=i,this._preferredPipeline=n||void 0;case 9:case"end":return e.stop()}}),e,this)}))),function(){return Z.apply(this,arguments)})},{kind:"method",key:"_selectPipeline",value:(T=(0,y.A)((0,_.A)().mark((function e(t){return(0,_.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return this._pipelineId=t.currentTarget.pipeline,this._conversation=[{who:"hass",text:this.hass.localize("ui.dialogs.voice_command.how_can_i_help")}],e.next=4,this.updateComplete;case 4:this._scrollMessagesBottom();case 5:case"end":return e.stop()}}),e,this)}))),function(e){return T.apply(this,arguments)})},{kind:"method",key:"updated",value:function(e){(0,L.A)((0,M.A)(F.prototype),"updated",this).call(this,e),(e.has("_conversation")||e.has("results"))&&this._scrollMessagesBottom()}},{kind:"method",key:"_addMessage",value:function(e){this._conversation=[].concat((0,f.A)(this._conversation),[e])}},{kind:"method",key:"_handleKeyUp",value:function(e){var t=e.target;"Enter"===e.key&&t.value&&(this._processText(t.value),t.value="",this._showSendButton=!1)}},{kind:"method",key:"_handleInput",value:function(e){var t=e.target.value;t&&!this._showSendButton?this._showSendButton=!0:!t&&this._showSendButton&&(this._showSendButton=!1)}},{kind:"method",key:"_handleSendMessage",value:function(){this._messageInput.value&&(this._processText(this._messageInput.value.trim()),this._messageInput.value="",this._showSendButton=!1)}},{kind:"method",key:"_processText",value:(H=(0,y.A)((0,_.A)().mark((function e(t){var i,n,o,a,r=this;return(0,_.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return null===(i=this._audio)||void 0===i||i.pause(),this._addMessage({who:"user",text:t}),n={who:"hass",text:"…"},this._addMessage(n),e.prev=4,e.next=7,(0,q.vU)(this.hass,(function(e){if("intent-end"===e.type){var t;r._conversationId=e.data.intent_output.conversation_id;var i=null===(t=e.data.intent_output.response.speech)||void 0===t?void 0:t.plain;i&&(n.text=i.speech),r.requestUpdate("_conversation"),a()}"error"===e.type&&(n.text=e.data.message,n.error=!0,r.requestUpdate("_conversation"),a())}),{start_stage:"intent",input:{text:t},end_stage:"intent",pipeline:null===(o=this._pipeline)||void 0===o?void 0:o.id,conversation_id:this._conversationId});case 7:a=e.sent,e.next=15;break;case 10:e.prev=10,e.t0=e.catch(4),n.text=this.hass.localize("ui.dialogs.voice_command.error"),n.error=!0,this.requestUpdate("_conversation");case 15:case"end":return e.stop()}}),e,this,[[4,10]])}))),function(e){return H.apply(this,arguments)})},{kind:"method",key:"_handleListeningButton",value:function(e){e.stopPropagation(),e.preventDefault(),this._toggleListening()}},{kind:"method",key:"_toggleListening",value:function(){var e;P.N.isSupported?null!==(e=this._audioRecorder)&&void 0!==e&&e.active?this._stopListening():this._startListening():this._showNotSupportedMessage()}},{kind:"method",key:"_showNotSupportedMessage",value:(w=(0,y.A)((0,_.A)().mark((function e(){return(0,_.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:this._addMessage({who:"hass",text:(0,S.qy)(h||(h=(0,m.A)([""," ",""])),this.hass.localize("ui.dialogs.voice_command.not_supported_microphone_browser"),this.hass.localize("ui.dialogs.voice_command.not_supported_microphone_documentation",{documentation_link:(0,S.qy)(p||(p=(0,m.A)(['<a target="_blank" rel="noopener noreferrer" href="','">',"</a>"])),(0,U.o)(this.hass,"/docs/configuration/securing/#remote-access"),this.hass.localize("ui.dialogs.voice_command.not_supported_microphone_documentation_link"))}))});case 1:case"end":return e.stop()}}),e,this)}))),function(){return w.apply(this,arguments)})},{kind:"method",key:"_startListening",value:(i=(0,y.A)((0,_.A)().mark((function e(){var t,i,n,o,a,r,s=this;return(0,_.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return null===(t=this._audio)||void 0===t||t.pause(),this._audioRecorder||(this._audioRecorder=new P.N((function(e){s._audioBuffer?s._audioBuffer.push(e):s._sendAudioChunk(e)}))),this._stt_binary_handler_id=void 0,this._audioBuffer=[],i={who:"user",text:"…"},this._audioRecorder.start().then((function(){s._addMessage(i),s.requestUpdate("_audioRecorder")})),n={who:"hass",text:"…"},e.prev=7,e.next=10,(0,q.vU)(this.hass,(function(e){if("run-start"===e.type&&(s._stt_binary_handler_id=e.data.runner_data.stt_binary_handler_id),"stt-start"===e.type&&s._audioBuffer){var t,o=(0,g.A)(s._audioBuffer);try{for(o.s();!(t=o.n()).done;){var a=t.value;s._sendAudioChunk(a)}}catch(u){o.e(u)}finally{o.f()}s._audioBuffer=void 0}if("stt-end"===e.type&&(s._stt_binary_handler_id=void 0,s._stopListening(),i.text=e.data.stt_output.text,s.requestUpdate("_conversation"),s._addMessage(n)),"intent-end"===e.type){var d;s._conversationId=e.data.intent_output.conversation_id;var l=null===(d=e.data.intent_output.response.speech)||void 0===d?void 0:d.plain;l&&(n.text=l.speech),s.requestUpdate("_conversation")}if("tts-end"===e.type){var c=e.data.tts_output.url;s._audio=new Audio(c),s._audio.play(),s._audio.addEventListener("ended",s._unloadAudio),s._audio.addEventListener("pause",s._unloadAudio),s._audio.addEventListener("canplaythrough",s._playAudio),s._audio.addEventListener("error",s._audioError)}"run-end"===e.type&&(s._stt_binary_handler_id=void 0,r()),"error"===e.type&&(s._stt_binary_handler_id=void 0,"…"===i.text?(i.text=e.data.message,i.error=!0):(n.text=e.data.message,n.error=!0),s._stopListening(),s.requestUpdate("_conversation"),r())}),{start_stage:"stt",end_stage:null!==(o=this._pipeline)&&void 0!==o&&o.tts_engine?"tts":"intent",input:{sample_rate:this._audioRecorder.sampleRate},pipeline:null===(a=this._pipeline)||void 0===a?void 0:a.id,conversation_id:this._conversationId});case 10:r=e.sent,e.next=18;break;case 13:return e.prev=13,e.t0=e.catch(7),e.next=17,(0,V.showAlertDialog)(this,{title:"Error starting pipeline",text:e.t0.message||e.t0});case 17:this._stopListening();case 18:case"end":return e.stop()}}),e,this,[[7,13]])}))),function(){return i.apply(this,arguments)})},{kind:"method",key:"_stopListening",value:function(){var e;if(null===(e=this._audioRecorder)||void 0===e||e.stop(),this.requestUpdate("_audioRecorder"),this._stt_binary_handler_id){if(this._audioBuffer){var t,i=(0,g.A)(this._audioBuffer);try{for(i.s();!(t=i.n()).done;){var n=t.value;this._sendAudioChunk(n)}}catch(o){i.e(o)}finally{i.f()}}this._sendAudioChunk(new Int16Array),this._stt_binary_handler_id=void 0}this._audioBuffer=void 0}},{kind:"method",key:"_sendAudioChunk",value:function(e){if(this.hass.connection.socket.binaryType="arraybuffer",null!=this._stt_binary_handler_id){var t=new Uint8Array(1+2*e.length);t[0]=this._stt_binary_handler_id,t.set(new Uint8Array(e.buffer),1),this.hass.connection.socket.send(t)}}},{kind:"field",key:"_playAudio",value:function(){var e=this;return function(){var t;null===(t=e._audio)||void 0===t||t.play()}}},{kind:"field",key:"_audioError",value:function(){var e=this;return function(){var t;(0,V.showAlertDialog)(e,{title:"Error playing audio."}),null===(t=e._audio)||void 0===t||t.removeAttribute("src")}}},{kind:"field",key:"_unloadAudio",value:function(){var e=this;return function(){var t;null===(t=e._audio)||void 0===t||t.removeAttribute("src"),e._audio=void 0}}},{kind:"method",key:"_scrollMessagesBottom",value:function(){var e=this._scrollContainer;e&&e.scrollTo(0,99999)}},{kind:"method",key:"_computeMessageClasses",value:function(e){return"message ".concat(e.who," ").concat(e.error?" error":"")}},{kind:"get",static:!0,key:"styles",value:function(){return[E.nA,(0,S.AH)(v||(v=(0,m.A)([".listening-icon{position:relative;color:var(--secondary-text-color);margin-right:-24px;margin-inline-end:-24px;margin-inline-start:initial;direction:var(--direction)}.listening-icon[active]{color:var(--primary-color)}.unsupported{color:var(--error-color);position:absolute;--mdc-icon-size:16px;right:5px;inset-inline-end:5px;inset-inline-start:initial;top:0px}ha-dialog{--primary-action-button-flex:1;--secondary-action-button-flex:0;--mdc-dialog-max-width:500px;--mdc-dialog-max-height:500px;--dialog-content-padding:0}ha-dialog-header a{color:var(--primary-text-color)}div[slot=title]{display:flex;flex-direction:column;margin:-4px 0}ha-button-menu{--mdc-theme-on-primary:var(--text-primary-color);--mdc-theme-primary:var(--primary-color);margin-top:-8px;margin-bottom:0;margin-right:0;margin-inline-end:0;margin-left:-8px;margin-inline-start:-8px}ha-button-menu ha-button{--mdc-theme-primary:var(--secondary-text-color);--mdc-typography-button-text-transform:none;--mdc-typography-button-font-size:unset;--mdc-typography-button-font-weight:400;--mdc-typography-button-letter-spacing:var(\n            --mdc-typography-headline6-letter-spacing,\n            0.0125em\n          );--mdc-typography-button-line-height:var(\n            --mdc-typography-headline6-line-height,\n            2rem\n          );--button-height:auto}ha-button-menu ha-button ha-svg-icon{height:28px;margin-left:4px;margin-inline-start:4px;margin-inline-end:initial;direction:var(--direction)}ha-list-item{--mdc-list-item-meta-size:16px}ha-list-item ha-svg-icon{margin-left:4px;margin-inline-start:4px;margin-inline-end:initial;direction:var(--direction);display:block}ha-button-menu a{text-decoration:none}ha-textfield{display:block;overflow:hidden}a.button{text-decoration:none}a.button>mwc-button{width:100%}.side-by-side{display:flex;margin:8px 0}.side-by-side>*{flex:1 0;padding:4px}.messages{display:block;height:400px;box-sizing:border-box;position:relative}@media all and (max-width:450px),all and (max-height:500px){ha-dialog{--mdc-dialog-max-width:100%}.messages{height:100%;flex:1}}.messages-container{position:absolute;bottom:0px;right:0px;left:0px;padding:24px;box-sizing:border-box;overflow-y:auto;max-height:100%}.message{white-space:pre-line;font-size:18px;clear:both;margin:8px 0;padding:8px;border-radius:15px}.message p{margin:0}.message p:not(:last-child){margin-bottom:8px}.message.user{margin-left:24px;margin-inline-start:24px;margin-inline-end:initial;float:var(--float-end);text-align:right;border-bottom-right-radius:0px;background-color:var(--primary-color);color:var(--text-primary-color);direction:var(--direction)}.message.hass{margin-right:24px;margin-inline-end:24px;margin-inline-start:initial;float:var(--float-start);border-bottom-left-radius:0px;background-color:var(--secondary-background-color);color:var(--primary-text-color);direction:var(--direction)}.message.user a{color:var(--text-primary-color)}.message.hass a{color:var(--primary-text-color)}.message img{width:100%;border-radius:10px}.message.error{background-color:var(--error-color);color:var(--text-primary-color)}.input{margin-left:0;margin-right:0}.bouncer{width:48px;height:48px;position:absolute}.double-bounce1,.double-bounce2{width:48px;height:48px;border-radius:50%;background-color:var(--primary-color);opacity:.2;position:absolute;top:0;left:0;-webkit-animation:sk-bounce 2s infinite ease-in-out;animation:sk-bounce 2s infinite ease-in-out}.double-bounce2{-webkit-animation-delay:-1s;animation-delay:-1s}@-webkit-keyframes sk-bounce{0%,100%{-webkit-transform:scale(0)}50%{-webkit-transform:scale(1)}}@keyframes sk-bounce{0%,100%{transform:scale(0);-webkit-transform:scale(0)}50%{transform:scale(1);-webkit-transform:scale(1)}}@media all and (max-width:450px),all and (max-height:500px){.message{font-size:16px}}"])))]}}]}}),S.WF)},86176:function(){Element.prototype.toggleAttribute||(Element.prototype.toggleAttribute=function(e,t){return void 0!==t&&(t=!!t),this.hasAttribute(e)?!!t||(this.removeAttribute(e),!1):!1!==t&&(this.setAttribute(e,""),!0)})},92483:function(e,t,i){"use strict";i.d(t,{o:function(){return n}});i(77052),i(53501),i(34517);var n=function(e,t){return"https://".concat(e.config.version.includes("b")?"rc":e.config.version.includes("dev")?"next":"www",".home-assistant.io").concat(t)}},66584:function(e,t,i){function n(t){return e.exports=n="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},e.exports.__esModule=!0,e.exports.default=e.exports,n(t)}i(8485),i(98809),i(77817),i(21950),i(68113),i(56262),i(8339),e.exports=n,e.exports.__esModule=!0,e.exports.default=e.exports},69099:function(e,t,i){"use strict";i(24629)("Uint8",(function(e){return function(t,i,n){return e(this,t,i,n)}}))}}]);
//# sourceMappingURL=50320.odBI729fsh0.js.map