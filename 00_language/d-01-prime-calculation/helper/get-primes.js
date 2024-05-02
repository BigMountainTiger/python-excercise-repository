var fs = require('fs'),
path = require('path'),    
inputFile = path.join(__dirname, 'primes.txt');
outputFile = path.join(__dirname, 'primes_ouput.txt');

fs.readFile(inputFile, {encoding: 'utf-8'}, function(e, d){
  if (e) { console.log(e); return; }

  let i = 0;
  const rows = d.split('\n');
  const result_rows = [];
  rows.forEach(row => {
    const items = row.replace(/ +(?= )/g,'').trim().replace(/ /g, ', ');
    result_rows.push(items)
  });

  const result = result_rows.join(',\n');

  fs.writeFile(outputFile, result, (e) => {
    if (e) { console.log(e); return; }

    console.log('Done');
  });
});