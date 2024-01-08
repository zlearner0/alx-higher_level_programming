#!/usr/bin/node

function factorial (f) {
  if ((isNaN(f)) || (f === 1)) {
    return 1;
  } else {
    return f * factorial(f - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
