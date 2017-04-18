from __future__ import division
import nltk, re, pprint
from nltk import CFG
from nltk.parse import RecursiveDescentParser
from nltk.grammar import Nonterminal
from nltk.tree import Tree, ImmutableTree
from nltk.compat import unicode_repr

from nltk.parse.api import ParserI

imperative_grammar = nltk.CFG.fromstring("""                                                                                                                                     
  S -> S_Imperative | S_Interogative | S_Subjunctive 

  S_Interogative -> Aux NP VP Q 

  S_Imperative -> VP

  S_Subjunctive -> ConS S_Subjunctive S_Conditional | NP VP 

  S_Conditional -> NP Aux VP 

  VP -> V NP | V NP PP | V PP | V AVP |  V | Aux Con_Neg VP | Aux_Con VP | Aux VP
                                                                                                          
  PP -> P NP                                                                                                                                                                     
  V ->  "stop" | "change" | "run" | "play" | "snow" | "rain" | "go" | "work" | "were"                                                                                                               
  AVP -> ADV | ADV PP                                                                                                                                                                     
  ADV -> "left" | "right" | "straight"                                                                                                                                           
  NP -> Det NP | N PP | N 
                                                                                                                           
  Det -> "a" | "an" | "the" | "my"                                                                                                                                               
  N -> "man" | "dog" | "cat" | "soccer" | "park" | "song" | "you" | "I" | "he" | "she" | "we" | "it" | "they" | "San Francisco" | "Seattle" | "Stuttgart" | "them"
                                                                                                                   
  P -> "in" | "on" | "by" | "with" | "to"                                                                                                                                        
  Con_Neg -> "not"  

  Con -> "and"

  ConS -> "if"
                                                                                                                                         
  Aux -> "Do" | "Does" | "Can" | "Could" | "Would" | "would"                                                                                                                                                                 
  Aux_Con -> "Don't"  

  Q -> "?"

  """)

sentence = "if I were in Seattle it would rain ".split()
rd_parser = nltk.RecursiveDescentParser(imperative_grammar)
for tree in rd_parser.parse(sentence):
    print(tree)
    print("---" * 30)

