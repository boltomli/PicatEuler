#! /usr/bin/env python

# -*- coding: utf-8 -*-

from itertools import permutations, chain

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

mask_group_permutations = list(permutations(basic_masks))
mask_permutations = []
for mask_group in mask_group_permutations:
    for masks in mask_group:
        mask_permutations.append(masks)

target = Gazelle ** 5

for m in mask_permutations:
    masks = list(chain.from_iterable(m))
    if len(masks) == len(board):
        result = 1
        for i in range(0, len(board)):
            result *= board[i] ** masks[i]
        if result == target:
            print(masks)
