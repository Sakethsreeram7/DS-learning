import argparse

parser = argparse.ArgumentParser(description="My first argparse app")
parser.add_argument("name", help="Your name")
args = parser.parse_args()

print(args.name)