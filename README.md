Parsing 911 calls to Generate Knowledge Graph and Run analysis on conversation.

Created By: Mahershi Bhavsar (mahershi1999@gmail.com) / University of Regina

To install,
1. Download StanfordCoreNLP Package.
   1. https://stanfordnlp.github.io/CoreNLP/download.html
   2. Start the server by running the following command root folder of the downloaded package.
   </br></br>
   <i>java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000 </i>
   </br></br>
2. Create python virtual environment if not created already
   1. Start the virtual environment
3. Download Required packages, mentions in requirements.txt
   1. Run the following command in the root directory of this project.
   <br><br>
   <i>pip install -r requirements. txt</i>
   <br><br>
4. Run the program.
<br><br>
   Select the call input type (in main.py) and run the main.py file