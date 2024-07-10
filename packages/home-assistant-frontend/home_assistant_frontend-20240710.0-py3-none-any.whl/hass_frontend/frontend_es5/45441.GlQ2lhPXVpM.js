"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[45441],{94027:function(a,t,e){e.d(t,{E:function(){return u}});var l=e(66123),c=e(36683),s=e(89231),d=e(29864),r=e(83647),o=e(8364),n=e(76504),_=e(80792),i=(e(77052),e(53501),e(21950),e(68113),e(55888),e(34517),e(66274),e(22836),e(8339),e(196)),u=function(a){var t=(0,o.A)(null,(function(a,t){var e=function(t){function e(){var t;(0,s.A)(this,e);for(var l=arguments.length,c=new Array(l),r=0;r<l;r++)c[r]=arguments[r];return t=(0,d.A)(this,e,[].concat(c)),a(t),t}return(0,r.A)(e,t),(0,c.A)(e)}(t);return{F:e,d:[{kind:"field",decorators:[(0,i.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:void 0},{kind:"field",key:"__unsubs",value:void 0},{kind:"method",key:"connectedCallback",value:function(){(0,n.A)((0,_.A)(e.prototype),"connectedCallback",this).call(this),this.__checkSubscribed()}},{kind:"method",key:"disconnectedCallback",value:function(){if((0,n.A)((0,_.A)(e.prototype),"disconnectedCallback",this).call(this),this.__unsubs){for(;this.__unsubs.length;){var a=this.__unsubs.pop();a instanceof Promise?a.then((function(a){return a()})):a()}this.__unsubs=void 0}}},{kind:"method",key:"updated",value:function(a){if((0,n.A)((0,_.A)(e.prototype),"updated",this).call(this,a),a.has("hass"))this.__checkSubscribed();else if(this.hassSubscribeRequiredHostProps){var t,c=(0,l.A)(a.keys());try{for(c.s();!(t=c.n()).done;){var s=t.value;if(this.hassSubscribeRequiredHostProps.includes(s))return void this.__checkSubscribed()}}catch(d){c.e(d)}finally{c.f()}}}},{kind:"method",key:"hassSubscribe",value:function(){return[]}},{kind:"method",key:"__checkSubscribed",value:function(){var a,t=this;void 0!==this.__unsubs||!this.isConnected||void 0===this.hass||null!==(a=this.hassSubscribeRequiredHostProps)&&void 0!==a&&a.some((function(a){return void 0===t[a]}))||(this.__unsubs=this.hassSubscribe())}}]}}),a);return t}},83256:function(a,t,e){e.d(t,{g:function(){return s}});e(64148);var l=e(92849),c=e(1471);function s(a,t,e,s,d,r){var o=a.getPropertyValue(d+"-"+r).trim(),n=o.length>0?o:a.getPropertyValue(d).trim(),_=(0,l.RQ)(n);return 0===o.length&&r&&(_=(0,l.v2)((0,l.BE)(t?(0,c.T)((0,l.Nc)((0,l.xp)(_)),r):(0,c.d)((0,l.Nc)((0,l.xp)(_)),r)))),s?_+=e?"32":"7F":e&&(_+="7F"),_}},45441:function(a,t,e){var l=e(1781).A,c=e(94881).A;e.a(a,function(){var a=l(c().mark((function a(l,s){var d,r,o,n,_,i,u,h,m,b,y,g,v,f,p,k,A,q,w,V,Z,C,$,M,W,j,x,z,S,P,E,H,O,R,F,B,N,T,J,K,Q,U,D,G,I,L,X,Y,aa,ta,ea,la,ca,sa,da,ra,oa,na,_a,ia,ua,ha,ma,ba,ya,ga,va,fa,pa,ka,Aa,qa,wa,Va,Za,Ca,$a,Ma,Wa,ja,xa,za,Sa,Pa,Ea;return c().wrap((function(a){for(;;)switch(a.prev=a.next){case 0:if(a.prev=0,e.r(t),e.d(t,{HuiEnergySourcesTableCard:function(){return Ea}}),d=e(6238),r=e(36683),o=e(89231),n=e(29864),_=e(83647),i=e(8364),u=e(77052),h=e(69466),m=e(36724),b=e(68113),y=e(66274),g=e(85038),v=e(98168),f=e(22836),p=e(68560),k=e(40924),A=e(196),q=e(80204),w=e(56601),V=e(83256),e(54373),Z=e(41525),C=e(74959),$=e(94027),M=e(15821),!(W=l([w,Z])).then){a.next=44;break}return a.next=40,W;case 40:a.t1=a.sent,a.t0=(0,a.t1)(),a.next=45;break;case 44:a.t0=W;case 45:j=a.t0,w=j[0],Z=j[1],Pa={grid_return:"--energy-grid-return-color",grid_consumption:"--energy-grid-consumption-color",battery_in:"--energy-battery-in-color",battery_out:"--energy-battery-out-color",solar:"--energy-solar-color",gas:"--energy-gas-color",water:"--energy-water-color"},Ea=(0,i.A)([(0,A.EM)("hui-energy-sources-table-card")],(function(a,t){var e=function(t){function e(){var t;(0,o.A)(this,e);for(var l=arguments.length,c=new Array(l),s=0;s<l;s++)c[s]=arguments[s];return t=(0,n.A)(this,e,[].concat(c)),a(t),t}return(0,_.A)(e,t),(0,r.A)(e)}(t);return{F:e,d:[{kind:"field",decorators:[(0,A.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,A.wk)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,A.wk)()],key:"_data",value:void 0},{kind:"field",key:"hassSubscribeRequiredHostProps",value:function(){return["_config"]}},{kind:"method",key:"hassSubscribe",value:function(){var a,t=this;return[(0,Z.tb)(this.hass,{key:null===(a=this._config)||void 0===a?void 0:a.collection_key}).subscribe((function(a){t._data=a}))]}},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"setConfig",value:function(a){this._config=a}},{kind:"method",key:"shouldUpdate",value:function(a){return(0,M.xP)(this,a)||a.size>1||!a.has("hass")}},{kind:"method",key:"render",value:function(){var a,t,e,l,c,s,r,o,n,_,i,u=this;if(!this.hass||!this._config)return k.s6;if(!this._data)return(0,k.qy)(x||(x=(0,d.A)(["",""])),this.hass.localize("ui.panel.lovelace.cards.energy.loading"));var h=0,m=0,b=0,y=0,g=0,v=0,f=0,p=0,A=!1,$=!1,M=!1,W=0,j=0,Sa=0,Ea=0,Ha=0,Oa=0,Ra=0,Fa=0,Ba=(0,Z.E$)(this._data.prefs),Na=getComputedStyle(this),Ta=(null===(a=Ba.grid)||void 0===a?void 0:a[0].flow_from.some((function(a){return a.stat_cost||a.entity_energy_price||a.number_energy_price})))||(null===(t=Ba.grid)||void 0===t?void 0:t[0].flow_to.some((function(a){return a.stat_compensation||a.entity_energy_price||a.number_energy_price})))||(null===(e=Ba.gas)||void 0===e?void 0:e.some((function(a){return a.stat_cost||a.entity_energy_price||a.number_energy_price})))||(null===(l=Ba.water)||void 0===l?void 0:l.some((function(a){return a.stat_cost||a.entity_energy_price||a.number_energy_price}))),Ja=(0,Z.KJ)(this.hass,this._data.prefs,this._data.statsMetadata)||"",Ka=(0,Z.yM)(this.hass)||"m³",Qa=void 0!==this._data.statsCompare;return(0,k.qy)(z||(z=(0,d.A)([" <ha-card> ",' <div class="mdc-data-table"> <div class="mdc-data-table__table-container"> <table class="mdc-data-table__table" aria-label="Energy sources"> <thead> <tr class="mdc-data-table__header-row"> <th class="mdc-data-table__header-cell"></th> <th class="mdc-data-table__header-cell" role="columnheader" scope="col"> '," </th> ",' <th class="mdc-data-table__header-cell mdc-data-table__header-cell--numeric" role="columnheader" scope="col"> '," </th> ",' </tr> </thead> <tbody class="mdc-data-table__content"> '," "," "," "," "," "," "," "," "," "," "," </tbody> </table> </div> </div> </ha-card>"])),this._config.title?(0,k.qy)(S||(S=(0,d.A)(['<h1 class="card-header">',"</h1>"])),this._config.title):"",this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.source"),Qa?(0,k.qy)(P||(P=(0,d.A)(['<th class="mdc-data-table__header-cell mdc-data-table__header-cell--numeric" role="columnheader" scope="col"> '," </th> ",""])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.previous_energy"),Ta?(0,k.qy)(E||(E=(0,d.A)(['<th class="mdc-data-table__header-cell mdc-data-table__header-cell--numeric" role="columnheader" scope="col"> '," </th>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.previous_cost")):""):"",this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.energy"),Ta?(0,k.qy)(H||(H=(0,d.A)([' <th class="mdc-data-table__header-cell mdc-data-table__header-cell--numeric" role="columnheader" scope="col"> '," </th>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.cost")):"",null===(c=Ba.solar)||void 0===c?void 0:c.map((function(a,t){var e,l=(0,C.$j)(u._data.stats[a.stat_energy_from])||0;b+=l;var c=Qa&&(0,C.$j)(u._data.statsCompare[a.stat_energy_from])||0;return Sa+=c,(0,k.qy)(O||(O=(0,d.A)(['<tr class="mdc-data-table__row"> <td class="mdc-data-table__cell cell-bullet"> <div class="bullet" style="','"></div> </td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> "," </tr>"])),(0,q.W)({borderColor:(0,V.g)(Na,u.hass.themes.darkMode,!1,!1,Pa.solar,t),backgroundColor:(0,V.g)(Na,u.hass.themes.darkMode,!0,!1,Pa.solar,t)}),(0,C.$O)(u.hass,a.stat_energy_from,null===(e=u._data)||void 0===e?void 0:e.statsMetadata[a.stat_energy_from]),Qa?(0,k.qy)(R||(R=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> ",""])),(0,w.ZV)(c,u.hass.locale),Ta?(0,k.qy)(F||(F=(0,d.A)(['<td class="mdc-data-table__cell"></td>']))):""):"",(0,w.ZV)(l,u.hass.locale),Ta?(0,k.qy)(B||(B=(0,d.A)(['<td class="mdc-data-table__cell"></td>']))):"")})),Ba.solar?(0,k.qy)(N||(N=(0,d.A)(['<tr class="mdc-data-table__row total"> <td class="mdc-data-table__cell"></td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> "," </tr>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.solar_total"),Qa?(0,k.qy)(T||(T=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> ",""])),(0,w.ZV)(Sa,this.hass.locale),Ta?(0,k.qy)(J||(J=(0,d.A)(['<td class="mdc-data-table__cell"></td>']))):""):"",(0,w.ZV)(b,this.hass.locale),Ta?(0,k.qy)(K||(K=(0,d.A)(['<td class="mdc-data-table__cell"></td>']))):""):"",null===(s=Ba.battery)||void 0===s?void 0:s.map((function(a,t){var e,l,c=(0,C.$j)(u._data.stats[a.stat_energy_from])||0,s=(0,C.$j)(u._data.stats[a.stat_energy_to])||0;y+=c-s;var r=Qa&&(0,C.$j)(u._data.statsCompare[a.stat_energy_from])||0,o=Qa&&(0,C.$j)(u._data.statsCompare[a.stat_energy_to])||0;return Ea+=r-o,(0,k.qy)(Q||(Q=(0,d.A)(['<tr class="mdc-data-table__row"> <td class="mdc-data-table__cell cell-bullet"> <div class="bullet" style="','"></div> </td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> ",' </tr> <tr class="mdc-data-table__row"> <td class="mdc-data-table__cell cell-bullet"> <div class="bullet" style="','"></div> </td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> "," </tr>"])),(0,q.W)({borderColor:(0,V.g)(Na,u.hass.themes.darkMode,!1,!1,Pa.battery_out,t),backgroundColor:(0,V.g)(Na,u.hass.themes.darkMode,!0,!1,Pa.battery_out,t)}),(0,C.$O)(u.hass,a.stat_energy_from,null===(e=u._data)||void 0===e?void 0:e.statsMetadata[a.stat_energy_from]),Qa?(0,k.qy)(U||(U=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> ",""])),(0,w.ZV)(r,u.hass.locale),Ta?(0,k.qy)(D||(D=(0,d.A)(['<td class="mdc-data-table__cell"></td>']))):""):"",(0,w.ZV)(c,u.hass.locale),Ta?(0,k.qy)(G||(G=(0,d.A)(['<td class="mdc-data-table__cell"></td>']))):"",(0,q.W)({borderColor:(0,V.g)(Na,u.hass.themes.darkMode,!1,!1,Pa.battery_in,t),backgroundColor:(0,V.g)(Na,u.hass.themes.darkMode,!0,!1,Pa.battery_in,t)}),(0,C.$O)(u.hass,a.stat_energy_to,null===(l=u._data)||void 0===l?void 0:l.statsMetadata[a.stat_energy_to]),Qa?(0,k.qy)(I||(I=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> ",""])),(0,w.ZV)(-1*o,u.hass.locale),Ta?(0,k.qy)(L||(L=(0,d.A)(['<td class="mdc-data-table__cell"></td>']))):""):"",(0,w.ZV)(-1*s,u.hass.locale),Ta?(0,k.qy)(X||(X=(0,d.A)(['<td class="mdc-data-table__cell"></td>']))):"")})),Ba.battery?(0,k.qy)(Y||(Y=(0,d.A)(['<tr class="mdc-data-table__row total"> <td class="mdc-data-table__cell"></td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> "," </tr>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.battery_total"),Qa?(0,k.qy)(aa||(aa=(0,d.A)([' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> ",""])),(0,w.ZV)(Ea,this.hass.locale),Ta?(0,k.qy)(ta||(ta=(0,d.A)(['<td class="mdc-data-table__cell"></td>']))):""):"",(0,w.ZV)(y,this.hass.locale),Ta?(0,k.qy)(ea||(ea=(0,d.A)(['<td class="mdc-data-table__cell"></td>']))):""):"",null===(r=Ba.grid)||void 0===r?void 0:r.map((function(a){return(0,k.qy)(la||(la=(0,d.A)([""," ",""])),a.flow_from.map((function(a,t){var e,l=(0,C.$j)(u._data.stats[a.stat_energy_from])||0;h+=l;var c=Qa&&(0,C.$j)(u._data.statsCompare[a.stat_energy_from])||0;W+=c;var s=a.stat_cost||u._data.info.cost_sensors[a.stat_energy_from],r=s?(0,C.$j)(u._data.stats[s])||0:null;null!==r&&(A=!0,m+=r);var o=Qa&&s?(0,C.$j)(u._data.statsCompare[s])||0:null;return null!==o&&(j+=o),(0,k.qy)(ca||(ca=(0,d.A)(['<tr class="mdc-data-table__row"> <td class="mdc-data-table__cell cell-bullet"> <div class="bullet" style="','"></div> </td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> "," </tr>"])),(0,q.W)({borderColor:(0,V.g)(Na,u.hass.themes.darkMode,!1,!1,Pa.grid_consumption,t),backgroundColor:(0,V.g)(Na,u.hass.themes.darkMode,!0,!1,Pa.grid_consumption,t)}),(0,C.$O)(u.hass,a.stat_energy_from,null===(e=u._data)||void 0===e?void 0:e.statsMetadata[a.stat_energy_from]),Qa?(0,k.qy)(sa||(sa=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> ",""])),(0,w.ZV)(c,u.hass.locale),Ta?(0,k.qy)(da||(da=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),null!==o?(0,w.ZV)(o,u.hass.locale,{style:"currency",currency:u.hass.config.currency}):""):""):"",(0,w.ZV)(l,u.hass.locale),Ta?(0,k.qy)(ra||(ra=(0,d.A)([' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),null!==r?(0,w.ZV)(r,u.hass.locale,{style:"currency",currency:u.hass.config.currency}):""):"")})),a.flow_to.map((function(a,t){var e,l=-1*((0,C.$j)(u._data.stats[a.stat_energy_to])||0);h+=l;var c=a.stat_compensation||u._data.info.cost_sensors[a.stat_energy_to],s=c?-1*((0,C.$j)(u._data.stats[c])||0):null;null!==s&&(A=!0,m+=s);var r=-1*(Qa&&(0,C.$j)(u._data.statsCompare[a.stat_energy_to])||0);W+=r;var o=Qa&&c?-1*((0,C.$j)(u._data.statsCompare[c])||0):null;return null!==o&&(j+=o),(0,k.qy)(oa||(oa=(0,d.A)(['<tr class="mdc-data-table__row"> <td class="mdc-data-table__cell cell-bullet"> <div class="bullet" style="','"></div> </td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> "," </tr>"])),(0,q.W)({borderColor:(0,V.g)(Na,u.hass.themes.darkMode,!1,!1,Pa.grid_return,t),backgroundColor:(0,V.g)(Na,u.hass.themes.darkMode,!0,!1,Pa.grid_return,t)}),(0,C.$O)(u.hass,a.stat_energy_to,null===(e=u._data)||void 0===e?void 0:e.statsMetadata[a.stat_energy_to]),Qa?(0,k.qy)(na||(na=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> ",""])),(0,w.ZV)(r,u.hass.locale),Ta?(0,k.qy)(_a||(_a=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),null!==o?(0,w.ZV)(o,u.hass.locale,{style:"currency",currency:u.hass.config.currency}):""):""):"",(0,w.ZV)(l,u.hass.locale),Ta?(0,k.qy)(ia||(ia=(0,d.A)([' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),null!==s?(0,w.ZV)(s,u.hass.locale,{style:"currency",currency:u.hass.config.currency}):""):"")})))})),Ba.grid&&(null!==(o=Ba.grid)&&void 0!==o&&null!==(o=o[0].flow_from)&&void 0!==o&&o.length||null!==(n=Ba.grid)&&void 0!==n&&null!==(n=n[0].flow_to)&&void 0!==n&&n.length)?(0,k.qy)(ua||(ua=(0,d.A)([' <tr class="mdc-data-table__row total"> <td class="mdc-data-table__cell"></td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> "," </tr>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.grid_total"),Qa?(0,k.qy)(ha||(ha=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," kWh </td> ",""])),(0,w.ZV)(W,this.hass.locale),Ta?(0,k.qy)(ma||(ma=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),A?(0,w.ZV)(j,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""):""):"",(0,w.ZV)(h,this.hass.locale),Ta?(0,k.qy)(ba||(ba=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),A?(0,w.ZV)(m,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""):""):"",null===(_=Ba.gas)||void 0===_?void 0:_.map((function(a,t){var e,l=(0,C.$j)(u._data.stats[a.stat_energy_from])||0;g+=l;var c=Qa&&(0,C.$j)(u._data.statsCompare[a.stat_energy_from])||0;Ha+=c;var s=a.stat_cost||u._data.info.cost_sensors[a.stat_energy_from],r=s?(0,C.$j)(u._data.stats[s])||0:null;null!==r&&($=!0,v+=r);var o=Qa&&s?(0,C.$j)(u._data.statsCompare[s])||0:null;return null!==o&&(Oa+=o),(0,k.qy)(ya||(ya=(0,d.A)(['<tr class="mdc-data-table__row"> <td class="mdc-data-table__cell cell-bullet"> <div class="bullet" style="','"></div> </td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," "," </td> "," </tr>"])),(0,q.W)({borderColor:(0,V.g)(Na,u.hass.themes.darkMode,!1,!1,Pa.gas,t),backgroundColor:(0,V.g)(Na,u.hass.themes.darkMode,!0,!1,Pa.gas,t)}),(0,C.$O)(u.hass,a.stat_energy_from,null===(e=u._data)||void 0===e?void 0:e.statsMetadata[a.stat_energy_from]),Qa?(0,k.qy)(ga||(ga=(0,d.A)([' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," "," </td> ",""])),(0,w.ZV)(c,u.hass.locale),Ja,Ta?(0,k.qy)(va||(va=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),null!==o?(0,w.ZV)(o,u.hass.locale,{style:"currency",currency:u.hass.config.currency}):""):""):"",(0,w.ZV)(l,u.hass.locale),Ja,Ta?(0,k.qy)(fa||(fa=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),null!==r?(0,w.ZV)(r,u.hass.locale,{style:"currency",currency:u.hass.config.currency}):""):"")})),Ba.gas?(0,k.qy)(pa||(pa=(0,d.A)(['<tr class="mdc-data-table__row total"> <td class="mdc-data-table__cell"></td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," "," </td> "," </tr>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.gas_total"),Qa?(0,k.qy)(ka||(ka=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," "," </td> ",""])),(0,w.ZV)(Ha,this.hass.locale),Ja,Ta?(0,k.qy)(Aa||(Aa=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),$?(0,w.ZV)(Oa,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""):""):"",(0,w.ZV)(g,this.hass.locale),Ja,Ta?(0,k.qy)(qa||(qa=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),$?(0,w.ZV)(v,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""):""):"",null===(i=Ba.water)||void 0===i?void 0:i.map((function(a,t){var e,l=(0,C.$j)(u._data.stats[a.stat_energy_from])||0;f+=l;var c=Qa&&(0,C.$j)(u._data.statsCompare[a.stat_energy_from])||0;Ra+=c;var s=a.stat_cost||u._data.info.cost_sensors[a.stat_energy_from],r=s?(0,C.$j)(u._data.stats[s])||0:null;null!==r&&(M=!0,p+=r);var o=Qa&&s?(0,C.$j)(u._data.statsCompare[s])||0:null;return null!==o&&(Fa+=o),(0,k.qy)(wa||(wa=(0,d.A)(['<tr class="mdc-data-table__row"> <td class="mdc-data-table__cell cell-bullet"> <div class="bullet" style="','"></div> </td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," "," </td> "," </tr>"])),(0,q.W)({borderColor:(0,V.g)(Na,u.hass.themes.darkMode,!1,!1,Pa.water,t),backgroundColor:(0,V.g)(Na,u.hass.themes.darkMode,!0,!1,Pa.water,t)}),(0,C.$O)(u.hass,a.stat_energy_from,null===(e=u._data)||void 0===e?void 0:e.statsMetadata[a.stat_energy_from]),Qa?(0,k.qy)(Va||(Va=(0,d.A)([' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," "," </td> ",""])),(0,w.ZV)(c,u.hass.locale),Ka,Ta?(0,k.qy)(Za||(Za=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),null!==o?(0,w.ZV)(o,u.hass.locale,{style:"currency",currency:u.hass.config.currency}):""):""):"",(0,w.ZV)(l,u.hass.locale),Ka,Ta?(0,k.qy)(Ca||(Ca=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),null!==r?(0,w.ZV)(r,u.hass.locale,{style:"currency",currency:u.hass.config.currency}):""):"")})),Ba.water?(0,k.qy)($a||($a=(0,d.A)(['<tr class="mdc-data-table__row total"> <td class="mdc-data-table__cell"></td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," "," </td> "," </tr>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.water_total"),Qa?(0,k.qy)(Ma||(Ma=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," "," </td> ",""])),(0,w.ZV)(Ra,this.hass.locale),Ka,Ta?(0,k.qy)(Wa||(Wa=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),M?(0,w.ZV)(Fa,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""):""):"",(0,w.ZV)(f,this.hass.locale),Ka,Ta?(0,k.qy)(ja||(ja=(0,d.A)(['<td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),M?(0,w.ZV)(p,this.hass.locale,{style:"currency",currency:this.hass.config.currency}):""):""):"",[$,M,A].filter(Boolean).length>1?(0,k.qy)(xa||(xa=(0,d.A)(['<tr class="mdc-data-table__row total"> <td class="mdc-data-table__cell"></td> <th class="mdc-data-table__cell" scope="row"> '," </th> ",' <td class="mdc-data-table__cell"></td> <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td> </tr>"])),this.hass.localize("ui.panel.lovelace.cards.energy.energy_sources_table.total_costs"),Qa?(0,k.qy)(za||(za=(0,d.A)(['<td class="mdc-data-table__cell"></td> <td class="mdc-data-table__cell mdc-data-table__cell--numeric"> '," </td>"])),(0,w.ZV)(Oa+j+Fa,this.hass.locale,{style:"currency",currency:this.hass.config.currency})):"",(0,w.ZV)(v+m+p,this.hass.locale,{style:"currency",currency:this.hass.config.currency})):"")}},{kind:"get",static:!0,key:"styles",value:function(){return(0,k.AH)(Sa||(Sa=(0,d.A)([""," .mdc-data-table{width:100%;border:0}.mdc-data-table__cell,.mdc-data-table__header-cell{color:var(--primary-text-color);border-bottom-color:var(--divider-color);text-align:var(--float-start)}.mdc-data-table__row:not(.mdc-data-table__row--selected):hover{background-color:rgba(var(--rgb-primary-text-color),.04)}.total{--mdc-typography-body2-font-weight:500}.total .mdc-data-table__cell{border-top:1px solid var(--divider-color)}ha-card{height:100%;overflow:hidden}.card-header{padding-bottom:0}.content{padding:16px}.has-header{padding-top:0}.cell-bullet{width:32px;padding-right:0;padding-inline-end:0;padding-inline-start:16px;direction:var(--direction)}.bullet{border-width:1px;border-style:solid;border-radius:4px;height:16px;width:32px}.mdc-data-table__cell--numeric{direction:ltr}"])),(0,k.iz)(p))}}]}}),(0,$.E)(k.WF)),s(),a.next=56;break;case 53:a.prev=53,a.t2=a.catch(0),s(a.t2);case 56:case"end":return a.stop()}}),a,null,[[0,53]])})));return function(t,e){return a.apply(this,arguments)}}())}}]);
//# sourceMappingURL=45441.GlQ2lhPXVpM.js.map