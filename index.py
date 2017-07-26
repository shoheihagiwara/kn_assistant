#!/bin/python3

'''what I want to do in this script.

Build something to help find helpful information when I am doing my work.
Creating a knowledge base. Or rather, index system. Easily searchable knowledge base.
Knowledge is stored in some form of text. With no redundancy. So duplication is minimal.
Search is done by typing succinct query. Thus, the name index.
Information is shown in an easy-to-understand format.
'''
if __name__ == "__main__":
    input_list = input("What are you looking for? : ").strip().split(" ")
    key_set = set(input_list)

    # make the index
    index = dict()

    index[""] = """
    you didn't specify anything you are looking for.
    I can't help you if you won't let me...\n"""

    index[frozenset(["1","2","3"])] = """
    This is ["1","2","3"].\n"""

    index[frozenset(["4","2","3"])] = """
    This is ["4","2","3"].\n"""

    max_fit_index = dict()
    max_fit_val = 0
    max_fit_index[""] = index[""]
    for key in index:
        tmp_fit_val = len(key_set.intersection(key))
        if tmp_fit_val < max_fit_val:
            continue
        if tmp_fit_val == max_fit_val and max_fit_val == 0:
            continue
        if tmp_fit_val > max_fit_val:
            max_fit_index.clear()
            max_fit_val = tmp_fit_val
        max_fit_index[key] = index[key]

    for key in max_fit_index:
        print("{}: {}".format(key, max_fit_index[key]))
