"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[89205],{89205:function(e,t,a){a.r(t);var n=a(36683),r=a(89231),i=a(29864),o=a(83647),s=a(8364),u=(a(49150),a(77052),a(21950),a(68113),a(55888),a(26777),a(58971),a(56262),a(85812),a(8339),a(7146),a(97157),a(56648),a(72435),a(196)),d=a(28825),h=a(70881);(0,s.A)([(0,u.EM)("zha-config-dashboard-router")],(function(e,t){var s=function(t){function a(){var t;(0,r.A)(this,a);for(var n=arguments.length,o=new Array(n),s=0;s<n;s++)o[s]=arguments[s];return t=(0,i.A)(this,a,[].concat(o)),e(t),t}return(0,o.A)(a,t),(0,n.A)(a)}(t);return{F:s,d:[{kind:"field",decorators:[(0,u.MZ)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,u.MZ)({type:Boolean})],key:"isWide",value:function(){return!1}},{kind:"field",decorators:[(0,u.MZ)({type:Boolean})],key:"narrow",value:function(){return!1}},{kind:"field",key:"_configEntry",value:function(){return new URLSearchParams(window.location.search).get("config_entry")}},{kind:"field",key:"routerOptions",value:function(){return{defaultPage:"dashboard",showLoading:!0,routes:{dashboard:{tag:"zha-config-dashboard",load:function(){return Promise.all([a.e(29292),a.e(28591),a.e(87515),a.e(76078),a.e(33066),a.e(28021),a.e(16052),a.e(53868)]).then(a.bind(a,4264))}},add:{tag:"zha-add-devices-page",load:function(){return Promise.all([a.e(27311),a.e(26255),a.e(89226),a.e(29292),a.e(88201),a.e(28591),a.e(36768),a.e(87515),a.e(76078),a.e(32056),a.e(33066),a.e(57780),a.e(38696),a.e(37482),a.e(37382),a.e(28021),a.e(16052),a.e(85689),a.e(16536)]).then(a.bind(a,77159))}},groups:{tag:"zha-groups-dashboard",load:function(){return Promise.all([a.e(27311),a.e(26255),a.e(29292),a.e(22658),a.e(28591),a.e(49774),a.e(87515),a.e(87777),a.e(81550),a.e(76078),a.e(13538),a.e(88130),a.e(12743),a.e(59154),a.e(20493),a.e(33066),a.e(28021),a.e(10957),a.e(59011),a.e(16052),a.e(67373)]).then(a.bind(a,88713))}},group:{tag:"zha-group-page",load:function(){return Promise.all([a.e(27311),a.e(26255),a.e(89226),a.e(29292),a.e(29805),a.e(28591),a.e(49774),a.e(35024),a.e(10957),a.e(55198),a.e(73925)]).then(a.bind(a,73925))}},"group-add":{tag:"zha-add-group-page",load:function(){return Promise.all([a.e(27311),a.e(26255),a.e(29292),a.e(28591),a.e(49774),a.e(35024),a.e(10957),a.e(55198),a.e(82491)]).then(a.bind(a,82491))}},visualization:{tag:"zha-network-visualization-page",load:function(){return Promise.all([a.e(27311),a.e(26255),a.e(89226),a.e(29292),a.e(29805),a.e(88201),a.e(28591),a.e(36768),a.e(34667),a.e(27350),a.e(49774),a.e(35894),a.e(87515),a.e(76078),a.e(12743),a.e(98691),a.e(33066),a.e(38696),a.e(28021),a.e(16052),a.e(57923)]).then(a.bind(a,37341))}}}}}},{kind:"method",key:"updatePageEl",value:function(e){e.route=this.routeTail,e.hass=this.hass,e.isWide=this.isWide,e.narrow=this.narrow,e.configEntryId=this._configEntry,"group"===this._currentPage?e.groupId=this.routeTail.path.substr(1):"device"===this._currentPage?e.ieee=this.routeTail.path.substr(1):"visualization"===this._currentPage&&(e.zoomedDeviceIdFromURL=this.routeTail.path.substr(1));var t=new URLSearchParams(window.location.search);this._configEntry&&!t.has("config_entry")&&(t.append("config_entry",this._configEntry),(0,d.o)("".concat(this.routeTail.prefix).concat(this.routeTail.path,"?").concat(t.toString()),{replace:!0}))}}]}}),h.a)}}]);
//# sourceMappingURL=89205.Fgv_KfbmLak.js.map