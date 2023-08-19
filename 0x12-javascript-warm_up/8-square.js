#!/usr/bin/node
const argSize = Number(process.argv[2]);

console.log(argSize ? 'X'.repeat(argSize) : 'Missing size');
