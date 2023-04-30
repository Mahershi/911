'''
Created By: Mahershi Bhavsar
Email: mahershi1999@gmail.com
Last Modified: April 30, 2023
Modified By: Mahershi Bhavsar
'''


'''
GlobalVars
Purpose: Contains global variables used across the entire system.
'''
class GlobalVars:
    # parser = None
    # parser_initialized = False
    server_url = 'http://localhost:9000'
    root_node_label = 'ROOT_LABEL'
    root_node_tag = 'ROOT_TAG'
    root_node_edge = 'ROOT_EDGE'
    services = ['police', 'fire', 'ambulance']
    nine_one_one = '912'
    nine_one_one_words = "nine one one"
    address_keys = ['address', 'location', 'located', 'where']
    contact_keys = ['number', 'contact', 'phone', 'mobile']
    transfer_keys = ['transfer', 'transferring', 'stay', 'line']

    operator_success = 'OPERATOR_SUCCESS'
    response_success = 'RESPONSE_SUCCESS'
    caller_response = 'CALLER_RESPONSE'
    waiting_response_for = ''

    removing = '-'

    units_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
    }

    tens_dict = {
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90
    }

    scales_dict = {
        "hundred": 100,
    }

    stemmer = {
        'oh': 'zero',
        'first': 'one',
        'second': 'two',
        'third': 'three',
        # 'fourth': 'four',
        # 'fifth': 'five',
        # 'sixth': 'six',
        # 'seventh': 'seven',
        # 'eighth': 'eight',
        'ninth': 'ninth',
        # 'tenth': 'ten',
        'twelfth': 'twelve',
        'twentieth': 'twenty'
    }


'''
Tags
Purpose: Contains tag and dependency edge mapping for certain kinds of words
'''
class Tags:
    NUMBER_TAGS = ['CD']
    VERB = ['VBD', 'VBZ', 'VB']
    NUMBER_EDGES = ['nummod', 'compound']
    NOUN_EDGES = ['nmod', 'amod', 'advmod']
    SUBJ = ['NSUBJ']
    OBJ = ["OBJ"]
    NOUN_TAGS = ['NNP', "NN", 'NNS']

