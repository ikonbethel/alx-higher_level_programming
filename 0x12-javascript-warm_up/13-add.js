#!/usr/bin/node
// Print Javascript is amazing

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return parseInt(a, 10) + parseInt(b, 10);
}

module.exports = {
  add
};
