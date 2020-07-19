#!/usr/bin/python3


def canUnlockAll(boxes):
    if not boxes:
        return False
    if len(boxes) == 0:
        return False
    keys = boxes[0]
    keys.insert(0, 0)
    return go_to_box(keys, boxes)


def go_to_box(keys, boxes):
    for key in keys:
        new_keys = boxes[key]
        for new_key in new_keys:
            if new_key not in keys:
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False
