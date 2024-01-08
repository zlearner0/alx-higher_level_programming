#!/usr/bin/node

exports.callMeMoby = function (j, theFunction) {
  for (let i = 0; i < j; i++) theFunction();
};
