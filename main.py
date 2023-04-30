'''
Created By: Mahershi Bhavsar
Email: mahershi1999@gmail.com
Last Modified: April 30, 2023
Modified By: Mahershi Bhavsar
'''


# Command to start server: java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000

from lib.corenlp import CoreNLPService
from lib.scripts import Scripts


call_inputs = {
    'ideal': "nine one one for police fire ambulance\n"\
                "fire please\n"\
                "okay for what address\n"\
                "yeah it's nine - seven - one - zero, sixty-sixth avenue north west\n"\
                "okay and you're calling from which number\n"\
                "my phone number is seven - eight - zero, two - seven - six, ninety-two - forty-seven\n"\
                "ok transferring you to fire",

    'ask_again': "nine one one for police fire ambulance\n"\
                    "fire please\n"\
                    "okay for what address\n"\
                    "yeah it's nine - seven - one - zero, sixty-sixth avenue north west\n"\
                    "okay and you're calling from which number\n"\
                    "no no no fast\n"\
                    "okay and you're calling from which number\n"\
                    "my phone number is seven - eight - zero, two - seven - six, ninety-two - forty-seven\n"\
                    "ok transferring you to fire",

    'missing': "nine one one for police fire ambulance\n"\
                "fire please\n"\
                "okay for what address\n"\
                "yeah it's nine - seven - one - zero, sixty-sixth avenue north west\n"\
                "ok transferring you to fire",

'transfer_first': "nine one one for police fire ambulance\n"\
                    "fire please\n"\
                    "okay for what address\n"\
                    "yeah it's nine - seven - one - zero, sixty-sixth avenue north west\n"\
                    "ok transferring you to fire\n"\
                    "okay and you're calling from which number\n"\
                    "my phone number is seven - eight - zero, two - seven - six, ninety-two - forty-seven"
}


'''
Runner
'''
if not CoreNLPService.is_initialized():
    CoreNLPService.initialize()
    print(CoreNLPService.parser_initialized)
    lines = call_inputs['transfer_first'].split('\n')
    print("No of lines", len(lines), end='\n\n')
    # Scripts.process_instance(lines)
    Scripts.process_input(lines)
    # CoreNLPService.parse_line('nine one two for police fire ambulance', line_number=1)


