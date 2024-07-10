export const id=99368;export const ids=[99368];export const modules={43690:(t,e,i)=>{i.d(e,{p:()=>p});var a=i(62659),s=i(76504),o=i(80792),d=(i(21950),i(14460),i(55888),i(66274),i(84531),i(98168),i(22836),i(15445),i(24483),i(13478),i(46355),i(14612),i(53691),i(48455),i(8339),i(40924)),n=i(18791),r=i(69760),l=i(80204),h=i(77664),c=i(38519),u=i(47394);const p=3e5;(0,a.A)([(0,n.EM)("ha-chart-base")],(function(t,e){class a extends e{constructor(...e){super(...e),t(this)}}return{F:a,d:[{kind:"field",key:"chart",value:void 0},{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.MZ)({attribute:"chart-type",reflect:!0})],key:"chartType",value:()=>"line"},{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"data",value:()=>({datasets:[]})},{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"extraData",value:void 0},{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"options",value:void 0},{kind:"field",decorators:[(0,n.MZ)({attribute:!1})],key:"plugins",value:void 0},{kind:"field",decorators:[(0,n.MZ)({type:Number})],key:"height",value:void 0},{kind:"field",decorators:[(0,n.MZ)({type:Number})],key:"paddingYAxis",value:()=>0},{kind:"field",decorators:[(0,n.MZ)({type:Boolean})],key:"externalHidden",value:()=>!1},{kind:"field",decorators:[(0,n.wk)()],key:"_chartHeight",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"_tooltip",value:void 0},{kind:"field",decorators:[(0,n.wk)()],key:"_hiddenDatasets",value:()=>new Set},{kind:"field",key:"_paddingUpdateCount",value:()=>0},{kind:"field",key:"_paddingUpdateLock",value:()=>!1},{kind:"field",key:"_paddingYAxisInternal",value:()=>0},{kind:"field",key:"_datasetOrder",value:()=>[]},{kind:"method",key:"disconnectedCallback",value:function(){(0,s.A)((0,o.A)(a.prototype),"disconnectedCallback",this).call(this),this._releaseCanvas()}},{kind:"method",key:"connectedCallback",value:function(){(0,s.A)((0,o.A)(a.prototype),"connectedCallback",this).call(this),this.hasUpdated&&(this._releaseCanvas(),this._setupChart())}},{kind:"field",key:"updateChart",value(){return t=>{var e;null===(e=this.chart)||void 0===e||e.update(t)}}},{kind:"field",key:"resize",value(){return t=>{var e,i,a,s;if(null!=t&&t.aspectRatio&&!t.height)t.height=Math.round((null!==(s=t.width)&&void 0!==s?s:this.clientWidth)/t.aspectRatio);else if(null!=t&&t.aspectRatio&&!t.width){var o;t.width=Math.round((null!==(o=t.height)&&void 0!==o?o:this.clientHeight)*t.aspectRatio)}null===(e=this.chart)||void 0===e||e.resize(null!==(i=null==t?void 0:t.width)&&void 0!==i?i:this.clientWidth,null!==(a=null==t?void 0:t.height)&&void 0!==a?a:this.clientHeight)}}},{kind:"method",key:"firstUpdated",value:function(){this._setupChart(),this.data.datasets.forEach(((t,e)=>{t.hidden&&this._hiddenDatasets.add(e)}))}},{kind:"method",key:"shouldUpdate",value:function(t){return!this._paddingUpdateLock||1!==t.size||!t.has("paddingYAxis")}},{kind:"field",key:"_debouncedClearUpdates",value(){return(0,u.s)((()=>{this._paddingUpdateCount=0}),2e3,!1)}},{kind:"method",key:"willUpdate",value:function(t){var e,i;((0,s.A)((0,o.A)(a.prototype),"willUpdate",this).call(this,t),this._paddingUpdateLock||(this._paddingYAxisInternal=this.paddingYAxis,1===t.size&&t.has("paddingYAxis")&&(this._paddingUpdateCount++,this._paddingUpdateCount>300?(this._paddingUpdateLock=!0,console.error("Detected excessive chart padding updates, possibly an infinite loop. Disabling axis padding.")):this._debouncedClearUpdates())),t.has("data"))&&(this._datasetOrder=this.data.datasets.map(((t,e)=>e)),null!==(e=this.data)&&void 0!==e&&e.datasets.some((t=>t.order))&&this._datasetOrder.sort(((t,e)=>(this.data.datasets[t].order||0)-(this.data.datasets[e].order||0))),this.externalHidden&&(this._hiddenDatasets=new Set,null!==(i=this.data)&&void 0!==i&&i.datasets&&this.data.datasets.forEach(((t,e)=>{t.hidden&&this._hiddenDatasets.add(e)}))));if(this.hasUpdated&&this.chart){if(t.has("plugins")||t.has("chartType"))return this._releaseCanvas(),void this._setupChart();t.has("data")&&(this._hiddenDatasets.size&&!this.externalHidden&&this.data.datasets.forEach(((t,e)=>{t.hidden=this._hiddenDatasets.has(e)})),this.chart.data=this.data),t.has("options")&&(this.chart.options=this._createOptions()),this.chart.update("none")}}},{kind:"method",key:"render",value:function(){var t,e,i;return d.qy` ${!0===(null===(t=this.options)||void 0===t||null===(t=t.plugins)||void 0===t||null===(t=t.legend)||void 0===t?void 0:t.display)?d.qy`<div class="chartLegend"> <ul> ${this._datasetOrder.map((t=>{var e,i,a,s,o;const n=this.data.datasets[t];return!1===(null===(e=this.extraData)||void 0===e||null===(e=e[t])||void 0===e?void 0:e.show_legend)?d.s6:d.qy`<li .datasetIndex="${t}" @click="${this._legendClick}" class="${(0,r.H)({hidden:this._hiddenDatasets.has(t)})}" .title="${null!==(i=null===(a=this.extraData)||void 0===a||null===(a=a[t])||void 0===a?void 0:a.legend_label)&&void 0!==i?i:n.label}"> <div class="bullet" style="${(0,l.W)({backgroundColor:n.backgroundColor,borderColor:n.borderColor})}"></div> <div class="label"> ${null!==(s=null===(o=this.extraData)||void 0===o||null===(o=o[t])||void 0===o?void 0:o.legend_label)&&void 0!==s?s:n.label} </div> </li>`}))} </ul> </div>`:""} <div class="animationContainer" style="${(0,l.W)({height:`${this.height||this._chartHeight||0}px`,overflow:this._chartHeight?"initial":"hidden"})}"> <div class="chartContainer" style="${(0,l.W)({height:`${null!==(e=null!==(i=this.height)&&void 0!==i?i:this._chartHeight)&&void 0!==e?e:this.clientWidth/2}px`,"padding-left":`${this._paddingYAxisInternal}px`,"padding-right":0,"padding-inline-start":`${this._paddingYAxisInternal}px`,"padding-inline-end":0})}"> <canvas></canvas> ${this._tooltip?d.qy`<div class="chartTooltip ${(0,r.H)({[this._tooltip.yAlign]:!0})}" style="${(0,l.W)({top:this._tooltip.top,left:this._tooltip.left})}"> <div class="title">${this._tooltip.title}</div> ${this._tooltip.beforeBody?d.qy`<div class="beforeBody"> ${this._tooltip.beforeBody} </div>`:""} <div> <ul> ${this._tooltip.body.map(((t,e)=>d.qy`<li> <div class="bullet" style="${(0,l.W)({backgroundColor:this._tooltip.labelColors[e].backgroundColor,borderColor:this._tooltip.labelColors[e].borderColor})}"></div> ${t.lines.join("\n")} </li>`))} </ul> </div> ${this._tooltip.footer.length?d.qy`<div class="footer"> ${this._tooltip.footer.map((t=>d.qy`${t}<br>`))} </div>`:""} </div>`:""} </div> </div> `}},{kind:"field",key:"_loading",value:()=>!1},{kind:"method",key:"_setupChart",value:async function(){if(this._loading)return;const t=this.renderRoot.querySelector("canvas").getContext("2d");this._loading=!0;try{const e=(await Promise.all([i.e(55285),i.e(50893),i.e(60386),i.e(80928)]).then(i.bind(i,50713))).Chart,a=getComputedStyle(this);e.defaults.borderColor=a.getPropertyValue("--divider-color"),e.defaults.color=a.getPropertyValue("--secondary-text-color"),e.defaults.font.family=a.getPropertyValue("--mdc-typography-body1-font-family")||a.getPropertyValue("--mdc-typography-font-family")||"Roboto, Noto, sans-serif",this.chart=new e(t,{type:this.chartType,data:this.data,options:this._createOptions(),plugins:this._createPlugins()})}finally{this._loading=!1}}},{kind:"method",key:"_createOptions",value:function(){var t,e,i;return{maintainAspectRatio:!1,...this.options,plugins:{...null===(t=this.options)||void 0===t?void 0:t.plugins,tooltip:{...null===(e=this.options)||void 0===e||null===(e=e.plugins)||void 0===e?void 0:e.tooltip,enabled:!1,external:t=>this._handleTooltip(t)},legend:{...null===(i=this.options)||void 0===i||null===(i=i.plugins)||void 0===i?void 0:i.legend,display:!1}}}}},{kind:"method",key:"_createPlugins",value:function(){var t;return[...this.plugins||[],{id:"resizeHook",resize:t=>{var e;const i=t.height-(null!==(e=this._chartHeight)&&void 0!==e?e:0);(!this._chartHeight||i>12||i<-12)&&(this._chartHeight=t.height)},legend:{...null===(t=this.options)||void 0===t||null===(t=t.plugins)||void 0===t?void 0:t.legend,display:!1}}]}},{kind:"method",key:"_legendClick",value:function(t){if(!this.chart)return;const e=t.currentTarget.datasetIndex;this.chart.isDatasetVisible(e)?(this.chart.setDatasetVisibility(e,!1),this._hiddenDatasets.add(e),this.externalHidden&&(0,h.r)(this,"dataset-hidden",{index:e})):(this.chart.setDatasetVisibility(e,!0),this._hiddenDatasets.delete(e),this.externalHidden&&(0,h.r)(this,"dataset-unhidden",{index:e})),this.chart.update("none"),this.requestUpdate("_hiddenDatasets")}},{kind:"method",key:"_handleTooltip",value:function(t){0!==t.tooltip.opacity?this._tooltip={...t.tooltip,top:this.chart.canvas.offsetTop+t.tooltip.caretY+12+"px",left:this.chart.canvas.offsetLeft+(0,c.q)(t.tooltip.caretX,100,this.clientWidth-100-this._paddingYAxisInternal)-100+"px"}:this._tooltip=void 0}},{kind:"method",key:"_releaseCanvas",value:function(){this.chart&&this.chart.destroy()}},{kind:"get",static:!0,key:"styles",value:function(){return d.AH`:host{display:block;position:var(--chart-base-position,relative)}.animationContainer{overflow:hidden;height:0;transition:height .3s cubic-bezier(.4, 0, .2, 1)}canvas{max-height:var(--chart-max-height,400px)}.chartLegend{text-align:center}.chartLegend li{cursor:pointer;display:inline-grid;grid-auto-flow:column;padding:0 8px;box-sizing:border-box;align-items:center;color:var(--secondary-text-color)}.chartLegend .hidden{text-decoration:line-through}.chartLegend .label{text-overflow:ellipsis;white-space:nowrap;overflow:hidden}.chartLegend .bullet,.chartTooltip .bullet{border-width:1px;border-style:solid;border-radius:50%;display:inline-block;height:16px;margin-right:6px;width:16px;flex-shrink:0;box-sizing:border-box;margin-inline-end:6px;margin-inline-start:initial;direction:var(--direction)}.chartTooltip .bullet{align-self:baseline}.chartTooltip{padding:8px;font-size:90%;position:absolute;background:rgba(80,80,80,.9);color:#fff;border-radius:4px;pointer-events:none;z-index:1;-ms-user-select:none;-webkit-user-select:none;-moz-user-select:none;width:200px;box-sizing:border-box;direction:var(--direction)}.chartLegend ul,.chartTooltip ul{display:inline-block;padding:0 0px;margin:8px 0 0 0;width:100%}.chartTooltip ul{margin:0 4px}.chartTooltip li{display:flex;white-space:pre-line;word-break:break-word;align-items:center;line-height:16px;padding:4px 0}.chartTooltip .title{text-align:center;font-weight:500;word-break:break-word;direction:ltr}.chartTooltip .footer{font-weight:500}.chartTooltip .beforeBody{text-align:center;font-weight:300;word-break:break-all}`}}]}}),d.WF)},83256:(t,e,i)=>{i.d(e,{g:()=>o});var a=i(92849),s=i(1471);function o(t,e,i,o,d,n){const r=t.getPropertyValue(d+"-"+n).trim(),l=r.length>0?r:t.getPropertyValue(d).trim();let h=(0,a.RQ)(l);return 0===r.length&&n&&(h=(0,a.v2)((0,a.BE)(e?(0,s.T)((0,a.Nc)((0,a.xp)(h)),n):(0,s.d)((0,a.Nc)((0,a.xp)(h)),n)))),o?h+=i?"32":"7F":i&&(h+="7F"),h}},72113:(t,e,i)=>{i.a(t,(async(t,a)=>{try{i.d(e,{o:()=>p});var s=i(81408),o=i(81438),d=i(28252),n=i(84749),r=i(56601),l=i(77396),h=i(60441),c=t([r,l,h]);function u(t,e){let i=new Date(e);return t>2&&0===i.getHours()&&(i=(0,s.O)(i,1)),i.setMinutes(0,0,0),t>35&&i.setDate(1),t>2&&i.setHours(0),i.getTime()}function p(t,e,i,a,s,c,p){const g=(0,o.c)(e,t),v=void 0!==c&&void 0!==p;if(v&&g<=35){const i=(0,d.M)(e,t),a=(0,d.M)(p,c);a>i?e=(0,n.L)(e,a-i):i>a&&(p=(0,n.L)(p,i-a))}const y={parsing:!1,animation:!1,interaction:{mode:"x"},scales:{x:{type:"time",suggestedMin:t.getTime(),max:u(g,e),adapters:{date:{locale:i,config:a}},ticks:{maxRotation:0,sampleSize:5,autoSkipPadding:20,font:t=>t.tick&&t.tick.major?{weight:"bold"}:{}},time:{tooltipFormat:g>35?"monthyear":g>7?"date":g>2?"weekday":g>0?"datetime":"hour",minUnit:g>35?"month":g>2?"day":"hour"}},y:{stacked:!0,type:"linear",title:{display:!0,text:s},ticks:{beginAtZero:!0,callback:t=>(0,r.ZV)(Math.abs(t),i)}}},plugins:{tooltip:{position:"nearest",filter:t=>"0"!==t.formattedValue,itemSort:function(t,e){return e.datasetIndex-t.datasetIndex},callbacks:{title:t=>{if(g>0)return t[0].label;const e=new Date(t[0].parsed.x);return`${v?`${(0,l.sl)(e,i,a)}: `:""}${(0,h.fU)(e,i,a)} – ${(0,h.fU)((0,n.L)(e,1),i,a)}`},label:t=>`${t.dataset.label}: ${(0,r.ZV)(t.parsed.y,i)} ${s}`}},filler:{propagate:!1},legend:{display:!1,labels:{usePointStyle:!0}}},elements:{bar:{borderWidth:1.5,borderRadius:4},point:{hitRadius:50}},locale:(0,r.Yf)(i)};return v&&(y.scales.xAxisCompare={...y.scales.x,suggestedMin:c.getTime(),max:u(g,p),display:!1}),y}[r,l,h]=c.then?(await c)():c,a()}catch(g){a(g)}}))},99368:(t,e,i)=>{i.a(t,(async(t,a)=>{try{i.r(e),i.d(e,{HuiEnergyGasGraphCard:()=>b});var s=i(62659),o=(i(21950),i(71936),i(55888),i(66274),i(85038),i(84531),i(8339),i(40133)),d=i(42180),n=i(79581),r=i(40924),l=i(18791),h=i(69760),c=i(45081),u=i(83256),p=i(56601),g=(i(43690),i(54373),i(41525)),v=i(74959),y=i(94027),k=i(15821),f=i(72113),_=t([p,g,f]);[p,g,f]=_.then?(await _)():_;let b=(0,s.A)([(0,l.EM)("hui-energy-gas-graph-card")],(function(t,e){return{F:class extends e{constructor(...e){super(...e),t(this)}},d:[{kind:"field",decorators:[(0,l.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,l.wk)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,l.wk)()],key:"_chartData",value:()=>({datasets:[]})},{kind:"field",decorators:[(0,l.wk)()],key:"_start",value:()=>(0,o.R)()},{kind:"field",decorators:[(0,l.wk)()],key:"_end",value:()=>(0,d.o)()},{kind:"field",decorators:[(0,l.wk)()],key:"_compareStart",value:void 0},{kind:"field",decorators:[(0,l.wk)()],key:"_compareEnd",value:void 0},{kind:"field",decorators:[(0,l.wk)()],key:"_unit",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:()=>["_config"]},{kind:"method",key:"hassSubscribe",value:function(){var t;return[(0,g.tb)(this.hass,{key:null===(t=this._config)||void 0===t?void 0:t.collection_key}).subscribe((t=>this._getStatistics(t)))]}},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"setConfig",value:function(t){this._config=t}},{kind:"method",key:"shouldUpdate",value:function(t){return(0,k.xP)(this,t)||t.size>1||!t.has("hass")}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?r.qy` <ha-card> ${this._config.title?r.qy`<h1 class="card-header">${this._config.title}</h1>`:""} <div class="content ${(0,h.H)({"has-header":!!this._config.title})}"> <ha-chart-base .hass="${this.hass}" .data="${this._chartData}" .options="${this._createOptions(this._start,this._end,this.hass.locale,this.hass.config,this._unit,this._compareStart,this._compareEnd)}" chart-type="bar"></ha-chart-base> ${this._chartData.datasets.length?"":r.qy`<div class="no-data"> ${(0,n.c)(this._start)?this.hass.localize("ui.panel.lovelace.cards.energy.no_data"):this.hass.localize("ui.panel.lovelace.cards.energy.no_data_period")} </div>`} </div> </ha-card> `:r.s6}},{kind:"field",key:"_createOptions",value(){return(0,c.A)(((t,e,i,a,s,o,d)=>{const n=(0,f.o)(t,e,i,a,s,o,d);return{...n,plugins:{...n.plugins,tooltip:{...n.plugins.tooltip,callbacks:{...n.plugins.tooltip.callbacks,footer:t=>{if(t.length<2)return[];let e=0;for(const i of t)e+=i.dataset.data[i.dataIndex].y;return 0===e?[]:[this.hass.localize("ui.panel.lovelace.cards.energy.energy_gas_graph.total_consumed",{num:(0,p.ZV)(e,i),unit:s})]}}}}}}))}},{kind:"method",key:"_getStatistics",value:async function(t){const e=t.prefs.energy_sources.filter((t=>"gas"===t.type));this._unit=(0,g.KJ)(this.hass,t.prefs,t.statsMetadata)||"m³";const i=[],a=getComputedStyle(this);i.push(...this._processDataSet(t.stats,t.statsMetadata,e,a)),t.statsCompare&&(i.push({order:0,data:[]}),i.push({order:999,data:[],xAxisID:"xAxisCompare"}),i.push(...this._processDataSet(t.statsCompare,t.statsMetadata,e,a,!0))),this._start=t.start,this._end=t.end||(0,d.o)(),this._compareStart=t.startCompare,this._compareEnd=t.endCompare,this._chartData={datasets:i}}},{kind:"method",key:"_processDataSet",value:function(t,e,i,a,s=!1){const o=[];return i.forEach(((i,d)=>{let n=null;const r=[];if(i.stat_energy_from in t){const e=t[i.stat_energy_from];let a;for(const t of e){if(null===t.change||void 0===t.change)continue;if(n===t.start)continue;const e=new Date(t.start);r.push({x:e.getTime(),y:t.change}),n=t.start,a=t.end}1===r.length&&r.push({x:a,y:0})}o.push({label:(0,v.$O)(this.hass,i.stat_energy_from,e[i.stat_energy_from]),borderColor:(0,u.g)(a,this.hass.themes.darkMode,!1,s,"--energy-gas-color",d),backgroundColor:(0,u.g)(a,this.hass.themes.darkMode,!0,s,"--energy-gas-color",d),data:r,order:1,stack:"gas",xAxisID:s?"xAxisCompare":void 0})})),o}},{kind:"get",static:!0,key:"styles",value:function(){return r.AH`ha-card{height:100%}.card-header{padding-bottom:0}.content{padding:16px}.has-header{padding-top:0}.no-data{position:absolute;height:100%;top:0;left:0;right:0;display:flex;justify-content:center;align-items:center;padding:20%;margin-left:32px;margin-inline-start:32px;margin-inline-end:initial;box-sizing:border-box}`}}]}}),(0,y.E)(r.WF));a()}catch(t){a(t)}}))}};
//# sourceMappingURL=99368.em10SMF6MhA.js.map