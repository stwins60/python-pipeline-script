import argparse
import random

def generate_lottery_numbers():
    # Generate 6 unique random numbers between 1 and 49 for the lottery
    numbers = random.sample(range(1, 50), 6)
    return sorted(numbers)

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="A script that greets you and optionally generates lottery numbers.")

    # Add a positional argument
    parser.add_argument("name", type=str, help="Your name")

    # Add an optional argument with a default value
    parser.add_argument("--age", type=int, default=25, help="Your age (default: 25)")

    # Add a flag for generating lottery numbers
    parser.add_argument("--lottery", action="store_true", help="Generate lottery numbers")

    # Parse the arguments
    args = parser.parse_args()

    # Access the arguments
    name = args.name
    age = args.age

    # Output a greeting
    print(f"Hello, {name}! You are {age} years old.")

    # Generate and print lottery numbers if the flag is set
    if args.lottery:
        lottery_numbers = generate_lottery_numbers()
        print("Your lottery numbers are:", lottery_numbers)

if __name__ == "__main__":
    main()
