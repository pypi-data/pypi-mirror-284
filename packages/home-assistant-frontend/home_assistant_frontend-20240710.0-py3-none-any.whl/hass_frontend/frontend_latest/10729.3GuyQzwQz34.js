/*! For license information please see 10729.3GuyQzwQz34.js.LICENSE.txt */
export const id=10729;export const ids=[10729];export const modules={91619:(r,t,e)=>{e.d(t,{$:()=>g});e(21950),e(8339);var o=e(76513),i=e(54788),a=e(18791),s=e(71086),n=e(86029),c=e(69303),l=e(40924),d=e(69760);const p=n.QQ?{passive:!0}:void 0;class v extends s.O{constructor(){super(...arguments),this.centerTitle=!1,this.handleTargetScroll=()=>{this.mdcFoundation.handleTargetScroll()},this.handleNavigationClick=()=>{this.mdcFoundation.handleNavigationClick()}}get scrollTarget(){return this._scrollTarget||window}set scrollTarget(r){this.unregisterScrollListener();const t=this.scrollTarget;this._scrollTarget=r,this.updateRootPosition(),this.requestUpdate("scrollTarget",t),this.registerScrollListener()}updateRootPosition(){if(this.mdcRoot){const r=this.scrollTarget===window;this.mdcRoot.style.position=r?"":"absolute"}}render(){let r=l.qy`<span class="mdc-top-app-bar__title"><slot name="title"></slot></span>`;return this.centerTitle&&(r=l.qy`<section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-center">${r}</section>`),l.qy` <header class="mdc-top-app-bar ${(0,d.H)(this.barClasses())}"> <div class="mdc-top-app-bar__row"> <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start" id="navigation"> <slot name="navigationIcon" @click="${this.handleNavigationClick}"></slot> ${this.centerTitle?null:r} </section> ${this.centerTitle?r:null} <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end" id="actions" role="toolbar"> <slot name="actionItems"></slot> </section> </div> </header> <div class="${(0,d.H)(this.contentClasses())}"> <slot></slot> </div> `}createAdapter(){return Object.assign(Object.assign({},(0,s.i)(this.mdcRoot)),{setStyle:(r,t)=>this.mdcRoot.style.setProperty(r,t),getTopAppBarHeight:()=>this.mdcRoot.clientHeight,notifyNavigationIconClicked:()=>{this.dispatchEvent(new Event(c.P$.NAVIGATION_EVENT,{bubbles:!0,cancelable:!0}))},getViewportScrollY:()=>this.scrollTarget instanceof Window?this.scrollTarget.pageYOffset:this.scrollTarget.scrollTop,getTotalActionItems:()=>this._actionItemsSlot.assignedNodes({flatten:!0}).length})}registerListeners(){this.registerScrollListener()}unregisterListeners(){this.unregisterScrollListener()}registerScrollListener(){this.scrollTarget.addEventListener("scroll",this.handleTargetScroll,p)}unregisterScrollListener(){this.scrollTarget.removeEventListener("scroll",this.handleTargetScroll)}firstUpdated(){super.firstUpdated(),this.updateRootPosition(),this.registerListeners()}disconnectedCallback(){super.disconnectedCallback(),this.unregisterListeners()}}(0,o.__decorate)([(0,a.P)(".mdc-top-app-bar")],v.prototype,"mdcRoot",void 0),(0,o.__decorate)([(0,a.P)('slot[name="actionItems"]')],v.prototype,"_actionItemsSlot",void 0),(0,o.__decorate)([(0,a.MZ)({type:Boolean})],v.prototype,"centerTitle",void 0),(0,o.__decorate)([(0,a.MZ)({type:Object})],v.prototype,"scrollTarget",null);class h extends v{constructor(){super(...arguments),this.mdcFoundationClass=i.A,this.prominent=!1,this.dense=!1,this.handleResize=()=>{this.mdcFoundation.handleWindowResize()}}barClasses(){return{"mdc-top-app-bar--dense":this.dense,"mdc-top-app-bar--prominent":this.prominent,"center-title":this.centerTitle}}contentClasses(){return{"mdc-top-app-bar--fixed-adjust":!this.dense&&!this.prominent,"mdc-top-app-bar--dense-fixed-adjust":this.dense&&!this.prominent,"mdc-top-app-bar--prominent-fixed-adjust":!this.dense&&this.prominent,"mdc-top-app-bar--dense-prominent-fixed-adjust":this.dense&&this.prominent}}registerListeners(){super.registerListeners(),window.addEventListener("resize",this.handleResize,p)}unregisterListeners(){super.unregisterListeners(),window.removeEventListener("resize",this.handleResize)}}(0,o.__decorate)([(0,a.MZ)({type:Boolean,reflect:!0})],h.prototype,"prominent",void 0),(0,o.__decorate)([(0,a.MZ)({type:Boolean,reflect:!0})],h.prototype,"dense",void 0);var u=e(70750);class g extends h{constructor(){super(...arguments),this.mdcFoundationClass=u.A}barClasses(){return Object.assign(Object.assign({},super.barClasses()),{"mdc-top-app-bar--fixed":!0})}registerListeners(){this.scrollTarget.addEventListener("scroll",this.handleTargetScroll,p)}unregisterListeners(){this.scrollTarget.removeEventListener("scroll",this.handleTargetScroll)}}},79372:(r,t,e)=>{var o=e(73155),i=e(33817),a=e(3429),s=e(75077);r.exports=function(r,t){t&&"string"==typeof r||i(r);var e=s(r);return a(i(void 0!==e?o(e,r):r))}},18684:(r,t,e)=>{var o=e(87568),i=e(42509),a=e(30356),s=e(51607),n=e(95124),c=e(79635);o({target:"Array",proto:!0},{flatMap:function(r){var t,e=s(this),o=n(e);return a(r),(t=c(e,0)).length=i(t,e,e,o,0,1,r,arguments.length>1?arguments[1]:void 0),t}})},74991:(r,t,e)=>{e(33523)("flatMap")},66076:(r,t,e)=>{var o=e(87568),i=e(73155),a=e(82374),s=e(43972),n=e(38095),c=e(52579),l=e(95358),d=e(83841),p=e(18720),v=e(18532),h=e(4624),u=e(60533),g=e(89385),m=u("replace"),f=TypeError,b=a("".indexOf),_=a("".replace),y=a("".slice),x=Math.max;o({target:"String",proto:!0},{replaceAll:function(r,t){var e,o,a,u,w,T,C,k,L,S=s(this),z=0,M=0,R="";if(!c(r)){if((e=l(r))&&(o=d(s(v(r))),!~b(o,"g")))throw new f("`.replaceAll` does not allow non-global regexes");if(a=p(r,m))return i(a,r,S,t);if(g&&e)return _(d(S),r,t)}for(u=d(S),w=d(r),(T=n(t))||(t=d(t)),C=w.length,k=x(1,C),z=b(u,w);-1!==z;)L=T?d(t(w,z,u)):h(w,u,z,[],void 0,t),R+=y(u,M,z)+L,M=z+C,z=z+k>u.length?-1:b(u,w,z+k);return M<u.length&&(R+=y(u,M)),R}})},69704:(r,t,e)=>{var o=e(87568),i=e(73155),a=e(30356),s=e(33817),n=e(3429),c=e(79372),l=e(23408),d=e(44933),p=e(89385),v=l((function(){for(var r,t,e=this.iterator,o=this.mapper;;){if(t=this.inner)try{if(!(r=s(i(t.next,t.iterator))).done)return r.value;this.inner=null}catch(r){d(e,"throw",r)}if(r=s(i(this.next,e)),this.done=!!r.done)return;try{this.inner=c(o(r.value,this.counter++),!1)}catch(r){d(e,"throw",r)}}}));o({target:"Iterator",proto:!0,real:!0,forced:p},{flatMap:function(r){return s(this),a(r),new v(n(this),{mapper:r,inner:null})}})},57305:(r,t,e)=>{e.d(t,{U:()=>p});var o=e(76513),i=e(18791),a=e(40924),s=(e(21950),e(8339),e(69760)),n=e(67371);class c extends a.WF{constructor(){super(...arguments),this.value=0,this.max=1,this.indeterminate=!1,this.fourColor=!1}render(){const{ariaLabel:r}=this;return a.qy` <div class="progress ${(0,s.H)(this.getRenderClasses())}" role="progressbar" aria-label="${r||a.s6}" aria-valuemin="0" aria-valuemax="${this.max}" aria-valuenow="${this.indeterminate?a.s6:this.value}">${this.renderIndicator()}</div> `}getRenderClasses(){return{indeterminate:this.indeterminate,"four-color":this.fourColor}}}(0,n.F)(c),(0,o.__decorate)([(0,i.MZ)({type:Number})],c.prototype,"value",void 0),(0,o.__decorate)([(0,i.MZ)({type:Number})],c.prototype,"max",void 0),(0,o.__decorate)([(0,i.MZ)({type:Boolean})],c.prototype,"indeterminate",void 0),(0,o.__decorate)([(0,i.MZ)({type:Boolean,attribute:"four-color"})],c.prototype,"fourColor",void 0);class l extends c{renderIndicator(){return this.indeterminate?this.renderIndeterminateContainer():this.renderDeterminateContainer()}renderDeterminateContainer(){const r=100*(1-this.value/this.max);return a.qy` <svg viewBox="0 0 4800 4800"> <circle class="track" pathLength="100"></circle> <circle class="active-track" pathLength="100" stroke-dashoffset="${r}"></circle> </svg> `}renderIndeterminateContainer(){return a.qy` <div class="spinner"> <div class="left"> <div class="circle"></div> </div> <div class="right"> <div class="circle"></div> </div> </div>`}}const d=a.AH`:host{--_active-indicator-color:var(--md-circular-progress-active-indicator-color, var(--md-sys-color-primary, #6750a4));--_active-indicator-width:var(--md-circular-progress-active-indicator-width, 10);--_four-color-active-indicator-four-color:var(--md-circular-progress-four-color-active-indicator-four-color, var(--md-sys-color-tertiary-container, #ffd8e4));--_four-color-active-indicator-one-color:var(--md-circular-progress-four-color-active-indicator-one-color, var(--md-sys-color-primary, #6750a4));--_four-color-active-indicator-three-color:var(--md-circular-progress-four-color-active-indicator-three-color, var(--md-sys-color-tertiary, #7d5260));--_four-color-active-indicator-two-color:var(--md-circular-progress-four-color-active-indicator-two-color, var(--md-sys-color-primary-container, #eaddff));--_size:var(--md-circular-progress-size, 48px);display:inline-flex;vertical-align:middle;width:var(--_size);height:var(--_size);position:relative;align-items:center;justify-content:center;contain:strict;content-visibility:auto}.progress{flex:1;align-self:stretch;margin:4px}.active-track,.circle,.left,.progress,.right,.spinner,.track,svg{position:absolute;inset:0}svg{transform:rotate(-90deg)}circle{cx:50%;cy:50%;r:calc(50%*(1 - var(--_active-indicator-width)/ 100));stroke-width:calc(var(--_active-indicator-width)*1%);stroke-dasharray:100;fill:rgba(0,0,0,0)}.active-track{transition:stroke-dashoffset .5s cubic-bezier(0, 0, .2, 1);stroke:var(--_active-indicator-color)}.track{stroke:rgba(0,0,0,0)}.progress.indeterminate{animation:linear infinite linear-rotate;animation-duration:1.568s}.spinner{animation:infinite both rotate-arc;animation-duration:5332ms;animation-timing-function:cubic-bezier(0.4,0,0.2,1)}.left{overflow:hidden;inset:0 50% 0 0}.right{overflow:hidden;inset:0 0 0 50%}.circle{box-sizing:border-box;border-radius:50%;border:solid calc(var(--_active-indicator-width)/ 100*(var(--_size) - 8px));border-color:var(--_active-indicator-color) var(--_active-indicator-color) transparent transparent;animation:expand-arc;animation-iteration-count:infinite;animation-fill-mode:both;animation-duration:1333ms,5332ms;animation-timing-function:cubic-bezier(0.4,0,0.2,1)}.four-color .circle{animation-name:expand-arc,four-color}.left .circle{rotate:135deg;inset:0 -100% 0 0}.right .circle{rotate:100deg;inset:0 0 0 -100%;animation-delay:-.666s,0s}@media(forced-colors:active){.active-track{stroke:CanvasText}.circle{border-color:CanvasText CanvasText Canvas Canvas}}@keyframes expand-arc{0%{transform:rotate(265deg)}50%{transform:rotate(130deg)}100%{transform:rotate(265deg)}}@keyframes rotate-arc{12.5%{transform:rotate(135deg)}25%{transform:rotate(270deg)}37.5%{transform:rotate(405deg)}50%{transform:rotate(540deg)}62.5%{transform:rotate(675deg)}75%{transform:rotate(810deg)}87.5%{transform:rotate(945deg)}100%{transform:rotate(1080deg)}}@keyframes linear-rotate{to{transform:rotate(360deg)}}@keyframes four-color{0%{border-top-color:var(--_four-color-active-indicator-one-color);border-right-color:var(--_four-color-active-indicator-one-color)}15%{border-top-color:var(--_four-color-active-indicator-one-color);border-right-color:var(--_four-color-active-indicator-one-color)}25%{border-top-color:var(--_four-color-active-indicator-two-color);border-right-color:var(--_four-color-active-indicator-two-color)}40%{border-top-color:var(--_four-color-active-indicator-two-color);border-right-color:var(--_four-color-active-indicator-two-color)}50%{border-top-color:var(--_four-color-active-indicator-three-color);border-right-color:var(--_four-color-active-indicator-three-color)}65%{border-top-color:var(--_four-color-active-indicator-three-color);border-right-color:var(--_four-color-active-indicator-three-color)}75%{border-top-color:var(--_four-color-active-indicator-four-color);border-right-color:var(--_four-color-active-indicator-four-color)}90%{border-top-color:var(--_four-color-active-indicator-four-color);border-right-color:var(--_four-color-active-indicator-four-color)}100%{border-top-color:var(--_four-color-active-indicator-one-color);border-right-color:var(--_four-color-active-indicator-one-color)}}`;let p=class extends l{};p.styles=[d],p=(0,o.__decorate)([(0,i.EM)("md-circular-progress")],p)},28252:(r,t,e)=>{e.d(t,{M:()=>s});var o=e(80345),i=e(49518),a=e(53181);function s(r,t,e){const s=(0,a.b)(r,t)/i.s0;return(0,o.u)(null==e?void 0:e.roundingMethod)(s)}},53181:(r,t,e)=>{e.d(t,{b:()=>i});var o=e(74396);function i(r,t){return+(0,o.a)(r)-+(0,o.a)(t)}}};
//# sourceMappingURL=10729.3GuyQzwQz34.js.map