# Kuba Gasiorowski
# 109776237
# kgasiorowski
#
# CSE 337 (Fall 2019)
# Unit Homework 1

from highest_value_key import highest_value_key
from consolidate_sources import consolidate_sources


def most_frequent_attacker(addresses):

    return highest_value_key(consolidate_sources(addresses))


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("test-log-1.txt produced the dictionary:")
    print(most_frequent_attacker("test-log-1.txt"))
    print()

    print("test-log-2.txt produced the dictionary:")
    print(most_frequent_attacker("test-log-2.txt"))
    print()

    print("test-log-3.txt produced the dictionary:")
    print(most_frequent_attacker("test-log-3.txt"))
    print()

    print("test-log-4.txt produced the dictionary:")
    print(most_frequent_attacker("test-log-4.txt"))
    print()

    print("auth.log.1 produced the dictionary:")
    print(most_frequent_attacker("auth.log.1"))
    print()

    print("auth.log.2 produced the dictionary:")
    print(most_frequent_attacker("auth.log.2"))
    print()

    print("auth.log.3 produced the dictionary:")
    print(most_frequent_attacker("auth.log.3"))
    print()

    print("auth.log.4 produced the dictionary:")
    print(most_frequent_attacker("auth.log.4"))
    print()


