def largest_contiguous_subarray(arr):
    curr_max, sum_to_here = 0, 0
    for num in arr:
        sum_to_here = max(sum_to_here+num, 0)
        curr_max = max(curr_max, sum_to_here)
    return curr_max

"""Module docstring.

This serves as a long usage message.
"""
import sys
import getopt

def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    input_array = []
    for arg in args:
        input_array.append(int(arg))
    print("Input array: {0}".format(input_array))
    print("Largest contiguous sum: {0}".format(largest_contiguous_subarray(input_array)))

if __name__ == "__main__":
    main()