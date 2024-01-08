#!/usr/bin/node
function factorial (fc) {
  return fc === 0 || isNaN(fc) ? 1 : fc * factorial(fc - 1);
}

console.log(factorial(Number(process.argv[2])));
