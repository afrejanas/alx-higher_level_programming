#!/usr/bin/python2
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("{:d}".format(argc - 1))
    else:
        i = 1
        sum = 0
        while i < argc:
            sum += int(sys.argv[i])
            i = i + 1
        print('{:d}'.format(sum))
