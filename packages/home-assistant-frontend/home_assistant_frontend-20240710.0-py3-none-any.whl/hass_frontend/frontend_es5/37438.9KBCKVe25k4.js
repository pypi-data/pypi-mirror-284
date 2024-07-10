"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[37438],{36471:function(t,e,i){i.d(e,{_:function(){return c}});var n=i(539),a=i(89231),r=i(36683),o=i(29864),s=i(83647),d=(i(27934),i(21968),i(68113),i(66274),i(84531),i(34290),i(40924)),l=i(3358),c=(0,l.u$)(function(t){function e(t){var i;if((0,a.A)(this,e),(i=(0,o.A)(this,e,[t]))._element=void 0,t.type!==l.OA.CHILD)throw new Error("dynamicElementDirective can only be used in content bindings");return i}return(0,s.A)(e,t),(0,r.A)(e,[{key:"update",value:function(t,e){var i=this,a=(0,n.A)(e,2),r=a[0],o=a[1];return this._element&&this._element.localName===r?(o&&Object.entries(o).forEach((function(t){var e=(0,n.A)(t,2),a=e[0],r=e[1];i._element[a]=r})),d.c0):this.render(r,o)}},{key:"render",value:function(t,e){var i=this;return this._element=document.createElement(t),e&&Object.entries(e).forEach((function(t){var e=(0,n.A)(t,2),a=e[0],r=e[1];i._element[a]=r})),this._element}}])}(l.WL))},26846:function(t,e,i){var n=i(1781).A,a=i(94881).A;i.a(t,function(){var t=n(a().mark((function t(n,r){var o,s,d,l,c,u,h,f,p,m,v,k,g,y,_,x,b,A,w,E,M,q,D,S,j,C,O,Z,I,L,Y,z,T,H,F,P,W,R,N,U,B,K,V,J,G,Q,$,X,tt;return a().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(t.prev=0,i.d(e,{n:function(){return tt}}),o=i(539),s=i(61780),d=i(94881),l=i(1781),c=i(6238),u=i(36683),h=i(89231),f=i(29864),p=i(83647),m=i(8364),v=i(77052),k=i(53501),g=i(21950),y=i(36724),_=i(71936),x=i(14460),b=i(21968),A=i(1158),w=i(68113),E=i(57733),M=i(34517),q=i(56262),D=i(66274),S=i(84531),j=i(98168),C=i(15445),O=i(24483),Z=i(13478),I=i(46355),L=i(14612),Y=i(53691),z=i(48455),T=i(34290),H=i(8339),F=i(40924),P=i(196),W=i(45081),R=i(76502),N=i(6699),U=i(77664),B=i(56601),K=i(74959),i(43690),!(V=n([B])).then){t.next=77;break}return t.next=73,V;case 73:t.t1=t.sent,t.t0=(0,t.t1)(),t.next=78;break;case 77:t.t0=V;case 78:B=t.t0[0],tt={mean:"mean",min:"min",max:"max",sum:"sum",state:"sum",change:"sum"},(0,m.A)([(0,P.EM)("statistics-chart")],(function(t,e){var i,n=function(e){function i(){var e;(0,h.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return e=(0,f.A)(this,i,[].concat(a)),t(e),e}return(0,p.A)(i,e),(0,u.A)(i)}(e);return{F:n,d:[{kind:"field",decorators:[(0,P.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,P.MZ)({attribute:!1})],key:"statisticsData",value:void 0},{kind:"field",decorators:[(0,P.MZ)({attribute:!1})],key:"metadata",value:void 0},{kind:"field",decorators:[(0,P.MZ)({attribute:!1})],key:"names",value:void 0},{kind:"field",decorators:[(0,P.MZ)()],key:"unit",value:void 0},{kind:"field",decorators:[(0,P.MZ)({attribute:!1})],key:"endTime",value:void 0},{kind:"field",decorators:[(0,P.MZ)({type:Array})],key:"statTypes",value:function(){return["sum","min","mean","max"]}},{kind:"field",decorators:[(0,P.MZ)()],key:"chartType",value:function(){return"line"}},{kind:"field",decorators:[(0,P.MZ)({type:Boolean})],key:"hideLegend",value:function(){return!1}},{kind:"field",decorators:[(0,P.MZ)({type:Boolean})],key:"logarithmicScale",value:function(){return!1}},{kind:"field",decorators:[(0,P.MZ)({type:Boolean})],key:"isLoadingData",value:function(){return!1}},{kind:"field",decorators:[(0,P.MZ)({type:Boolean})],key:"clickForMoreInfo",value:function(){return!0}},{kind:"field",decorators:[(0,P.MZ)()],key:"period",value:void 0},{kind:"field",decorators:[(0,P.wk)()],key:"_chartData",value:function(){return{datasets:[]}}},{kind:"field",decorators:[(0,P.wk)()],key:"_chartDatasetExtra",value:function(){return[]}},{kind:"field",decorators:[(0,P.wk)()],key:"_statisticIds",value:function(){return[]}},{kind:"field",decorators:[(0,P.wk)()],key:"_chartOptions",value:void 0},{kind:"field",decorators:[(0,P.wk)()],key:"_hiddenStats",value:function(){return new Set}},{kind:"field",decorators:[(0,P.P)("ha-chart-base")],key:"_chart",value:void 0},{kind:"field",key:"_computedStyle",value:void 0},{kind:"field",key:"resize",value:function(){var t=this;return function(e){var i;null===(i=t._chart)||void 0===i||i.resize(e)}}},{kind:"method",key:"shouldUpdate",value:function(t){return t.size>1||!t.has("hass")}},{kind:"method",key:"willUpdate",value:function(t){t.has("legendMode")&&this._hiddenStats.clear(),(!this.hasUpdated||t.has("unit")||t.has("period")||t.has("chartType")||t.has("logarithmicScale")||t.has("hideLegend"))&&this._createOptions(),(t.has("statisticsData")||t.has("statTypes")||t.has("chartType")||t.has("hideLegend")||t.has("_hiddenStats"))&&this._generateData()}},{kind:"method",key:"firstUpdated",value:function(){this._computedStyle=getComputedStyle(this)}},{kind:"method",key:"render",value:function(){return(0,N.x)(this.hass,"history")?this.isLoadingData&&!this.statisticsData?(0,F.qy)(G||(G=(0,c.A)(['<div class="info"> '," </div>"])),this.hass.localize("ui.components.statistics_charts.loading_statistics")):this.statisticsData&&Object.keys(this.statisticsData).length?(0,F.qy)($||($=(0,c.A)([' <ha-chart-base externalHidden .hass="','" .data="','" .extraData="','" .options="','" .chartType="','" @dataset-hidden="','" @dataset-unhidden="','"></ha-chart-base> '])),this.hass,this._chartData,this._chartDatasetExtra,this._chartOptions,this.chartType,this._datasetHidden,this._datasetUnhidden):(0,F.qy)(Q||(Q=(0,c.A)(['<div class="info"> '," </div>"])),this.hass.localize("ui.components.statistics_charts.no_statistics_found")):(0,F.qy)(J||(J=(0,c.A)(['<div class="info"> '," </div>"])),this.hass.localize("ui.components.history_charts.history_disabled"))}},{kind:"method",key:"_datasetHidden",value:function(t){t.stopPropagation(),this._hiddenStats.add(this._statisticIds[t.detail.index]),this.requestUpdate("_hiddenStats")}},{kind:"method",key:"_datasetUnhidden",value:function(t){t.stopPropagation(),this._hiddenStats.delete(this._statisticIds[t.detail.index]),this.requestUpdate("_hiddenStats")}},{kind:"method",key:"_createOptions",value:function(t){var e=this;this._chartOptions={parsing:!1,animation:!1,interaction:{mode:"nearest",axis:"x"},scales:{x:{type:"time",adapters:{date:{locale:this.hass.locale,config:this.hass.config}},ticks:{source:"bar"===this.chartType?"data":void 0,maxRotation:0,sampleSize:5,autoSkipPadding:20,major:{enabled:!0},font:function(t){return t.tick&&t.tick.major?{weight:"bold"}:{}}},time:{tooltipFormat:"datetime",unit:"bar"===this.chartType&&this.period&&["hour","day","week","month"].includes(this.period)?this.period:void 0}},y:{beginAtZero:"bar"===this.chartType,ticks:{maxTicksLimit:7},title:{display:t||this.unit,text:t||this.unit},type:this.logarithmicScale?"logarithmic":"linear"}},plugins:{tooltip:{callbacks:{label:function(t){return"".concat(t.dataset.label,": ").concat((0,B.ZV)(t.parsed.y,e.hass.locale,(0,B.ZQ)(void 0,e.hass.entities[e._statisticIds[t.datasetIndex]]))," ").concat(t.dataset.unit||"")}}},filler:{propagate:!0},legend:{display:!this.hideLegend,labels:{usePointStyle:!0}}},elements:{line:{tension:.4,cubicInterpolationMode:"monotone",borderWidth:1.5},bar:{borderWidth:1.5,borderRadius:4},point:{hitRadius:50}},locale:(0,B.Yf)(this.hass.locale),onClick:function(t){if(e.clickForMoreInfo&&t.native instanceof MouseEvent&&!(t.native instanceof PointerEvent&&"mouse"!==t.native.pointerType)){var i=t.chart,n=i.getElementsAtEventForMode(t,"nearest",{intersect:!0},!0);if(n.length){var a=n[0],r=e._statisticIds[a.datasetIndex];(0,K.OQ)(r)||((0,U.r)(e,"hass-more-info",{entityId:r}),i.canvas.dispatchEvent(new Event("mouseout")))}}}}}},{kind:"field",key:"_getStatisticsMetaData",value:function(){var t=this;return(0,W.A)(function(){var e=(0,l.A)((0,d.A)().mark((function e(i){var n,a;return(0,d.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,(0,K.Wr)(t.hass,i);case 2:return n=e.sent,a={},n.forEach((function(t){a[t.statistic_id]=t})),e.abrupt("return",a);case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}())}},{kind:"method",key:"_generateData",value:(i=(0,l.A)((0,d.A)().mark((function t(){var e,i,n,a,r,l,c,u,h=this;return(0,d.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(this.statisticsData){t.next=2;break}return t.abrupt("return");case 2:if(t.t0=this.metadata,t.t0){t.next=7;break}return t.next=6,this._getStatisticsMetaData(Object.keys(this.statisticsData));case 6:t.t0=t.sent;case 7:if(e=t.t0,i=0,n=Object.entries(this.statisticsData),a=[],r=[],l=[],0!==n.length){t.next=15;break}return t.abrupt("return");case 15:(this.endTime||new Date(Math.max.apply(Math,(0,s.A)(n.map((function(t){var e=(0,o.A)(t,2),i=(e[0],e[1]);return new Date(i[i.length-1].start).getTime()}))))))>new Date&&new Date,u=this.names||{},n.forEach((function(t){var n=(0,o.A)(t,2),d=n[0],f=n[1],p=null==e?void 0:e[d],m=u[d];void 0===m&&(m=(0,K.$O)(h.hass,d,p)),h.unit||(void 0===c?c=(0,K.JE)(h.hass,d,p):null!==c&&c!==(0,K.JE)(h.hass,d,p)&&(c=null));var v,k=null,g=[],y=[],_=(0,R.fI)(i,h._computedStyle||getComputedStyle(h));i++;var x=[],b=h.statTypes.includes("mean")&&(0,K.iY)(f,"mean"),A=b||h.statTypes.includes("min")&&(0,K.iY)(f,"min")&&h.statTypes.includes("max")&&(0,K.iY)(f,"max"),w=A?(0,s.A)(h.statTypes).sort((function(t,e){return"min"===t||"max"===e?-1:"max"===t||"min"===e?1:0})):h.statTypes,E=!1;w.forEach((function(t){if((0,K.iY)(f,t)){var e=A&&("min"===t||"max"===t);if(!h.hideLegend){var i=b?"mean"===t:!1===E;y.push({legend_label:m,show_legend:i}),E=E||i}x.push(t),g.push({label:m?"".concat(m," (").concat(h.hass.localize("ui.components.statistics_charts.statistic_types.".concat(t)),")\n            "):h.hass.localize("ui.components.statistics_charts.statistic_types.".concat(t)),fill:!!A&&("min"===t&&b?"+1":"max"===t&&"-1"),borderColor:e&&b?_+(h.hideLegend?"00":"7F"):_,backgroundColor:e?_+"3F":_+"7F",pointRadius:0,hidden:!h.hideLegend&&h._hiddenStats.has(d),data:[],unit:null==p?void 0:p.unit_of_measurement,band:e}),l.push(d)}}));var M=null,q=null;f.forEach((function(t){var e=new Date(t.start);if(M!==e){M=e;var i=[];x.forEach((function(e){var n,a;"sum"===e?null==q?(a=0,q=t.sum):a=(t.sum||0)-q:a=t[e],i.push(null!==(n=a)&&void 0!==n?n:null)})),function(t,e,i){i&&(t>e||(g.forEach((function(e,n){"line"===h.chartType&&v&&k&&v.getTime()!==t.getTime()&&(e.data.push({x:v.getTime(),y:k[n]}),e.data.push({x:v.getTime(),y:null})),e.data.push({x:t.getTime(),y:i[n]})})),k=i,v=e))}(e,new Date(t.end),i)}})),Array.prototype.push.apply(a,g),Array.prototype.push.apply(r,y)})),c&&this._createOptions(c),this._chartData={datasets:a},this._chartDatasetExtra=r,this._statisticIds=l;case 23:case"end":return t.stop()}}),t,this)}))),function(){return i.apply(this,arguments)})},{kind:"get",static:!0,key:"styles",value:function(){return(0,F.AH)(X||(X=(0,c.A)([":host{display:block;min-height:60px}.info{text-align:center;line-height:60px;color:var(--secondary-text-color)}"])))}}]}}),F.WF),r(),t.next=87;break;case 84:t.prev=84,t.t2=t.catch(0),r(t.t2);case 87:case"end":return t.stop()}}),t,null,[[0,84]])})));return function(e,i){return t.apply(this,arguments)}}())},23006:function(t,e,i){var n,a,r,o,s,d,l,c,u,h=i(23141),f=i(539),p=i(6238),m=i(94881),v=i(66123),k=i(1781),g=i(36683),y=i(89231),_=i(29864),x=i(83647),b=i(8364),A=i(76504),w=i(80792),E=(i(77052),i(21950),i(36724),i(848),i(43859),i(21968),i(68113),i(55888),i(56262),i(66274),i(84531),i(98168),i(34290),i(8339),i(40924)),M=i(196),q=i(36471),D=i(77664),S=(i(12261),i(33066),{boolean:function(){return Promise.all([i.e(49774),i.e(93039)]).then(i.bind(i,93039))},constant:function(){return i.e(77855).then(i.bind(i,77855))},float:function(){return Promise.all([i.e(27311),i.e(26255),i.e(30150)]).then(i.bind(i,19605))},grid:function(){return i.e(92415).then(i.bind(i,92415))},expandable:function(){return i.e(27335).then(i.bind(i,27335))},integer:function(){return Promise.all([i.e(87515),i.e(81550),i.e(30885),i.e(98945)]).then(i.bind(i,16073))},multi_select:function(){return Promise.all([i.e(27311),i.e(26255),i.e(89226),i.e(29805),i.e(34667),i.e(27350),i.e(49774),i.e(26410),i.e(90113)]).then(i.bind(i,90113))},positive_time_period_dict:function(){return Promise.all([i.e(26255),i.e(89226),i.e(29805),i.e(34667),i.e(50988),i.e(27350),i.e(32503),i.e(50983),i.e(16858)]).then(i.bind(i,66655))},select:function(){return Promise.all([i.e(27311),i.e(26255),i.e(89226),i.e(29805),i.e(88201),i.e(36768),i.e(34667),i.e(50988),i.e(27350),i.e(49774),i.e(32503),i.e(87515),i.e(81550),i.e(13538),i.e(88436),i.e(73977),i.e(63593),i.e(11627),i.e(57244),i.e(6015)]).then(i.bind(i,6015))},string:function(){return Promise.all([i.e(27311),i.e(26255),i.e(99629)]).then(i.bind(i,6006))}}),j=function(t,e){return t?e.name?t[e.name]:t:null};(0,b.A)([(0,M.EM)("ha-form")],(function(t,e){var i,b=function(e){function i(){var e;(0,y.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return e=(0,_.A)(this,i,[].concat(a)),t(e),e}return(0,x.A)(i,e),(0,g.A)(i)}(e);return{F:b,d:[{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"schema",value:void 0},{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"error",value:void 0},{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"warning",value:void 0},{kind:"field",decorators:[(0,M.MZ)({type:Boolean})],key:"disabled",value:function(){return!1}},{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"computeError",value:void 0},{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"computeWarning",value:void 0},{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"computeLabel",value:void 0},{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"computeHelper",value:void 0},{kind:"field",decorators:[(0,M.MZ)({attribute:!1})],key:"localizeValue",value:void 0},{kind:"method",key:"getFormProperties",value:function(){return{}}},{kind:"method",key:"focus",value:(i=(0,k.A)((0,m.A)().mark((function t(){var e,i,n,a;return(0,m.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,this.updateComplete;case 2:if(e=this.renderRoot.querySelector(".root")){t.next=5;break}return t.abrupt("return");case 5:i=(0,v.A)(e.children),t.prev=6,i.s();case 8:if((n=i.n()).done){t.next=18;break}if("HA-ALERT"===(a=n.value).tagName){t.next=16;break}if(!(a instanceof E.mN)){t.next=14;break}return t.next=14,a.updateComplete;case 14:return a.focus(),t.abrupt("break",18);case 16:t.next=8;break;case 18:t.next=23;break;case 20:t.prev=20,t.t0=t.catch(6),i.e(t.t0);case 23:return t.prev=23,i.f(),t.finish(23);case 26:case"end":return t.stop()}}),t,this,[[6,20,23,26]])}))),function(){return i.apply(this,arguments)})},{kind:"method",key:"willUpdate",value:function(t){t.has("schema")&&this.schema&&this.schema.forEach((function(t){var e;"selector"in t||null===(e=S[t.type])||void 0===e||e.call(S)}))}},{kind:"method",key:"render",value:function(){var t=this;return(0,E.qy)(n||(n=(0,p.A)([' <div class="root" part="root"> '," "," </div> "])),this.error&&this.error.base?(0,E.qy)(a||(a=(0,p.A)([' <ha-alert alert-type="error"> '," </ha-alert> "])),this._computeError(this.error.base,this.schema)):"",this.schema.map((function(e){var i,n=function(t,e){return t&&e.name?t[e.name]:null}(t.error,e),a=function(t,e){return t&&e.name?t[e.name]:null}(t.warning,e);return(0,E.qy)(r||(r=(0,p.A)([" "," "," "])),n?(0,E.qy)(o||(o=(0,p.A)([' <ha-alert own-margin alert-type="error"> '," </ha-alert> "])),t._computeError(n,e)):a?(0,E.qy)(s||(s=(0,p.A)([' <ha-alert own-margin alert-type="warning"> '," </ha-alert> "])),t._computeWarning(a,e)):"","selector"in e?(0,E.qy)(d||(d=(0,p.A)(['<ha-selector .schema="','" .hass="','" .name="','" .selector="','" .value="','" .label="','" .disabled="','" .placeholder="','" .helper="','" .localizeValue="','" .required="','" .context="','"></ha-selector>'])),e,t.hass,e.name,e.selector,j(t.data,e),t._computeLabel(e,t.data),e.disabled||t.disabled||!1,e.required?"":e.default,t._computeHelper(e),t.localizeValue,e.required||!1,t._generateContext(e)):(0,q._)(t.fieldElementName(e.type),Object.assign({schema:e,data:j(t.data,e),label:t._computeLabel(e,t.data),helper:t._computeHelper(e),disabled:t.disabled||e.disabled||!1,hass:t.hass,localize:null===(i=t.hass)||void 0===i?void 0:i.localize,computeLabel:t.computeLabel,computeHelper:t.computeHelper,context:t._generateContext(e)},t.getFormProperties())))})))}},{kind:"method",key:"fieldElementName",value:function(t){return"ha-form-".concat(t)}},{kind:"method",key:"_generateContext",value:function(t){if(t.context){for(var e={},i=0,n=Object.entries(t.context);i<n.length;i++){var a=(0,f.A)(n[i],2),r=a[0],o=a[1];e[r]=this.data[o]}return e}}},{kind:"method",key:"createRenderRoot",value:function(){var t=(0,A.A)((0,w.A)(b.prototype),"createRenderRoot",this).call(this);return this.addValueChangedListener(t),t}},{kind:"method",key:"addValueChangedListener",value:function(t){var e=this;t.addEventListener("value-changed",(function(t){t.stopPropagation();var i=t.target.schema;if(t.target!==e){var n=i.name?(0,h.A)({},i.name,t.detail.value):t.detail.value;e.data=Object.assign(Object.assign({},e.data),n),(0,D.r)(e,"value-changed",{value:e.data})}}))}},{kind:"method",key:"_computeLabel",value:function(t,e){return this.computeLabel?this.computeLabel(t,e):t?t.name:""}},{kind:"method",key:"_computeHelper",value:function(t){return this.computeHelper?this.computeHelper(t):""}},{kind:"method",key:"_computeError",value:function(t,e){var i=this;return Array.isArray(t)?(0,E.qy)(l||(l=(0,p.A)(["<ul> "," </ul>"])),t.map((function(t){return(0,E.qy)(c||(c=(0,p.A)(["<li> "," </li>"])),i.computeError?i.computeError(t,e):t)}))):this.computeError?this.computeError(t,e):t}},{kind:"method",key:"_computeWarning",value:function(t,e){return this.computeWarning?this.computeWarning(t,e):t}},{kind:"get",static:!0,key:"styles",value:function(){return(0,E.AH)(u||(u=(0,p.A)([".root>*{display:block}.root>:not([own-margin]):not(:last-child){margin-bottom:24px}ha-alert[own-margin]{margin-bottom:4px}"])))}}]}}),E.WF)},42398:function(t,e,i){var n,a,r,o,s=i(6238),d=i(36683),l=i(89231),c=i(29864),u=i(83647),h=i(8364),f=i(76504),p=i(80792),m=(i(77052),i(94400)),v=i(65050),k=i(40924),g=i(196),y=i(51150);(0,h.A)([(0,g.EM)("ha-textfield")],(function(t,e){var i=function(e){function i(){var e;(0,l.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return e=(0,c.A)(this,i,[].concat(a)),t(e),e}return(0,u.A)(i,e),(0,d.A)(i)}(e);return{F:i,d:[{kind:"field",decorators:[(0,g.MZ)({type:Boolean})],key:"invalid",value:function(){return!1}},{kind:"field",decorators:[(0,g.MZ)({attribute:"error-message"})],key:"errorMessage",value:void 0},{kind:"field",decorators:[(0,g.MZ)({type:Boolean})],key:"icon",value:function(){return!1}},{kind:"field",decorators:[(0,g.MZ)({type:Boolean})],key:"iconTrailing",value:function(){return!1}},{kind:"field",decorators:[(0,g.MZ)()],key:"autocomplete",value:void 0},{kind:"field",decorators:[(0,g.MZ)()],key:"autocorrect",value:void 0},{kind:"field",decorators:[(0,g.MZ)({attribute:"input-spellcheck"})],key:"inputSpellcheck",value:void 0},{kind:"field",decorators:[(0,g.P)("input")],key:"formElement",value:void 0},{kind:"method",key:"updated",value:function(t){(0,f.A)((0,p.A)(i.prototype),"updated",this).call(this,t),(t.has("invalid")&&(this.invalid||void 0!==t.get("invalid"))||t.has("errorMessage"))&&(this.setCustomValidity(this.invalid?this.errorMessage||"Invalid":""),this.reportValidity()),t.has("autocomplete")&&(this.autocomplete?this.formElement.setAttribute("autocomplete",this.autocomplete):this.formElement.removeAttribute("autocomplete")),t.has("autocorrect")&&(this.autocorrect?this.formElement.setAttribute("autocorrect",this.autocorrect):this.formElement.removeAttribute("autocorrect")),t.has("inputSpellcheck")&&(this.inputSpellcheck?this.formElement.setAttribute("spellcheck",this.inputSpellcheck):this.formElement.removeAttribute("spellcheck"))}},{kind:"method",key:"renderIcon",value:function(t){var e=arguments.length>1&&void 0!==arguments[1]&&arguments[1],i=e?"trailing":"leading";return(0,k.qy)(n||(n=(0,s.A)([' <span class="mdc-text-field__icon mdc-text-field__icon--','" tabindex="','"> <slot name="','Icon"></slot> </span> '])),i,e?1:-1,i)}},{kind:"field",static:!0,key:"styles",value:function(){return[v.R,(0,k.AH)(a||(a=(0,s.A)([".mdc-text-field__input{width:var(--ha-textfield-input-width,100%)}.mdc-text-field:not(.mdc-text-field--with-leading-icon){padding:var(--text-field-padding,0px 16px)}.mdc-text-field__affix--suffix{padding-left:var(--text-field-suffix-padding-left,12px);padding-right:var(--text-field-suffix-padding-right,0px);padding-inline-start:var(--text-field-suffix-padding-left,12px);padding-inline-end:var(--text-field-suffix-padding-right,0px);direction:ltr}.mdc-text-field--with-leading-icon{padding-inline-start:var(--text-field-suffix-padding-left,0px);padding-inline-end:var(--text-field-suffix-padding-right,16px);direction:var(--direction)}.mdc-text-field--with-leading-icon.mdc-text-field--with-trailing-icon{padding-left:var(--text-field-suffix-padding-left,0px);padding-right:var(--text-field-suffix-padding-right,0px);padding-inline-start:var(--text-field-suffix-padding-left,0px);padding-inline-end:var(--text-field-suffix-padding-right,0px)}.mdc-text-field:not(.mdc-text-field--disabled) .mdc-text-field__affix--suffix{color:var(--secondary-text-color)}.mdc-text-field__icon{color:var(--secondary-text-color)}.mdc-text-field__icon--leading{margin-inline-start:16px;margin-inline-end:8px;direction:var(--direction)}.mdc-text-field__icon--trailing{padding:var(--textfield-icon-trailing-padding,12px)}.mdc-floating-label:not(.mdc-floating-label--float-above){text-overflow:ellipsis;width:inherit;padding-right:30px;padding-inline-end:30px;padding-inline-start:initial;box-sizing:border-box;direction:var(--direction)}input{text-align:var(--text-field-text-align,start)}::-ms-reveal{display:none}:host([no-spinner]) input::-webkit-inner-spin-button,:host([no-spinner]) input::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}:host([no-spinner]) input[type=number]{-moz-appearance:textfield}.mdc-text-field__ripple{overflow:hidden}.mdc-text-field{overflow:var(--text-field-overflow)}.mdc-floating-label{inset-inline-start:16px!important;inset-inline-end:initial!important;transform-origin:var(--float-start);direction:var(--direction);text-align:var(--float-start)}.mdc-text-field--with-leading-icon.mdc-text-field--filled .mdc-floating-label{max-width:calc(100% - 48px - var(--text-field-suffix-padding-left,0px));inset-inline-start:calc(48px + var(--text-field-suffix-padding-left,0px))!important;inset-inline-end:initial!important;direction:var(--direction)}.mdc-text-field__input[type=number]{direction:var(--direction)}.mdc-text-field__affix--prefix{padding-right:var(--text-field-prefix-padding-right,2px);padding-inline-end:var(--text-field-prefix-padding-right,2px);padding-inline-start:initial}.mdc-text-field:not(.mdc-text-field--disabled) .mdc-text-field__affix--prefix{color:var(--mdc-text-field-label-ink-color)}"]))),"rtl"===y.G.document.dir?(0,k.AH)(r||(r=(0,s.A)([".mdc-floating-label,.mdc-text-field--with-leading-icon,.mdc-text-field--with-leading-icon.mdc-text-field--filled .mdc-floating-label,.mdc-text-field__icon--leading,.mdc-text-field__input[type=number]{direction:rtl;--direction:rtl}"]))):(0,k.AH)(o||(o=(0,s.A)([""])))]}}]}}),m.J)},17876:function(t,e,i){i.d(e,{L:function(){return a},z:function(){return r}});var n=i(1751),a=["input_boolean","input_button","input_text","input_number","input_datetime","input_select","counter","timer","schedule"],r=(0,n.g)(a)},15696:function(t,e,i){i.d(e,{j:function(){return n}});var n=["relative","total","date","time","datetime"]},69317:function(t,e,i){var n=i(1781).A,a=i(94881).A;i.a(t,function(){var t=n(a().mark((function t(n,r){var o,s,d,l,c,u,h,f,p,m,v,k,g,y,_,x,b,A,w,E,M,q,D,S,j,C,O,Z,I,L,Y,z,T,H,F,P,W,R,N,U,B,K,V,J,G,Q,$,X,tt,et,it,nt,at,rt,ot,st,dt,lt;return a().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(t.prev=0,i.r(e),i.d(e,{HuiStatisticsGraphCardEditor:function(){return lt}}),o=i(6238),s=i(94881),d=i(1781),l=i(36683),c=i(89231),u=i(29864),h=i(83647),f=i(8364),p=i(77052),m=i(69466),v=i(4187),k=i(35848),g=i(21950),y=i(36724),_=i(71936),x=i(848),b=i(43859),A=i(68113),w=i(57733),E=i(56262),M=i(66274),q=i(85038),D=i(85767),S=i(84531),j=i(98168),C=i(22836),O=i(15445),Z=i(24483),I=i(13478),L=i(46355),Y=i(14612),z=i(53691),T=i(48455),H=i(34290),F=i(8339),P=i(40924),W=i(196),R=i(45081),N=i(63428),U=i(68286),B=i(77664),K=i(61314),V=i(26846),J=i(60819),i(23006),G=i(74959),Q=i(67990),$=i(2977),X=i(7941),tt=i(24212),!(et=n([V,J])).then){t.next=88;break}return t.next=84,et;case 84:t.t1=t.sent,t.t0=(0,t.t1)(),t.next=89;break;case 88:t.t0=et;case 89:it=t.t0,V=it[0],J=it[1],rt=(0,N.KC)([(0,N.eu)("state"),(0,N.eu)("sum"),(0,N.eu)("change"),(0,N.eu)("min"),(0,N.eu)("max"),(0,N.eu)("mean")]),ot=(0,N.kp)($.H,(0,N.Ik)({entities:(0,N.YO)(X.l),title:(0,N.lq)((0,N.Yj)()),days_to_show:(0,N.lq)((0,N.ai)()),period:(0,N.lq)((0,N.KC)([(0,N.eu)("5minute"),(0,N.eu)("hour"),(0,N.eu)("day"),(0,N.eu)("week"),(0,N.eu)("month")])),chart_type:(0,N.lq)((0,N.KC)([(0,N.eu)("bar"),(0,N.eu)("line")])),stat_types:(0,N.lq)((0,N.KC)([(0,N.YO)(rt),rt])),unit:(0,N.lq)((0,N.Yj)()),hide_legend:(0,N.lq)((0,N.zM)()),logarithmic_scale:(0,N.lq)((0,N.zM)())})),st=["5minute","hour","day","week","month"],dt=["mean","min","max","sum","state","change"],lt=(0,f.A)([(0,W.EM)("hui-statistics-graph-card-editor")],(function(t,e){var i,n=function(e){function i(){var e;(0,c.A)(this,i);for(var n=arguments.length,a=new Array(n),r=0;r<n;r++)a[r]=arguments[r];return e=(0,u.A)(this,i,[].concat(a)),t(e),e}return(0,h.A)(i,e),(0,l.A)(i)}(e);return{F:n,d:[{kind:"field",decorators:[(0,W.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,W.wk)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,W.wk)()],key:"_configEntities",value:void 0},{kind:"field",decorators:[(0,W.wk)()],key:"_metaDatas",value:void 0},{kind:"method",key:"setConfig",value:function(t){(0,N.vA)(t,ot),this._config=t,this._configEntities=t.entities?(0,Q.L)(t.entities,!1).map((function(t){return t.entity})):[]}},{kind:"field",key:"_getStatisticsMetaData",value:function(){var t=this;return function(){var e=(0,d.A)((0,s.A)().mark((function e(i){return(0,s.A)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,(0,G.Wr)(t.hass,i||[]);case 2:t._metaDatas=e.sent;case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()}},{kind:"method",key:"willUpdate",value:function(t){var e;t.has("_configEntities")&&!(0,K.b)(this._configEntities,t.get("_configEntities"))&&(this._metaDatas=void 0,null!==(e=this._configEntities)&&void 0!==e&&e.length&&this._getStatisticsMetaData(this._configEntities))}},{kind:"field",key:"_schema",value:function(){var t=this;return(0,R.A)((function(e,i,n){var a=new Set;null==n||n.forEach((function(e){var i=(0,G.JE)(t.hass,e.statistic_id,e);i&&a.add(i)}));var r=[{name:"title",selector:{text:{}}},{name:"",type:"grid",schema:[{name:"period",required:!0,selector:{select:{options:st.map((function(t){return{value:t,label:e("ui.panel.lovelace.editor.card.statistics-graph.periods.".concat(t)),disabled:"5minute"===t&&(null==i?void 0:i.some((function(t){return(0,G.OQ)(t)})))}}))}}},{name:"days_to_show",default:tt.DEFAULT_DAYS_TO_SHOW,selector:{number:{min:1,mode:"box"}}},{name:"stat_types",required:!0,selector:{select:{multiple:!0,mode:"list",options:dt.map((function(t){return{value:t,label:e("ui.panel.lovelace.editor.card.statistics-graph.stat_type_labels.".concat(t)),disabled:!n||!n.some((function(e){return(0,G.nN)(e,V.n[t])}))}}))}}},{name:"chart_type",required:!0,type:"select",options:[["line","Line"],["bar","Bar"]]},{name:"hide_legend",required:!1,selector:{boolean:{}}},{name:"logarithmic_scale",required:!1,selector:{boolean:{}}}]}];return a.size>1&&r[1].schema.push({name:"unit",required:!1,selector:{select:{options:Array.from(a).map((function(t){return{value:t,label:t}}))}}}),r}))}},{kind:"method",key:"render",value:function(){var t,e,i=this;if(!this.hass||!this._config)return P.s6;var n=this._schema(this.hass.localize,this._configEntities,this._metaDatas),a=this._config.stat_types?(0,U.e)(this._config.stat_types):dt.filter((function(t){var e;return null===(e=i._metaDatas)||void 0===e?void 0:e.some((function(e){return(0,G.nN)(e,t)}))})),r=Object.assign(Object.assign({chart_type:"line",period:"hour"},this._config),{},{stat_types:a}),s=null===(t=this._metaDatas)||void 0===t||null===(t=t[0])||void 0===t?void 0:t.unit_class,d=s||null===(e=this._metaDatas)||void 0===e||null===(e=e[0])||void 0===e?void 0:e.statistics_unit_of_measurement;return(0,P.qy)(nt||(nt=(0,o.A)([' <ha-form .hass="','" .data="','" .schema="','" .computeLabel="','" @value-changed="','"></ha-form> <ha-statistics-picker allow-custom-entity .hass="','" .pickStatisticLabel="','" .pickedStatisticLabel="','" .includeStatisticsUnitOfMeasurement="','" .includeUnitClass="','" .ignoreRestrictionsOnFirstStatistic="','" .value="','" .configValue="','" @value-changed="','"></ha-statistics-picker> '])),this.hass,r,n,this._computeLabelCallback,this._valueChanged,this.hass,this.hass.localize("ui.panel.lovelace.editor.card.statistics-graph.pick_statistic"),this.hass.localize("ui.panel.lovelace.editor.card.statistics-graph.picked_statistic"),d,s,!0,this._configEntities,"entities",this._entitiesChanged)}},{kind:"method",key:"_valueChanged",value:function(t){(0,B.r)(this,"config-changed",{config:t.detail.value})}},{kind:"method",key:"_entitiesChanged",value:(i=(0,d.A)((0,s.A)().mark((function t(e){var i,n,a,r,o=this;return(0,s.A)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(i=e.detail.value,n=i.map((function(t){var e=o._config.entities.find((function(e){return"string"!=typeof e&&e.entity===t}));return null!=e?e:t})),a=Object.assign(Object.assign({},this._config),{},{entities:n}),null!=i&&i.some((function(t){return(0,G.OQ)(t)}))&&"5minute"===a.period&&delete a.period,!a.stat_types&&!a.unit){t.next=10;break}return t.next=7,(0,G.Wr)(this.hass,i);case 7:t.t0=t.sent,t.next=11;break;case 10:t.t0=void 0;case 11:r=t.t0,a.stat_types&&a.entities.length&&(a.stat_types=(0,U.e)(a.stat_types).filter((function(t){return r.some((function(e){return(0,G.nN)(e,t)}))})),a.stat_types.length||delete a.stat_types),a.unit&&!r.some((function(t){return(0,G.JE)(o.hass,null==t?void 0:t.statistic_id,t)===a.unit}))&&delete a.unit,(0,B.r)(this,"config-changed",{config:a});case 15:case"end":return t.stop()}}),t,this)}))),function(t){return i.apply(this,arguments)})},{kind:"field",key:"_computeLabelCallback",value:function(){var t=this;return function(e){switch(e.name){case"chart_type":case"stat_types":case"period":case"unit":case"hide_legend":case"logarithmic_scale":return t.hass.localize("ui.panel.lovelace.editor.card.statistics-graph.".concat(e.name));default:return t.hass.localize("ui.panel.lovelace.editor.card.generic.".concat(e.name))}}}},{kind:"field",static:!0,key:"styles",value:function(){return(0,P.AH)(at||(at=(0,o.A)(["ha-statistics-picker{width:100%}"])))}}]}}),P.WF),r(),t.next=103;break;case 100:t.prev=100,t.t2=t.catch(0),r(t.t2);case 103:case"end":return t.stop()}}),t,null,[[0,100]])})));return function(e,i){return t.apply(this,arguments)}}())},54293:function(t,e,i){i.d(e,{k:function(){return h}});var n=i(67234),a=i(63428),r=(0,a.Ik)({user:(0,a.Yj)()}),o=(0,a.KC)([(0,a.zM)(),(0,a.Ik)({text:(0,a.lq)((0,a.Yj)()),excemptions:(0,a.lq)((0,a.YO)(r))})]),s=(0,a.Ik)({action:(0,a.eu)("url"),url_path:(0,a.Yj)(),confirmation:(0,a.lq)(o)}),d=(0,a.Ik)({action:(0,a.eu)("call-service"),service:(0,a.Yj)(),service_data:(0,a.lq)((0,a.Ik)()),data:(0,a.lq)((0,a.Ik)()),target:(0,a.lq)((0,a.Ik)({entity_id:(0,a.lq)((0,a.KC)([(0,a.Yj)(),(0,a.YO)((0,a.Yj)())])),device_id:(0,a.lq)((0,a.KC)([(0,a.Yj)(),(0,a.YO)((0,a.Yj)())])),area_id:(0,a.lq)((0,a.KC)([(0,a.Yj)(),(0,a.YO)((0,a.Yj)())]))})),confirmation:(0,a.lq)(o)}),l=(0,a.Ik)({action:(0,a.eu)("navigate"),navigation_path:(0,a.Yj)(),navigation_replace:(0,a.lq)((0,a.zM)()),confirmation:(0,a.lq)(o)}),c=(0,a.NW)({action:(0,a.eu)("assist"),pipeline_id:(0,a.lq)((0,a.Yj)()),start_listening:(0,a.lq)((0,a.zM)())}),u=(0,a.Ik)({action:(0,a.vP)(["none","toggle","more-info","call-service","url","navigate","assist"]),confirmation:(0,a.lq)(o)}),h=(0,a.OR)((function(t){if(t&&"object"===(0,n.A)(t)&&"action"in t)switch(t.action){case"call-service":return d;case"navigate":return l;case"url":return s;case"assist":return c}return u}))},2977:function(t,e,i){i.d(e,{H:function(){return a}});var n=i(63428),a=(0,n.Ik)({type:(0,n.Yj)(),view_layout:(0,n.bz)(),layout_options:(0,n.bz)(),visibility:(0,n.bz)()})},7941:function(t,e,i){i.d(e,{l:function(){return o}});var n=i(63428),a=i(15696),r=i(54293),o=(0,n.KC)([(0,n.Ik)({entity:(0,n.Yj)(),name:(0,n.lq)((0,n.Yj)()),icon:(0,n.lq)((0,n.Yj)()),image:(0,n.lq)((0,n.Yj)()),secondary_info:(0,n.lq)((0,n.Yj)()),format:(0,n.lq)((0,n.vP)(a.j)),state_color:(0,n.lq)((0,n.zM)()),tap_action:(0,n.lq)(r.k),hold_action:(0,n.lq)(r.k),double_tap_action:(0,n.lq)(r.k)}),(0,n.Yj)()])},79372:function(t,e,i){var n=i(73155),a=i(33817),r=i(3429),o=i(75077);t.exports=function(t,e){e&&"string"==typeof t||a(t);var i=o(t);return r(a(void 0!==i?n(i,t):t))}},18684:function(t,e,i){var n=i(87568),a=i(42509),r=i(30356),o=i(51607),s=i(95124),d=i(79635);n({target:"Array",proto:!0},{flatMap:function(t){var e,i=o(this),n=s(i);return r(t),(e=d(i,0)).length=a(e,i,i,n,0,1,t,arguments.length>1?arguments[1]:void 0),e}})},74991:function(t,e,i){i(33523)("flatMap")},80295:function(t,e,i){i(87568)({target:"Number",stat:!0,nonConfigurable:!0,nonWritable:!0},{MAX_SAFE_INTEGER:9007199254740991})},34917:function(t,e,i){i(87568)({target:"Number",stat:!0,nonConfigurable:!0,nonWritable:!0},{MIN_SAFE_INTEGER:-9007199254740991})},91438:function(t,e,i){var n=i(87568),a=i(78133).codeAt;n({target:"String",proto:!0},{codePointAt:function(t){return a(this,t)}})},69704:function(t,e,i){var n=i(87568),a=i(73155),r=i(30356),o=i(33817),s=i(3429),d=i(79372),l=i(23408),c=i(44933),u=i(89385),h=l((function(){for(var t,e,i=this.iterator,n=this.mapper;;){if(e=this.inner)try{if(!(t=o(a(e.next,e.iterator))).done)return t.value;this.inner=null}catch(r){c(i,"throw",r)}if(t=o(a(this.next,i)),this.done=!!t.done)return;try{this.inner=d(n(t.value,this.counter++),!1)}catch(r){c(i,"throw",r)}}}));n({target:"Iterator",proto:!0,real:!0,forced:u},{flatMap:function(t){return o(this),r(t),new h(s(this),{mapper:t,inner:null})}})}}]);
//# sourceMappingURL=37438.9KBCKVe25k4.js.map