#!/bin/python3

import json
import os.path
import re

'''what I want to do in this script.

Build something to help find helpful information when I am doing my work.
Creating a knowledge base. Or rather, index system. Easily searchable knowledge base.
Knowledge is stored in some form of text. With no redundancy. So duplication is minimal.
Search is done by typing succinct query. Thus, the name index.
Information is shown in an easy-to-understand format.
'''

class Knowledge:

    def __init__(self, kn_id, f_data, info):
        self.id = kn_id
        self.fitness_data = f_data
        self.info = info

    @classmethod
    def load(cls, path):
        '''create a list of Knowledge instances from a json file.

        json file format:
            "00001": {
                "fitness_data": "1 2 3",
                "info": "blah blah blah blah "
            },
        '''
        with open(path, "r") as f:
            kn_dict = json.load(f)

        kn_list = []
        for key in kn_dict:
            kn = kn_dict[key]
            f_data = kn["fitness_data"]
            info = kn["info"]
            kn_list.append(Knowledge(key, f_data, info))
        return kn_list

    def calc_f_val(self, user_in):
        '''calculate and return this knowledge's fitness value, given the user input.

        fitness value equation:
        (fitness value) = 
            { (num of unique words that were in fitness_data) / (num of unique words) }
            * { (sum of numbers of characters that matched with unique words of user input) / (num of characters in fitness_data) }
        '''
        unique_words = set()
        for line in user_in:
            for word in line.split(" "):
                unique_words.add(word)

        sum_of_mached_chars = 0
        num_of_uniq_words_in_f_data = 0
        for uniq_word in unique_words:
            matched_word_list = re.findall(uniq_word, self.fitness_data)
            if len(matched_word_list) == 0:
                continue
            else:
                num_of_uniq_words_in_f_data += 1
                for matched_word in matched_word_list:
                    sum_of_mached_chars =+ len(matched_word)

        return (num_of_uniq_words_in_f_data / len(unique_words)) * \
                (sum_of_mached_chars / len(self.fitness_data))


if __name__ == "__main__":
    print("What are you looking for? (Once done, press Ctrl+D)")
    user_in = ""
    try:
        while True:
            line = input(">>").strip()
            user_in += line
    except EOFError:
        pass

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
