#!/usr/bin/node
// Convert a argument to an int

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2], 10));
}
