#! /usr/bin/env python

# -*- coding: utf-8 -*-

from itertools import permutations, chain, product

# Board

Empty = 1
Elephant = 2
Lion = 3
Zebra = 5
Gazelle = 7
Rhino = 11

# E   L | G   L
# Z G Z |   Z E
# R L E | L R G
# -------------
# R E Z |
# G   G |   R L
# L   R | G E Z

board = [Elephant, Empty, Lion, Zebra, Gazelle, Zebra, Rhino, Lion, Elephant,
         Gazelle, Empty, Lion, Empty, Zebra, Elephant, Lion, Rhino, Gazelle,
         Rhino, Elephant, Zebra, Gazelle, Empty, Gazelle, Lion, Empty, Rhino,
         Empty, Empty, Empty, Empty, Rhino, Lion, Gazelle, Elephant, Zebra]

# Masks (distinct with rotations)
# ████
#   ████
#   ████
#
# ██████
#   ██
# ██████
#
# ██  ██
# ██  ██
# ██████
#
# ████
# ██████
# ██  ██


def rotate(mask):
    return [mask[2], mask[5], mask[8],
            mask[1], mask[4], mask[7],
            mask[0], mask[3], mask[6]]

def visualize(masks):
    assert len(masks) == 3 * 3 * 4
    mask = ''
    for i in range(0, len(masks)):
        if i % 3 == 0:
            mask += '\n'
        if i % 9 == 0:
            mask += '------\n'
        if masks[i] == 0:
            mask += '██'
        else:
            mask += '  '
    mask += '\n------'
    print(mask)

basic_masks = [
                  [
                      [0, 0, 1, 1, 0, 0, 1, 0, 0]
                  ],
                  [
                      [0, 0, 0, 1, 0, 1, 0, 0, 0]
                  ],
                  [
                      [0, 1, 0, 0, 1, 0, 0, 0, 0]
                  ],
                  [
                      [0, 0, 1, 0, 0, 0, 0, 1, 0]
                  ]
              ]

length = len(basic_masks)

for i in range(0, length):
    rotated_mask = rotate(basic_masks[i][0])
    while rotated_mask not in basic_masks[i]:
        basic_masks[i].append(rotated_mask)
        rotated_mask = rotate(rotated_mask)

all_permutations = []
for order in list(permutations(range(length))):
    all_permutations.insert(0, list(chain(product(basic_masks[order[0]], basic_masks[order[1]], basic_masks[order[2]], basic_masks[order[3]]))))

target = (Elephant ** 3) * (Lion ** 1) * (Zebra ** 1) * (Gazelle ** 2) * (Rhino ** 1) 

for g in all_permutations:
    for m in g:
        masks = list(chain.from_iterable(m))
        assert len(masks) == len(board)
        result = 1
        for i in range(0, len(board)):
            result *= (board[i] ** masks[i])
        if result == target:
            visualize(masks)
