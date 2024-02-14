#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const newList = list.map((number, index) => number * index);
console.log(newList);
