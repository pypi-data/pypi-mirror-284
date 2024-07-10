/*!-----------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Version: 0.50.0(c321d0fbecb50ab8a5365fa1965476b0ae63fc87)
 * Released under the MIT license
 * https://github.com/microsoft/monaco-editor/blob/main/LICENSE.txt
 *-----------------------------------------------------------------------------*/
define("vs/basic-languages/sparql/sparql", ["require","require"],(require)=>{
"use strict";var moduleExports=(()=>{var o=Object.defineProperty;var i=Object.getOwnPropertyDescriptor;var a=Object.getOwnPropertyNames;var l=Object.prototype.hasOwnProperty;var d=(s,e)=>{for(var n in e)o(s,n,{get:e[n],enumerable:!0})},c=(s,e,n,r)=>{if(e&&typeof e=="object"||typeof e=="function")for(let t of a(e))!l.call(s,t)&&t!==n&&o(s,t,{get:()=>e[t],enumerable:!(r=i(e,t))||r.enumerable});return s};var g=s=>c(o({},"__esModule",{value:!0}),s);var m={};d(m,{conf:()=>u,language:()=>p});var u={comments:{lineComment:"#"},brackets:[["{","}"],["[","]"],["(",")"]],autoClosingPairs:[{open:"'",close:"'",notIn:["string"]},{open:'"',close:'"',notIn:["string"]},{open:"{",close:"}"},{open:"[",close:"]"},{open:"(",close:")"}]},p={defaultToken:"",tokenPostfix:".rq",brackets:[{token:"delimiter.curly",open:"{",close:"}"},{token:"delimiter.parenthesis",open:"(",close:")"},{token:"delimiter.square",open:"[",close:"]"},{token:"delimiter.angle",open:"<",close:">"}],keywords:["add","as","asc","ask","base","by","clear","construct","copy","create","data","delete","desc","describe","distinct","drop","false","filter","from","graph","group","having","in","insert","limit","load","minus","move","named","not","offset","optional","order","prefix","reduced","select","service","silent","to","true","undef","union","using","values","where","with"],builtinFunctions:["a","abs","avg","bind","bnode","bound","ceil","coalesce","concat","contains","count","datatype","day","encode_for_uri","exists","floor","group_concat","hours","if","iri","isblank","isiri","isliteral","isnumeric","isuri","lang","langmatches","lcase","max","md5","min","minutes","month","now","rand","regex","replace","round","sameterm","sample","seconds","sha1","sha256","sha384","sha512","str","strafter","strbefore","strdt","strends","strlang","strlen","strstarts","struuid","substr","sum","timezone","tz","ucase","uri","uuid","year"],ignoreCase:!0,tokenizer:{root:[[/<[^\s\u00a0>]*>?/,"tag"],{include:"@strings"},[/#.*/,"comment"],[/[{}()\[\]]/,"@brackets"],[/[;,.]/,"delimiter"],[/[_\w\d]+:(\.(?=[\w_\-\\%])|[:\w_-]|\\[-\\_~.!$&'()*+,;=/?#@%]|%[a-f\d][a-f\d])*/,"tag"],[/:(\.(?=[\w_\-\\%])|[:\w_-]|\\[-\\_~.!$&'()*+,;=/?#@%]|%[a-f\d][a-f\d])+/,"tag"],[/[$?]?[_\w\d]+/,{cases:{"@keywords":{token:"keyword"},"@builtinFunctions":{token:"predefined.sql"},"@default":"identifier"}}],[/\^\^/,"operator.sql"],[/\^[*+\-<>=&|^\/!?]*/,"operator.sql"],[/[*+\-<>=&|\/!?]/,"operator.sql"],[/@[a-z\d\-]*/,"metatag.html"],[/\s+/,"white"]],strings:[[/'([^'\\]|\\.)*$/,"string.invalid"],[/'$/,"string.sql","@pop"],[/'/,"string.sql","@stringBody"],[/"([^"\\]|\\.)*$/,"string.invalid"],[/"$/,"string.sql","@pop"],[/"/,"string.sql","@dblStringBody"]],stringBody:[[/[^\\']+/,"string.sql"],[/\\./,"string.escape"],[/'/,"string.sql","@pop"]],dblStringBody:[[/[^\\"]+/,"string.sql"],[/\\./,"string.escape"],[/"/,"string.sql","@pop"]]}};return g(m);})();
return moduleExports;
});
