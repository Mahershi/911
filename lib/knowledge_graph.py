'''
Created By: Mahershi Bhavsar
Email: mahershi1999@gmail.com
Last Modified: April 30, 2023
Modified By: Mahershi Bhavsar
'''


from .models import Node, CallInstance
from lib.global_vars import Tags, GlobalVars
from lib.number import NumberResolve
from lib.corenlp import CoreNLPService


'''
KG
Purpose: Handles Knowledge graph related logic such as iterating through a knowledge graph.
Also handles traversing KG for deducing what kind of a statement is the it
'''
class KG:
    # Unused, was used in previous version
    # Do not remove as it can be used in future
    # @staticmethod
    # def traverse_node_skip_one(root: Node, line_number):
    #     root: Node = root.next[-1]
    #     print("LineNO: " + str(line_number))
    #     # When line number even, its a reply
    #     if line_number % 2 == 0:
    #         pass
    #     else:
    #         while line_number < 8 and not CallInstance.mymap[line_number]['success']:
    #             result = mapping[line_number](root)
    #             print("Suceess: " + str(line_number) + ": " + str(result))
    #             CallInstance.mymap[line_number]['success'] = result
    #
    #             if not result:
    #                 line_number += 2
    #
    #     # KG.traverse(root)
    #     # CallInstance.show_success()

    # Traverses the given KG to decide whether it is a 'transfer' or not, returns boolean
    # Does so by looking for transfer keywords mentioned in GlobalVars
    # KG traversal is recursive
    @staticmethod
    def traverse_transfer(root: Node):
        # print("Checking transfer")
        success = False
        # print(root.label)
        if root.label in GlobalVars.transfer_keys:
            return True

        for node in root.next:
            success = KG.traverse_transfer(node)
            if success:
                break

        return success

    # Traverses the given KG to decide whether it is a 'contact' question or not, returns boolean
    # Does so by looking for contact keywords mentioned in GlobalVars
    # KG traversal is recursive
    @staticmethod
    def traverse_contact(root: Node):
        # print("Checking contact")
        success = False
        if root.label in GlobalVars.contact_keys:
            return True

        for node in root.next:
            success = KG.traverse_contact(node)
            if success:
                break

        return success

    # Traverses the given KG to decide whether it is a 'address' question or not, returns boolean
    # Does so by looking for address keywords mentioned in GlobalVars
    # KG traversal is recursive
    @staticmethod
    def traverse_address(root: Node):
        # print("Checking Address")
        success = False
        # print(root.label)
        if root.label in GlobalVars.address_keys:
            return True

        for node in root.next:
            success = KG.traverse_address(node)
            if success:
                break

        return success

    # Traverses the given KG to decide whether it is a 'opening' statement or not, sets the current call instance flag accordingly
    # Does so by looking for opening/service keywords and 911 as mentioned in GlobalVars
    # KG traversal is recursive
    @staticmethod
    def traverse_opening(sent=''):
        # print("Checking opening")
        got_services = True
        got_intro = sent.find(GlobalVars.nine_one_one_words)
        for noun in GlobalVars.services:
            if noun not in sent:
                got_services = False

        if got_services and got_intro != -1:
            CallInstance.mymap['opening'][GlobalVars.operator_success] = True
            GlobalVars.waiting_response_for = 'opening'


    '''
    For Traversing Different kinds of responses to: opening, address, contact
    '''
    @staticmethod
    def traverse_service_response(sent=''):
        print("SERVICE RESPONSE: " + sent)
        for service in GlobalVars.services:
            if service in sent:
                print("Got service:", service)
                CallInstance.mymap['opening'][GlobalVars.response_success] = True
                CallInstance.mymap['opening'][GlobalVars.caller_response] = service
                break

    @staticmethod
    def traverse_address_response(sent=''):
        sent = sent.replace(GlobalVars.removing, '')
        print("Checking address resp:", sent)
        root = CoreNLPService.parse_line(sent=sent, debug=True)
        root = root.next[0]
        number, keys = KG.traverse_for_number2(root)
        number = number + root.label
        number = NumberResolve.resolve_number_words(number)
        print(number, " ", keys)

        if number or keys:
            CallInstance.mymap['address'][GlobalVars.response_success] = True
            CallInstance.mymap['address'][GlobalVars.caller_response] = [number, keys]


    @staticmethod
    def traverse_contact_response(sent=''):
        sent = sent.replace(GlobalVars.removing, '')
        li = sent.split(',')
        print(li)
        temp_numbers = []
        number = ''
        for i in li:
            temp_numbers.append(KG.clear_num_string(i))

        for i in temp_numbers:
            number += NumberResolve.resolve_number_words(i) + ' '

        if len(number) > 3:
            CallInstance.mymap['contact'][GlobalVars.response_success] = True
            CallInstance.mymap['contact'][GlobalVars.caller_response] = number
        # for s in sent:
        #     if s not in GlobalVars.units_dict and s not in GlobalVars.tens_dict:
        #         sent.
        # print("Checking address resp:", sent)
        # root = CoreNLPService.parse_line(sent=sent)


    # removes no numerals from a string and converts the numerals to digits
    @staticmethod
    def clear_num_string(sent):
        final = ''
        l = sent.split(' ')
        for i in l:
            if i in GlobalVars.units_dict or i in GlobalVars.tens_dict:
                final += i + ' '

            else:
                for o in GlobalVars.tens_dict:
                    for k, p in enumerate(GlobalVars.units_dict):
                        if k > 0 and k < 11:
                            if str(o + p) == i:
                                final += o + ' ' + p + ' '

        return final



    @staticmethod
    def traverse_for_number2(root):
        number = ''
        for node in root.next:
            if node.tag in Tags.NUMBER_TAGS:
                number += node.label + ' '

            if node.tag in Tags.NOUN_TAGS:
                print("Noun: ", node.label)
                keys = [node.label]
                for n, e in zip(node.next, node.edge):
                    if e in Tags.NOUN_EDGES:
                        keys.append(n.label)


        return number, keys

    # unused currently
    # Check if operator introduced 9-1-1 and asked for services required.
    # @staticmethod
    # def traverse_opening(root: Node):
    #     print("Traversing Opening: " + root.label + '\n')
    #     got_services = True
    #     got_number = False
    #     # check = False
    #     number = '000'
    #     nouns = []
    #
    #     if root.tag in Tags.VERB:
    #         # root is a VERB
    #         for node, edge in zip(root.next, root.edge):
    #             if node.tag in Tags.NUMBER_TAGS:
    #                 # node is a number, last digit.
    #                 # check = True
    #                 number = KG.traverse_for_number(node)
    #                 print("Number: " + str(number))
    #
    #             elif node.tag in Tags.NOUN_TAGS:
    #                 # node is a noun
    #                 nouns = KG.traverse_for_noun(node)
    #                 # check = True
    #                 print("Nouns: " + str(nouns))
    #
    #     elif root.tag in Tags.NUMBER_TAGS:
    #         print("Root is a Number")
    #
    #         for node, edge in zip(root.next, root.edge):
    #
    #             if node.tag in Tags.NUMBER_TAGS and edge in Tags.NUMBER_EDGES:
    #                 if not root.visited:
    #                     #node is number, second last. last digit is root.
    #                     number = KG.traverse_for_number(root)
    #                     print("Number: " + str(number))
    #
    #             elif node.tag in Tags.NOUN_TAGS and edge in Tags.NOUN_EDGES:
    #                 # node is a noun
    #                 nouns = KG.traverse_for_noun(node)
    #                 print("Nouns: " + str(nouns))
    #
    #     if number == GlobalVars.nine_one_one:
    #         got_number = True
    #
    #     for noun in GlobalVars.services:
    #         if noun not in nouns:
    #             got_services = False
    #             break
    #
    #     return got_number and got_services







    # Checking line number = 1
    # @staticmethod
    # def traverse_openi(root: Node):
    #     print("Traversing: " + root.label)
    #     got_services = True
    #
    #     while root.next:
    #         if root.tag in Tags.NUMBER_TAGS:
    #             if root.edge[0] in Tags.NUMBER_EDGES:
    #                 if not root.visited:
    #                     number = KG.traverse_for_number(root)
    #                     if number == GlobalVars.nine_one_one:
    #                         print("911 Got")
    #
    #             elif root.edge[0] in Tags.NOUN_EDGES:
    #                 if not root.visited:
    #                     nouns = KG.traverse_for_noun(root)
    #                     got_services = True
    #                     for service in GlobalVars.services:
    #                         if service not in nouns:
    #                             got_services = False
    #                             break
    #
    #         elif root.tag in Tags.NOUN_TAGS:
    #             if not root.visited:
    #                 nouns = KG.traverse_for_noun(root)
    #                 got_services = True
    #                 for service in GlobalVars.services:
    #                     if service not in nouns:
    #                         got_services = False
    #                         break
    #
    #         if got_services:
    #             print("Got All Services")
    #
    #         new_root = root.next.pop(0)
    #         print("New Root: " + new_root.label + " " + str(new_root.visited))
    #         if not new_root.visited:
    #             nouns = KG.traverse_one(new_root)



    # considering growing from a single root
    @staticmethod
    def traverse_for_noun(root: Node):
        nouns = []
        root.visited = True
        print("traversing for noun root: " + root.label)
        nouns.append(root.label)
        for next_node, edge in zip(root.next, root.edge):
            if next_node.tag in Tags.NOUN_TAGS:
                next_node.visited = True
                nouns.append(next_node.label)

        # print(nouns)
        return nouns


    # # considering growing from a single root
    # @staticmethod
    # def traverse_for_number(root: Node):
    #     print("Traversing Number: " + root.label)
    #     base = root.label
    #     root.visited = True
    #     my_string = ''
    #     for next_node, edge in zip(root.next, root.edge):
    #         if edge in Tags.NUMBER_EDGES and next_node.tag in Tags.NUMBER_TAGS:
    #             next_node.visited = True
    #             my_string += next_node.label + ' '
    #
    #     my_string += base
    #     number = NumberResolve.resolve_number_words(my_string)
    #
    #     return number



# Unused
# Do not delete
# not sending line 1 to parse through mapping method.

# mapping = {
#     # 1: KG.traverse_opening,
#     3: KG.traverse_address,
#     5: KG.traverse_contact,
#     7: KG.traverse_transfer,
# }

