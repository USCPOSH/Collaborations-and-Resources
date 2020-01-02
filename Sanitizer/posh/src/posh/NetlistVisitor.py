# Copyright 2019 USC. All rights reserved.
# Use of this source code is governed by an Apache 2.0 license that can be 
# found in the LICENSE file.

from netlist_parser.SpectreParserVisitor import SpectreParserVisitor
#from netlist_parser.SpectreParser import VectorContext

class NetlistVisitor_sanitizer(SpectreParserVisitor):

    def __init__(self,scsfile,devfile):
        newscs = scsfile.split('.')[0]+'_sanitized'+'.scs'
        self.devfp = open(devfile,'r')
        self.fp = open(newscs,'w')
        self.dict = {}
        lines = self.devfp.readlines()
        for line in lines:
            if(line[0:2] != '//'):
                dev_name = line.split(',')[0]
                dev_para = line.split(',')[1]
                self.dict[dev_name] = dev_para
        self.devfp.close()



    # TODO: not sture  WORK FOR *S*S*S.TXT
    # THis function judge is pch_lvt is a type of pch* or *lvt in config 
    # return the diction value in self.dict if dev_name exist 
    def has_key(self,dev_name):
        #print(dev_name)
        for key in self.dict:
            keywords = key.split('*')
            #print('keywords',keywords)
            flag = 0
            for keyword in keywords:
                if keyword not in dev_name:
                    flag = 1  
                    break
                else:
                    # 'nch*'.split('*') => ['nch',''] '' is unmwanted
                    # TODO: WHY this happen ? 
                    if(keyword != ''):
                        dev_name = dev_name.split(keyword,1)[1]
            if(flag == 0):
                return self.dict[key]
        return '0'
                

    def sanitization(self,dev_name,exp):
        key_para_name = self.has_key(dev_name)
        if(key_para_name == '0'):
            return dev_name+' '+ exp
        else:
            exp_new = ''
            dev_para = key_para_name.split('#')[0].split()
            if('#' not in key_para_name):
                dev_name_new = dev_name
            else:
                dev_name_new = key_para_name.split('#')[1]
            for st in exp.split(' '):
                if(st.split('=')[0] in dev_para):
                    exp_new = exp_new + st +' '
        return dev_name_new + ' ' + exp_new


    def visitNetlist(self, ctx):
        print "Start Netlist"
        x = self.visitChildren(ctx)
        print "End Netlist"
        return x

    def visitTitleStatement(self, ctx):
        #print('log: visitTitleStatement')
        self.fp.write(ctx.getText()+'\n')
        return self.visitChildren(ctx)
    
    def visitModeStatement(self, ctx):
        #print('log: visitModeStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)
    
    def visitGlobalStatement(self, ctx):
        #print('log: visitGlobalStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)

    def visitParameterStatement(self, ctx):
        #print('log: visitParameterStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            if(i == 1):
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    self.fp.write(temp_ctx_j.getText()+' ')
            else:
                self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)
    


    def visitIncludeStatement(self, ctx):
        #print('log: visitIncludeStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)

    #BODY Visitor
    #TODO(Li): analysisStatement | controlStatement | modelStatement |  
    def visitInstanceStatement(self, ctx):
        #print('log: visitInstanceStatement')
        self.fp.write('\t')
        dev_name = ctx.getChild(2).getText()
        #Vectorinstance = VectorContex()
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            # nodeList
            if(i == 1):
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    self.fp.write(temp_ctx_j.getText()+' ')
            # paramList
            elif(i == 3):
                exp = ''
                for j in range(0,temp_ctx.getChildCount()):
                    suspectvector = temp_ctx.getChild(j).getChild(2).getChild(0)
                    #if(isinstance(suspectvector,VectorContex)):
                    #    print('Finding')
                    exp = exp + temp_ctx.getChild(j).getText() + ' '
                exp = self.sanitization(dev_name,exp)
                self.fp.write(exp+' ')
            elif(i != 2):
                self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)

    def visitSubCircuit(self, ctx):
        #print('log: visitSubCircuit')
        for i in range(0,6):
            temp_ctx = ctx.getChild(i)
            #nodelist
            if(i == 2):
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    self.fp.write(temp_ctx_j.getText()+' ')
                self.fp.write('\n')
            elif(i == 3):
                x = self.visitChildren(ctx)
            else:
                self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return x

    def visitControlStatement(self, ctx):
        #print('log: visitControlStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            if(i == 2):
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    self.fp.write(temp_ctx_j.getText()+' ')
            else:
                self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)
    
    def visitIcStatement(self, ctx):
        #print('log: visitIcStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            if(i == 1):
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    self.fp.write(temp_ctx_j.getText()+' ')
            else:
                self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)

    def visit(self,ctx):
        x = self.visitChildren(ctx)
        self.devfp.close()
        self.fp.close()
        return x


# Desanitizer
class AssignmentVisitor(SpectreParserVisitor):

    def __init__(self):
        #newscs = scsfile +'_desanitized'+'.scs'
        self.assignmentList = []
        self.dict_parameter = {}

    #change the expression string into a list
    # etc: sa = a*b*c+1
    # ls = [a,*,b,*,c,+,1]
    def expression(self,temp_ctx):
        ls = []
        if(temp_ctx.getChildCount() == 0 or temp_ctx.getChildCount() == 1):
            ls.append(temp_ctx.getText())
        else:
            #print('expression',temp_ctx.getText())
            for j in range(0,temp_ctx.getChildCount()):
                temp_ctx_j = temp_ctx.getChild(j)
                ls = ls + self.expression(temp_ctx_j)
        return ls

    def visitAssignment(self, ctx):
        #assigment statment
        #IDENTIFIER '=' expression
        #print(dir(ctx))
        assList = []
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            #node expression 
            if(i == 2):
                #print(temp_ctx.getText())
                expList = []
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    #print('j',temp_ctx_j.getText())
                    expList = expList + self.expression(temp_ctx_j)
                assList = assList + expList
            #node IDENTIFIER '=' 
            else:
                assList.append(temp_ctx.getText())
        #print(assList)
        #self.assignmentList.append(ctx.getText())
        self.assignmentList.append(assList)
        return self.visitChildren(ctx)

    def visitExpression(self, ctx):
        return self.visitChildren(ctx)

    def visit(self,ctx):
        x = self.visitChildren(ctx)
        return self.assignmentList


class NetlistVisitor_desanitizer(SpectreParserVisitor):

    def __init__(self,scsfile,dict_assign):
        self.dict_assign = dict_assign
        newscs = scsfile.split('sanitized')[0]+'desanitized'+'.scs'
        self.fp = open(newscs,'w')
        self.dict_parameter = {}

    def listtostring(List):
        st = ''
        for i in List:
            st = st + i
        return st


    def desanitization(self,dev_name,exp,dict_instanceparamList):
        if(not self.dict_assign.has_key(dev_name)):
            return exp
        else:
            assigmentList = self.dict_assign[dev_name]
            for assigment in assigmentList:
                temp_str = ' '
                for expression in assigment:
                    if(self.dict_parameter.has_key(expression)):
                        temp_str = temp_str + self.dict_parameter[expression]
                    elif(dict_instanceparamList.has_key(expression)):
                        temp_str = temp_str + dict_instanceparamList[expression]
                    else:
                        temp_str = temp_str + expression
                exp = exp + temp_str        
        return exp


    def visitNetlist(self, ctx):
        print "Start Netlist"
        x = self.visitChildren(ctx)
        print "End Netlist"
        return x

    def visitTitleStatement(self, ctx):
        #print('log: visitTitleStatement')
        self.fp.write(ctx.getText()+'\n')
        return self.visitChildren(ctx)
    
    def visitModeStatement(self, ctx):
        #print('log: visitModeStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)
    
    def visitGlobalStatement(self, ctx):
        #print('log: visitGlobalStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)

    def visitParameterStatement(self, ctx):
        #print('log: visitParameterStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            # node parametlist
            if(i == 1):
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    temp_string = temp_ctx_j.getText().split('=')
                    self.dict_parameter[temp_string[0]] = '('+temp_string[1]+')'
                    self.fp.write(temp_ctx_j.getText()+' ')
            else:
                self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)

    def visitIncludeStatement(self, ctx):
        #print('log: visitIncludeStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)

    #BODY Visitor
    #TODO(Li): analysisStatement | controlStatement | modelStatement |  
    def visitInstanceStatement(self, ctx):
        #print('log: visitInstanceStatement')
        dev_name = ctx.getChild(2).getText()
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            # nodeList
            if(i == 1):
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    self.fp.write(temp_ctx_j.getText()+' ')
            # paramList
            elif(i == 3):
                dict_instanceparamList = {}
                exp = ''
                for j in range(0,temp_ctx.getChildCount()):
                    exp = exp + temp_ctx.getChild(j).getText() + ' '
                    temp_string = temp_ctx.getChild(j).getText().split('=')
                    dict_instanceparamList[temp_string[0]] = '('+temp_string[1]+')'
                exp = self.desanitization(dev_name,exp,dict_instanceparamList)
                self.fp.write(exp+' ')
            else:
                self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)

    def visitSubCircuit(self, ctx):
        #print('log: visitSubCircuit')
        for i in range(0,6):
            temp_ctx = ctx.getChild(i)
            #nodelist
            if(i == 2):
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    self.fp.write(temp_ctx_j.getText()+' ')
                self.fp.write('\n')
            elif(i == 3):
                x = self.visitChildren(ctx)
            else:
                self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return x

    def visitControlStatement(self, ctx):
        #print('log: visitControlStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            if(i == 2):
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    self.fp.write(temp_ctx_j.getText()+' ')
            else:
                self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)

    def visitIcStatement(self, ctx):
        #print('log: visitIcStatement')
        for i in range(0,ctx.getChildCount()):
            temp_ctx = ctx.getChild(i)
            if(i == 1):
                for j in range(0,temp_ctx.getChildCount()):
                    temp_ctx_j = temp_ctx.getChild(j)
                    self.fp.write(temp_ctx_j.getText()+' ')
            else:
                self.fp.write(temp_ctx.getText()+' ')
        self.fp.write('\n')
        return self.visitChildren(ctx)


    def visit(self,ctx):
        x = self.visitChildren(ctx)
        self.fp.close()
        return x




''' 
    # TEST
        print(type(ctx.getChild(3)),ctx.getChild(3).getChildCount())
        print(type(ctx.getChild(3).getChild(0)),dir(ctx.getChild(3).getChild(0)))
        print('\n')
        exp = ctx.getChild(3).getChild(0)
        exp2 = ctx.getChild(3).getChild(1)
        print('rule context',exp.getRuleContext())
        print('payload',exp.getPayload())
        print('altnumber',exp.getAltNumber())
        print('ruleindex',exp.getRuleIndex())
        print('ruleindex',exp2.getRuleIndex())
        print('ruleindex',ctx.getChild(3).getRuleIndex())



'''
