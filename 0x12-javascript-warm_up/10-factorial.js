#!/usr/bin/node
function fact (x) {
  if (!x) return 1;
  return x * fact(x - 1);
}

console.log(fact(parseInt(process.argv[2])));
