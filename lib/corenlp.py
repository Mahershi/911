'''
Created By: Mahershi Bhavsar
Email: mahershi1999@gmail.com
Last Modified: April 30, 2023
Modified By: Mahershi Bhavsar
'''


from nltk import CoreNLPDependencyParser
from lib.global_vars import GlobalVars
from .models import Node


'''
CoreNLPService
Purpose: Handles corenlp related tasks such as generating sentence dependencies using CoreNLPDependencyParser from nltk package
'''
class CoreNLPService:
    parser: CoreNLPDependencyParser = None
    parser_initialized = False

    @staticmethod
    def is_initialized():
        return CoreNLPService.parser_initialized


    @staticmethod
    def initialize():
        try:
            CoreNLPService.parser = CoreNLPDependencyParser(url=GlobalVars.server_url)
            CoreNLPService.parser_initialized = True

        except Exception as e:
            print("Exception Init Parser: " + str(e))
            CoreNLPService.parser_initialized = False


    # Generated Knowledge graph for the given line.
    @staticmethod
    def parse_line(sent='', debug=False):
        print("Parsing: " + sent)
        root_node: Node = Node.create_head()
        prev: Node = root_node
        # prev_dep = None
        parse = CoreNLPService.parser.raw_parse(sent)
        dep = parse.__next__()
        for i, d in enumerate(list(dep.triples())):
            if debug:
                print(d)
            if i == 0:
                current: Node = Node(tag=d[0][1], label=d[0][0], prev=[], next=[], edge=[])
                prev.attach(edge=GlobalVars.root_node_edge, node=current)

                prev = prev.next[-1]

            while prev.label != d[0][0]:
                prev = prev.prev

            current = Node(tag=d[2][1], label=d[2][0], prev=prev, next=[], edge=[])
            prev.attach(edge=d[1], node=current)

            if prev.next:
                prev = prev.next[-1]

        print()
        if debug:
            print("Root node")
            root_node.show()
        return root_node
            # KG.traverse_node_skip_one(root_node, line_number)






