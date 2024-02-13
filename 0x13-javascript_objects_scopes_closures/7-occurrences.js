#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  for (const e of list) {
    if (e === searchElement) cnt += 1;
  }
  return cnt;
};
