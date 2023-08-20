#!/usr/bin/node
const dict = require('./101-data').dict;

const totalList = Object.entries(dict);
const values = Object.values(dict);
const uniqueValues = [...new Set(values)];
const newDict = {};
for (const i in uniqueValues) {
  const list = [];
  for (const j in totalList) {
    if (totalList[j][1] === uniqueValues[i]) {
      list.unshift(totalList[j][0]);
    }
  }
  newDict[uniqueValues[i]] = list;
}
console.log(newDict);
