"use strict";(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[5441],{5441:(e,t,o)=>{o.r(t),o.d(t,{default:()=>P});var n=o(66845),i=o(25621),s=o(72965),a=o(94206),r=o(60784),l=o(62813),d=o.n(l),c=o(50641),h=o(23849),u=o(23593),m=o(63765),g=o(87814),p=o(91191);const f={DATAFRAME_INDEX:"(index)"},b=new Set([p.GI.DatetimeIndex,p.GI.Float64Index,p.GI.Int64Index,p.GI.RangeIndex,p.GI.UInt64Index]);function v(e){var t;if(0===(null===(t=e.datasets)||void 0===t?void 0:t.length))return null;const o={};return e.datasets.forEach((e=>{if(!e)return;const t=e.hasName?e.name:null;o[t]=e.data})),o}function w(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0;if(e.isEmpty())return[];const o=[],{dataRows:n,dataColumns:i}=e.dimensions,s=p.fu.getTypeName(e.types.index[0]),a=b.has(s);for(let r=t;r<n;r++){const t={};if(a){const o=e.getIndexValue(r,0);t[f.DATAFRAME_INDEX]="bigint"===typeof o?Number(o):o}for(let o=0;o<i;o++){const n=e.getDataValue(r,o),i=e.types.data[o],s=p.fu.getTypeName(i);if("datetimetz"!==s&&(n instanceof Date||Number.isFinite(n))&&(s.startsWith("datetime")||"date"===s)){const i=60*new Date(n).getTimezoneOffset()*1e3;t[e.columns[0][o]]=n.valueOf()+i}else t[e.columns[0][o]]="bigint"===typeof n?Number(n):n}o.push(t)}return o}var y=o(96825),x=o.n(y),S=o(99394),F=o.n(S),C=o(27466);function z(e,t){const o={font:t.genericFonts.bodyFont,background:t.colors.bgColor,fieldTitle:"verbal",autosize:{type:"fit",contains:"padding"},title:{align:"left",anchor:"start",color:t.colors.headingColor,titleFontStyle:"normal",fontWeight:t.fontWeights.bold,fontSize:t.fontSizes.smPx+2,orient:"top",offset:26},header:{titleFontWeight:t.fontWeights.normal,titleFontSize:t.fontSizes.mdPx,titleColor:(0,C.Xy)(t),titleFontStyle:"normal",labelFontSize:t.fontSizes.twoSmPx,labelFontWeight:t.fontWeights.normal,labelColor:(0,C.Xy)(t),labelFontStyle:"normal"},axis:{labelFontSize:t.fontSizes.twoSmPx,labelFontWeight:t.fontWeights.normal,labelColor:(0,C.Xy)(t),labelFontStyle:"normal",titleFontWeight:t.fontWeights.normal,titleFontSize:t.fontSizes.smPx,titleColor:(0,C.Xy)(t),titleFontStyle:"normal",ticks:!1,gridColor:(0,C.ny)(t),domain:!1,domainWidth:1,domainColor:(0,C.ny)(t),labelFlush:!0,labelFlushOffset:1,labelBound:!1,labelLimit:100,titlePadding:t.spacing.lgPx,labelPadding:t.spacing.lgPx,labelSeparation:t.spacing.twoXSPx,labelOverlap:!0},legend:{labelFontSize:t.fontSizes.smPx,labelFontWeight:t.fontWeights.normal,labelColor:(0,C.Xy)(t),titleFontSize:t.fontSizes.smPx,titleFontWeight:t.fontWeights.normal,titleFontStyle:"normal",titleColor:(0,C.Xy)(t),titlePadding:5,labelPadding:t.spacing.lgPx,columnPadding:t.spacing.smPx,rowPadding:t.spacing.twoXSPx,padding:7,symbolStrokeWidth:4},range:{category:(0,C.iY)(t),diverging:(0,C.ru)(t),ramp:(0,C.Gy)(t),heatmap:(0,C.Gy)(t)},view:{columns:1,strokeWidth:0,stroke:"transparent",continuousHeight:350,continuousWidth:400},concat:{columns:1},facet:{columns:1},mark:{tooltip:!0,...(0,C.Iy)(t)?{color:"#0068C9"}:{color:"#83C9FF"}},bar:{binSpacing:t.spacing.twoXSPx,discreteBandSize:{band:.85}},axisDiscrete:{grid:!1},axisXPoint:{grid:!1},axisTemporal:{grid:!1},axisXBand:{grid:!1}};return e?F()({},o,e,((e,t)=>Array.isArray(t)?t:void 0)):o}const W=(0,o(1515).Z)("div",{target:"egd2k5h0"})((e=>{let{theme:t,useContainerWidth:o,isFullScreen:n}=e;return{width:o||n?"100%":"auto",height:n?"100%":"auto","&.vega-embed":{"&:hover summary, .vega-embed:focus summary":{background:"transparent"},"&.has-actions":{paddingRight:0},".vega-actions":{zIndex:t.zIndices.popupMenu,backgroundColor:t.colors.bgColor,boxShadow:"rgb(0 0 0 / 16%) 0px 4px 16px",border:"".concat(t.sizes.borderWidth," solid ").concat(t.colors.fadedText10),a:{fontFamily:t.genericFonts.bodyFont,fontWeight:t.fontWeights.normal,fontSize:t.fontSizes.md,margin:0,padding:"".concat(t.spacing.twoXS," ").concat(t.spacing.twoXL),color:t.colors.bodyText},"a:hover":{backgroundColor:t.colors.secondaryBg,color:t.colors.bodyText},":before":{content:"none"},":after":{content:"none"}},summary:{opacity:0,height:"auto",zIndex:t.zIndices.menuButton,border:"none",boxShadow:"none",borderRadius:t.radii.default,color:t.colors.fadedText10,backgroundColor:"transparent",transition:"opacity 300ms 150ms,transform 300ms 150ms","&:active, &:focus-visible, &:hover":{border:"none",boxShadow:"none",color:t.colors.bodyText,opacity:"1 !important",background:t.colors.darkenedBgMix25}}}}}),"");var V=o(40864);const I="source";class D extends n.PureComponent{constructor(){super(...arguments),this.vegaView=void 0,this.vegaFinalizer=void 0,this.defaultDataName=I,this.element=null,this.formClearHelper=new g.K,this.state={error:void 0},this.finalizeView=()=>{this.vegaFinalizer&&this.vegaFinalizer(),this.vegaFinalizer=void 0,this.vegaView=void 0},this.generateSpec=()=>{var e,t;const{element:o,theme:n,isFullScreen:i,width:s,height:a}=this.props,r=JSON.parse(o.spec),{useContainerWidth:l}=o;if("streamlit"===o.vegaLiteTheme?r.config=z(r.config,n):"streamlit"===(null===(e=r.usermeta)||void 0===e||null===(t=e.embedOptions)||void 0===t?void 0:t.theme)?(r.config=z(r.config,n),r.usermeta.embedOptions.theme=void 0):r.config=function(e,t){const{colors:o,fontSizes:n,genericFonts:i}=t,s={labelFont:i.bodyFont,titleFont:i.bodyFont,labelFontSize:n.twoSmPx,titleFontSize:n.twoSmPx},a={background:o.bgColor,axis:{labelColor:o.bodyText,titleColor:o.bodyText,gridColor:(0,C.ny)(t),...s},legend:{labelColor:o.bodyText,titleColor:o.bodyText,...s},title:{color:o.bodyText,subtitleColor:o.bodyText,...s},header:{labelColor:o.bodyText,titleColor:o.bodyText,...s},view:{stroke:(0,C.ny)(t),continuousHeight:350,continuousWidth:400},mark:{tooltip:!0}};return e?x()({},a,e):a}(r.config,n),i?(r.width=s,r.height=a,"vconcat"in r&&r.vconcat.forEach((e=>{e.width=s}))):l&&(r.width=s,"vconcat"in r&&r.vconcat.forEach((e=>{e.width=s}))),r.padding||(r.padding={}),null==r.padding.bottom&&(r.padding.bottom=20),r.datasets)throw new Error("Datasets should not be passed as part of the spec");return o.selectionMode.length>0&&function(e){"params"in e&&"encoding"in e&&e.params.forEach((t=>{"select"in t&&(["interval","point"].includes(t.select)&&(t.select={type:t.select}),"type"in t.select&&"point"===t.select.type&&!("encodings"in t.select)&&(0,c.le)(t.select.encodings)&&(t.select.encodings=Object.keys(e.encoding)))}))}(r),r},this.maybeConfigureSelections=()=>{if(void 0===this.vegaView)return;const{widgetMgr:e,element:t}=this.props;if(null===t||void 0===t||!t.id||0===t.selectionMode.length)return;const o=e.getElementState(this.props.element.id,"viewState");if((0,c.bb)(o))try{this.vegaView=this.vegaView.setState(o)}catch(i){(0,h.KE)("Failed to restore view state",i)}t.selectionMode.forEach(((o,n)=>{var i;null===(i=this.vegaView)||void 0===i||i.addSignalListener(o,(0,c.Ds)(150,((o,n)=>{var i;const s=null===(i=this.vegaView)||void 0===i?void 0:i.getState({data:(e,o)=>t.selectionMode.some((t=>"".concat(t,"_store")===e)),recurse:!1});(0,c.bb)(s)&&e.setElementState(t.id,"viewState",s);let a=n;"vlPoint"in n&&"or"in n.vlPoint&&(a=n.vlPoint.or);const r=JSON.parse(e.getStringValue(t)||"{}"),l={selection:{...(null===r||void 0===r?void 0:r.selection)||{},[o]:a||{}}};d()(r,l)||e.setStringValue(t,JSON.stringify(l),{fromUi:!0},this.props.fragmentId)})))}));const n=()=>{const o={selection:{}};this.props.element.selectionMode.forEach((e=>{o.selection[e]={}}));const n=e.getStringValue(t),i=n?JSON.parse(n):o;var s;d()(i,o)||(null===(s=this.props.widgetMgr)||void 0===s||s.setStringValue(this.props.element,JSON.stringify(o),{fromUi:!0},this.props.fragmentId))};this.props.element.formId&&this.formClearHelper.manageFormClearListener(this.props.widgetMgr,this.props.element.formId,n)}}async componentDidMount(){try{await this.createView()}catch(e){const t=(0,m.b)(e);this.setState({error:t})}}componentWillUnmount(){this.finalizeView()}async componentDidUpdate(e){const{element:t,theme:o}=e,{element:n,theme:i}=this.props,s=t.spec,{spec:a}=n;if(!this.vegaView||s!==a||o!==i||e.width!==this.props.width||e.height!==this.props.height||e.element.vegaLiteTheme!==this.props.element.vegaLiteTheme||!d()(e.element.selectionMode,this.props.element.selectionMode)){(0,h.ji)("Vega spec changed.");try{await this.createView()}catch(g){const e=(0,m.b)(g);this.setState({error:e})}return}const r=t.data,{data:l}=n;(r||l)&&this.updateData(this.defaultDataName,r,l);const c=v(t)||{},u=v(n)||{};for(const[d,h]of Object.entries(u)){const e=d||this.defaultDataName,t=c[e];this.updateData(e,t,h)}for(const d of Object.keys(c))u.hasOwnProperty(d)||d===this.defaultDataName||this.updateData(d,null,null);this.vegaView.resize().runAsync()}updateData(e,t,o){if(!this.vegaView)throw new Error("Chart has not been drawn yet");if(!o||0===o.data.numRows)try{this.vegaView.remove(e,a.truthy)}finally{return}if(!t||0===t.data.numRows)return void this.vegaView.insert(e,w(o));const{dataRows:n,dataColumns:i}=t.dimensions,{dataRows:s,dataColumns:r}=o.dimensions;!function(e,t,o,n,i,s){if(o!==s)return!1;if(t>=i)return!1;if(0===t)return!1;const a=s-1,r=t-1;return e.getDataValue(0,a)===n.getDataValue(0,a)&&e.getDataValue(r,a)===n.getDataValue(r,a)}(t,n,i,o,s,r)?(this.vegaView.data(e,w(o)),(0,h.ji)("Had to clear the ".concat(e," dataset before inserting data through Vega view."))):n<s&&this.vegaView.insert(e,w(o,n))}async createView(){if((0,h.ji)("Creating a new Vega view."),!this.element)throw Error("Element missing.");this.finalizeView();const{element:e}=this.props,t=this.generateSpec(),o={ast:!0,expr:r.N,tooltip:{disableDefaultStyle:!0},defaultStyle:!1,forceActionsMenu:!0},{vgSpec:n,view:i,finalize:a}=await(0,s.ZP)(this.element,t,o);this.vegaView=i,this.maybeConfigureSelections(),this.vegaFinalizer=a;const l=function(e){const t=v(e);if(null==t)return null;const o={};for(const[n,i]of Object.entries(t))o[n]=w(i);return o}(e),d=l?Object.keys(l):[];if(1===d.length){const[e]=d;this.defaultDataName=e}else 0===d.length&&n.data&&(this.defaultDataName=I);const c=function(e){const t=e.data;return t&&0!==t.data.numRows?w(t):null}(e);if(c&&i.insert(this.defaultDataName,c),l)for(const[s,r]of Object.entries(l))i.insert(s,r);await i.runAsync(),this.vegaView.resize().runAsync()}render(){if(this.state.error)throw this.state.error;return(0,V.jsx)(W,{"data-testid":"stArrowVegaLiteChart",useContainerWidth:this.props.element.useContainerWidth,isFullScreen:this.props.isFullScreen,ref:e=>{this.element=e}})}}const P=(0,i.b)((0,u.Z)(D))},23593:(e,t,o)=>{o.d(t,{Z:()=>b});var n=o(66845),i=o(13005),s=o.n(i),a=o(25621),r=o(82218),l=o(97781),d=o(46927),c=o(66694),h=o(1515);const u=(0,h.Z)("button",{target:"e1vs0wn31"})((e=>{let{isExpanded:t,theme:o}=e;const n=t?{right:"0.4rem",top:"0.5rem",backgroundColor:"transparent"}:{right:"-3.0rem",top:"-0.375rem",opacity:0,transform:"scale(0)",backgroundColor:o.colors.lightenedBg05};return{position:"absolute",display:"flex",alignItems:"center",justifyContent:"center",zIndex:o.zIndices.sidebar+1,height:"2.5rem",width:"2.5rem",transition:"opacity 300ms 150ms, transform 300ms 150ms",border:"none",color:o.colors.fadedText60,borderRadius:"50%",...n,"&:focus":{outline:"none"},"&:active, &:focus-visible, &:hover":{opacity:1,outline:"none",transform:"scale(1)",color:o.colors.bodyText,transition:"none"}}}),""),m=(0,h.Z)("div",{target:"e1vs0wn30"})((e=>{let{theme:t,isExpanded:o}=e;return{"&:hover":{[u]:{opacity:1,transform:"scale(1)",transition:"none"}},...o?{position:"fixed",top:0,left:0,bottom:0,right:0,background:t.colors.bgColor,zIndex:t.zIndices.fullscreenWrapper,padding:t.spacing.md,paddingTop:"2.875rem",overflow:["auto","overlay"],display:"flex",alignItems:"center",justifyContent:"center"}:{}}}),"");var g=o(40864);class p extends n.PureComponent{constructor(e){super(e),this.context=void 0,this.controlKeys=e=>{const{expanded:t}=this.state;27===e.keyCode&&t&&this.zoomOut()},this.zoomIn=()=>{document.body.style.overflow="hidden",this.context.setFullScreen(!0),this.setState({expanded:!0})},this.zoomOut=()=>{document.body.style.overflow="unset",this.context.setFullScreen(!1),this.setState({expanded:!1})},this.convertScssRemValueToPixels=e=>parseFloat(e)*parseFloat(getComputedStyle(document.documentElement).fontSize),this.getWindowDimensions=()=>{const e=this.convertScssRemValueToPixels(this.props.theme.spacing.md),t=this.convertScssRemValueToPixels("2.875rem");return{fullWidth:window.innerWidth-2*e,fullHeight:window.innerHeight-(e+t)}},this.updateWindowDimensions=()=>{this.setState(this.getWindowDimensions())},this.state={expanded:!1,...this.getWindowDimensions()}}componentDidMount(){window.addEventListener("resize",this.updateWindowDimensions),document.addEventListener("keydown",this.controlKeys,!1)}componentWillUnmount(){window.removeEventListener("resize",this.updateWindowDimensions),document.removeEventListener("keydown",this.controlKeys,!1)}render(){const{expanded:e,fullWidth:t,fullHeight:o}=this.state,{children:n,width:i,height:s,disableFullscreenMode:a}=this.props;let c=r.d,h=this.zoomIn,p="View fullscreen";return e&&(c=l.m,h=this.zoomOut,p="Exit fullscreen"),(0,g.jsxs)(m,{isExpanded:e,"data-testid":"stFullScreenFrame",children:[!a&&(0,g.jsx)(u,{"data-testid":"StyledFullScreenButton",onClick:h,title:p,isExpanded:e,children:(0,g.jsx)(d.Z,{content:c})}),n(e?{width:t,height:o,expanded:e,expand:this.zoomIn,collapse:this.zoomOut}:{width:i,height:s,expanded:e,expand:this.zoomIn,collapse:this.zoomOut})]})}}p.contextType=c.E;const f=(0,a.b)(p);const b=function(e){let t=arguments.length>1&&void 0!==arguments[1]&&arguments[1];class o extends n.PureComponent{constructor(){super(...arguments),this.render=()=>{const{width:o,height:n,disableFullscreenMode:i}=this.props;return(0,g.jsx)(f,{width:o,height:n,disableFullscreenMode:t||i,children:t=>{let{width:o,height:n,expanded:i,expand:s,collapse:a}=t;return(0,g.jsx)(e,{...this.props,width:o,height:n,isFullScreen:i,expand:s,collapse:a})}})}}}return o.displayName="withFullScreenWrapper(".concat(e.displayName||e.name,")"),s()(o,e)}},87814:(e,t,o)=>{o.d(t,{K:()=>i});var n=o(50641);class i{constructor(){this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}manageFormClearListener(e,t,o){null!=this.formClearListener&&this.lastWidgetMgr===e&&this.lastFormId===t||(this.disconnect(),(0,n.bM)(t)&&(this.formClearListener=e.addFormClearedListener(t,o),this.lastWidgetMgr=e,this.lastFormId=t))}disconnect(){var e;null===(e=this.formClearListener)||void 0===e||e.disconnect(),this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}}}}]);