const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('index.html', 'utf8');
const scripts = html.match(/<script>([\s\S]*?)<\/script>/gi);

console.log(`Found ${scripts ? scripts.length : 0} script tags`);
if (scripts) {
  scripts.forEach((s, idx) => {
    const code = s.replace(/<\/?script>/gi, '');
    try {
      new vm.Script(code);
      console.log(`Script ${idx + 1}: Syntax VALID! (${code.length} chars)`);
    } catch (err) {
      console.error(`Script ${idx + 1}: SYNTAX ERROR:`, err);
      process.exit(1);
    }
  });
}
