// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		
		let nums = line.split(' ').map(Number).reduce((acc, cur) => acc + cur).toFixed(7);
		nums = nums.substring(0, nums.length-1);
		
		console.log(nums);
		
		rl.close();
	}
	
	process.exit();
})();
