(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[8691],{79986:(t,e,r)=>{"use strict";r.d(e,{Z:()=>d});r(66845);var n,o=r(50641),i=r(86659),s=r(50669),a=r(1515);const l=(0,r(7865).F4)(n||(n=(0,s.Z)(["\n  50% {\n    color: rgba(0, 0, 0, 0);\n  }\n"]))),u=(0,a.Z)("span",{target:"edlqvik0"})((t=>{let{includeDot:e,shouldBlink:r,theme:n}=t;return{...e?{"&::before":{opacity:1,content:'"\u2022"',animation:"none",color:n.colors.gray,margin:"0 5px"}}:{},...r?{color:n.colors.red,animationName:"".concat(l),animationDuration:"0.5s",animationIterationCount:5}:{}}}),"");var c=r(40864);const d=t=>{let{dirty:e,value:r,maxLength:n,className:s,type:a="single",inForm:l}=t;const d=[],p=function(t){let e=arguments.length>1&&void 0!==arguments[1]&&arguments[1];d.push((0,c.jsx)(u,{includeDot:d.length>0,shouldBlink:e,children:t},d.length))};if(e){const t=l?"submit form":"apply";if("multiline"===a){const e=(0,o.Ge)()?"\u2318":"Ctrl";p("Press ".concat(e,"+Enter to ").concat(t))}else"single"===a&&p("Press Enter to ".concat(t))}return n&&("chat"!==a||e)&&p("".concat(r.length,"/").concat(n),e&&r.length>=n),(0,c.jsx)(i.X7,{"data-testid":"InputInstructions",className:s,children:d})}},87814:(t,e,r)=>{"use strict";r.d(e,{K:()=>o});var n=r(50641);class o{constructor(){this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}manageFormClearListener(t,e,r){null!=this.formClearListener&&this.lastWidgetMgr===t&&this.lastFormId===e||(this.disconnect(),(0,n.bM)(e)&&(this.formClearListener=t.addFormClearedListener(e,r),this.lastWidgetMgr=t,this.lastFormId=e))}disconnect(){var t;null===(t=this.formClearListener)||void 0===t||t.disconnect(),this.formClearListener=void 0,this.lastWidgetMgr=void 0,this.lastFormId=void 0}}},58691:(t,e,r)=>{"use strict";r.r(e),r.d(e,{default:()=>w});var n=r(66845),o=r(70479),i=r.n(o),s=r(82534),a=r(25621),l=r(16295),u=r(87814),c=r(79986),d=r(98478),p=r(86659),h=r(8879),f=r(68411),m=r(50641),y=r(48266);const b=(0,r(1515).Z)("div",{target:"e11y4ecf0"})((t=>{let{width:e}=t;return{position:"relative",width:e}}),"");var g=r(40864);class v extends n.PureComponent{constructor(t){var e;super(t),e=this,this.formClearHelper=new u.K,this.id=void 0,this.state={dirty:!1,value:this.initialValue},this.commitWidgetValue=function(t){let r=!(arguments.length>1&&void 0!==arguments[1])||arguments[1];const{widgetMgr:n,element:o,fragmentId:i}=e.props;n.setStringValue(o,e.state.value,t,i),r&&e.setState({dirty:!1})},this.onFormCleared=()=>{this.setState(((t,e)=>{var r;return{value:null!==(r=e.element.default)&&void 0!==r?r:null}}),(()=>this.commitWidgetValue({fromUi:!0})))},this.onBlur=()=>{this.state.dirty&&this.commitWidgetValue({fromUi:!0})},this.onChange=t=>{const{value:e}=t.target,{element:r}=this.props,{maxChars:n}=r;0!==n&&e.length>n||((0,m.$b)(this.props.element)?this.setState({dirty:!0,value:e},(()=>{this.commitWidgetValue({fromUi:!0},!1)})):this.setState({dirty:!0,value:e}))},this.onKeyPress=t=>{"Enter"===t.key&&(this.state.dirty&&this.commitWidgetValue({fromUi:!0}),(0,m.$b)(this.props.element)&&this.props.widgetMgr.submitForm(this.props.element.formId,this.props.fragmentId))},this.id=i()("text_input_")}get initialValue(){var t;const e=this.props.widgetMgr.getStringValue(this.props.element);return null!==(t=null!==e&&void 0!==e?e:this.props.element.default)&&void 0!==t?t:null}componentDidMount(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}componentDidUpdate(){this.maybeUpdateFromProtobuf()}componentWillUnmount(){this.formClearHelper.disconnect()}maybeUpdateFromProtobuf(){const{setValue:t}=this.props.element;t&&this.updateFromProtobuf()}updateFromProtobuf(){const{value:t}=this.props.element;this.props.element.setValue=!1,this.setState({value:null!==t&&void 0!==t?t:null},(()=>{this.commitWidgetValue({fromUi:!1})}))}getTypeString(){return this.props.element.type===l.oi.Type.PASSWORD?"password":"text"}render(){var t;const{dirty:e,value:r}=this.state,{element:n,width:o,disabled:i,widgetMgr:a,theme:l}=this.props,{placeholder:u}=n;return this.formClearHelper.manageFormClearListener(a,n.formId,this.onFormCleared),(0,g.jsxs)(b,{className:"row-widget stTextInput","data-testid":"stTextInput",width:o,children:[(0,g.jsx)(d.O,{label:n.label,disabled:i,labelVisibility:(0,m.iF)(null===(t=n.labelVisibility)||void 0===t?void 0:t.value),htmlFor:this.id,children:n.help&&(0,g.jsx)(p.dT,{children:(0,g.jsx)(h.Z,{content:n.help,placement:f.u.TOP_RIGHT})})}),(0,g.jsx)(s.Z,{value:null!==r&&void 0!==r?r:"",placeholder:u,onBlur:this.onBlur,onChange:this.onChange,onKeyPress:this.onKeyPress,"aria-label":n.label,disabled:i,id:this.id,type:this.getTypeString(),autoComplete:n.autocomplete,overrides:{Input:{style:{minWidth:0,"::placeholder":{opacity:"0.7"},lineHeight:l.lineHeights.inputWidget,paddingRight:l.spacing.sm,paddingLeft:l.spacing.sm,paddingBottom:l.spacing.sm,paddingTop:l.spacing.sm}},Root:{props:{"data-testid":"stTextInput-RootElement"},style:{height:l.sizes.minElementHeight,borderLeftWidth:l.sizes.borderWidth,borderRightWidth:l.sizes.borderWidth,borderTopWidth:l.sizes.borderWidth,borderBottomWidth:l.sizes.borderWidth}}}}),o>y.A.hideWidgetDetails&&(0,g.jsx)(c.Z,{dirty:e,value:null!==r&&void 0!==r?r:"",maxLength:n.maxChars,inForm:(0,m.$b)({formId:n.formId})})]})}}const w=(0,a.b)(v)},82534:(t,e,r)=>{"use strict";r.d(e,{Z:()=>S});var n=r(66845),o=r(80318),i=r(32510),s=r(9656),a=r(98479),l=r(38254);function u(t){return u="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},u(t)}var c=["Root","StartEnhancer","EndEnhancer"],d=["startEnhancer","endEnhancer","overrides"];function p(){return p=Object.assign?Object.assign.bind():function(t){for(var e=1;e<arguments.length;e++){var r=arguments[e];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(t[n]=r[n])}return t},p.apply(this,arguments)}function h(t,e){return function(t){if(Array.isArray(t))return t}(t)||function(t,e){var r=null==t?null:"undefined"!==typeof Symbol&&t[Symbol.iterator]||t["@@iterator"];if(null==r)return;var n,o,i=[],s=!0,a=!1;try{for(r=r.call(t);!(s=(n=r.next()).done)&&(i.push(n.value),!e||i.length!==e);s=!0);}catch(l){a=!0,o=l}finally{try{s||null==r.return||r.return()}finally{if(a)throw o}}return i}(t,e)||function(t,e){if(!t)return;if("string"===typeof t)return f(t,e);var r=Object.prototype.toString.call(t).slice(8,-1);"Object"===r&&t.constructor&&(r=t.constructor.name);if("Map"===r||"Set"===r)return Array.from(t);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return f(t,e)}(t,e)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function f(t,e){(null==e||e>t.length)&&(e=t.length);for(var r=0,n=new Array(e);r<e;r++)n[r]=t[r];return n}function m(t,e){if(null==t)return{};var r,n,o=function(t,e){if(null==t)return{};var r,n,o={},i=Object.keys(t);for(n=0;n<i.length;n++)r=i[n],e.indexOf(r)>=0||(o[r]=t[r]);return o}(t,e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);for(n=0;n<i.length;n++)r=i[n],e.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(t,r)&&(o[r]=t[r])}return o}function y(t,e){for(var r=0;r<e.length;r++){var n=e[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(t,n.key,n)}}function b(t,e){return b=Object.setPrototypeOf?Object.setPrototypeOf.bind():function(t,e){return t.__proto__=e,t},b(t,e)}function g(t){var e=function(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(t){return!1}}();return function(){var r,n=w(t);if(e){var o=w(this).constructor;r=Reflect.construct(n,arguments,o)}else r=n.apply(this,arguments);return function(t,e){if(e&&("object"===u(e)||"function"===typeof e))return e;if(void 0!==e)throw new TypeError("Derived constructors may only return object or undefined");return v(t)}(this,r)}}function v(t){if(void 0===t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}function w(t){return w=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(t){return t.__proto__||Object.getPrototypeOf(t)},w(t)}function j(t,e,r){return e in t?Object.defineProperty(t,e,{value:r,enumerable:!0,configurable:!0,writable:!0}):t[e]=r,t}var O=function(t){!function(t,e){if("function"!==typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),Object.defineProperty(t,"prototype",{writable:!1}),e&&b(t,e)}(w,t);var e,r,u,f=g(w);function w(){var t;!function(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}(this,w);for(var e=arguments.length,r=new Array(e),n=0;n<e;n++)r[n]=arguments[n];return j(v(t=f.call.apply(f,[this].concat(r))),"state",{isFocused:t.props.autoFocus||!1}),j(v(t),"onFocus",(function(e){t.setState({isFocused:!0}),t.props.onFocus(e)})),j(v(t),"onBlur",(function(e){t.setState({isFocused:!1}),t.props.onBlur(e)})),t}return e=w,(r=[{key:"render",value:function(){var t=this.props,e=t.startEnhancer,r=t.endEnhancer,u=t.overrides,f=u.Root,y=u.StartEnhancer,b=u.EndEnhancer,g=m(u,c),v=m(t,d),w=h((0,o.jb)(f,a.fC),2),j=w[0],O=w[1],S=h((0,o.jb)(y,a.Fp),2),E=S[0],P=S[1],x=h((0,o.jb)(b,a.Fp),2),W=x[0],I=x[1],T=(0,i.t)(this.props,this.state);return n.createElement(j,p({"data-baseweb":"input"},T,O,{$adjoined:F(e,r),$hasIconTrailing:this.props.clearable||"password"==this.props.type}),C(e)&&n.createElement(E,p({},T,P,{$position:l.Xf.start}),"function"===typeof e?e(T):e),n.createElement(s.Z,p({},v,{overrides:g,adjoined:F(e,r),onFocus:this.onFocus,onBlur:this.onBlur})),C(r)&&n.createElement(W,p({},T,I,{$position:l.Xf.end}),"function"===typeof r?r(T):r))}}])&&y(e.prototype,r),u&&y(e,u),Object.defineProperty(e,"prototype",{writable:!1}),w}(n.Component);function F(t,e){return C(t)&&C(e)?l.y4.both:C(t)?l.y4.left:C(e)?l.y4.right:l.y4.none}function C(t){return Boolean(t||0===t)}j(O,"defaultProps",{autoComplete:"on",autoFocus:!1,disabled:!1,name:"",onBlur:function(){},onFocus:function(){},overrides:{},required:!1,size:l.NO.default,startEnhancer:null,endEnhancer:null,clearable:!1,type:"text",readOnly:!1});const S=O},70479:(t,e,r)=>{var n=r(38145),o=0;t.exports=function(t){var e=++o;return n(t)+e}}}]);