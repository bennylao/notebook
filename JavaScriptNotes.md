# JavaScript

## CLI

`npm` is a package manager for Node.js packages

To install a package
```terminal
npm install package
```

To uninstall a package
```terminal
npm uninstall package
```

To list all installed packages
```terminal
npm list
npm ls
```

## Basics

To make variables accessible from other modules, use `module.exports.var`
```javascript
module.exports.name = 'James';
module.exports.age = '18';
```

To access variables from other modules, use `require("targetModule")`

```javascript
var myModule = require('./myModule');
var myNname = myModule.name;
```

To use the function of the installed package
```javascript
var myModule = require('myPackage').myModule;
myModule.myFunction();
```

```javascript
// define a global variable
var myVar = 100;

if (True) {
let innerVar = 100;
    console.log(innerVar);
}
console.long(innerVar); // innerVar is not defined
```

`var` can be dupated and re-declared
`let` can be updated but not re-declared
`const` object itself cannot be updated, but its properties can be updated


## Examples

Traditional JavaScript
```javascript
const app = document.getElementById("app");
const header = document.createElement("h1");

const text = "MSc CS";
const headerContent = document.createTextNode(text);

header.appendChild(headerContent);

app.appendChild(header);
```

