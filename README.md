Experiments using the Web Assembly toolchain.

Compile c to wat/wasm [WasmFiddle](https://wasdk.github.io/WasmFiddle/).

Install emsdk, wabt, pywasm, and node.

Compile and run 
```
% cat add.c
int add(int a, int b) {
    return a + b;
}

% emcc -Os -s EXPORTED_FUNCTIONS="['_add']" -o add.wasm add.c
% wasm2wat hello.wasm
(module
  (type (;0;) (func (param i32 i32) (result i32)))
  (func (;0;) (type 0) (param i32 i32) (result i32)
    local.get 0
    local.get 1
    i32.add)
  (export "_add" (func 0)))

% python wasm.py add.wasm _add 10 20
```
Note that emcc changes the name "add" to "_add".

Run it using node.

```
% cat add.js
const fs = require('fs');
const buf = fs.readFileSync('./add.wasm');

WebAssembly.instantiate(buf, {
}).then(result => {
    console.log(result.instance.exports._add(2,2));
}).catch( e => {
    console.log(e);
});
% node add.js
4
```

