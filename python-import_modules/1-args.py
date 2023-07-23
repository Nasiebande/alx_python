import sys

# Get the number of arguments passed (excluding the script name itself)
num_arguments = len(sys.argv) - 1

# Print the number of arguments
print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}:", end=' ')

# Print the list of arguments
if num_arguments == 0:
    print(".", end='')
else:
    print()

    # Print each argument with its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

# Print a new line
print()