
def more_version_specific_code():
    print("More version 2")


def generic_code():
    print("Hello World!")
    print("Even more code.")


def version_specific_code():
    print("I am version 2")
    print("Change specific to version 2")


def main():
    generic_code()
    version_specific_code()
    more_version_specific_code()


if __name__ == "__main__":
    main()
