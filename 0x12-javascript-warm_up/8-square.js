#!/usr/bin/node

const arg = process.argv[2];
const num = Number(arg);

if (isNaN(num))
console.log('Missing size');
else
{
for (let i = 0; i < num; i++)
{
let str  = 'x'.repeat(num);
console.log(str);
}
}
