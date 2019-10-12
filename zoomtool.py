import sys
from util import main

if len(sys.argv) < 2:
    print("No verb supplied")
else:
    verb = sys.argv[1]
    main(verb)
