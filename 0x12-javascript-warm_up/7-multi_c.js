#!/usr/bin/node
const myvar = Math.floor(process.argv[2])
if (isNaN(myvar)) {
	console.log('Missing number of occurrences');}
else {for (let i=0;i<myvar;i++){
	console.log('C is fun')}
}

