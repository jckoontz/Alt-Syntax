from __future__ import division
import nltk, re, pprint
from nltk import CFG
from nltk.parse import RecursiveDescentParser
from nltk.grammar import Nonterminal
from nltk.tree import Tree, ImmutableTree
from nltk.compat import unicode_repr

from nltk.parse.api import ParserI

imperative_grammar = nltk.CFG.fromstring("""

  S ->  VP 
  VP -> V NP | V NP PP | V PP | V AVP | Aux Con_Neg VP | Aux_Con VP | V
  PP -> P NP
  V -> "Turn" | "Stop" | "Change" | "Go" | "stop" | "change" | "run"
  AVP -> ADV 
  ADV -> "left" | "right" | "straight"
  NP -> "John" | "Mary" | "Roberto" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park" | "song"
  P -> "in" | "on" | "by" | "with" | "to"
  Con_Neg -> "not"
  Aux -> "Do"
  Aux_Con -> "Don't" 
  """)

sentence = "Do not run ".split()
rd_parser = nltk.RecursiveDescentParser(imperative_grammar)
for tree in rd_parser.parse(sentence):
    print(tree)
    print("---" * 30)




