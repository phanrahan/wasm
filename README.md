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
% wasm2wat add.wasm
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

# compile c to assembly language
% riscv64-unknown-elf-gcc -march=rv32i -mabi=ilp32 -Og -S add.c
# assembler
% riscv64-unknown-elf-as add.s -o add.o
# disassembler
% riscv64-unknown-elf-objdump -d add.o
# convert elf to binary
% riscv64-unknown-elf-objcopy add.o -O binary add.bin
# disassemble binary file
% riscv64-unknown-elf-objdump -b binary -m riscv:rv32 -D add.bin
# hexdump
% xxd -g 1 add.bin > add.hex
# cool hack - convert hex file to a binary file
% xxd -g 1 -r add.hex add2.bin
% cmp add.bin add2.bin

Install

- wabt - web assembly binary toolkit
  - https://github.com/WebAssembly/wabt

- emscripten (emcc)
  - brew install emscripten
  - git/emsdk

- pywasm
  - https://github.com/mohanson/pywasm
  - pip install pywasm

- riscv tool chain
  - https://github.com/riscv/homebrew-riscv
  - https://github.com/riscv/riscv-gnu-toolchain
  - https://github.com/riscv/riscv-isa-sim
  - brew test riscv-tools
  - https://www.sifive.com/blog/all-aboard-part-1-compiler-args

