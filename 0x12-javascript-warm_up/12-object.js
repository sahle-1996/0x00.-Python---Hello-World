#!/usr/bin/node

const item = {
  kind: 'object',
  quantity: 12
};
console.log(item);

item['quantity'] = 89;

console.log(item);
