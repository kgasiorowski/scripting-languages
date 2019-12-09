# Kuba Gasiorowski
# 109776237
# kgasiorowski
#
# CSE 337 (Fall 2019)
# Unit Homework 2

class Room:

    def __init__(self):

        self.id = None
        self.exits = None
        self.items = None
        self.puzzle = None

    def print(self):

        print('ID:', self.id)
        print('EXITS:', self.exits)
        print('ITEMS:', self.items)
        print('PUZZLE:', self.puzzle)

    @staticmethod
    def parse_file(filename):

        rooms = {}
        with open(filename) as fp:

            r = None

            for line in fp:

                line = line.strip()

                if line.startswith('ROOM'):
                    r = Room()
                    r.id = int(line.split()[1])
                elif line.startswith('DESC') or line.startswith('TITLE'):
                    continue
                elif line.startswith('EXITS'):
                    r.exits = [int(exit_num) for exit_num in line.split()[1:]]
                elif line.startswith('ITEMS'):
                    r.items = line.split()[1:]
                elif line.startswith('PUZZLE'):
                    r.puzzle = line[len('PUZZLE'):].strip()
                else:
                    rooms.setdefault(r.id, r)
                    r = None

            rooms.setdefault(r.id, r)

        return rooms


def recip(index):
    return (index + 2) % 4


def validate(filename):

    room_dict = Room.parse_file(filename)
    solution_dict = {}

    solution_dict['phantoms'] = []
    solution_dict['missing'] = []
    solution_dict['mismatch'] = []

    available_items = []

    # Compile the available items
    for room in room_dict.values():
        if room.items is not None:
            for item in room.items:
                available_items.append(item)

    # Iterate through the rooms
    for room in room_dict.values():

        roomids = room_dict.keys()

        for roomid in room.exits:
            if roomid not in roomids and roomid != -1:
                solution_dict['phantoms'].append(roomid)

        if room.puzzle not in available_items and room.puzzle is not None:
            solution_dict['missing'].append(room.puzzle)

    # We have to iterate a second time since part 3 depends on phantoms
    for room in room_dict.values():

        for neighbor_index in range(4):

            neighbor_id = room.exits[neighbor_index]
            if neighbor_id == -1:
                continue
            elif neighbor_id in solution_dict['phantoms']:
                solution_dict['mismatch'].append((room.id, neighbor_index, "unknown"))
            elif room_dict[neighbor_id].exits[recip(neighbor_index)] != room.id:
                solution_dict['mismatch'].append((room.id, neighbor_index, "mismatch"))

    return solution_dict


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print('validate("map1.txt") produces:', validate("map1.txt"), sep="\n")
    print()
    print('validate("map2.txt") produces:', validate("map2.txt"), sep="\n")
    print()
    print('validate("map3.txt") produces:', validate("map3.txt"), sep="\n")
    print()
    print('validate("map4.txt") produces:', validate("map4.txt"), sep="\n")
    print()
    print()

