#!/usr/bin/node
const argSize = Number(process.argv[2]);

if (Number(argSize)) {
  for (let i = 0; i < argSize; i++)
    console.log('X'.repeat(argSize));
} else {
  console.log('Missing size');
}
