# Kuba Gasiorowski
# 109776237
# kgasiorowski
#
# CSE 337 (Fall 2019)
# Unit Homework 1
from count_failed_addresses import count_failed_addresses


def consolidate_sources(logname):

    consolidated_addr = {}
    failed_addr = count_failed_addresses(logname)

    for addr, count in failed_addr.items():

        new_addr = addr[:addr.rfind('.')]
        consolidated_addr.setdefault(new_addr, 0)
        consolidated_addr[new_addr] += count

    return consolidated_addr


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("test-log-1.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-1.txt"))
    print()

    print("test-log-2.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-2.txt"))
    print()

    print("test-log-3.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-3.txt"))
    print()

    print("test-log-4.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-4.txt"))
    print()

