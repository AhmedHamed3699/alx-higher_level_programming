#!/usr/bin/node
exports.converter = function (base) {
  const digits = '0123456789abcdef';
  return function (number) {
    let ans = '';
    while (number) {
      ans = digits[number % base].toString() + ans;
      number = parseInt(number / base);
    }
    return ans;
  };
};
