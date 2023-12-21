"use strict";
// Example of generics 
const score = [];
const names = [];
// generics are already provided by ts 
function indentityOne(val) {
    return val;
}
// we do not know what type of data woud be return 
// like nothing is fix
function indentityTwo(val) {
    return val;
}
// here if Type if string string would be returned and same in case of other Types 
function identityThree(val) {
    return val;
}
// generic usage in different type here we know if the val is string the return value automatically becomes string
identityThree(3);
identityThree("a");
// shortcut 
function identityThree2(val) {
    return val;
}
// if user custom made type or interface use the follwing syntax
identityThree2({});
