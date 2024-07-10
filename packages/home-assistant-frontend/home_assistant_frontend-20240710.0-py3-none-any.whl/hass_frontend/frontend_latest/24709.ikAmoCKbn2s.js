/*! For license information please see 24709.ikAmoCKbn2s.js.LICENSE.txt */
export const id=24709;export const ids=[24709];export const modules={87565:(t,e,i)=>{i.d(e,{h:()=>c});i(21950),i(55888),i(8339);var s=i(76513),o=i(18791),n=i(51497),r=i(48678);let h=class extends n.L{};h.styles=[r.R],h=(0,s.__decorate)([(0,o.EM)("mwc-checkbox")],h);var l=i(40924),a=i(69760),d=i(46175);class c extends d.J{constructor(){super(...arguments),this.left=!1,this.graphic="control"}render(){const t={"mdc-deprecated-list-item__graphic":this.left,"mdc-deprecated-list-item__meta":!this.left},e=this.renderText(),i=this.graphic&&"control"!==this.graphic&&!this.left?this.renderGraphic():l.qy``,s=this.hasMeta&&this.left?this.renderMeta():l.qy``,o=this.renderRipple();return l.qy` ${o} ${i} ${this.left?"":e} <span class="${(0,a.H)(t)}"> <mwc-checkbox reducedTouchTarget tabindex="${this.tabindex}" .checked="${this.selected}" ?disabled="${this.disabled}" @change="${this.onChange}"> </mwc-checkbox> </span> ${this.left?e:""} ${s}`}async onChange(t){const e=t.target;this.selected===e.checked||(this._skipPropRequest=!0,this.selected=e.checked,await this.updateComplete,this._skipPropRequest=!1)}}(0,s.__decorate)([(0,o.P)("slot")],c.prototype,"slotElement",void 0),(0,s.__decorate)([(0,o.P)("mwc-checkbox")],c.prototype,"checkboxElement",void 0),(0,s.__decorate)([(0,o.MZ)({type:Boolean})],c.prototype,"left",void 0),(0,s.__decorate)([(0,o.MZ)({type:String,reflect:!0})],c.prototype,"graphic",void 0)},56220:(t,e,i)=>{i.d(e,{R:()=>s});const s=i(40924).AH`:host(:not([twoline])){height:56px}:host(:not([left])) .mdc-deprecated-list-item__meta{height:40px;width:40px}`},99791:(t,e,i)=>{i.d(e,{i0:()=>y});i(27934),i(21950),i(71936),i(55888),i(66274),i(38129),i(85038),i(84531),i(98168),i(8339);var s=i(34078),o=i(3358),n=i(75031);i(22836),i(15445),i(24483),i(13478),i(46355),i(14612),i(53691),i(48455);const r=new WeakMap;let h=0;const l=new Map,a=new WeakSet,d=()=>new Promise((t=>requestAnimationFrame(t))),c=(t,e)=>{const i=t-e;return 0===i?void 0:i},p=(t,e)=>{const i=t/e;return 1===i?void 0:i},u={left:(t,e)=>{const i=c(t,e);return{value:i,transform:null==i||isNaN(i)?void 0:`translateX(${i}px)`}},top:(t,e)=>{const i=c(t,e);return{value:i,transform:null==i||isNaN(i)?void 0:`translateY(${i}px)`}},width:(t,e)=>{let i;0===e&&(e=1,i={width:"1px"});const s=p(t,e);return{value:s,overrideFrom:i,transform:null==s||isNaN(s)?void 0:`scaleX(${s})`}},height:(t,e)=>{let i;0===e&&(e=1,i={height:"1px"});const s=p(t,e);return{value:s,overrideFrom:i,transform:null==s||isNaN(s)?void 0:`scaleY(${s})`}}},v={duration:333,easing:"ease-in-out"},m=["left","top","width","height","opacity","color","background"],f=new WeakMap;class g extends n.Kq{constructor(t){if(super(t),this.t=!1,this.i=null,this.o=null,this.h=!0,this.shouldLog=!1,t.type===o.OA.CHILD)throw Error("The `animate` directive must be used in attribute position.");this.createFinished()}createFinished(){var t;null!==(t=this.resolveFinished)&&void 0!==t&&t.call(this),this.finished=new Promise((t=>{this.l=t}))}async resolveFinished(){var t;null!==(t=this.l)&&void 0!==t&&t.call(this),this.l=void 0}render(t){return s.s6}getController(){return r.get(this.u)}isDisabled(){var t;return this.options.disabled||(null===(t=this.getController())||void 0===t?void 0:t.disabled)}update(t,[e]){var i;const s=void 0===this.u;return s&&(this.u=null===(i=t.options)||void 0===i?void 0:i.host,this.u.addController(this),this.u.updateComplete.then((t=>this.t=!0)),this.element=t.element,f.set(this.element,this)),this.optionsOrCallback=e,(s||"function"!=typeof e)&&this.p(e),this.render(e)}p(t){var e,i,s;t=null!==(e=t)&&void 0!==e?e:{};const o=this.getController();void 0!==o&&((t={...o.defaultOptions,...t}).keyframeOptions={...o.defaultOptions.keyframeOptions,...t.keyframeOptions}),null!==(s=(i=t).properties)&&void 0!==s||(i.properties=m),this.options=t}m(){const t={},e=this.element.getBoundingClientRect(),i=getComputedStyle(this.element);return this.options.properties.forEach((s=>{var o;const n=null!==(o=e[s])&&void 0!==o?o:u[s]?void 0:i[s],r=Number(n);t[s]=isNaN(r)?n+"":r})),t}v(){let t,e=!0;return this.options.guard&&(t=this.options.guard(),e=((t,e)=>{if(Array.isArray(t)){if(Array.isArray(e)&&e.length===t.length&&t.every(((t,i)=>t===e[i])))return!1}else if(e===t)return!1;return!0})(t,this._)),this.h=this.t&&!this.isDisabled()&&!this.isAnimating()&&e&&this.element.isConnected,this.h&&(this._=Array.isArray(t)?Array.from(t):t),this.h}hostUpdate(){var t;"function"==typeof this.optionsOrCallback&&this.p(this.optionsOrCallback()),this.v()&&(this.A=this.m(),this.i=null!==(t=this.i)&&void 0!==t?t:this.element.parentNode,this.o=this.element.nextSibling)}async hostUpdated(){if(!this.h||!this.element.isConnected||this.options.skipInitial&&!this.isHostRendered)return;let t;this.prepare(),await d;const e=this.O(),i=this.j(this.options.keyframeOptions,e),s=this.m();if(void 0!==this.A){const{from:i,to:o}=this.N(this.A,s,e);this.log("measured",[this.A,s,i,o]),t=this.calculateKeyframes(i,o)}else{const i=l.get(this.options.inId);if(i){l.delete(this.options.inId);const{from:o,to:n}=this.N(i,s,e);t=this.calculateKeyframes(o,n),t=this.options.in?[{...this.options.in[0],...t[0]},...this.options.in.slice(1),t[1]]:t,h++,t.forEach((t=>t.zIndex=h))}else this.options.in&&(t=[...this.options.in,{}])}this.animate(t,i)}resetStyles(){var t;void 0!==this.P&&(this.element.setAttribute("style",null!==(t=this.P)&&void 0!==t?t:""),this.P=void 0)}commitStyles(){var t,e;this.P=this.element.getAttribute("style"),null!==(t=this.webAnimation)&&void 0!==t&&t.commitStyles(),null===(e=this.webAnimation)||void 0===e||e.cancel()}reconnected(){}async disconnected(){var t;if(!this.h)return;if(void 0!==this.options.id&&l.set(this.options.id,this.A),void 0===this.options.out)return;if(this.prepare(),await d(),null!==(t=this.i)&&void 0!==t&&t.isConnected){const t=this.o&&this.o.parentNode===this.i?this.o:null;if(this.i.insertBefore(this.element,t),this.options.stabilizeOut){const t=this.m();this.log("stabilizing out");const e=this.A.left-t.left,i=this.A.top-t.top;!("static"===getComputedStyle(this.element).position)||0===e&&0===i||(this.element.style.position="relative"),0!==e&&(this.element.style.left=e+"px"),0!==i&&(this.element.style.top=i+"px")}}const e=this.j(this.options.keyframeOptions);await this.animate(this.options.out,e),this.element.remove()}prepare(){this.createFinished()}start(){var t,e;null===(t=(e=this.options).onStart)||void 0===t||t.call(e,this)}didFinish(t){var e,i;t&&null!==(e=(i=this.options).onComplete)&&void 0!==e&&e.call(i,this),this.A=void 0,this.animatingProperties=void 0,this.frames=void 0,this.resolveFinished()}O(){const t=[];for(let i=this.element.parentNode;i;i=null===(e=i)||void 0===e?void 0:e.parentNode){var e;const s=f.get(i);s&&!s.isDisabled()&&s&&t.push(s)}return t}get isHostRendered(){const t=a.has(this.u);return t||this.u.updateComplete.then((()=>{a.add(this.u)})),t}j(t,e=this.O()){const i={...v};return e.forEach((t=>Object.assign(i,t.options.keyframeOptions))),Object.assign(i,t),i}N(t,e,i){t={...t},e={...e};const s=i.map((t=>t.animatingProperties)).filter((t=>void 0!==t));let o=1,n=1;return s.length>0&&(s.forEach((t=>{t.width&&(o/=t.width),t.height&&(n/=t.height)})),void 0!==t.left&&void 0!==e.left&&(t.left=o*t.left,e.left=o*e.left),void 0!==t.top&&void 0!==e.top&&(t.top=n*t.top,e.top=n*e.top)),{from:t,to:e}}calculateKeyframes(t,e,i=!1){const s={},o={};let n=!1;const r={};for(const i in e){const l=t[i],a=e[i];if(i in u){var h;const t=u[i];if(void 0===l||void 0===a)continue;const e=t(l,a);void 0!==e.transform&&(r[i]=e.value,n=!0,s.transform=`${null!==(h=s.transform)&&void 0!==h?h:""} ${e.transform}`,void 0!==e.overrideFrom&&Object.assign(s,e.overrideFrom))}else l!==a&&void 0!==l&&void 0!==a&&(n=!0,s[i]=l,o[i]=a)}return s.transformOrigin=o.transformOrigin=i?"center center":"top left",this.animatingProperties=r,n?[s,o]:void 0}async animate(t,e=this.options.keyframeOptions){this.start(),this.frames=t;let i=!1;if(!this.isAnimating()&&!this.isDisabled()&&(this.options.onFrames&&(this.frames=t=this.options.onFrames(this),this.log("modified frames",t)),void 0!==t)){this.log("animate",[t,e]),i=!0,this.webAnimation=this.element.animate(t,e);const s=this.getController();null==s||s.add(this);try{await this.webAnimation.finished}catch(t){}null==s||s.remove(this)}return this.didFinish(i),i}isAnimating(){var t,e;return"running"===(null===(t=this.webAnimation)||void 0===t?void 0:t.playState)||(null===(e=this.webAnimation)||void 0===e?void 0:e.pending)}log(t,e){this.shouldLog&&!this.isDisabled()&&console.log(t,this.options.id,e)}}const y=(0,o.u$)(g);i(53501);const x=["top","right","bottom","left"];class b extends n.Kq{constructor(t){if(super(t),t.type!==o.OA.ELEMENT)throw Error("The `position` directive must be used in attribute position.")}render(t,e){return s.s6}update(t,[e,i]){var s;return void 0===this.u&&(this.u=null===(s=t.options)||void 0===s?void 0:s.host,this.u.addController(this)),this.S=t.element,this.C=e,this.F=null!=i?i:["left","top","width","height"],this.render(e,i)}hostUpdated(){this.$()}$(){var t,e;const i="function"==typeof this.C?this.C():null===(t=this.C)||void 0===t?void 0:t.value,s=i.offsetParent;if(void 0===i||!s)return;const o=i.getBoundingClientRect(),n=s.getBoundingClientRect();null===(e=this.F)||void 0===e||e.forEach((t=>{const e=x.includes(t)?o[t]-n[t]:o[t];this.S.style[t]=e+"px"}))}}(0,o.u$)(b)},66580:(t,e,i)=>{i.d(e,{u:()=>h});i(27934),i(21950),i(8339);var s=i(34078),o=i(2154),n=i(3982);const r=(t,e,i)=>{const s=new Map;for(let o=e;o<=i;o++)s.set(t[o],o);return s},h=(0,o.u$)(class extends o.WL{constructor(t){if(super(t),t.type!==o.OA.CHILD)throw Error("repeat() can only be used in text expressions")}ct(t,e,i){let s;void 0===i?i=e:void 0!==e&&(s=e);const o=[],n=[];let r=0;for(const e of t)o[r]=s?s(e,r):r,n[r]=i(e,r),r++;return{values:n,keys:o}}render(t,e,i){return this.ct(t,e,i).values}update(t,[e,i,o]){var h;const l=(0,n.cN)(t),{values:a,keys:d}=this.ct(e,i,o);if(!Array.isArray(l))return this.ut=d,a;const c=null!==(h=this.ut)&&void 0!==h?h:this.ut=[],p=[];let u,v,m=0,f=l.length-1,g=0,y=a.length-1;for(;m<=f&&g<=y;)if(null===l[m])m++;else if(null===l[f])f--;else if(c[m]===d[g])p[g]=(0,n.lx)(l[m],a[g]),m++,g++;else if(c[f]===d[y])p[y]=(0,n.lx)(l[f],a[y]),f--,y--;else if(c[m]===d[y])p[y]=(0,n.lx)(l[m],a[y]),(0,n.Dx)(t,p[y+1],l[m]),m++,y--;else if(c[f]===d[g])p[g]=(0,n.lx)(l[f],a[g]),(0,n.Dx)(t,l[m],l[f]),f--,g++;else if(void 0===u&&(u=r(d,g,y),v=r(c,m,f)),u.has(c[m]))if(u.has(c[f])){const e=v.get(d[g]),i=void 0!==e?l[e]:null;if(null===i){const e=(0,n.Dx)(t,l[m]);(0,n.lx)(e,a[g]),p[g]=e}else p[g]=(0,n.lx)(i,a[g]),(0,n.Dx)(t,l[m],i),l[e]=null;g++}else(0,n.KO)(l[f]),f--;else(0,n.KO)(l[m]),m++;for(;g<=y;){const e=(0,n.Dx)(t,p[y+1]);(0,n.lx)(e,a[g]),p[g++]=e}for(;m<=f;){const t=l[m++];null!==t&&(0,n.KO)(t)}return this.ut=d,(0,n.mY)(t,p),s.c0}})}};
//# sourceMappingURL=24709.ikAmoCKbn2s.js.map