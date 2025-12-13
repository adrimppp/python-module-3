import sys

arg_num = len(sys.argv)
print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
i = 1
if(arg_num > 1):
    print(f"Arguments received: {arg_num}")
    while (i < arg_num):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
print(f"Total arguments: {arg_num}")
