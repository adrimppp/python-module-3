import sys

arg_num = len(sys.argv)
print("=== Command Quest ===")
i = 1
if arg_num > 1:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {arg_num - 1}")
    while i < arg_num:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
else:
    print(f"No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
print(f"Total arguments: {arg_num}")

