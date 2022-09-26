import sys


module_path = 'C:\\Users\\André\\Code\\design-patterns\\src\\patterns'

if module_path not in sys.path:
    sys.path.append(module_path)


print("Path:")
print(sys.path)