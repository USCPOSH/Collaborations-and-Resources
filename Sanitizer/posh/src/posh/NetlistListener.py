# Copyright 2019 USC. All rights reserved.
# Use of this source code is governed by an Apache 2.0 license that can be 
# found in the LICENSE file.

from netlist_parser.SpectreParserListener import SpectreParserListener


class NetlistListener(SpectreParserListener):
    def enterNetlist(self, ctx):
        print "Enter netlist"

    def exitNetlist(self, ctx):
        print "Exit netlist"

    def enterEveryRule(self, ctx):
        #print "All", type(ctx)
        pass
