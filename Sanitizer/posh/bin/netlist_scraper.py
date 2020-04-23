# Use of this source code is governed by an Apache 2.0 license that can be
# found in the LICENSE file.

import sys
import os
import yaml
from antlr4 import *
from netlist_parser.SpectreLexer import SpectreLexer
from netlist_parser.SpectreParser import SpectreParser
from posh.NetlistListener import *
from posh.NetlistVisitor import *


def listtostring(List):
    st = ''
    for i in List:
        st = st + i
    return st



def splitsimulation(file):
    fp = open(file,'r')
    lines = fp.readlines()
    mid = len(lines)
    for i in range(0,len(lines)):
        #print(lines[i][0:4])
        if(lines[i][0:16] == 'simulatorOptions'):
            mid  = i
    #print(mid)
    head_netlist = listtostring(lines[0:mid])
    simulation_measure = listtostring(lines[mid:len(lines)])
    return head_netlist,simulation_measure



def main(argv):

    input_scs = str(argv[1]).strip()
    print(input_scs)

    input_stream = FileStream(input_scs)
    head_netlist,simulation_measure = splitsimulation(input_scs)
    head_netlist_input_stream = InputStream(head_netlist)

    lexer = SpectreLexer(head_netlist_input_stream)
    #lexer = SpectreLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SpectreParser(stream)
    tree = parser.netlist()

    print("Here")
    dictToYAML = {"devices": []}
    devices = []
    for i in range(0, tree.getChild(1).getChildCount() - 2):
        if not(str(tree.getChild(1).getChild(i).getChild(2).getText()) in devices):
            devices.append(str(tree.getChild(1).getChild(i).getChild(2).getText()))
            dictToYAML["devices"].append({"name": str(tree.getChild(1).getChild(i).getChild(2).getText())})
            print(tree.getChild(1).getChild(i).getChild(2).getText())
    ostream = open('netlist.yaml', 'w')
    yaml.dump(dictToYAML, ostream)
    ostream.close()




if __name__ == '__main__':
    main(sys.argv)
