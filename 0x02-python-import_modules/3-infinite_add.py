#!/usr/bin/python2
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print("{:d}".format(argc - 1))
    else:
        i = 1
        sum = 0
        while i < argc:
            sum += int(argv[i])
            i = i + 1
        print('{:d}'.format(sum))
