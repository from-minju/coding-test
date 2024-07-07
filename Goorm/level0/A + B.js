// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		
		let numbers = line.split(' ').map(Number).reduce((acc,cur) => acc + cur);
		console.log(numbers)
		
		rl.close();
	}
	
	process.exit();
})();
