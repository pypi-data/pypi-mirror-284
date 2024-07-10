/*! For license information please see 77514.8aQ9AyzVfU8.js.LICENSE.txt */
export const id=77514;export const ids=[77514];export const modules={92518:(e,t,a)=>{a.d(t,{A:()=>s});a(66274),a(84531),a(98168);function s(e){if(!e||"object"!=typeof e)return e;if("[object Date]"==Object.prototype.toString.call(e))return new Date(e.getTime());if(Array.isArray(e))return e.map(s);var t={};return Object.keys(e).forEach((function(a){t[a]=s(e[a])})),t}},95265:(e,t,a)=>{a.a(e,(async(e,s)=>{try{a.d(t,{P:()=>o});var r=a(74808),i=(a(21950),a(55888),a(15445),a(24483),a(13478),a(46355),a(14612),a(53691),a(48455),a(8339),e([r]));r=(i.then?(await i)():i)[0];class o{constructor(e,{target:t,config:a,callback:s,skipInitial:r}){this.t=new Set,this.o=!1,this.i=!1,this.h=e,null!==t&&this.t.add(null!=t?t:e),this.l=a,this.o=null!=r?r:this.o,this.callback=s,window.ResizeObserver?(this.u=new ResizeObserver((e=>{this.handleChanges(e),this.h.requestUpdate()})),e.addController(this)):console.warn("ResizeController error: browser does not support ResizeObserver.")}handleChanges(e){var t;this.value=null===(t=this.callback)||void 0===t?void 0:t.call(this,e,this.u)}hostConnected(){for(const e of this.t)this.observe(e)}hostDisconnected(){this.disconnect()}async hostUpdated(){!this.o&&this.i&&this.handleChanges([]),this.i=!1}observe(e){this.t.add(e),this.u.observe(e,this.l),this.i=!0,this.h.requestUpdate()}unobserve(e){this.t.delete(e),this.u.unobserve(e)}disconnect(){this.u.disconnect()}}s()}catch(e){s(e)}}))},93386:(e,t,a)=>{a.d(t,{z:()=>h});var s=a(76513),r=a(18791),i=(a(21950),a(8339),a(75291),a(40924)),o=a(52162);class n extends o.v{constructor(){super(...arguments),this.elevated=!1,this.href="",this.target=""}get primaryId(){return this.href?"link":"button"}get rippleDisabled(){return!this.href&&this.disabled}getContainerClasses(){return{...super.getContainerClasses(),disabled:!this.href&&this.disabled,elevated:this.elevated,link:!!this.href}}renderPrimaryAction(e){const{ariaLabel:t}=this;return this.href?i.qy` <a class="primary action" id="link" aria-label="${t||i.s6}" href="${this.href}" target="${this.target||i.s6}">${e}</a> `:i.qy` <button class="primary action" id="button" aria-label="${t||i.s6}" ?disabled="${this.disabled&&!this.alwaysFocusable}" type="button">${e}</button> `}renderOutline(){return this.elevated?i.qy`<md-elevation part="elevation"></md-elevation>`:super.renderOutline()}}(0,s.__decorate)([(0,r.MZ)({type:Boolean})],n.prototype,"elevated",void 0),(0,s.__decorate)([(0,r.MZ)()],n.prototype,"href",void 0),(0,s.__decorate)([(0,r.MZ)()],n.prototype,"target",void 0);const l=i.AH`:host{--_container-height:var(--md-assist-chip-container-height, 32px);--_disabled-label-text-color:var(--md-assist-chip-disabled-label-text-color, var(--md-sys-color-on-surface, #1d1b20));--_disabled-label-text-opacity:var(--md-assist-chip-disabled-label-text-opacity, 0.38);--_elevated-container-color:var(--md-assist-chip-elevated-container-color, var(--md-sys-color-surface-container-low, #f7f2fa));--_elevated-container-elevation:var(--md-assist-chip-elevated-container-elevation, 1);--_elevated-container-shadow-color:var(--md-assist-chip-elevated-container-shadow-color, var(--md-sys-color-shadow, #000));--_elevated-disabled-container-color:var(--md-assist-chip-elevated-disabled-container-color, var(--md-sys-color-on-surface, #1d1b20));--_elevated-disabled-container-elevation:var(--md-assist-chip-elevated-disabled-container-elevation, 0);--_elevated-disabled-container-opacity:var(--md-assist-chip-elevated-disabled-container-opacity, 0.12);--_elevated-focus-container-elevation:var(--md-assist-chip-elevated-focus-container-elevation, 1);--_elevated-hover-container-elevation:var(--md-assist-chip-elevated-hover-container-elevation, 2);--_elevated-pressed-container-elevation:var(--md-assist-chip-elevated-pressed-container-elevation, 1);--_focus-label-text-color:var(--md-assist-chip-focus-label-text-color, var(--md-sys-color-on-surface, #1d1b20));--_hover-label-text-color:var(--md-assist-chip-hover-label-text-color, var(--md-sys-color-on-surface, #1d1b20));--_hover-state-layer-color:var(--md-assist-chip-hover-state-layer-color, var(--md-sys-color-on-surface, #1d1b20));--_hover-state-layer-opacity:var(--md-assist-chip-hover-state-layer-opacity, 0.08);--_label-text-color:var(--md-assist-chip-label-text-color, var(--md-sys-color-on-surface, #1d1b20));--_label-text-font:var(--md-assist-chip-label-text-font, var(--md-sys-typescale-label-large-font, var(--md-ref-typeface-plain, Roboto)));--_label-text-line-height:var(--md-assist-chip-label-text-line-height, var(--md-sys-typescale-label-large-line-height, 1.25rem));--_label-text-size:var(--md-assist-chip-label-text-size, var(--md-sys-typescale-label-large-size, 0.875rem));--_label-text-weight:var(--md-assist-chip-label-text-weight, var(--md-sys-typescale-label-large-weight, var(--md-ref-typeface-weight-medium, 500)));--_pressed-label-text-color:var(--md-assist-chip-pressed-label-text-color, var(--md-sys-color-on-surface, #1d1b20));--_pressed-state-layer-color:var(--md-assist-chip-pressed-state-layer-color, var(--md-sys-color-on-surface, #1d1b20));--_pressed-state-layer-opacity:var(--md-assist-chip-pressed-state-layer-opacity, 0.12);--_disabled-outline-color:var(--md-assist-chip-disabled-outline-color, var(--md-sys-color-on-surface, #1d1b20));--_disabled-outline-opacity:var(--md-assist-chip-disabled-outline-opacity, 0.12);--_focus-outline-color:var(--md-assist-chip-focus-outline-color, var(--md-sys-color-on-surface, #1d1b20));--_outline-color:var(--md-assist-chip-outline-color, var(--md-sys-color-outline, #79747e));--_outline-width:var(--md-assist-chip-outline-width, 1px);--_disabled-leading-icon-color:var(--md-assist-chip-disabled-leading-icon-color, var(--md-sys-color-on-surface, #1d1b20));--_disabled-leading-icon-opacity:var(--md-assist-chip-disabled-leading-icon-opacity, 0.38);--_focus-leading-icon-color:var(--md-assist-chip-focus-leading-icon-color, var(--md-sys-color-primary, #6750a4));--_hover-leading-icon-color:var(--md-assist-chip-hover-leading-icon-color, var(--md-sys-color-primary, #6750a4));--_leading-icon-color:var(--md-assist-chip-leading-icon-color, var(--md-sys-color-primary, #6750a4));--_icon-size:var(--md-assist-chip-icon-size, 18px);--_pressed-leading-icon-color:var(--md-assist-chip-pressed-leading-icon-color, var(--md-sys-color-primary, #6750a4));--_container-shape-start-start:var(--md-assist-chip-container-shape-start-start, var(--md-assist-chip-container-shape, var(--md-sys-shape-corner-small, 8px)));--_container-shape-start-end:var(--md-assist-chip-container-shape-start-end, var(--md-assist-chip-container-shape, var(--md-sys-shape-corner-small, 8px)));--_container-shape-end-end:var(--md-assist-chip-container-shape-end-end, var(--md-assist-chip-container-shape, var(--md-sys-shape-corner-small, 8px)));--_container-shape-end-start:var(--md-assist-chip-container-shape-end-start, var(--md-assist-chip-container-shape, var(--md-sys-shape-corner-small, 8px)));--_leading-space:var(--md-assist-chip-leading-space, 16px);--_trailing-space:var(--md-assist-chip-trailing-space, 16px);--_icon-label-space:var(--md-assist-chip-icon-label-space, 8px);--_with-leading-icon-leading-space:var(--md-assist-chip-with-leading-icon-leading-space, 8px)}@media(forced-colors:active){.link .outline{border-color:ActiveText}}`;var c=a(80101),d=a(25348);let h=class extends n{};h.styles=[d.R,c.R,l],h=(0,s.__decorate)([(0,r.EM)("md-assist-chip")],h)},84292:(e,t,a)=>{a.d(t,{LV:()=>p});a(98809),a(27934),a(21950),a(19954),a(18347),a(55888),a(44186),a(90591),a(26777),a(66274),a(98168),a(91078),a(8339);const s=Symbol("Comlink.proxy"),r=Symbol("Comlink.endpoint"),i=Symbol("Comlink.releaseProxy"),o=Symbol("Comlink.finalizer"),n=Symbol("Comlink.thrown"),l=e=>"object"==typeof e&&null!==e||"function"==typeof e,c=new Map([["proxy",{canHandle:e=>l(e)&&e[s],serialize(e){const{port1:t,port2:a}=new MessageChannel;return d(e,t),[a,[a]]},deserialize:e=>(e.start(),p(e))}],["throw",{canHandle:e=>l(e)&&n in e,serialize({value:e}){let t;return t=e instanceof Error?{isError:!0,value:{message:e.message,name:e.name,stack:e.stack}}:{isError:!1,value:e},[t,[]]},deserialize(e){if(e.isError)throw Object.assign(new Error(e.value.message),e.value);throw e.value}}]]);function d(e,t=globalThis,a=["*"]){t.addEventListener("message",(function r(i){if(!i||!i.data)return;if(!function(e,t){for(const a of e){if(t===a||"*"===a)return!0;if(a instanceof RegExp&&a.test(t))return!0}return!1}(a,i.origin))return void console.warn(`Invalid origin '${i.origin}' for comlink proxy`);const{id:l,type:c,path:p}=Object.assign({path:[]},i.data),v=(i.data.argumentList||[]).map(x);let u;try{const t=p.slice(0,-1).reduce(((e,t)=>e[t]),e),a=p.reduce(((e,t)=>e[t]),e);switch(c){case"GET":u=a;break;case"SET":t[p.slice(-1)[0]]=x(i.data.value),u=!0;break;case"APPLY":u=a.apply(t,v);break;case"CONSTRUCT":u=function(e){return Object.assign(e,{[s]:!0})}(new a(...v));break;case"ENDPOINT":{const{port1:t,port2:a}=new MessageChannel;d(e,a),u=function(e,t){return g.set(e,t),e}(t,[t])}break;case"RELEASE":u=void 0;break;default:return}}catch(e){u={value:e,[n]:0}}Promise.resolve(u).catch((e=>({value:e,[n]:0}))).then((a=>{const[s,i]=_(a);t.postMessage(Object.assign(Object.assign({},s),{id:l}),i),"RELEASE"===c&&(t.removeEventListener("message",r),h(t),o in e&&"function"==typeof e[o]&&e[o]())})).catch((e=>{const[a,s]=_({value:new TypeError("Unserializable return value"),[n]:0});t.postMessage(Object.assign(Object.assign({},a),{id:l}),s)}))})),t.start&&t.start()}function h(e){(function(e){return"MessagePort"===e.constructor.name})(e)&&e.close()}function p(e,t){return y(e,[],t)}function v(e){if(e)throw new Error("Proxy has been released and is not useable")}function u(e){return w(e,{type:"RELEASE"}).then((()=>{h(e)}))}const m=new WeakMap,b="FinalizationRegistry"in globalThis&&new FinalizationRegistry((e=>{const t=(m.get(e)||0)-1;m.set(e,t),0===t&&u(e)}));function y(e,t=[],a=function(){}){let s=!1;const o=new Proxy(a,{get(a,r){if(v(s),r===i)return()=>{!function(e){b&&b.unregister(e)}(o),u(e),s=!0};if("then"===r){if(0===t.length)return{then:()=>o};const a=w(e,{type:"GET",path:t.map((e=>e.toString()))}).then(x);return a.then.bind(a)}return y(e,[...t,r])},set(a,r,i){v(s);const[o,n]=_(i);return w(e,{type:"SET",path:[...t,r].map((e=>e.toString())),value:o},n).then(x)},apply(a,i,o){v(s);const n=t[t.length-1];if(n===r)return w(e,{type:"ENDPOINT"}).then(x);if("bind"===n)return y(e,t.slice(0,-1));const[l,c]=f(o);return w(e,{type:"APPLY",path:t.map((e=>e.toString())),argumentList:l},c).then(x)},construct(a,r){v(s);const[i,o]=f(r);return w(e,{type:"CONSTRUCT",path:t.map((e=>e.toString())),argumentList:i},o).then(x)}});return function(e,t){const a=(m.get(t)||0)+1;m.set(t,a),b&&b.register(e,t,e)}(o,e),o}function f(e){const t=e.map(_);return[t.map((e=>e[0])),(a=t.map((e=>e[1])),Array.prototype.concat.apply([],a))];var a}const g=new WeakMap;function _(e){for(const[t,a]of c)if(a.canHandle(e)){const[s,r]=a.serialize(e);return[{type:"HANDLER",name:t,value:s},r]}return[{type:"RAW",value:e},g.get(e)||[]]}function x(e){switch(e.type){case"HANDLER":return c.get(e.name).deserialize(e.value);case"RAW":return e.value}}function w(e,t,a){return new Promise((s=>{const r=new Array(4).fill(0).map((()=>Math.floor(Math.random()*Number.MAX_SAFE_INTEGER).toString(16))).join("-");e.addEventListener("message",(function t(a){a.data&&a.data.id&&a.data.id===r&&(e.removeEventListener("message",t),s(a.data))})),e.start&&e.start(),e.postMessage(Object.assign({id:r},t),a)}))}}};
//# sourceMappingURL=77514.8aQ9AyzVfU8.js.map