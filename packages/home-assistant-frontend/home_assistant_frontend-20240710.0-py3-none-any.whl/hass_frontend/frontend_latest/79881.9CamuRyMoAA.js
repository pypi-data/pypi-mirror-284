export const id=79881;export const ids=[79881];export const modules={46054:(o,r,a)=>{a.a(o,(async(o,e)=>{try{a.r(r),a.d(r,{EditorState:()=>n.$t,EditorView:()=>d.Lz,autocompletion:()=>p.yU,crosshairCursor:()=>d.HJ,defaultKeymap:()=>t.pw,drawSelection:()=>d.VH,haSyntaxHighlighting:()=>_,haTheme:()=>h,highlightActiveLine:()=>d.dz,highlightSelectionMatches:()=>g.gN,highlightingFor:()=>c.GY,history:()=>t.b6,historyKeymap:()=>t.cL,keymap:()=>d.w4,langCompartment:()=>b,langs:()=>x,lineNumbers:()=>d.$K,linewrapCompartment:()=>y,readonlyCompartment:()=>v,rectangularSelection:()=>d.D4,searchKeymap:()=>g.Eo,tabKeyBindings:()=>u,tags:()=>m._A});var t=a(380),c=a(22828),i=a(53354),l=a(59032),n=a(62423),d=a(31609),m=a(7398),p=a(52478),g=a(45106),s=o([p,t,c,g,d]);[p,t,c,g,d]=s.then?(await s)():s;const x={jinja2:c.Tg.define(i.n),yaml:c.Tg.define(l.o)},b=new n.xx,v=new n.xx,y=new n.xx,u=[{key:"Tab",run:t.UY},{key:"Shift-Tab",run:t.Mg}],h=d.Lz.theme({"&":{color:"var(--primary-text-color)",backgroundColor:"var(--code-editor-background-color, var(--mdc-text-field-fill-color, whitesmoke))",borderRadius:"var(--mdc-shape-small, 4px) var(--mdc-shape-small, 4px) 0px 0px",caretColor:"var(--secondary-text-color)",height:"var(--code-mirror-height, auto)",maxHeight:"var(--code-mirror-max-height, unset)"},"&.cm-editor.cm-focused":{outline:"none"},"&.cm-focused .cm-cursor":{borderLeftColor:"var(--secondary-text-color)"},".cm-selectionBackground, ::selection":{backgroundColor:"rgba(var(--rgb-primary-color), 0.1)"},"&.cm-focused > .cm-scroller > .cm-selectionLayer .cm-selectionBackground":{backgroundColor:"rgba(var(--rgb-primary-color), 0.2)"},".cm-activeLine":{backgroundColor:"rgba(var(--rgb-secondary-text-color), 0.1)"},".cm-scroller":{outline:"none"},".cm-content":{caretColor:"var(--secondary-text-color)",paddingTop:"16px",paddingBottom:"16px"},".cm-panels":{backgroundColor:"var(--primary-background-color)",color:"var(--primary-text-color)"},".cm-panels.top":{borderBottom:"1px solid var(--divider-color)"},".cm-panels.bottom":{borderTop:"1px solid var(--divider-color)"},".cm-button":{border:"1px solid var(--primary-color)",padding:"0px 16px",textTransform:"uppercase",margin:"4px",background:"none",color:"var(--primary-color)",fontFamily:"var(--mdc-typography-button-font-family, var(--mdc-typography-font-family, Roboto, sans-serif))",fontSize:"var(--mdc-typography-button-font-size, 0.875rem)",height:"36px",fontWeight:"var(--mdc-typography-button-font-weight, 500)",borderRadius:"4px",letterSpacing:"var(--mdc-typography-button-letter-spacing, 0.0892857em)"},".cm-textfield":{padding:"4px 0px 5px",borderRadius:"0",fontSize:"16px",color:"var(--primary-text-color)",border:"0",background:"none",fontFamily:"Roboto",borderBottom:"1px solid var(--secondary-text-color)",margin:"4px 4px 0","& ::placeholder":{color:"var(--secondary-text-color)"},"&:focus":{outline:"none",borderBottom:"2px solid var(--primary-color)",paddingBottom:"4px"}},".cm-tooltip":{color:"var(--primary-text-color)",backgroundColor:"var(--code-editor-background-color, var(--card-background-color))",border:"1px solid var(--divider-color)",borderRadius:"var(--mdc-shape-medium, 4px)",boxShadow:"0px 5px 5px -3px rgb(0 0 0 / 20%), 0px 8px 10px 1px rgb(0 0 0 / 14%), 0px 3px 14px 2px rgb(0 0 0 / 12%)"},"& .cm-tooltip.cm-tooltip-autocomplete > ul > li":{padding:"4px 8px"},"& .cm-tooltip-autocomplete ul li[aria-selected]":{background:"var(--primary-color)",color:"var(--text-primary-color)"},".cm-completionIcon":{display:"none"},".cm-completionDetail":{fontFamily:"Roboto",color:"var(--secondary-text-color)"},"li[aria-selected] .cm-completionDetail":{color:"var(--text-primary-color)"},"& .cm-completionInfo.cm-completionInfo-right":{left:"calc(100% + 4px)"},"& .cm-tooltip.cm-completionInfo":{padding:"4px 8px",marginTop:"-5px"},".cm-selectionMatch":{backgroundColor:"rgba(var(--rgb-primary-color), 0.1)"},".cm-searchMatch":{backgroundColor:"rgba(var(--rgb-accent-color), .2)",outline:"1px solid rgba(var(--rgb-accent-color), .4)"},".cm-searchMatch.selected":{backgroundColor:"rgba(var(--rgb-accent-color), .4)",outline:"1px solid var(--accent-color)"},".cm-gutters":{backgroundColor:"var(--code-editor-gutter-color, var(--secondary-background-color, whitesmoke))",color:"var(--paper-dialog-color, var(--secondary-text-color))",border:"none",borderRight:"1px solid var(--secondary-text-color)",paddingRight:"1px"},"&.cm-focused .cm-gutters":{borderRight:"2px solid var(--primary-color)",paddingRight:"0"},".cm-gutterElement.lineNumber":{color:"inherit"}}),A=c.cr.define([{tag:m._A.keyword,color:"var(--codemirror-keyword, #6262FF)"},{tag:[m._A.name,m._A.deleted,m._A.character,m._A.propertyName,m._A.macroName],color:"var(--codemirror-property, #905)"},{tag:[m._A.function(m._A.variableName),m._A.labelName],color:"var(--codemirror-variable, #07a)"},{tag:[m._A.color,m._A.constant(m._A.name),m._A.standard(m._A.name)],color:"var(--codemirror-qualifier, #690)"},{tag:[m._A.definition(m._A.name),m._A.separator],color:"var(--codemirror-def, #8DA6CE)"},{tag:[m._A.typeName,m._A.className,m._A.number,m._A.changed,m._A.annotation,m._A.modifier,m._A.self,m._A.namespace],color:"var(--codemirror-number, #ca7841)"},{tag:[m._A.operator,m._A.operatorKeyword,m._A.url,m._A.escape,m._A.regexp,m._A.link,m._A.special(m._A.string)],color:"var(--codemirror-operator, #cda869)"},{tag:m._A.comment,color:"var(--codemirror-comment, #777)"},{tag:m._A.meta,color:"var(--codemirror-meta, var(--primary-text-color))"},{tag:m._A.strong,fontWeight:"bold"},{tag:m._A.emphasis,fontStyle:"italic"},{tag:m._A.link,color:"var(--primary-color)",textDecoration:"underline"},{tag:m._A.heading,fontWeight:"bold"},{tag:m._A.atom,color:"var(--codemirror-atom, #F90)"},{tag:m._A.bool,color:"var(--codemirror-atom, #F90)"},{tag:m._A.special(m._A.variableName),color:"var(--codemirror-variable-2, #690)"},{tag:m._A.processingInstruction,color:"var(--secondary-text-color)"},{tag:m._A.string,color:"var(--codemirror-string, #07a)"},{tag:m._A.inserted,color:"var(--codemirror-string2, #07a)"},{tag:m._A.invalid,color:"var(--error-color)"}]),_=(0,c.y9)(A);e()}catch(o){e(o)}}))},74808:(o,r,a)=>{a.a(o,(async(o,r)=>{try{a(21950),a(55888),a(8339);"function"!=typeof window.ResizeObserver&&(window.ResizeObserver=(await a.e(76071).then(a.bind(a,76071))).default),r()}catch(o){r(o)}}),1)}};
//# sourceMappingURL=79881.9CamuRyMoAA.js.map