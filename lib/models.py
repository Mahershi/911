"""
Created By: Mahershi Bhavsar
Email: mahershi1999@gmail.com
Last Modified: April 30, 2023
Modified By: Mahershi Bhavsar
"""

from lib.global_vars import GlobalVars


"""
CallInstance
Purpose: Represents the current input instance and holds the results.
"""
class CallInstance:
    # FLAGS
    # Maps the statment type to its results and responses
    mymap = {
        'opening': {
            GlobalVars.operator_success: False,
            GlobalVars.response_success: False,
            GlobalVars.caller_response: ''
        },
        'address': {
            GlobalVars.operator_success: False,
            GlobalVars.response_success: False,
            GlobalVars.caller_response: ''

        },
        'contact': {
            GlobalVars.operator_success: False,
            GlobalVars.response_success: False,
            GlobalVars.caller_response: ''
        },
        'transfer': {
            GlobalVars.operator_success: False,
            GlobalVars.response_success: False,
            GlobalVars.caller_response: ''
        },
    }

    # Prints the flags to console
    @staticmethod
    def show_success():
        print("\n\n")
        print("Result")
        for i in CallInstance.mymap:
            print(end='\n')
            print(i)
            print("Operator: ", CallInstance.mymap[i][GlobalVars.operator_success])
            print("Response: ", CallInstance.mymap[i][GlobalVars.response_success])
            print("Response String: ", CallInstance.mymap[i][GlobalVars.caller_response])


"""
Node
Purpose: Model on which KG is built. Represents each node and has various methods to handle the KG
"""
class Node:
    next = []
    prev = None
    label = None
    edge = []
    tag = None
    visited = False

    # To create a general node given specific values
    def __init__(self, prev = None, next=[], edge=[], tag=None, label=None,):
        self.prev = prev
        self.label = label
        self.edge = edge
        self.next = next
        self.tag = tag

    # To create head node
    @classmethod
    def create_head(cls):
        return cls(tag=GlobalVars.root_node_tag, label=GlobalVars.root_node_label, next=[], edge=[])

    # To attach a node to another. Used when depicting dependencies between nodes.
    def attach(self, edge, node):
        self.next.append(node)
        self.edge.append(edge)

    # Iterate the KG from root/head node and print to console. Shows the entire KG
    def show(self):
        if self.prev:
            print("LABEL:", self.label, "\tTAG:", self.tag, "\tPREV:", self.prev.label)
        else:
            print("LABEL:", self.label, "\tTAG:", self.tag, "\tPREV: NONE",)

        for e, n in zip(self.edge, self.next):
            print(e.ljust(15), end="")
            n.show()

