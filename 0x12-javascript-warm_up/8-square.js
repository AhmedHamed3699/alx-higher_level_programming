#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (!x) console.log('Missing size');
else for (let i = 0; i < x; i++) console.log('X'.repeat(x));
