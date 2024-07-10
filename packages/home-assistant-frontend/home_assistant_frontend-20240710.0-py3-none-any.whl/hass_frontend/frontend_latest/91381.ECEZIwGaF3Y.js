export const id=91381;export const ids=[91381];export const modules={6699:(e,i,t)=>{t.d(i,{x:()=>n});t(53501);const n=(e,i)=>e&&e.config.components.includes(i)},60280:(e,i,t)=>{t.d(i,{TC:()=>n,VN:()=>s,Vx:()=>o,eM:()=>r});t(21950),t(14460),t(8339);const n=(e,i,t)=>{const n={type:"config_entries/subscribe"};return t&&t.type&&(n.type_filter=t.type),e.connection.subscribeMessage((e=>i(e)),n)},s=(e,i)=>{const t={};return i&&(i.type&&(t.type_filter=i.type),i.domain&&(t.domain=i.domain)),e.callWS({type:"config_entries/get",...t})},o=(e,i)=>e.callWS({type:"config_entries/get_single",entry_id:i}),r=(e,i)=>e.callApi("DELETE",`config/config_entries/entry/${i}`)},31142:(e,i,t)=>{t.d(i,{PN:()=>a,jm:()=>d,sR:()=>c,t1:()=>r,x:()=>p,yu:()=>l});var n=t(99955),s=t(47394);t(58587);const o={"HA-Frontend-Base":`${location.protocol}//${location.host}`},r=(e,i,t)=>{var n;return e.callApi("POST","config/config_entries/flow",{handler:i,show_advanced_options:Boolean(null===(n=e.userData)||void 0===n?void 0:n.showAdvanced),entry_id:t},o)},a=(e,i)=>e.callApi("GET",`config/config_entries/flow/${i}`,void 0,o),d=(e,i,t)=>e.callApi("POST",`config/config_entries/flow/${i}`,t,o),c=(e,i)=>e.callApi("DELETE",`config/config_entries/flow/${i}`),l=(e,i)=>e.callApi("GET","config/config_entries/flow_handlers"+(i?`?type=${i}`:"")),h=e=>e.sendMessagePromise({type:"config_entries/flow/progress"}),u=(e,i)=>e.subscribeEvents((0,s.s)((()=>h(e).then((e=>i.setState(e,!0)))),500,!0),"config_entry_discovered"),p=(e,i)=>{return(t=e.connection,(0,n.X)(t,"_configFlowProgress",h,u)).subscribe(i);var t}},94027:(e,i,t)=>{t.d(i,{E:()=>a});var n=t(62659),s=t(76504),o=t(80792),r=(t(53501),t(21950),t(55888),t(66274),t(22836),t(8339),t(18791));const a=e=>(0,n.A)(null,(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,r.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:void 0},{kind:"field",key:"__unsubs",value:void 0},{kind:"method",key:"connectedCallback",value:function(){(0,s.A)((0,o.A)(t.prototype),"connectedCallback",this).call(this),this.__checkSubscribed()}},{kind:"method",key:"disconnectedCallback",value:function(){if((0,s.A)((0,o.A)(t.prototype),"disconnectedCallback",this).call(this),this.__unsubs){for(;this.__unsubs.length;){const e=this.__unsubs.pop();e instanceof Promise?e.then((e=>e())):e()}this.__unsubs=void 0}}},{kind:"method",key:"updated",value:function(e){if((0,s.A)((0,o.A)(t.prototype),"updated",this).call(this,e),e.has("hass"))this.__checkSubscribed();else if(this.hassSubscribeRequiredHostProps)for(const i of e.keys())if(this.hassSubscribeRequiredHostProps.includes(i))return void this.__checkSubscribed()}},{kind:"method",key:"hassSubscribe",value:function(){return[]}},{kind:"method",key:"__checkSubscribed",value:function(){var e;void 0!==this.__unsubs||!this.isConnected||void 0===this.hass||null!==(e=this.hassSubscribeRequiredHostProps)&&void 0!==e&&e.some((e=>void 0===this[e]))||(this.__unsubs=this.hassSubscribe())}}]}}),e)},91381:(e,i,t)=>{t.r(i);var n=t(62659),s=t(76504),o=t(80792),r=(t(21950),t(71936),t(14460),t(55888),t(66274),t(85038),t(84531),t(98168),t(15445),t(24483),t(13478),t(46355),t(14612),t(53691),t(48455),t(8339),t(58068),t(40924)),a=t(18791),d=t(6699),c=t(77664),l=t(95507),h=t(60280),u=t(31142),p=t(58587);var f=t(94027),g=(t(1683),t(5203));(0,n.A)([(0,a.EM)("integration-badge")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,a.MZ)()],key:"domain",value:void 0},{kind:"field",decorators:[(0,a.MZ)()],key:"title",value:void 0},{kind:"field",decorators:[(0,a.MZ)({type:Boolean})],key:"darkOptimizedIcon",value:()=>!1},{kind:"field",decorators:[(0,a.MZ)({type:Boolean,reflect:!0})],key:"clickable",value:()=>!1},{kind:"method",key:"render",value:function(){return r.qy` <div class="icon"> <img alt="" src="${(0,g.MR)({domain:this.domain,type:"icon",darkOptimized:this.darkOptimizedIcon})}" crossorigin="anonymous" referrerpolicy="no-referrer"> </div> <div class="title">${this.title}</div> `}},{kind:"get",static:!0,key:"styles",value:function(){return r.AH`:host{display:inline-flex;flex-direction:column;text-align:center;color:var(--primary-text-color)}img{max-width:100%;max-height:100%}.icon{position:relative;margin:0 auto 8px;height:40px;width:40px;display:flex;align-items:center;justify-content:center}.title{min-height:2.3em;word-break:break-word}`}}]}}),r.WF);var y=t(89084);const v=new Set(["google_translate","hassio","met","radio_browser","rpi_power","shopping_list","sun"]);(0,n.A)([(0,a.EM)("onboarding-integrations")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,a.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.MZ)({attribute:!1})],key:"onboardingLocalize",value:void 0},{kind:"field",decorators:[(0,a.wk)()],key:"_entries",value:()=>[]},{kind:"field",decorators:[(0,a.wk)()],key:"_discoveredDomains",value:void 0},{kind:"method",key:"hassSubscribe",value:function(){return[(0,u.x)(this.hass,(e=>{this._discoveredDomains=new Set(e.filter((e=>!v.has(e.handler))).map((e=>e.handler))),this.hass.loadBackendTranslation("title",Array.from(this._discoveredDomains))})),(0,h.TC)(this.hass,(e=>{let i=!1;const t=[],n=new Set;if(e.forEach((e=>{if(null===e.type||"added"===e.type){if(v.has(e.entry.domain))return;t.push(e.entry),n.add(e.entry.domain),null===e.type&&(i=!0)}else if("removed"===e.type)this._entries=this._entries.filter((i=>i.entry_id!==e.entry.entry_id));else if("updated"===e.type){if(v.has(e.entry.domain))return;const i=e.entry;this._entries=this._entries.map((e=>e.entry_id===i.entry_id?i:e))}})),!t.length&&!i)return;this.hass.loadBackendTranslation("title",Array.from(n));const s=i?[]:this._entries;this._entries=[...s,...t]}),{type:["device","hub","service"]})]}},{kind:"method",key:"render",value:function(){if(!this._discoveredDomains)return r.s6;let e=new Set;this._entries.forEach((i=>{e.add(i.domain)})),e=new Set([...e,...this._discoveredDomains]);let i=[];for(const t of e.values())i.push([t,(0,p.p$)(this.hass.localize,t)]);i=i.sort(((e,i)=>(0,l.x)(e[0],i[0],this.hass.locale.language)));const t=i.length;return i.length>12&&(i=i.slice(0,11)),r.qy` <h1> ${this.onboardingLocalize("ui.panel.page-onboarding.integration.header")} </h1> <p> ${this.onboardingLocalize("ui.panel.page-onboarding.integration.intro")} </p> <div class="badges"> ${i.map((([e,i])=>{var t;return r.qy`<integration-badge .domain="${e}" .title="${i}" .darkOptimizedIcon="${null===(t=this.hass.themes)||void 0===t?void 0:t.darkMode}"></integration-badge>`}))} ${t>i.length?r.qy`<div class="more"> ${this.onboardingLocalize("ui.panel.page-onboarding.integration.more_integrations",{count:t-i.length})} </div>`:r.s6} </div> <div class="footer"> <mwc-button unelevated @click="${this._finish}"> ${this.onboardingLocalize("ui.panel.page-onboarding.integration.finish")} </mwc-button> </div> `}},{kind:"method",key:"firstUpdated",value:function(e){(0,s.A)((0,o.A)(t.prototype),"firstUpdated",this).call(this,e),this.hass.loadBackendTranslation("title"),this._scanUSBDevices()}},{kind:"method",key:"_scanUSBDevices",value:async function(){var e;(0,d.x)(this.hass,"usb")&&await(e=this.hass,e.callWS({type:"usb/scan"}))}},{kind:"method",key:"_finish",value:async function(){(0,c.r)(this,"onboarding-step",{type:"integration"})}},{kind:"get",static:!0,key:"styles",value:function(){return[y.o,r.AH`.badges{margin-top:24px;display:grid;grid-template-columns:repeat(auto-fill,minmax(106px,1fr));row-gap:24px}.more{display:flex;justify-content:center;align-items:center;height:100%}`]}}]}}),(0,f.E)(r.WF))},5203:(e,i,t)=>{t.d(i,{MR:()=>n,a_:()=>s,bg:()=>o});const n=e=>`https://brands.home-assistant.io/${e.brand?"brands/":""}${e.useFallback?"_/":""}${e.domain}/${e.darkOptimized?"dark_":""}${e.type}.png`,s=e=>e.split("/")[4],o=e=>e.startsWith("https://brands.home-assistant.io/")}};
//# sourceMappingURL=91381.ECEZIwGaF3Y.js.map