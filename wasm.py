import sys
import pywasm
# pywasm.on_debug()

vm = pywasm.load(sys.argv[1])
name = sys.argv[2]
args = [int(arg) for arg in sys.argv[3:]]
r = vm.exec(name, args)
print(r) 
