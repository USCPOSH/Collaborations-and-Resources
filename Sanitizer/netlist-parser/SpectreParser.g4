parser grammar SpectreParser;

options { tokenVocab=SpectreLexer; }

//import SpectreLexer;


// Main
netlist
    : ( header
        body
        saveSection?
        EOF
      )
    | (
        LINE_COMMENT*
        modeStatement
        library
        EOF
      )
    ;

header
    : LINE_COMMENT* modeStatement globalStatement (includeStatement | LINE_COMMENT)* parameterStatement? (includeStatement | LINE_COMMENT)*
    ;

// Mode Statement
modeStatement
    : SIMULATOR LANG '=' LANGUAGES assignment*
    ;

// Gobal statement
// TODO: Li: extension
globalStatement
    : GLOBAL INT_LITERAL*
    ;

// Include Statement
includeStatement
    : 'include' STR_LITERAL ('section' '=' IDENTIFIER)?
    | HASH 'include' STR_LITERAL ('section' '=' IDENTIFIER)?
    ;

// Parameter Statement
parameterStatement
    : 'parameters' paramList
    ;

paramList
    : '(' assignment* ')'
    | assignment*
    ;

assignment
    : IDENTIFIER '=' expression
    ;

expression
    : '(' expression ')'
    | BUILT_IN_FUNCTIONS '(' expression ')'
    | BUILT_IN_CONSTANTS
    | INT_LITERAL
    | STR_LITERAL
    | vector
    | methodCall
    | prefix=('+'|'-') expression
    | expression bop='**' expression
    | expression bop=('*'|'/') expression
    | expression bop=('+'|'-') expression
    | expression ('<<' | '>>') expression
    | expression bop=('<=' | '>=' | '>' | '<') expression
    | expression bop=('==' | '!=') expression
    | expression bop='&' expression
    | expression bop=XOR expression
    | expression bop='&&' expression
    | expression bop='||' expression
    | <assoc=right> expression bop='?' expression ':' expression
    | IDENTIFIER
    ;

vector
    : '[' vectorExpression* ']'
    ;

vectorExpression
    : '(' vectorExpression ')'
    | BUILT_IN_CONSTANTS
    | INT_LITERAL
    | STR_LITERAL
    | '[' vectorExpression* ']'
    | '(' methodCall ')'
    | prefix=('+'|'-') vectorExpression
    | vectorExpression bop='**' vectorExpression
    | vectorExpression bop=('*'|'/') vectorExpression
    | vectorExpression bop=('+'|'-') vectorExpression
    | vectorExpression ('<<' | '>>') vectorExpression
    | vectorExpression bop=('<=' | '>=' | '>' | '<') vectorExpression
    | vectorExpression bop=('==' | '!=') vectorExpression
    | vectorExpression bop='&' vectorExpression
    | vectorExpression bop='|' vectorExpression
    | vectorExpression bop=XOR vectorExpression
    | vectorExpression bop='&&' vectorExpression
    | vectorExpression bop='||' vectorExpression
    | vectorExpression bop='?' vectorExpression ':' vectorExpression
    | IDENTIFIER
    ;

methodCall
    : (BUILT_IN_FUNCTIONS | IDENTIFIER) '(' expression ')'
    ;

body
    : (instanceStatement | analysisStatement | controlStatement | modelStatement | subCircuit | ifBlock | functionBlock | LINE_COMMENT | icStatement | includeStatement)*
    ;

// ic Statement
icStatement
    : 'ic' paramList
    ;

// Instance Statement
instanceStatement
    : IDENTIFIER nodeList (primitives | IDENTIFIER) paramList
    ;

primitives
    : RESISTOR
    | CAPACITOR
    | BJT
    | NMOS
    ;

// Analysis Statement
analysisStatement
    : IDENTIFIER nodeList analysisType paramList
    ;

analysisType
    : IDENTIFIER
    ;

/*
analysisTypes
    : AC
    | DC
    | NOISE
    | TDR
    | ENVLP
    | PDISTO
    | PNOISE
    | PSS
    | PXF
    | SP
    | TRAN
    | XF
    | SENS
    | FOURIER
    | DCMATCH
    | STB
    | SWEEP
    | MONTECARLO
    ;
*/

// Control Statement
controlStatement
    : IDENTIFIER controlStatementTypes paramList
    | IDENTIFIER 'altergroup' alterGroupBody
    ;

alterGroupBody
    : '{' (parameterStatement | instanceStatement | modelStatement | includeStatement)* '}'
    ;

controlStatementTypes
    : 'alter'
    | 'check'
    | 'ic'
    | 'info'
    | 'nodeset'
    | 'options'
    | 'paramset'
    | 'save'
    | 'set'
    | 'shell'
    | 'statistics'
    ;

// Model Statement
modelStatement
    : 'model' IDENTIFIER (primitives | IDENTIFIER) paramList
    ;

subCircuit
    : ('subckt' IDENTIFIER  | 'inline' 'subckt' IDENTIFIER ) nodeList
      subCircuitBody
      'ends' IDENTIFIER
    ;

subCircuitBody
    : parameterStatement?
      body
    ;

ifBlock
    : 'if' parExpression ifBody ('else' elseBody)?
    ;

parExpression
    : '(' expression ')'
    ;

ifBody
    : '{' (instanceStatement | ifBlock)* '}'
    ;

elseBody
    : '{' (instanceStatement | ifBlock)* '}'
    ;


functionBlock
    : rType IDENTIFIER '(' (rType IDENTIFIER)* ')' functionBody
    ;

rType
    : 'real'
    ;

functionBody
    : '{' 'return' expression ';' '}'
    ;

saveSection
    : saveStatement+
    ;

saveStatement
    : 'save' (
        qualifiedName
        | qualifiedName ':' (saveModifiers | IDENTIFIER)
        | ':' (saveModifiers | IDENTIFIER)
      )
    ;

saveModifiers
    : 'currents'
    | 'static'
    | 'displacement'
    | 'dynamic'
    | 'oppoint'
    | 'probe'
    | 'pwr'
    ;

nodeList
    : '(' (INT_LITERAL | IDENTIFIER)* ')'
    | (INT_LITERAL | IDENTIFIER)*
    ;

modelBlockTypes
    : INT_LITERAL ':' paramList
    ;

modelBlock
    : '{' modelBlockTypes+ '}'
    ;

sectionBody
    : (
          LINE_COMMENT
        | includeStatement
        | parameterStatement
        | statisticsBlock
        | subCircuit
        | modelStatement
        | modelBlock
      )*
    ;

section
    : 'section' IDENTIFIER
      sectionBody
      'endsection' IDENTIFIER
    ;

libraryBody
    : LINE_COMMENT*
      section*
    ;

library
    : 'library' IDENTIFIER
      libraryBody
      'endlibrary' IDENTIFIER
    ;

// Spectre userguide Page 186
// TODO: Improve
checkStatement
    : IDENTIFIER 'check' paramList
    ;

// Spectre userguide Page 187
// TODO: Set ic condition for Node

// Spectre userguide Page 189
// TODO: nodeset

// Spectre userguide Page 192
// TODO: Improve
infoStatement
    : IDENTIFIER 'info' paramList
    ;

// Spectre userguide Page 198
// TODO: Improve
optionsStatement
    : IDENTIFIER 'options' paramList
    ;

// Spectre userguide Page 200
// parameters p1=1 p2=2 p3=3
// data paramset {
// p1 p2 p3
// 5 5 5
// 4 3 2
// }
// TODO: Improve
paramsetStatement
    : IDENTIFIER 'paramset' paramsetBlock
    ;

paramsetBlock
    : '{' IDENTIFIER+ '}'
      (INT_LITERAL+)+
    ;

// Spectre userguide Page 210
setStatement
    : IDENTIFIER 'set' paramList
    ;

// Spectre userguide Page 211
shellStatement
    : IDENTIFIER 'shell' paramList
    ;

// Spectre userguide Page 170
// TODO: statistics statement
// The statistics blocks are used to specify the input statistical variations for a Monte Carlo
// analysis. A statistics block can contain one or more process blocks (which represent batchto-
// batch type variations) and/or one or more mismatch blocks (which represent on-chip or
// device mismatch variations), in which the distributions for parameters are specified. Statistics
// blocks can also contain one or more correlation statements to specify the correlations
// between specified process parameters and/or to specify correlated device instances (such as
// matched pairs). Statistics blocks can also contain a truncate statement that can be used
// for generating truncated distributions.
// statistics { process {}+ | mismatch {}+ | correlateStatement+ | truncateStatement   }

statisticsBlock
    : 'statistics'
      statisticsBody
    ;

statisticsBody
    : '{' (processBlock | mismatchBlock | correlateStatement )+ truncateStatement? '}'
    ;

processBlock
    : processBody
    ;

processBody
    : '{' varyStatement* '}'
    ;

mismatchBlock
    : 'mismatch' mismatchBody
    ;

mismatchBody
    : '{' varyStatement* '}'
    ;

// TODO: correlateStatement
correlateStatement
    : 'correlate' paramList
    ;


// TODO: truncateStatement
// TODO: Improve
truncateStatement
    : 'truncate' paramList
    ;

// TODO: varyStatement
varyStatement
    : 'vary' IDENTIFIER paramList
    ;

// TODO: Handle block analysis types

// From Java
qualifiedName
    : IDENTIFIER ('.' IDENTIFIER)*
    ;
