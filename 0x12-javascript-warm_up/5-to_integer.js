#!/usr/bin/node
let ans = parseInt(process.argv[2]);
if (!ans) ans = 'Not a number';
else ans = `My number: ${ans}`;
console.log(ans);
