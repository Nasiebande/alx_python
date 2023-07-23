import sys

def main():
    # Get the number of arguments passed (excluding the script name itself)
    num_arguments = len(sys.argv) - 1

    # Print the number of arguments
    if num_arguments == 0:
        print("0 arguments.")
    else:
        print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}:")
        
        # Print each argument with its position
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()