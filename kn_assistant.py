#!/bin/python3

import json
import os.path

'''what I want to do in this script.

Build something to help find helpful information when I am doing my work.
Creating a knowledge base. Or rather, index system. Easily searchable knowledge base.
Knowledge is stored in some form of text. With no redundancy. So duplication is minimal.
Search is done by typing succinct query. Thus, the name index.
Information is shown in an easy-to-understand format.
'''

class Knowledge:

    def __init__(self, kn_id, f_method, f_data, info):
        self.id = kn_id
        self.fitness_method = f_method
        self.fitness_data = f_data
        self.info = info

    @classmethod
    def load(cls, path):
        '''create a list of Knowledge instances from a json file.

        json file format:
            "00001": {
                "fitness_method": "space_split_and_compare_words",
                "fitness_data": "1 2 3",
                "info": "blah blah blah blah "
            },
        '''
        with open(path, "r") as f:
            kn_dict = json.load(f)

        kn_list = []
        for key in kn_dict:
            kn = kn_dict[key]
            f_method = kn["fitness_method"]
            f_data = kn["fitness_data"]
            info = kn["info"]
            kn_list.append(Knowledge(key, f_method, f_data, info))
        return kn_list

    def calc_f_val(self, user_in):
        # TODO: just increment a member variable and return for now.
        try:
            Knowledge.count = Knowledge.count + 1
        except AttributeError:
            Knowledge.count = 1
        return Knowledge.count

if __name__ == "__main__":
    user_in = input("What are you looking for? : ").strip()

    basename = os.path.dirname(os.path.abspath(__file__))
    kn_list = Knowledge.load(os.path.join(basename, "kn_assistant.json"))
    for kn in kn_list:
        kn.f_val = kn.calc_f_val(user_in)

    sorted_kn_list = sorted(kn_list, key=lambda kn: kn.f_val, reverse=True)
    for kn in sorted_kn_list:
        print("id: %s,\tf_val: %s" % (kn.id, kn.f_val))

    # key_set = set(input_list)

    # # make the index. index will have a set as its key and string as its value.
    # basename = os.path.dirname(os.path.abspath(__file__))
    # with open(os.path.join(basename,"index.json"), "r") as f:
        # tmp_index = json.load(f)
    # index = {}
    # for key in tmp_index["keys"]:
        # set_for_key = frozenset(key.strip().split(" "))
        # index[set_for_key] = tmp_index[key]
# 
    # max_fit_index = dict()
    # max_fit_val = 0
    # max_fit_index[frozenset("".split(" "))] = index[frozenset("".split(" "))]
    # for key in index:
        # tmp_fit_val = len(key_set.intersection(key))
        # if tmp_fit_val < max_fit_val:
            # continue
        # if tmp_fit_val == max_fit_val and max_fit_val == 0:
            # continue
        # if tmp_fit_val > max_fit_val:
            # max_fit_index.clear()
            # max_fit_val = tmp_fit_val
        # max_fit_index[key] = index[key]
# 
    # for key in max_fit_index:
        # print("{}: {}".format(key, max_fit_index[key]))
