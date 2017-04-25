#!/usr/bin/env python3
# (C) 2017 by Damir Cavar <dcavar@iu.edu>
#
# Use this script as follows:
#
# Requirement: the grammar file named with grammarFile, in this case featureGrammar.fcfg has to be located in the
# same folder as the script.
#
# In the command line run:
# python Parsing1.py John calls Mary
#
# or any other sentence following "python Parsing1.py"


import sys, nltk

# define the name of your grammar here
grammarFile = 'featureGrammarYID.fcfg'

# loading the grammar
fcfg = nltk.data.load(grammarFile)

# defining the parser
fcp = nltk.parse.FeatureChartParser(fcfg, trace=1)


def main(input):
        result = list(fcp.parse(input))
        if result:
            for x in result:
                print(x)
        else:
            print("*", " ".join(tokens))


if __name__=="__main__":
        main(sys.argv[1:])


