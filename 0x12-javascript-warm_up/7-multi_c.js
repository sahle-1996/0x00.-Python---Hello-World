#!/usr/bin/node

const n = parseInt(process.argv[2]);
if (Number.isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  Array.from({ length: n }).forEach(() => console.log('C is fun'));
}
