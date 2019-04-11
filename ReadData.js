var fs = require("fs");
console.log("\n *START* \n");
var content = fs.readFileSync('data.json', 'utf8');
var sensorData = JSON.parse(content);
console.log(sensorData)
console.log("\n *EXIT* \n");