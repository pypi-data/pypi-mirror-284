import argparse

def add(x=3, y=4):
    return x + y



def add_main():
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()

    result = add(args.a, args.b)
    print(f"The result of {args.a} + {args.b} is {result}")