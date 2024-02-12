#!/usr/bin/node
function secondBiggest (arr) {
  if (arr.length <= 1) return 0;
  let first = Number.MIN_SAFE_INTEGER;
  let second = 0;
  for (const i of arr) {
    if (i > first) {
      second = first;
      first = i;
    } else if (i > second) second = i;
  }
  return second;
}

const arr = process.argv.slice(2).map((i) => parseInt(i));
console.log(secondBiggest(arr));
