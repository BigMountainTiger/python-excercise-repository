var fs = require('fs'),
path = require('path'),    
filePath = path.join(__dirname, 'primes.txt');

console.log(filePath)
fs.readFile(filePath, {encoding: 'utf-8'}, function(e, d){
  if (e) { console.log(e); return; }

  let i = 0;
  const rows = d.split('\n');
  const result_rows = [];
  rows.forEach(row => {
    const items = row.replace(/ +(?= )/g,'').trim().replace(/ /g, ', ');
    result_rows.push(items)
  });

  const result = result_rows.join(',\n');

  console.log(result);
});