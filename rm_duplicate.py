import argparse
import fileinput

def remove_duplicates(lines):
    """
    Remove duplicate lines from a list of strings.
    """
    seen = set()
    return [x for x in lines if not (x in seen or seen.add(x))]

def main():
    """
    Main function.
    """
    parser = argparse.ArgumentParser(description="Remove duplicate lines from a file.")
    parser.add_argument("-f", "--file", type=str, nargs="+", help="Path to the input file(s)")
    args = parser.parse_args()

    total_lines = 0
    duplicate_lines = 0
    unique_lines = 0

    for file_path in args.file:
        with open(file_path, "r") as f:
            lines = list(f.readlines())

        total_lines += len(lines)
        lines = remove_duplicates(lines)
        unique_lines += len(lines)
        duplicate_lines += total_lines - unique_lines

        with open(f"dups{file_path}", "w") as f:
            f.writelines(lines)

    print(f"Total lines: {total_lines}")
    print(f"Duplicate lines: {duplicate_lines}")
    print(f"Unique lines: {unique_lines}")

if __name__ == "__main__":
    main()