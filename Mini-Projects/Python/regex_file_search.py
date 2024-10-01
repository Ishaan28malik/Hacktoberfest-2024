#! python3

import re
import pprint
import argparse
import textwrap
from Typing import List


def find_match(file: str, pattern: str) => List[str]:
    """
    searches through every line in a given file, and returns the lines that match the regex
    
    file: str, location of the file to search through
    pattern: str, regex to match to
    
    out: List[str], a list containing all lines where regex matched
    """
    out = []
    ptrn = re.compile(pattern)
    with open(file) as f:
        for line in f.readlines():
            if ptrn.search(line):
                out.append(line.strip())
    return out


if __name__ == "__main__":
    re_eli5 = textwrap.dedent("""
    -------------------
    
    Building a pattern:
    
    Any letter/number -> matches itself
    ^ -> matches start of the line
    $ -> matches end of the line
    . -> matches one of any character
    \d -> matches any digit
    \D -> mathes anything that is not a digit
    \s -> matches any whitespace
    ( ) -> used to group things together
    [ ] -> matches one of the items inside
    + -> matches one or more of the previous thing
    * -> matches zero or more of the previous thing
    ? -> matches zero or one of the previous things
    | -> matches either the left or the right thing
    \ -> used to "escape" a special character and match it literally (one of the ".^$()[]+*?|" for example)
    """)
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=f"Find all lines in a file that mathch given criteria", epilog=re_eli5)
    parser.add_argument("pattern", help=f"Regular Expression to match the text.")
    parser.add_argument("file", help="File with the list of words to match.", metavar="in_file")
    parser.add_argument("--out", "-o", help="Optional output file, will print on screen if not given", default=None,
                        metavar="out_file")
    args = parser.parse_args()

    result = find_match(args.file, args.pattern)
    if args.out is not None:
        with open(args.out, "w") as o:
            for match in result:
                print(match, file=o)
        print("Done!")
    else:
        pprint.pprint(result)
