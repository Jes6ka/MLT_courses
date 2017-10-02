# Assignment2

## First, need  StanfordParser.
### go to here
> https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software

In window,

> install java or check java version(must be >=1.8)
> how to check : cmd >> java -version
> where it is installed : cmd >> where java
> #need this address for JAVAHOME, JAVA_HOME in system environments. go and Create, save!

### Go here, https://nlp.stanford.edu/software/lex-parser.shtml 
download parser, e.g., Download : Version 3.8.0 

Unzip(extract) it, and find "stanford-parser.jar" file. then look at the directory, that addr is where we have to save as system environment.
e.g., D:\GU_MLT\Semester_3\Machine_Learning\lab2\stanford-parser-full-2017-06-09


- TEST:
>
from nltk.parse.stanford import StanfordParser
parser=StanfordParser(model_path="D:\GU_MLT\Semester_3\Machine_Learning\lab2\stanford-parser-full-2017-06-09\englishPCFG.ser.gz")

list(parser.raw_parse("the quick brown fox jumps over the lazy

![alt text](https://github.com/sungmin-yang/MLT_courses/blob/master/Semester3/Machine_learning/lab2/window_stanford_ex.JPG)
