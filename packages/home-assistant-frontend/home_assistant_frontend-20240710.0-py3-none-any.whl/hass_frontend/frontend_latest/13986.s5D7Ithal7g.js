export const id=13986;export const ids=[13986];export const modules={97484:(e,t,i)=>{i.d(t,{J:()=>l});i(53501);var a=i(45081),d=i(25786);const l=(0,a.A)((e=>{if(e.time_format===d.Hg.language||e.time_format===d.Hg.system){const t=e.time_format===d.Hg.language?e.language:void 0;return new Date("January 1, 2023 22:00:00").toLocaleString(t).includes("10")}return e.time_format===d.Hg.am_pm}))},48962:(e,t,i)=>{i.d(t,{d:()=>a});const a=e=>e.stopPropagation()},34800:(e,t,i)=>{i.d(t,{E:()=>d,m:()=>a});i(55888);const a=e=>{requestAnimationFrame((()=>setTimeout(e,0)))},d=()=>new Promise((e=>{a(e)}))},50983:(e,t,i)=>{var a=i(62659),d=(i(21950),i(8339),i(23981),i(40924)),l=i(18791),n=i(79278),s=i(77664),o=i(48962);i(59799),i(55118);(0,a.A)([(0,l.EM)("ha-base-time-input")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,l.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,l.MZ)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"autoValidate",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"required",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Number})],key:"format",value:()=>12},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Number})],key:"days",value:()=>0},{kind:"field",decorators:[(0,l.MZ)({type:Number})],key:"hours",value:()=>0},{kind:"field",decorators:[(0,l.MZ)({type:Number})],key:"minutes",value:()=>0},{kind:"field",decorators:[(0,l.MZ)({type:Number})],key:"seconds",value:()=>0},{kind:"field",decorators:[(0,l.MZ)({type:Number})],key:"milliseconds",value:()=>0},{kind:"field",decorators:[(0,l.MZ)()],key:"dayLabel",value:()=>""},{kind:"field",decorators:[(0,l.MZ)()],key:"hourLabel",value:()=>""},{kind:"field",decorators:[(0,l.MZ)()],key:"minLabel",value:()=>""},{kind:"field",decorators:[(0,l.MZ)()],key:"secLabel",value:()=>""},{kind:"field",decorators:[(0,l.MZ)()],key:"millisecLabel",value:()=>""},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"enableSecond",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"enableMillisecond",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"enableDay",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"noHoursLimit",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)()],key:"amPm",value:()=>"AM"},{kind:"method",key:"render",value:function(){return d.qy` ${this.label?d.qy`<label>${this.label}${this.required?" *":""}</label>`:""} <div class="time-input-wrap"> ${this.enableDay?d.qy` <ha-textfield id="day" type="number" inputmode="numeric" .value="${this.days.toFixed()}" .label="${this.dayLabel}" name="days" @change="${this._valueChanged}" @focusin="${this._onFocus}" no-spinner .required="${this.required}" .autoValidate="${this.autoValidate}" min="0" .disabled="${this.disabled}" suffix=":" class="hasSuffix"> </ha-textfield> `:""} <ha-textfield id="hour" type="number" inputmode="numeric" .value="${this.hours.toFixed()}" .label="${this.hourLabel}" name="hours" @change="${this._valueChanged}" @focusin="${this._onFocus}" no-spinner .required="${this.required}" .autoValidate="${this.autoValidate}" maxlength="2" max="${(0,n.J)(this._hourMax)}" min="0" .disabled="${this.disabled}" suffix=":" class="hasSuffix"> </ha-textfield> <ha-textfield id="min" type="number" inputmode="numeric" .value="${this._formatValue(this.minutes)}" .label="${this.minLabel}" @change="${this._valueChanged}" @focusin="${this._onFocus}" name="minutes" no-spinner .required="${this.required}" .autoValidate="${this.autoValidate}" maxlength="2" max="59" min="0" .disabled="${this.disabled}" .suffix="${this.enableSecond?":":""}" class="${this.enableSecond?"has-suffix":""}"> </ha-textfield> ${this.enableSecond?d.qy`<ha-textfield id="sec" type="number" inputmode="numeric" .value="${this._formatValue(this.seconds)}" .label="${this.secLabel}" @change="${this._valueChanged}" @focusin="${this._onFocus}" name="seconds" no-spinner .required="${this.required}" .autoValidate="${this.autoValidate}" maxlength="2" max="59" min="0" .disabled="${this.disabled}" .suffix="${this.enableMillisecond?":":""}" class="${this.enableMillisecond?"has-suffix":""}"> </ha-textfield>`:""} ${this.enableMillisecond?d.qy`<ha-textfield id="millisec" type="number" .value="${this._formatValue(this.milliseconds,3)}" .label="${this.millisecLabel}" @change="${this._valueChanged}" @focusin="${this._onFocus}" name="milliseconds" no-spinner .required="${this.required}" .autoValidate="${this.autoValidate}" maxlength="3" max="999" min="0" .disabled="${this.disabled}"> </ha-textfield>`:""} ${24===this.format?"":d.qy`<ha-select .required="${this.required}" .value="${this.amPm}" .disabled="${this.disabled}" name="amPm" naturalMenuWidth fixedMenuPosition @selected="${this._valueChanged}" @closed="${o.d}"> <mwc-list-item value="AM">AM</mwc-list-item> <mwc-list-item value="PM">PM</mwc-list-item> </ha-select>`} </div> ${this.helper?d.qy`<ha-input-helper-text>${this.helper}</ha-input-helper-text>`:""} `}},{kind:"method",key:"_valueChanged",value:function(e){const t=e.currentTarget;this[t.name]="amPm"===t.name?t.value:Number(t.value);const i={hours:this.hours,minutes:this.minutes,seconds:this.seconds,milliseconds:this.milliseconds};this.enableDay&&(i.days=this.days),12===this.format&&(i.amPm=this.amPm),(0,s.r)(this,"value-changed",{value:i})}},{kind:"method",key:"_onFocus",value:function(e){e.currentTarget.select()}},{kind:"method",key:"_formatValue",value:function(e,t=2){return e.toString().padStart(t,"0")}},{kind:"get",key:"_hourMax",value:function(){if(!this.noHoursLimit)return 12===this.format?12:23}},{kind:"field",static:!0,key:"styles",value:()=>d.AH`:host{display:block}.time-input-wrap{display:flex;border-radius:var(--mdc-shape-small,4px) var(--mdc-shape-small,4px) 0 0;overflow:hidden;position:relative;direction:ltr}ha-textfield{width:40px;text-align:center;--mdc-shape-small:0;--text-field-appearance:none;--text-field-padding:0 4px;--text-field-suffix-padding-left:2px;--text-field-suffix-padding-right:0;--text-field-text-align:center}ha-textfield.hasSuffix{--text-field-padding:0 0 0 4px}ha-textfield:first-child{--text-field-border-top-left-radius:var(--mdc-shape-medium)}ha-textfield:last-child{--text-field-border-top-right-radius:var(--mdc-shape-medium)}ha-select{--mdc-shape-small:0;width:85px}label{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:var(
        --mdc-typography-body2-font-family,
        var(--mdc-typography-font-family, Roboto, sans-serif)
      );font-size:var(--mdc-typography-body2-font-size, .875rem);line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:var(--mdc-typography-body2-font-weight,400);letter-spacing:var(
        --mdc-typography-body2-letter-spacing,
        .0178571429em
      );text-decoration:var(--mdc-typography-body2-text-decoration,inherit);text-transform:var(--mdc-typography-body2-text-transform,inherit);color:var(--mdc-theme-text-primary-on-background,rgba(0,0,0,.87));padding-left:4px;padding-inline-start:4px;padding-inline-end:initial}`}]}}),d.WF)},55118:(e,t,i)=>{var a=i(62659),d=(i(21950),i(8339),i(40924)),l=i(18791);(0,a.A)([(0,l.EM)("ha-input-helper-text")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"method",key:"render",value:function(){return d.qy`<slot></slot>`}},{kind:"field",static:!0,key:"styles",value:()=>d.AH`:host{display:block;color:var(--mdc-text-field-label-ink-color,rgba(0,0,0,.6));font-size:.75rem;padding-left:16px;padding-right:16px;padding-inline-start:16px;padding-inline-end:16px}`}]}}),d.WF)},59799:(e,t,i)=>{var a=i(62659),d=i(76504),l=i(80792),n=(i(21950),i(55888),i(8339),i(32503)),s=i(50988),o=i(40924),r=i(18791),c=i(47394),u=i(34800);i(12731);(0,a.A)([(0,r.EM)("ha-select")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,r.MZ)({type:Boolean})],key:"icon",value:()=>!1},{kind:"field",decorators:[(0,r.MZ)({type:Boolean,reflect:!0})],key:"clearable",value:()=>!1},{kind:"method",key:"render",value:function(){return o.qy` ${(0,d.A)((0,l.A)(i.prototype),"render",this).call(this)} ${this.clearable&&!this.required&&!this.disabled&&this.value?o.qy`<ha-icon-button label="clear" @click="${this._clearValue}" .path="${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}"></ha-icon-button>`:o.s6} `}},{kind:"method",key:"renderLeadingIcon",value:function(){return this.icon?o.qy`<span class="mdc-select__icon"><slot name="icon"></slot></span>`:o.s6}},{kind:"method",key:"connectedCallback",value:function(){(0,d.A)((0,l.A)(i.prototype),"connectedCallback",this).call(this),window.addEventListener("translations-updated",this._translationsUpdated)}},{kind:"method",key:"disconnectedCallback",value:function(){(0,d.A)((0,l.A)(i.prototype),"disconnectedCallback",this).call(this),window.removeEventListener("translations-updated",this._translationsUpdated)}},{kind:"method",key:"_clearValue",value:function(){!this.disabled&&this.value&&(this.valueSetDirectly=!0,this.select(-1),this.mdcFoundation.handleChange())}},{kind:"field",key:"_translationsUpdated",value(){return(0,c.s)((async()=>{await(0,u.E)(),this.layoutOptions()}),500)}},{kind:"field",static:!0,key:"styles",value:()=>[s.R,o.AH`:host([clearable]){position:relative}.mdc-select:not(.mdc-select--disabled) .mdc-select__icon{color:var(--secondary-text-color)}.mdc-select__anchor{width:var(--ha-select-min-width,200px)}.mdc-select--filled .mdc-select__anchor{height:var(--ha-select-height,56px)}.mdc-select--filled .mdc-floating-label{inset-inline-start:12px;inset-inline-end:initial;direction:var(--direction)}.mdc-select--filled.mdc-select--with-leading-icon .mdc-floating-label{inset-inline-start:48px;inset-inline-end:initial;direction:var(--direction)}.mdc-select .mdc-select__anchor{padding-inline-start:12px;padding-inline-end:0px;direction:var(--direction)}.mdc-select__anchor .mdc-floating-label--float-above{transform-origin:var(--float-start)}.mdc-select__selected-text-container{padding-inline-end:var(--select-selected-text-padding-end,0px)}:host([clearable]) .mdc-select__selected-text-container{padding-inline-end:var(--select-selected-text-padding-end,12px)}ha-icon-button{position:absolute;top:10px;right:28px;--mdc-icon-button-size:36px;--mdc-icon-size:20px;color:var(--secondary-text-color);inset-inline-start:initial;inset-inline-end:28px;direction:var(--direction)}`]}]}}),n.o)},13986:(e,t,i)=>{i.r(t),i.d(t,{HaTimeSelector:()=>n});var a=i(62659),d=(i(21950),i(8339),i(40924)),l=i(18791);i(68467);let n=(0,a.A)([(0,l.EM)("ha-selector-time")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,l.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,l.MZ)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,l.MZ)()],key:"value",value:void 0},{kind:"field",decorators:[(0,l.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,l.MZ)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"required",value:()=>!1},{kind:"method",key:"render",value:function(){return d.qy` <ha-time-input .value="${"string"==typeof this.value?this.value:void 0}" .locale="${this.hass.locale}" .disabled="${this.disabled}" .required="${this.required}" .helper="${this.helper}" .label="${this.label}" enable-second></ha-time-input> `}}]}}),d.WF)},68467:(e,t,i)=>{var a=i(62659),d=(i(21950),i(8339),i(40924)),l=i(18791),n=i(97484),s=i(77664);i(50983);(0,a.A)([(0,l.EM)("ha-time-input")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,l.MZ)({attribute:!1})],key:"locale",value:void 0},{kind:"field",decorators:[(0,l.MZ)()],key:"value",value:void 0},{kind:"field",decorators:[(0,l.MZ)()],key:"label",value:void 0},{kind:"field",decorators:[(0,l.MZ)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"disabled",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean})],key:"required",value:()=>!1},{kind:"field",decorators:[(0,l.MZ)({type:Boolean,attribute:"enable-second"})],key:"enableSecond",value:()=>!1},{kind:"method",key:"render",value:function(){var e;const t=(0,n.J)(this.locale),i=(null===(e=this.value)||void 0===e?void 0:e.split(":"))||[];let a=i[0];const l=Number(i[0]);return l&&t&&l>12&&l<24&&(a=String(l-12).padStart(2,"0")),t&&0===l&&(a="12"),d.qy` <ha-base-time-input .label="${this.label}" .hours="${Number(a)}" .minutes="${Number(i[1])}" .seconds="${Number(i[2])}" .format="${t?12:24}" .amPm="${t&&l>=12?"PM":"AM"}" .disabled="${this.disabled}" @value-changed="${this._timeChanged}" .enableSecond="${this.enableSecond}" .required="${this.required}" .helper="${this.helper}"></ha-base-time-input> `}},{kind:"method",key:"_timeChanged",value:function(e){e.stopPropagation();const t=e.detail.value,i=(0,n.J)(this.locale);let a;if(!isNaN(t.hours)||!isNaN(t.minutes)||!isNaN(t.seconds)){let e=t.hours||0;t&&i&&("PM"===t.amPm&&e<12&&(e+=12),"AM"===t.amPm&&12===e&&(e=0)),a=`${e.toString().padStart(2,"0")}:${t.minutes?t.minutes.toString().padStart(2,"0"):"00"}:${t.seconds?t.seconds.toString().padStart(2,"0"):"00"}`}a!==this.value&&(this.value=a,(0,s.r)(this,"change"),(0,s.r)(this,"value-changed",{value:a}))}}]}}),d.WF)}};
//# sourceMappingURL=13986.s5D7Ithal7g.js.map