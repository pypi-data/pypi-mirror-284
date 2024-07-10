/*!-----------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Version: 0.50.0(c321d0fbecb50ab8a5365fa1965476b0ae63fc87)
 * Released under the MIT license
 * https://github.com/microsoft/monaco-editor/blob/main/LICENSE.txt
 *-----------------------------------------------------------------------------*/
define("vs/language/typescript/tsMode", ["require","require"],(require)=>{
"use strict";var moduleExports=(()=>{var ee=Object.create;var K=Object.defineProperty;var te=Object.getOwnPropertyDescriptor;var ie=Object.getOwnPropertyNames;var re=Object.getPrototypeOf,se=Object.prototype.hasOwnProperty;var B=(n=>typeof require<"u"?require:typeof Proxy<"u"?new Proxy(n,{get:(e,t)=>(typeof require<"u"?require:e)[t]}):n)(function(n){if(typeof require<"u")return require.apply(this,arguments);throw Error('Dynamic require of "'+n+'" is not supported')});var ne=(n,e)=>()=>(e||n((e={exports:{}}).exports,e),e.exports),oe=(n,e)=>{for(var t in e)K(n,t,{get:e[t],enumerable:!0})},H=(n,e,t,i)=>{if(e&&typeof e=="object"||typeof e=="function")for(let l of ie(e))!se.call(n,l)&&l!==t&&K(n,l,{get:()=>e[l],enumerable:!(i=te(e,l))||i.enumerable});return n},$=(n,e,t)=>(H(n,e,"default"),t&&H(t,e,"default")),z=(n,e,t)=>(t=n!=null?ee(re(n)):{},H(e||!n||!n.__esModule?K(t,"default",{value:n,enumerable:!0}):t,n)),ae=n=>H(K({},"__esModule",{value:!0}),n);var G=ne((he,J)=>{var le=z(B("vs/editor/editor.api"));J.exports=le});var me={};oe(me,{Adapter:()=>k,CodeActionAdaptor:()=>O,DefinitionAdapter:()=>F,DiagnosticsAdapter:()=>T,DocumentHighlightAdapter:()=>D,FormatAdapter:()=>A,FormatHelper:()=>x,FormatOnTypeAdapter:()=>R,InlayHintsAdapter:()=>N,Kind:()=>m,LibFiles:()=>_,OutlineAdapter:()=>M,QuickInfoAdapter:()=>P,ReferenceAdapter:()=>L,RenameAdapter:()=>E,SignatureHelpAdapter:()=>I,SuggestAdapter:()=>C,WorkerManager:()=>v,flattenDiagnosticMessageText:()=>U,getJavaScriptWorker:()=>pe,getTypeScriptWorker:()=>de,setupJavaScript:()=>ge,setupTypeScript:()=>ce});var s={};$(s,z(G()));var v=class{constructor(e,t){this._modeId=e;this._defaults=t;this._worker=null,this._client=null,this._configChangeListener=this._defaults.onDidChange(()=>this._stopWorker()),this._updateExtraLibsToken=0,this._extraLibsChangeListener=this._defaults.onDidExtraLibsChange(()=>this._updateExtraLibs())}dispose(){this._configChangeListener.dispose(),this._extraLibsChangeListener.dispose(),this._stopWorker()}_stopWorker(){this._worker&&(this._worker.dispose(),this._worker=null),this._client=null}async _updateExtraLibs(){if(!this._worker)return;let e=++this._updateExtraLibsToken,t=await this._worker.getProxy();this._updateExtraLibsToken===e&&t.updateExtraLibs(this._defaults.getExtraLibs())}_getClient(){return this._client||(this._client=(async()=>(this._worker=s.editor.createWebWorker({moduleId:"vs/language/typescript/tsWorker",label:this._modeId,keepIdleModels:!0,createData:{compilerOptions:this._defaults.getCompilerOptions(),extraLibs:this._defaults.getExtraLibs(),customWorkerPath:this._defaults.workerOptions.customWorkerPath,inlayHintsOptions:this._defaults.inlayHintsOptions}}),this._defaults.getEagerModelSync()?await this._worker.withSyncedResources(s.editor.getModels().filter(e=>e.getLanguageId()===this._modeId).map(e=>e.uri)):await this._worker.getProxy()))()),this._client}async getLanguageServiceWorker(...e){let t=await this._getClient();return this._worker&&await this._worker.withSyncedResources(e),t}};var q=B("./monaco.contribution");var r={};r["lib.d.ts"]=!0;r["lib.decorators.d.ts"]=!0;r["lib.decorators.legacy.d.ts"]=!0;r["lib.dom.asynciterable.d.ts"]=!0;r["lib.dom.d.ts"]=!0;r["lib.dom.iterable.d.ts"]=!0;r["lib.es2015.collection.d.ts"]=!0;r["lib.es2015.core.d.ts"]=!0;r["lib.es2015.d.ts"]=!0;r["lib.es2015.generator.d.ts"]=!0;r["lib.es2015.iterable.d.ts"]=!0;r["lib.es2015.promise.d.ts"]=!0;r["lib.es2015.proxy.d.ts"]=!0;r["lib.es2015.reflect.d.ts"]=!0;r["lib.es2015.symbol.d.ts"]=!0;r["lib.es2015.symbol.wellknown.d.ts"]=!0;r["lib.es2016.array.include.d.ts"]=!0;r["lib.es2016.d.ts"]=!0;r["lib.es2016.full.d.ts"]=!0;r["lib.es2016.intl.d.ts"]=!0;r["lib.es2017.d.ts"]=!0;r["lib.es2017.date.d.ts"]=!0;r["lib.es2017.full.d.ts"]=!0;r["lib.es2017.intl.d.ts"]=!0;r["lib.es2017.object.d.ts"]=!0;r["lib.es2017.sharedmemory.d.ts"]=!0;r["lib.es2017.string.d.ts"]=!0;r["lib.es2017.typedarrays.d.ts"]=!0;r["lib.es2018.asyncgenerator.d.ts"]=!0;r["lib.es2018.asynciterable.d.ts"]=!0;r["lib.es2018.d.ts"]=!0;r["lib.es2018.full.d.ts"]=!0;r["lib.es2018.intl.d.ts"]=!0;r["lib.es2018.promise.d.ts"]=!0;r["lib.es2018.regexp.d.ts"]=!0;r["lib.es2019.array.d.ts"]=!0;r["lib.es2019.d.ts"]=!0;r["lib.es2019.full.d.ts"]=!0;r["lib.es2019.intl.d.ts"]=!0;r["lib.es2019.object.d.ts"]=!0;r["lib.es2019.string.d.ts"]=!0;r["lib.es2019.symbol.d.ts"]=!0;r["lib.es2020.bigint.d.ts"]=!0;r["lib.es2020.d.ts"]=!0;r["lib.es2020.date.d.ts"]=!0;r["lib.es2020.full.d.ts"]=!0;r["lib.es2020.intl.d.ts"]=!0;r["lib.es2020.number.d.ts"]=!0;r["lib.es2020.promise.d.ts"]=!0;r["lib.es2020.sharedmemory.d.ts"]=!0;r["lib.es2020.string.d.ts"]=!0;r["lib.es2020.symbol.wellknown.d.ts"]=!0;r["lib.es2021.d.ts"]=!0;r["lib.es2021.full.d.ts"]=!0;r["lib.es2021.intl.d.ts"]=!0;r["lib.es2021.promise.d.ts"]=!0;r["lib.es2021.string.d.ts"]=!0;r["lib.es2021.weakref.d.ts"]=!0;r["lib.es2022.array.d.ts"]=!0;r["lib.es2022.d.ts"]=!0;r["lib.es2022.error.d.ts"]=!0;r["lib.es2022.full.d.ts"]=!0;r["lib.es2022.intl.d.ts"]=!0;r["lib.es2022.object.d.ts"]=!0;r["lib.es2022.regexp.d.ts"]=!0;r["lib.es2022.sharedmemory.d.ts"]=!0;r["lib.es2022.string.d.ts"]=!0;r["lib.es2023.array.d.ts"]=!0;r["lib.es2023.collection.d.ts"]=!0;r["lib.es2023.d.ts"]=!0;r["lib.es2023.full.d.ts"]=!0;r["lib.es5.d.ts"]=!0;r["lib.es6.d.ts"]=!0;r["lib.esnext.collection.d.ts"]=!0;r["lib.esnext.d.ts"]=!0;r["lib.esnext.decorators.d.ts"]=!0;r["lib.esnext.disposable.d.ts"]=!0;r["lib.esnext.full.d.ts"]=!0;r["lib.esnext.intl.d.ts"]=!0;r["lib.esnext.object.d.ts"]=!0;r["lib.esnext.promise.d.ts"]=!0;r["lib.scripthost.d.ts"]=!0;r["lib.webworker.asynciterable.d.ts"]=!0;r["lib.webworker.d.ts"]=!0;r["lib.webworker.importscripts.d.ts"]=!0;r["lib.webworker.iterable.d.ts"]=!0;function U(n,e,t=0){if(typeof n=="string")return n;if(n===void 0)return"";let i="";if(t){i+=e;for(let l=0;l<t;l++)i+="  "}if(i+=n.messageText,t++,n.next)for(let l of n.next)i+=U(l,e,t);return i}function S(n){return n?n.map(e=>e.text).join(""):""}var k=class{constructor(e){this._worker=e}_textSpanToRange(e,t){let i=e.getPositionAt(t.start),l=e.getPositionAt(t.start+t.length),{lineNumber:u,column:c}=i,{lineNumber:g,column:o}=l;return{startLineNumber:u,startColumn:c,endLineNumber:g,endColumn:o}}},_=class{constructor(e){this._worker=e;this._libFiles={},this._hasFetchedLibFiles=!1,this._fetchLibFilesPromise=null}isLibFile(e){return e&&e.path.indexOf("/lib.")===0?!!r[e.path.slice(1)]:!1}getOrCreateModel(e){let t=s.Uri.parse(e),i=s.editor.getModel(t);if(i)return i;if(this.isLibFile(t)&&this._hasFetchedLibFiles)return s.editor.createModel(this._libFiles[t.path.slice(1)],"typescript",t);let l=q.typescriptDefaults.getExtraLibs()[e];return l?s.editor.createModel(l.content,"typescript",t):null}_containsLibFile(e){for(let t of e)if(this.isLibFile(t))return!0;return!1}async fetchLibFilesIfNecessary(e){this._containsLibFile(e)&&await this._fetchLibFiles()}_fetchLibFiles(){return this._fetchLibFilesPromise||(this._fetchLibFilesPromise=this._worker().then(e=>e.getLibFiles()).then(e=>{this._hasFetchedLibFiles=!0,this._libFiles=e})),this._fetchLibFilesPromise}};var T=class extends k{constructor(t,i,l,u){super(u);this._libFiles=t;this._defaults=i;this._selector=l;this._disposables=[];this._listener=Object.create(null);let c=a=>{if(a.getLanguageId()!==l)return;let d=()=>{let{onlyVisible:y}=this._defaults.getDiagnosticsOptions();y?a.isAttachedToEditor()&&this._doValidate(a):this._doValidate(a)},p,f=a.onDidChangeContent(()=>{clearTimeout(p),p=window.setTimeout(d,500)}),b=a.onDidChangeAttached(()=>{let{onlyVisible:y}=this._defaults.getDiagnosticsOptions();y&&(a.isAttachedToEditor()?d():s.editor.setModelMarkers(a,this._selector,[]))});this._listener[a.uri.toString()]={dispose(){f.dispose(),b.dispose(),clearTimeout(p)}},d()},g=a=>{s.editor.setModelMarkers(a,this._selector,[]);let d=a.uri.toString();this._listener[d]&&(this._listener[d].dispose(),delete this._listener[d])};this._disposables.push(s.editor.onDidCreateModel(a=>c(a))),this._disposables.push(s.editor.onWillDisposeModel(g)),this._disposables.push(s.editor.onDidChangeModelLanguage(a=>{g(a.model),c(a.model)})),this._disposables.push({dispose(){for(let a of s.editor.getModels())g(a)}});let o=()=>{for(let a of s.editor.getModels())g(a),c(a)};this._disposables.push(this._defaults.onDidChange(o)),this._disposables.push(this._defaults.onDidExtraLibsChange(o)),s.editor.getModels().forEach(a=>c(a))}dispose(){this._disposables.forEach(t=>t&&t.dispose()),this._disposables=[]}async _doValidate(t){let i=await this._worker(t.uri);if(t.isDisposed())return;let l=[],{noSyntaxValidation:u,noSemanticValidation:c,noSuggestionDiagnostics:g}=this._defaults.getDiagnosticsOptions();u||l.push(i.getSyntacticDiagnostics(t.uri.toString())),c||l.push(i.getSemanticDiagnostics(t.uri.toString())),g||l.push(i.getSuggestionDiagnostics(t.uri.toString()));let o=await Promise.all(l);if(!o||t.isDisposed())return;let a=o.reduce((p,f)=>f.concat(p),[]).filter(p=>(this._defaults.getDiagnosticsOptions().diagnosticCodesToIgnore||[]).indexOf(p.code)===-1),d=a.map(p=>p.relatedInformation||[]).reduce((p,f)=>f.concat(p),[]).map(p=>p.file?s.Uri.parse(p.file.fileName):null);await this._libFiles.fetchLibFilesIfNecessary(d),!t.isDisposed()&&s.editor.setModelMarkers(t,this._selector,a.map(p=>this._convertDiagnostics(t,p)))}_convertDiagnostics(t,i){let l=i.start||0,u=i.length||1,{lineNumber:c,column:g}=t.getPositionAt(l),{lineNumber:o,column:a}=t.getPositionAt(l+u),d=[];return i.reportsUnnecessary&&d.push(s.MarkerTag.Unnecessary),i.reportsDeprecated&&d.push(s.MarkerTag.Deprecated),{severity:this._tsDiagnosticCategoryToMarkerSeverity(i.category),startLineNumber:c,startColumn:g,endLineNumber:o,endColumn:a,message:U(i.messageText,`
`),code:i.code.toString(),tags:d,relatedInformation:this._convertRelatedInformation(t,i.relatedInformation)}}_convertRelatedInformation(t,i){if(!i)return[];let l=[];return i.forEach(u=>{let c=t;if(u.file&&(c=this._libFiles.getOrCreateModel(u.file.fileName)),!c)return;let g=u.start||0,o=u.length||1,{lineNumber:a,column:d}=c.getPositionAt(g),{lineNumber:p,column:f}=c.getPositionAt(g+o);l.push({resource:c.uri,startLineNumber:a,startColumn:d,endLineNumber:p,endColumn:f,message:U(u.messageText,`
`)})}),l}_tsDiagnosticCategoryToMarkerSeverity(t){switch(t){case 1:return s.MarkerSeverity.Error;case 3:return s.MarkerSeverity.Info;case 0:return s.MarkerSeverity.Warning;case 2:return s.MarkerSeverity.Hint}return s.MarkerSeverity.Info}},C=class n extends k{get triggerCharacters(){return["."]}async provideCompletionItems(e,t,i,l){let u=e.getWordUntilPosition(t),c=new s.Range(t.lineNumber,u.startColumn,t.lineNumber,u.endColumn),g=e.uri,o=e.getOffsetAt(t),a=await this._worker(g);if(e.isDisposed())return;let d=await a.getCompletionsAtPosition(g.toString(),o);return!d||e.isDisposed()?void 0:{suggestions:d.entries.map(f=>{let b=c;if(f.replacementSpan){let W=e.getPositionAt(f.replacementSpan.start),w=e.getPositionAt(f.replacementSpan.start+f.replacementSpan.length);b=new s.Range(W.lineNumber,W.column,w.lineNumber,w.column)}let y=[];return f.kindModifiers!==void 0&&f.kindModifiers.indexOf("deprecated")!==-1&&y.push(s.languages.CompletionItemTag.Deprecated),{uri:g,position:t,offset:o,range:b,label:f.name,insertText:f.name,sortText:f.sortText,kind:n.convertKind(f.kind),tags:y}})}}async resolveCompletionItem(e,t){let i=e,l=i.uri,u=i.position,c=i.offset,o=await(await this._worker(l)).getCompletionEntryDetails(l.toString(),c,i.label);return o?{uri:l,position:u,label:o.name,kind:n.convertKind(o.kind),detail:S(o.displayParts),documentation:{value:n.createDocumentationString(o)}}:i}static convertKind(e){switch(e){case m.primitiveType:case m.keyword:return s.languages.CompletionItemKind.Keyword;case m.variable:case m.localVariable:return s.languages.CompletionItemKind.Variable;case m.memberVariable:case m.memberGetAccessor:case m.memberSetAccessor:return s.languages.CompletionItemKind.Field;case m.function:case m.memberFunction:case m.constructSignature:case m.callSignature:case m.indexSignature:return s.languages.CompletionItemKind.Function;case m.enum:return s.languages.CompletionItemKind.Enum;case m.module:return s.languages.CompletionItemKind.Module;case m.class:return s.languages.CompletionItemKind.Class;case m.interface:return s.languages.CompletionItemKind.Interface;case m.warning:return s.languages.CompletionItemKind.File}return s.languages.CompletionItemKind.Property}static createDocumentationString(e){let t=S(e.documentation);if(e.tags)for(let i of e.tags)t+=`

${Q(i)}`;return t}};function Q(n){let e=`*@${n.name}*`;if(n.name==="param"&&n.text){let[t,...i]=n.text;e+=`\`${t.text}\``,i.length>0&&(e+=` \u2014 ${i.map(l=>l.text).join(" ")}`)}else Array.isArray(n.text)?e+=` \u2014 ${n.text.map(t=>t.text).join(" ")}`:n.text&&(e+=` \u2014 ${n.text}`);return e}var I=class n extends k{constructor(){super(...arguments);this.signatureHelpTriggerCharacters=["(",","]}static _toSignatureHelpTriggerReason(t){switch(t.triggerKind){case s.languages.SignatureHelpTriggerKind.TriggerCharacter:return t.triggerCharacter?t.isRetrigger?{kind:"retrigger",triggerCharacter:t.triggerCharacter}:{kind:"characterTyped",triggerCharacter:t.triggerCharacter}:{kind:"invoked"};case s.languages.SignatureHelpTriggerKind.ContentChange:return t.isRetrigger?{kind:"retrigger"}:{kind:"invoked"};case s.languages.SignatureHelpTriggerKind.Invoke:default:return{kind:"invoked"}}}async provideSignatureHelp(t,i,l,u){let c=t.uri,g=t.getOffsetAt(i),o=await this._worker(c);if(t.isDisposed())return;let a=await o.getSignatureHelpItems(c.toString(),g,{triggerReason:n._toSignatureHelpTriggerReason(u)});if(!a||t.isDisposed())return;let d={activeSignature:a.selectedItemIndex,activeParameter:a.argumentIndex,signatures:[]};return a.items.forEach(p=>{let f={label:"",parameters:[]};f.documentation={value:S(p.documentation)},f.label+=S(p.prefixDisplayParts),p.parameters.forEach((b,y,W)=>{let w=S(b.displayParts),Z={label:w,documentation:{value:S(b.documentation)}};f.label+=w,f.parameters.push(Z),y<W.length-1&&(f.label+=S(p.separatorDisplayParts))}),f.label+=S(p.suffixDisplayParts),d.signatures.push(f)}),{value:d,dispose(){}}}},P=class extends k{async provideHover(e,t,i){let l=e.uri,u=e.getOffsetAt(t),c=await this._worker(l);if(e.isDisposed())return;let g=await c.getQuickInfoAtPosition(l.toString(),u);if(!g||e.isDisposed())return;let o=S(g.documentation),a=g.tags?g.tags.map(p=>Q(p)).join(`  

`):"",d=S(g.displayParts);return{range:this._textSpanToRange(e,g.textSpan),contents:[{value:"```typescript\n"+d+"\n```\n"},{value:o+(a?`

`+a:"")}]}}},D=class extends k{async provideDocumentHighlights(e,t,i){let l=e.uri,u=e.getOffsetAt(t),c=await this._worker(l);if(e.isDisposed())return;let g=await c.getDocumentHighlights(l.toString(),u,[l.toString()]);if(!(!g||e.isDisposed()))return g.flatMap(o=>o.highlightSpans.map(a=>({range:this._textSpanToRange(e,a.textSpan),kind:a.kind==="writtenReference"?s.languages.DocumentHighlightKind.Write:s.languages.DocumentHighlightKind.Text})))}},F=class extends k{constructor(t,i){super(i);this._libFiles=t}async provideDefinition(t,i,l){let u=t.uri,c=t.getOffsetAt(i),g=await this._worker(u);if(t.isDisposed())return;let o=await g.getDefinitionAtPosition(u.toString(),c);if(!o||t.isDisposed()||(await this._libFiles.fetchLibFilesIfNecessary(o.map(d=>s.Uri.parse(d.fileName))),t.isDisposed()))return;let a=[];for(let d of o){let p=this._libFiles.getOrCreateModel(d.fileName);p&&a.push({uri:p.uri,range:this._textSpanToRange(p,d.textSpan)})}return a}},L=class extends k{constructor(t,i){super(i);this._libFiles=t}async provideReferences(t,i,l,u){let c=t.uri,g=t.getOffsetAt(i),o=await this._worker(c);if(t.isDisposed())return;let a=await o.getReferencesAtPosition(c.toString(),g);if(!a||t.isDisposed()||(await this._libFiles.fetchLibFilesIfNecessary(a.map(p=>s.Uri.parse(p.fileName))),t.isDisposed()))return;let d=[];for(let p of a){let f=this._libFiles.getOrCreateModel(p.fileName);f&&d.push({uri:f.uri,range:this._textSpanToRange(f,p.textSpan)})}return d}},M=class extends k{async provideDocumentSymbols(e,t){let i=e.uri,l=await this._worker(i);if(e.isDisposed())return;let u=await l.getNavigationTree(i.toString());if(!u||e.isDisposed())return;let c=(o,a)=>({name:o.text,detail:"",kind:h[o.kind]||s.languages.SymbolKind.Variable,range:this._textSpanToRange(e,o.spans[0]),selectionRange:this._textSpanToRange(e,o.spans[0]),tags:[],children:o.childItems?.map(p=>c(p,o.text)),containerName:a});return u.childItems?u.childItems.map(o=>c(o)):[]}},m=class{static{this.unknown=""}static{this.keyword="keyword"}static{this.script="script"}static{this.module="module"}static{this.class="class"}static{this.interface="interface"}static{this.type="type"}static{this.enum="enum"}static{this.variable="var"}static{this.localVariable="local var"}static{this.function="function"}static{this.localFunction="local function"}static{this.memberFunction="method"}static{this.memberGetAccessor="getter"}static{this.memberSetAccessor="setter"}static{this.memberVariable="property"}static{this.constructorImplementation="constructor"}static{this.callSignature="call"}static{this.indexSignature="index"}static{this.constructSignature="construct"}static{this.parameter="parameter"}static{this.typeParameter="type parameter"}static{this.primitiveType="primitive type"}static{this.label="label"}static{this.alias="alias"}static{this.const="const"}static{this.let="let"}static{this.warning="warning"}},h=Object.create(null);h[m.module]=s.languages.SymbolKind.Module;h[m.class]=s.languages.SymbolKind.Class;h[m.enum]=s.languages.SymbolKind.Enum;h[m.interface]=s.languages.SymbolKind.Interface;h[m.memberFunction]=s.languages.SymbolKind.Method;h[m.memberVariable]=s.languages.SymbolKind.Property;h[m.memberGetAccessor]=s.languages.SymbolKind.Property;h[m.memberSetAccessor]=s.languages.SymbolKind.Property;h[m.variable]=s.languages.SymbolKind.Variable;h[m.const]=s.languages.SymbolKind.Variable;h[m.localVariable]=s.languages.SymbolKind.Variable;h[m.variable]=s.languages.SymbolKind.Variable;h[m.function]=s.languages.SymbolKind.Function;h[m.localFunction]=s.languages.SymbolKind.Function;var x=class extends k{static _convertOptions(e){return{ConvertTabsToSpaces:e.insertSpaces,TabSize:e.tabSize,IndentSize:e.tabSize,IndentStyle:2,NewLineCharacter:`
`,InsertSpaceAfterCommaDelimiter:!0,InsertSpaceAfterSemicolonInForStatements:!0,InsertSpaceBeforeAndAfterBinaryOperators:!0,InsertSpaceAfterKeywordsInControlFlowStatements:!0,InsertSpaceAfterFunctionKeywordForAnonymousFunctions:!0,InsertSpaceAfterOpeningAndBeforeClosingNonemptyParenthesis:!1,InsertSpaceAfterOpeningAndBeforeClosingNonemptyBrackets:!1,InsertSpaceAfterOpeningAndBeforeClosingTemplateStringBraces:!1,PlaceOpenBraceOnNewLineForControlBlocks:!1,PlaceOpenBraceOnNewLineForFunctions:!1}}_convertTextChanges(e,t){return{text:t.newText,range:this._textSpanToRange(e,t.span)}}},A=class extends x{constructor(){super(...arguments);this.canFormatMultipleRanges=!1}async provideDocumentRangeFormattingEdits(t,i,l,u){let c=t.uri,g=t.getOffsetAt({lineNumber:i.startLineNumber,column:i.startColumn}),o=t.getOffsetAt({lineNumber:i.endLineNumber,column:i.endColumn}),a=await this._worker(c);if(t.isDisposed())return;let d=await a.getFormattingEditsForRange(c.toString(),g,o,x._convertOptions(l));if(!(!d||t.isDisposed()))return d.map(p=>this._convertTextChanges(t,p))}},R=class extends x{get autoFormatTriggerCharacters(){return[";","}",`
`]}async provideOnTypeFormattingEdits(e,t,i,l,u){let c=e.uri,g=e.getOffsetAt(t),o=await this._worker(c);if(e.isDisposed())return;let a=await o.getFormattingEditsAfterKeystroke(c.toString(),g,i,x._convertOptions(l));if(!(!a||e.isDisposed()))return a.map(d=>this._convertTextChanges(e,d))}},O=class extends x{async provideCodeActions(e,t,i,l){let u=e.uri,c=e.getOffsetAt({lineNumber:t.startLineNumber,column:t.startColumn}),g=e.getOffsetAt({lineNumber:t.endLineNumber,column:t.endColumn}),o=x._convertOptions(e.getOptions()),a=i.markers.filter(b=>b.code).map(b=>b.code).map(Number),d=await this._worker(u);if(e.isDisposed())return;let p=await d.getCodeFixesAtPosition(u.toString(),c,g,a,o);return!p||e.isDisposed()?{actions:[],dispose:()=>{}}:{actions:p.filter(b=>b.changes.filter(y=>y.isNewFile).length===0).map(b=>this._tsCodeFixActionToMonacoCodeAction(e,i,b)),dispose:()=>{}}}_tsCodeFixActionToMonacoCodeAction(e,t,i){let l=[];for(let c of i.changes)for(let g of c.textChanges)l.push({resource:e.uri,versionId:void 0,textEdit:{range:this._textSpanToRange(e,g.span),text:g.newText}});return{title:i.description,edit:{edits:l},diagnostics:t.markers,kind:"quickfix"}}},E=class extends k{constructor(t,i){super(i);this._libFiles=t}async provideRenameEdits(t,i,l,u){let c=t.uri,g=c.toString(),o=t.getOffsetAt(i),a=await this._worker(c);if(t.isDisposed())return;let d=await a.getRenameInfo(g,o,{allowRenameOfImportPath:!1});if(d.canRename===!1)return{edits:[],rejectReason:d.localizedErrorMessage};if(d.fileToRename!==void 0)throw new Error("Renaming files is not supported.");let p=await a.findRenameLocations(g,o,!1,!1,!1);if(!p||t.isDisposed())return;let f=[];for(let b of p){let y=this._libFiles.getOrCreateModel(b.fileName);if(y)f.push({resource:y.uri,versionId:void 0,textEdit:{range:this._textSpanToRange(y,b.textSpan),text:l}});else throw new Error(`Unknown file ${b.fileName}.`)}return{edits:f}}},N=class extends k{async provideInlayHints(e,t,i){let l=e.uri,u=l.toString(),c=e.getOffsetAt({lineNumber:t.startLineNumber,column:t.startColumn}),g=e.getOffsetAt({lineNumber:t.endLineNumber,column:t.endColumn}),o=await this._worker(l);return e.isDisposed()?null:{hints:(await o.provideInlayHints(u,c,g)).map(p=>({...p,label:p.text,position:e.getPositionAt(p.position),kind:this._convertHintKind(p.kind)})),dispose:()=>{}}}_convertHintKind(e){switch(e){case"Parameter":return s.languages.InlayHintKind.Parameter;case"Type":return s.languages.InlayHintKind.Type;default:return s.languages.InlayHintKind.Type}}};var V,j;function ce(n){j=X(n,"typescript")}function ge(n){V=X(n,"javascript")}function pe(){return new Promise((n,e)=>{if(!V)return e("JavaScript not registered!");n(V)})}function de(){return new Promise((n,e)=>{if(!j)return e("TypeScript not registered!");n(j)})}function X(n,e){let t=[],i=[],l=new v(e,n);t.push(l);let u=(...o)=>l.getLanguageServiceWorker(...o),c=new _(u);function g(){let{modeConfiguration:o}=n;Y(i),o.completionItems&&i.push(s.languages.registerCompletionItemProvider(e,new C(u))),o.signatureHelp&&i.push(s.languages.registerSignatureHelpProvider(e,new I(u))),o.hovers&&i.push(s.languages.registerHoverProvider(e,new P(u))),o.documentHighlights&&i.push(s.languages.registerDocumentHighlightProvider(e,new D(u))),o.definitions&&i.push(s.languages.registerDefinitionProvider(e,new F(c,u))),o.references&&i.push(s.languages.registerReferenceProvider(e,new L(c,u))),o.documentSymbols&&i.push(s.languages.registerDocumentSymbolProvider(e,new M(u))),o.rename&&i.push(s.languages.registerRenameProvider(e,new E(c,u))),o.documentRangeFormattingEdits&&i.push(s.languages.registerDocumentRangeFormattingEditProvider(e,new A(u))),o.onTypeFormattingEdits&&i.push(s.languages.registerOnTypeFormattingEditProvider(e,new R(u))),o.codeActions&&i.push(s.languages.registerCodeActionProvider(e,new O(u))),o.inlayHints&&i.push(s.languages.registerInlayHintsProvider(e,new N(u))),o.diagnostics&&i.push(new T(c,n,e,u))}return g(),t.push(fe(i)),u}function fe(n){return{dispose:()=>Y(n)}}function Y(n){for(;n.length;)n.pop().dispose()}return ae(me);})();
return moduleExports;
});
