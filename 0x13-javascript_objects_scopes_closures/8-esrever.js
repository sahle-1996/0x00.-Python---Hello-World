#!/usr/bin/node

module.exports.esrever = function (list) {
  return list.reduce((array, current) => {
    array.unshift(current);
    return array;
  }, []);
};
