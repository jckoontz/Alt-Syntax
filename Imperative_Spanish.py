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
  VP -> V NP | V NP PP | V PP                                                                                                                                                    
  PP -> P NP                                                                                                                                                                     
  V -> "Cambia" | "Cambiá" | "Cambie" | "Cambiad" | "Cambien" | "Gira" | "Gire" | "Continúa" | "Continúe" | "Des" | "Dé" | "Ven" | "Vení" | "Venga"                                                                                                                                           
  NP -> Det N | Det N PP | N
                                                                                                                               
  Det -> "la" | "el" | "un" | "una"                                                                                                                                               
  N -> "Iñaki" | "tú" | "vos" | "usted" | "vosotros" | "usteders" | "canción" | "derecha" | "directo" | "izquierda" | "vuelta" | "camino" | "radio" | "estación" | "canción" 
                                                                                                                            
  P -> "de" | "en" | "por" | "con" | "a" | "aquí" | "acá"                                                                                                                                        
  """)

sentence = "Vení acá vos ".split()
rd_parser = nltk.RecursiveDescentParser(imperative_grammar)
for tree in rd_parser.parse(sentence):
    print(tree)
    print("---" * 30)

