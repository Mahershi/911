'''
Created By: Mahershi Bhavsar
Email: mahershi1999@gmail.com
Last Modified: April 30, 2023
Modified By: Mahershi Bhavsar
'''


from lib.global_vars import GlobalVars
from .models import CallInstance
from lib.corenlp import CoreNLPService
from lib.knowledge_graph import KG


"""
Scripts
Purpose: Scripts for general purpose.
"""
class Scripts:
    ask_map = {
        'address': None,
        'contact': None
    }

    wait_map = {
        'opening': KG.traverse_service_response,
        'address': KG.traverse_address_response,
        'contact': KG.traverse_contact_response,
    }

    # Older implementation, no longer used. Do not delete
    @staticmethod
    def process_instance(lines=[]):
        print("Process Instance")
        for i, l in enumerate(lines):
            CoreNLPService.parse_line(l)

        CallInstance.show_success()

    # Main script called from runner to start analysis on input
    @staticmethod
    def process_input(lines=[]):
        i = 0
        while i < len(lines):
            print("\n\nline number: ", str(i), " ", lines[i])
            if i==0:
                KG.traverse_opening(lines[i])

                if GlobalVars.waiting_response_for != '':
                    i += 1
                    Scripts.wait_map[GlobalVars.waiting_response_for](sent=lines[i])

            else:
                root_node = CoreNLPService.parse_line(lines[i])
                if KG.traverse_address(root=root_node):
                    print("Address Question to Response")
                    CallInstance.mymap['address'][GlobalVars.operator_success] = True
                    GlobalVars.waiting_response_for = 'address'
                elif KG.traverse_contact(root=root_node):
                    print("Contact Question to resp")
                    CallInstance.mymap['contact'][GlobalVars.operator_success] = True
                    GlobalVars.waiting_response_for = 'contact'
                elif KG.traverse_transfer(root=root_node):
                    # print("Transfer Question to resp")
                    CallInstance.mymap['transfer'][GlobalVars.operator_success] = True
                    GlobalVars.waiting_response_for = ''
                    break

                if GlobalVars.waiting_response_for != '':
                    i += 1
                    Scripts.wait_map[GlobalVars.waiting_response_for](sent=lines[i])
            i += 1

        CallInstance.show_success()


