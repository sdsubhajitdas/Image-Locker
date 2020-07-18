from image_encryptor import core
from image_encryptor import DEBUG

from argparse import ArgumentParser
from getpass import getpass
import sys


def getArguments():
    parser = ArgumentParser(description="List of commands for Image Encryptor")
    parser.add_argument("-d", "--dir", type=str,
                        help="The directory path for group of images.")
    parser.add_argument("-f", "--file", type=str,
                        help="The path of the file to encrpt.")

    args = parser.parse_args()
    return parser, args


def main():
    parser, args = getArguments()

    if DEBUG:
        print(args)

    if(len(sys.argv) == 1):
        parser.print_help()
        sys.exit(0)

    password = getpass("Enter the password for the operation\nPassword:  ")
    if args.dir:
        core.encryptDirectory(args.dir, password)
    elif args.file:
        core.encryptSingleImage(args.file, password)
    else:
        print("Use -h flag to get help on how to use.")


if __name__ == "__main__":
    main()
