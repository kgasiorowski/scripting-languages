# Kuba Gasiorowski
# 109776237
# kgasiorowski
#
# CSE 337 (Fall 2019)
# Unit Homework 1

import re

def count_failed_addresses(logname):

    ip_dict = {}
    ip_regex_pattern = r'Disconnected from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    regex = re.compile(ip_regex_pattern)

    with open(logname) as input_file:
        for line in input_file:
            result = regex.search(line)

            if result is not None:
                ip = result.group(1)
                ip_dict.setdefault(ip, 0)
                ip_dict[ip] += 1

    return ip_dict


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("test-log-1.txt produced the dictionary:")
    print(count_failed_addresses("test-log-1.txt"))
    print()

    print("test-log-2.txt produced the dictionary:")
    print(count_failed_addresses("test-log-2.txt"))
    print()

    print("test-log-3.txt produced the dictionary:")
    print(count_failed_addresses("test-log-3.txt"))
    print()

    print("test-log-4.txt produced the dictionary:")
    print(count_failed_addresses("test-log-4.txt"))
    print()

    print("auth.log.1 produced the dictionary:")
    print(count_failed_addresses("auth.log.1"))
    print()

    print("auth.log.2 produced the dictionary:")
    print(count_failed_addresses("auth.log.2"))
    print()

    print("auth.log.3 produced the dictionary:")
    print(count_failed_addresses("auth.log.3"))
    print()

    print("auth.log.4 produced the dictionary:")
    print(count_failed_addresses("auth.log.4"))
    print()
