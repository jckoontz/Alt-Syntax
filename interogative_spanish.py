from __future__ import division
import nltk, re, pprint
from nltk import CFG
from nltk.parse import RecursiveDescentParser
from nltk.grammar import Nonterminal
from nltk.tree import Tree, ImmutableTree
from nltk.compat import unicode_repr

from nltk.parse.api import ParserI

imperative_grammar = nltk.CFG.fromstring(""" 

 S -> Aux NP VP | NP Aux VP | VP | Aux VP  
 VP -> V PP | V NP | V 
 NP -> N VP | Det NP | N | N PP | N NP 
 PP -> P NP 
 V -> "estudiado" | "visto" | "leido" | "hecho" | "pasado" | "estudiar" | "ver" | "hacer" | "pasar" | "estudiaste" | "hiciste" | "viste"
 N -> "lo" | "la" | "le" | "fútbol" | "película" | "canción" | "tarea" | "él" | "ella" | "Iñaki" | "examen" | "oficina" | "tú" | "vos" | "usted" | "partido" | "Boca" | "Barcelona" 
 P -> "en" | "sobre" | "con" | "a" | "de" | "por" | "hacía" | "para" 
 Aux -> "has" | "ha" | "habéis" | "han" | "puedes" | "podés" | podéis | "pueden"  
 Det -> "la" | "el" | "estos" | "un" | "una" | "esta" | "mi" | "tu" | "su" 
 SI -> "si"
 NO -> "no"
""")
sentence = "no has visto tú el partido de Barcelona  ".split()
rd_parser = nltk.RecursiveDescentParser(imperative_grammar)
for tree in rd_parser.parse(sentence):
    print(tree)
    print("---" * 30)
