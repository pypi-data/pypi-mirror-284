export const id=94555;export const ids=[94555];export const modules={4940:(e,i,t)=>{t.d(i,{JW:()=>u,OW:()=>g,PO:()=>l,VN:()=>d,XG:()=>s,eB:()=>C,gZ:()=>v,hM:()=>c,k2:()=>r,lU:()=>m,nc:()=>_,vX:()=>p,z1:()=>n});t(21950),t(66274),t(85038),t(85767),t(98168),t(15445),t(24483),t(13478),t(46355),t(14612),t(53691),t(48455),t(8339);var a=t(28825),o=t(1169);let n=function(e){return e.THREAD="thread",e.WIFI="wifi",e.ETHERNET="ethernet",e.UNKNOWN="unknown",e}({});const r=e=>{var i;return null===(i=e.auth.external)||void 0===i?void 0:i.config.canCommissionMatter},d=e=>e.auth.external.fireMessage({type:"matter/commission"}),c=(e,i)=>{let t;const n=(0,o.Ag)(e.connection,(e=>{if(!t)return void(t=new Set(Object.values(e).filter((e=>e.identifiers.find((e=>"matter"===e[0])))).map((e=>e.id))));const o=Object.values(e).filter((e=>e.identifiers.find((e=>"matter"===e[0]))&&!t.has(e.id)));o.length&&(n(),t=void 0,null==i||i(),(0,a.o)(`/config/devices/device/${o[0].id}`))}));return()=>{n(),t=void 0}},l=(e,i)=>e.callWS({type:"matter/commission",code:i}),s=(e,i)=>e.callWS({type:"matter/commission_on_network",pin:i}),m=(e,i,t)=>e.callWS({type:"matter/set_wifi_credentials",network_name:i,password:t}),v=(e,i)=>e.callWS({type:"matter/set_thread",thread_operation_dataset:i}),C=(e,i)=>e.callWS({type:"matter/node_diagnostics",device_id:i}),g=(e,i)=>e.callWS({type:"matter/ping_node",device_id:i}),_=(e,i)=>e.callWS({type:"matter/open_commissioning_window",device_id:i}),p=(e,i,t)=>e.callWS({type:"matter/remove_matter_fabric",device_id:i,fabric_index:t}),u=(e,i)=>e.callWS({type:"matter/interview_node",device_id:i})},94555:(e,i,t)=>{t.r(i),t.d(i,{getMatterDeviceActions:()=>m});t(71936),t(55888);var a=t(4940),o=(t(21950),t(8339),t(77664));const n=()=>t.e(86936).then(t.bind(t,86936)),r=()=>t.e(82656).then(t.bind(t,82656)),d=()=>Promise.all([t.e(51859),t.e(28345),t.e(37954)]).then(t.bind(t,37954)),c=()=>Promise.all([t.e(51859),t.e(28345),t.e(67703)]).then(t.bind(t,67703));var l=t(28825);const s="M12,1L8,5H11V14H13V5H16M18,23H6C4.89,23 4,22.1 4,21V9A2,2 0 0,1 6,7H9V9H6V21H18V9H15V7H18A2,2 0 0,1 20,9V21A2,2 0 0,1 18,23Z",m=async(e,i,t)=>{if(null!==t.via_device_id)return[];const m=await(0,a.eB)(i,t.id),v=[];return m.available&&(v.push({label:i.localize("ui.panel.config.matter.device_actions.open_commissioning_window"),icon:s,action:()=>{return i=e,a={device_id:t.id},void(0,o.r)(i,"show-dialog",{dialogTag:"dialog-matter-open-commissioning-window",dialogImport:d,dialogParams:a});var i,a}}),v.push({label:i.localize("ui.panel.config.matter.device_actions.manage_fabrics"),icon:s,action:()=>{return i=e,a={device_id:t.id},void(0,o.r)(i,"show-dialog",{dialogTag:"dialog-matter-manage-fabrics",dialogImport:c,dialogParams:a});var i,a}}),v.push({label:i.localize("ui.panel.config.matter.device_actions.reinterview_device"),icon:"M12,3C17.5,3 22,6.58 22,11C22,15.42 17.5,19 12,19C10.76,19 9.57,18.82 8.47,18.5C5.55,21 2,21 2,21C4.33,18.67 4.7,17.1 4.75,16.5C3.05,15.07 2,13.13 2,11C2,6.58 6.5,3 12,3M17,12V10H15V12H17M13,12V10H11V12H13M9,12V10H7V12H9Z",action:()=>{return i=e,a={device_id:t.id},void(0,o.r)(i,"show-dialog",{dialogTag:"dialog-matter-reinterview-node",dialogImport:n,dialogParams:a});var i,a}})),m.network_type===a.z1.THREAD&&v.push({label:i.localize("ui.panel.config.matter.device_actions.view_thread_network"),icon:"M4.93,4.93C3.12,6.74 2,9.24 2,12C2,14.76 3.12,17.26 4.93,19.07L6.34,17.66C4.89,16.22 4,14.22 4,12C4,9.79 4.89,7.78 6.34,6.34L4.93,4.93M19.07,4.93L17.66,6.34C19.11,7.78 20,9.79 20,12C20,14.22 19.11,16.22 17.66,17.66L19.07,19.07C20.88,17.26 22,14.76 22,12C22,9.24 20.88,6.74 19.07,4.93M7.76,7.76C6.67,8.85 6,10.35 6,12C6,13.65 6.67,15.15 7.76,16.24L9.17,14.83C8.45,14.11 8,13.11 8,12C8,10.89 8.45,9.89 9.17,9.17L7.76,7.76M16.24,7.76L14.83,9.17C15.55,9.89 16,10.89 16,12C16,13.11 15.55,14.11 14.83,14.83L16.24,16.24C17.33,15.15 18,13.65 18,12C18,10.35 17.33,8.85 16.24,7.76M12,10A2,2 0 0,0 10,12A2,2 0 0,0 12,14A2,2 0 0,0 14,12A2,2 0 0,0 12,10Z",action:()=>(0,l.o)("/config/thread")}),v.push({label:i.localize("ui.panel.config.matter.device_actions.ping_device"),icon:"M12 3C6.5 3 2 6.6 2 11C2 13.1 3 15.1 4.8 16.5C4.8 17.1 4.4 18.7 2 21C2 21 5.5 21 8.5 18.5C9.6 18.8 10.8 19 12 19C17.5 19 22 15.4 22 11S17.5 3 12 3M13 15H11V13H13V15M14.8 10C14.5 10.4 14.1 10.6 13.7 10.8C13.4 11 13.3 11.1 13.2 11.3C13 11.5 13 11.7 13 12H11C11 11.5 11.1 11.2 11.3 10.9C11.5 10.7 11.9 10.4 12.4 10.1C12.7 10 12.9 9.8 13 9.6C13.1 9.4 13.2 9.1 13.2 8.9C13.2 8.6 13.1 8.4 12.9 8.2C12.7 8 12.4 7.9 12.1 7.9C11.8 7.9 11.6 8 11.4 8.1C11.2 8.2 11.1 8.4 11.1 8.7H9.1C9.2 8 9.5 7.4 10 7C10.5 6.6 11.2 6.5 12.1 6.5C13 6.5 13.8 6.7 14.3 7.1C14.8 7.5 15.1 8.1 15.1 8.8C15.2 9.2 15.1 9.6 14.8 10Z",action:()=>{return i=e,a={device_id:t.id},void(0,o.r)(i,"show-dialog",{dialogTag:"dialog-matter-ping-node",dialogImport:r,dialogParams:a});var i,a}}),v}}};
//# sourceMappingURL=94555.29zIby1uJa4.js.map