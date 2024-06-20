#!/usr/bin/node

module.exports.nbOccurences = function (list, searchElement) {
  return list.filter(element => element === searchElement).length;
};
