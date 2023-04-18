#!/usr/bin/node
// Convert a argument to an int

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2).sort(function (a, b) { return b - a; });
  console.log(list[1]);
}
