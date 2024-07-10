export const id=68943;export const ids=[68943];export const modules={48962:(e,i,t)=>{t.d(i,{d:()=>a});const a=e=>e.stopPropagation()},34800:(e,i,t)=>{t.d(i,{E:()=>d,m:()=>a});t(55888);const a=e=>{requestAnimationFrame((()=>setTimeout(e,0)))},d=()=>new Promise((e=>{a(e)}))},50983:(e,i,t)=>{var a=t(62659),d=(t(21950),t(8339),t(23981),t(40924)),n=t(18791),l=t(79278),s=t(77664),o=t(48962);t(59799),t(55118);(0,a.A)([(0,n.EM)("ha-base-time-input")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.MZ)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"autoValidate",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"required",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Number})],key:"format",value:()=>12},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Number})],key:"days",value:()=>0},{kind:"field",decorators:[(0,n.MZ)({type:Number})],key:"hours",value:()=>0},{kind:"field",decorators:[(0,n.MZ)({type:Number})],key:"minutes",value:()=>0},{kind:"field",decorators:[(0,n.MZ)({type:Number})],key:"seconds",value:()=>0},{kind:"field",decorators:[(0,n.MZ)({type:Number})],key:"milliseconds",value:()=>0},{kind:"field",decorators:[(0,n.MZ)()],key:"dayLabel",value:()=>""},{kind:"field",decorators:[(0,n.MZ)()],key:"hourLabel",value:()=>""},{kind:"field",decorators:[(0,n.MZ)()],key:"minLabel",value:()=>""},{kind:"field",decorators:[(0,n.MZ)()],key:"secLabel",value:()=>""},{kind:"field",decorators:[(0,n.MZ)()],key:"millisecLabel",value:()=>""},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"enableSecond",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"enableMillisecond",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"enableDay",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"noHoursLimit",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)()],key:"amPm",value:()=>"AM"},{kind:"method",key:"render",value:function(){return d.qy` ${this.label?d.qy`<label>${this.label}${this.required?" *":""}</label>`:""} <div class="time-input-wrap"> ${this.enableDay?d.qy` <ha-textfield id="day" type="number" inputmode="numeric" .value="${this.days.toFixed()}" .label="${this.dayLabel}" name="days" @change="${this._valueChanged}" @focusin="${this._onFocus}" no-spinner .required="${this.required}" .autoValidate="${this.autoValidate}" min="0" .disabled="${this.disabled}" suffix=":" class="hasSuffix"> </ha-textfield> `:""} <ha-textfield id="hour" type="number" inputmode="numeric" .value="${this.hours.toFixed()}" .label="${this.hourLabel}" name="hours" @change="${this._valueChanged}" @focusin="${this._onFocus}" no-spinner .required="${this.required}" .autoValidate="${this.autoValidate}" maxlength="2" max="${(0,l.J)(this._hourMax)}" min="0" .disabled="${this.disabled}" suffix=":" class="hasSuffix"> </ha-textfield> <ha-textfield id="min" type="number" inputmode="numeric" .value="${this._formatValue(this.minutes)}" .label="${this.minLabel}" @change="${this._valueChanged}" @focusin="${this._onFocus}" name="minutes" no-spinner .required="${this.required}" .autoValidate="${this.autoValidate}" maxlength="2" max="59" min="0" .disabled="${this.disabled}" .suffix="${this.enableSecond?":":""}" class="${this.enableSecond?"has-suffix":""}"> </ha-textfield> ${this.enableSecond?d.qy`<ha-textfield id="sec" type="number" inputmode="numeric" .value="${this._formatValue(this.seconds)}" .label="${this.secLabel}" @change="${this._valueChanged}" @focusin="${this._onFocus}" name="seconds" no-spinner .required="${this.required}" .autoValidate="${this.autoValidate}" maxlength="2" max="59" min="0" .disabled="${this.disabled}" .suffix="${this.enableMillisecond?":":""}" class="${this.enableMillisecond?"has-suffix":""}"> </ha-textfield>`:""} ${this.enableMillisecond?d.qy`<ha-textfield id="millisec" type="number" .value="${this._formatValue(this.milliseconds,3)}" .label="${this.millisecLabel}" @change="${this._valueChanged}" @focusin="${this._onFocus}" name="milliseconds" no-spinner .required="${this.required}" .autoValidate="${this.autoValidate}" maxlength="3" max="999" min="0" .disabled="${this.disabled}"> </ha-textfield>`:""} ${24===this.format?"":d.qy`<ha-select .required="${this.required}" .value="${this.amPm}" .disabled="${this.disabled}" name="amPm" naturalMenuWidth fixedMenuPosition @selected="${this._valueChanged}" @closed="${o.d}"> <mwc-list-item value="AM">AM</mwc-list-item> <mwc-list-item value="PM">PM</mwc-list-item> </ha-select>`} </div> ${this.helper?d.qy`<ha-input-helper-text>${this.helper}</ha-input-helper-text>`:""} `}},{kind:"method",key:"_valueChanged",value:function(e){const i=e.currentTarget;this[i.name]="amPm"===i.name?i.value:Number(i.value);const t={hours:this.hours,minutes:this.minutes,seconds:this.seconds,milliseconds:this.milliseconds};this.enableDay&&(t.days=this.days),12===this.format&&(t.amPm=this.amPm),(0,s.r)(this,"value-changed",{value:t})}},{kind:"method",key:"_onFocus",value:function(e){e.currentTarget.select()}},{kind:"method",key:"_formatValue",value:function(e,i=2){return e.toString().padStart(i,"0")}},{kind:"get",key:"_hourMax",value:function(){if(!this.noHoursLimit)return 12===this.format?12:23}},{kind:"field",static:!0,key:"styles",value:()=>d.AH`:host{display:block}.time-input-wrap{display:flex;border-radius:var(--mdc-shape-small,4px) var(--mdc-shape-small,4px) 0 0;overflow:hidden;position:relative;direction:ltr}ha-textfield{width:40px;text-align:center;--mdc-shape-small:0;--text-field-appearance:none;--text-field-padding:0 4px;--text-field-suffix-padding-left:2px;--text-field-suffix-padding-right:0;--text-field-text-align:center}ha-textfield.hasSuffix{--text-field-padding:0 0 0 4px}ha-textfield:first-child{--text-field-border-top-left-radius:var(--mdc-shape-medium)}ha-textfield:last-child{--text-field-border-top-right-radius:var(--mdc-shape-medium)}ha-select{--mdc-shape-small:0;width:85px}label{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:var(
        --mdc-typography-body2-font-family,
        var(--mdc-typography-font-family, Roboto, sans-serif)
      );font-size:var(--mdc-typography-body2-font-size, .875rem);line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:var(--mdc-typography-body2-font-weight,400);letter-spacing:var(
        --mdc-typography-body2-letter-spacing,
        .0178571429em
      );text-decoration:var(--mdc-typography-body2-text-decoration,inherit);text-transform:var(--mdc-typography-body2-text-transform,inherit);color:var(--mdc-theme-text-primary-on-background,rgba(0,0,0,.87));padding-left:4px;padding-inline-start:4px;padding-inline-end:initial}`}]}}),d.WF)},30658:(e,i,t)=>{var a=t(62659),d=(t(21950),t(8339),t(40924)),n=t(18791),l=t(77664);t(50983);(0,a.A)([(0,n.EM)("ha-duration-input")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,n.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.MZ)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"required",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"enableMillisecond",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"enableDay",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,n.P)("paper-time-input",!0)],key:"_input",value:void 0},{kind:"method",key:"focus",value:function(){this._input&&this._input.focus()}},{kind:"method",key:"render",value:function(){return d.qy` <ha-base-time-input .label="${this.label}" .helper="${this.helper}" .required="${this.required}" .autoValidate="${this.required}" .disabled="${this.disabled}" errorMessage="Required" enableSecond .enableMillisecond="${this.enableMillisecond}" .enableDay="${this.enableDay}" format="24" .days="${this._days}" .hours="${this._hours}" .minutes="${this._minutes}" .seconds="${this._seconds}" .milliseconds="${this._milliseconds}" @value-changed="${this._durationChanged}" noHoursLimit dayLabel="dd" hourLabel="hh" minLabel="mm" secLabel="ss" millisecLabel="ms"></ha-base-time-input> `}},{kind:"get",key:"_days",value:function(){var e;return null!==(e=this.data)&&void 0!==e&&e.days?Number(this.data.days):0}},{kind:"get",key:"_hours",value:function(){var e;return null!==(e=this.data)&&void 0!==e&&e.hours?Number(this.data.hours):0}},{kind:"get",key:"_minutes",value:function(){var e;return null!==(e=this.data)&&void 0!==e&&e.minutes?Number(this.data.minutes):0}},{kind:"get",key:"_seconds",value:function(){var e;return null!==(e=this.data)&&void 0!==e&&e.seconds?Number(this.data.seconds):0}},{kind:"get",key:"_milliseconds",value:function(){var e;return null!==(e=this.data)&&void 0!==e&&e.milliseconds?Number(this.data.milliseconds):0}},{kind:"method",key:"_durationChanged",value:function(e){e.stopPropagation();const i={...e.detail.value};var t;(this.enableMillisecond||i.milliseconds?i.milliseconds>999&&(i.seconds+=Math.floor(i.milliseconds/1e3),i.milliseconds%=1e3):delete i.milliseconds,i.seconds>59&&(i.minutes+=Math.floor(i.seconds/60),i.seconds%=60),i.minutes>59&&(i.hours+=Math.floor(i.minutes/60),i.minutes%=60),this.enableDay&&i.hours>24)&&(i.days=(null!==(t=i.days)&&void 0!==t?t:0)+Math.floor(i.hours/24),i.hours%=24);(0,l.r)(this,"value-changed",{value:i})}}]}}),d.WF)},55118:(e,i,t)=>{var a=t(62659),d=(t(21950),t(8339),t(40924)),n=t(18791);(0,a.A)([(0,n.EM)("ha-input-helper-text")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"method",key:"render",value:function(){return d.qy`<slot></slot>`}},{kind:"field",static:!0,key:"styles",value:()=>d.AH`:host{display:block;color:var(--mdc-text-field-label-ink-color,rgba(0,0,0,.6));font-size:.75rem;padding-left:16px;padding-right:16px;padding-inline-start:16px;padding-inline-end:16px}`}]}}),d.WF)},59799:(e,i,t)=>{var a=t(62659),d=t(76504),n=t(80792),l=(t(21950),t(55888),t(8339),t(32503)),s=t(50988),o=t(40924),r=t(18791),u=t(47394),c=t(34800);t(12731);(0,a.A)([(0,r.EM)("ha-select")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"icon",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean,reflect:!0})],key:"clearable",value:()=>!1},{kind:"method",key:"render",value:function(){return o.qy` ${(0,d.A)((0,n.A)(t.prototype),"render",this).call(this)} ${this.clearable&&!this.required&&!this.disabled&&this.value?o.qy`<ha-icon-button label="clear" @click="${this._clearValue}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}"></ha-icon-button>`:o.s6} `}},{kind:"method",key:"renderLeadingIcon",value:function(){return this.icon?o.qy`<span class="mdc-select__icon"><slot name="icon"></slot></span>`:o.s6}},{kind:"method",key:"connectedCallback",value:function(){(0,d.A)((0,n.A)(t.prototype),"connectedCallback",this).call(this),window.addEventListener("translations-updated",this._translationsUpdated)}},{kind:"method",key:"disconnectedCallback",value:function(){(0,d.A)((0,n.A)(t.prototype),"disconnectedCallback",this).call(this),window.removeEventListener("translations-updated",this._translationsUpdated)}},{kind:"method",key:"_clearValue",value:function(){!this.disabled&&this.value&&(this.valueSetDirectly=!0,this.select(-1),this.mdcFoundation.handleChange())}},{kind:"field",key:"_translationsUpdated",value(){return(0,u.s)((async()=>{await(0,c.E)(),this.layoutOptions()}),500)}},{kind:"field",static:!0,key:"styles",value:()=>[s.R,o.AH`:host([clearable]){position:relative}.mdc-select:not(.mdc-select--disabled) .mdc-select__icon{color:var(--secondary-text-color)}.mdc-select__anchor{width:var(--ha-select-min-width,200px)}.mdc-select--filled .mdc-select__anchor{height:var(--ha-select-height,56px)}.mdc-select--filled .mdc-floating-label{inset-inline-start:12px;inset-inline-end:initial;direction:var(--direction)}.mdc-select--filled.mdc-select--with-leading-icon .mdc-floating-label{inset-inline-start:48px;inset-inline-end:initial;direction:var(--direction)}.mdc-select .mdc-select__anchor{padding-inline-start:12px;padding-inline-end:0px;direction:var(--direction)}.mdc-select__anchor .mdc-floating-label--float-above{transform-origin:var(--float-start)}.mdc-select__selected-text-container{padding-inline-end:var(--select-selected-text-padding-end,0px)}:host([clearable]) .mdc-select__selected-text-container{padding-inline-end:var(--select-selected-text-padding-end,12px)}ha-icon-button{position:absolute;top:10px;right:28px;--mdc-icon-button-size:36px;--mdc-icon-size:20px;color:var(--secondary-text-color);inset-inline-start:initial;inset-inline-end:28px;direction:var(--direction)}`]}]}}),l.o)},68943:(e,i,t)=>{t.r(i),t.d(i,{HaTimeDuration:()=>l});var a=t(62659),d=(t(21950),t(8339),t(40924)),n=t(18791);t(30658);let l=(0,a.A)([(0,n.EM)("ha-selector-duration")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"value",value:void 0},{kind:"field",decorators:[(0,n.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.MZ)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"required",value:()=>!0},{kind:"method",key:"render",value:function(){var e;return d.qy` <ha-duration-input .label="${this.label}" .helper="${this.helper}" .data="${this.value}" .disabled="${this.disabled}" .required="${this.required}" ?enableDay="${null===(e=this.selector.duration)||void 0===e?void 0:e.enable_day}"></ha-duration-input> `}}]}}),d.WF)}};
//# sourceMappingURL=68943.BxamgwIqEGk.js.map