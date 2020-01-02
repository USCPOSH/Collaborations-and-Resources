lexer grammar SpectreLexer;

// https://stackoverflow.com/questions/31903723/how-to-detect-beginning-of-line-or-the-name-getcharpositioninline-does-not
// BOL: {getCharPositionInLine() == 0;};
// BOL : [\r\n\f]+ ;

LINE_COMMENT: ('//' | Newline+ Whitespace* '*' ) ~[\r\n]*;

// Keywords

SIMULATOR: 'simulator';
LANG: 'lang';
INCLUDE: 'include';
PARAMETERS: 'parameters';
MODEL: 'model';
INLINE: 'inline';
SUBCKT: 'subckt';
ENDS: 'ends';
LIBRARY: 'library';
SECTION: 'section';
ENDSECTION: 'endsection';
ENDLIBRARY: 'endlibrary';
SAVE: 'save';
IF: 'if';
ELSE: 'else';
REAL: 'real';
RETURN: 'return';
CORRELATE: 'correlate';
VARY: 'vary';
TRUNCATE: 'truncate';
PROCESS: 'process';
MISMATCH: 'mismatch';

// Reserved Names

// Pr-defined constants

/// M_E: 'M_E';
/// M_LOG2E: 'M_LOG2E';
/// M_LOG10E: 'M_LOG10E';
/// M_LN2: 'M_LN2';
/// M_LN10: 'M_LN10';
/// M_PI: 'M_PI';
/// M_TWO_PI: 'M_TWO_PI';
/// M_PI_2: 'M_PI_2';
/// M_PI_4: 'M_PI_4';
/// M_1_PI: 'M_1_PI';
/// M_2_PI: 'M_2_PI';
/// M_2_SQRTPI: 'M_2_SQRTPI';
/// M_SQRT2: 'M_SQRT2';
/// M_SQRT1_2: 'M_SQRT1_2';
/// M_DEGPERRAD: 'M_DEGPERRAD';
/// P_Q: 'P_Q';
/// P_C: 'P_C';
/// P_K: 'P_K';
/// P_H: 'P_H';
/// P_EPS0: 'P_EPS0';
/// P_U0: 'P_U0';
/// P_CELSIUS0: 'P_CELSIUS0';

//BUILT_IN_CONSTANTS
//    : 'M_' UppercaseLetter+
//    | 'P_' UppercaseLetter+
//    ;

BUILT_IN_CONSTANTS
    : 'M_E'
    | 'M_LOG2E'
    | 'M_LOG10E'
    | 'M_LN2'
    | 'M_LN10'
    | 'M_PI'
    | 'M_TWO_PI'
    | 'M_PI_2'
    | 'M_PI_4'
    | 'M_1_PI'
    | 'M_2_PI'
    | 'M_2_SQRTPI'
    | 'M_SQRT2'
    | 'M_SQRT1_2'
    | 'M_DEGPERRAD'
    | 'P_Q'
    | 'P_C'
    | 'P_K'
    | 'P_H'
    | 'P_EPS0'
    | 'P_U0'
    | 'P_CELSIUS0'
    ;

// Pr-defined methods

/// LOG: 'log';
/// LOG10: 'log10';
/// EXP: 'exp';
/// SQRT: 'sqrt';
/// MIN: 'min';
/// MAX: 'max';
/// ABS: 'abs';
/// POW: 'pow';
/// SIN: 'sin';
/// COS: 'cos';
/// TAN: 'tan';
/// ASIN: 'asin';
/// ACOS: 'acos';
/// ATAB: 'atan';
/// ATAN2: 'atan2';
/// SINH: 'sinh';
/// COSH: 'cosh';
/// TANH: 'tanh';
/// ASINH: 'asinh';
/// ACOSH: 'acosh';
/// ATANH: 'atanh';
/// CEIL: 'ceil';
/// FLOOR: 'floor';
/// HYPOT: 'hypot';
/// INT: 'int';
/// FMOD: 'fmod';

BUILT_IN_FUNCTIONS
    : 'log'
    | 'log10'
    | 'exp'
    | 'sqrt'
    | 'min'
    | 'max'
    | 'abs'
    | 'pow'
    | 'sin'
    | 'cos'
    | 'tan'
    | 'asin'
    | 'acos'
    | 'atan'
    | 'atan2'
    | 'sinh'
    | 'cosh'
    | 'tanh'
    | 'asinh'
    | 'acosh'
    | 'atanh'
    | 'ceil'
    | 'floor'
    | 'hypot'
    | 'int'
    | 'fmod'
    ;

// Usage unknown

END: 'end';
EXPORT: 'export';
FOR: 'for';
FUNCTION: 'function';
GLOBAL: 'global';
LOCAL: 'local';
MARCH: 'march';
MODELNODESET: 'modelnodeset';
PLOT: 'plot';
PRINT: 'print';
RETURNSAVE: 'returnsave';
TO: 'to';

// SCS Primitives

RESISTOR: 'resistor';
CAPACITOR: 'capacitor';
BJT: 'bjt';
NMOS: 'nmos';

// Analysis Types

// AC: 'ac';
// DC: 'dc';
// NOISE: 'noise';
// TDR: 'tdr';
// ENVLP: 'envlp';
// PDISTO: 'pdisto';
// PNOISE: 'pnoise';
// PSS: 'pss';
// PXF: 'pxf';
// SP: 'sp';
// TRAN: 'tran';
// XF: 'xf';
// SENS: 'sens';
// FOURIER: 'fourier';
// DCMATCH: 'dcmatch';
// STB: 'stb';
// SWEEP: 'sweep';
// MONTECARLO: 'montecarlo';

// Control Types

ALTER: 'alter';
ALTERGROUP: 'altergroup';
CHECK: 'check';
IC: 'ic';
INFO: 'info';
NODESET: 'nodeset';
OPTIONS: 'options';
PARAMSET: 'paramset';
SET: 'set';
SHELL: 'shell';
STATISTICS: 'statistics';

// Save Modifiers

CURRENT: 'currents';
STATIC: 'static';
DISPLACEMENT: 'displacement';
DYNAMIC: 'dynamic';
OPPOINT: 'oppoint';
PROBE: 'probe';
PWR: 'pwr';


// Literals

//INT_LITERAL
//    :    ('0' | [1-9] (Digits? | '_'+ Digits)) (ExponentPart | ScaleFactors)?
//   ;
INT_LITERAL
    : (Digits '.' Digits? | '.' Digits) (ExponentPart | ScaleFactors)? PreDefinedQuantities?
    | Digits (ExponentPart | ScaleFactors)? PreDefinedQuantities?
    ;

STR_LITERAL
    : '"' (~["\\\r\n] | EscapeSequence)* '"'
    ;


// Separators

LPAREN:             '(';
RPAREN:             ')';
LBRACE:             '{';
RBRACE:             '}';
LBRACK:             '[';
RBRACK:             ']';
SEMI:               ';';
//COMMA:              ',';
DOT:                '.';
HASH: '#';
COLON:               ':';

// Operators

ASSIGN:             '=';
GT:                 '>';
LT:                 '<';
EQUAL:              '==';
LE:                 '<=';
GE:                 '>=';
NOTEQUAL:           '!=';
AND:                '&&';
OR:                 '||';
INC:                '++';
DEC:                '--';
ADD:                '+';
SUB:                '-';
MUL:                '*';
DIV:                '/';
QUESTION:           '?';
BITAND:             '&';
BITOR:              '|';
XOR:              '^~' | '~^';
POW:              '**';
LSHIFT:           '<<';
RSHIFT:           '>>';

LANGUAGES: 'spectre' | 'spice';

// Identifiers
IDENTIFIER
    : Letter (LetterOrDigit | IdentifierEscapeSequence)*
    ;

// Whitespace and comments
// TODO: Add support for comments starting with *

// LINE_COMMENT: ('//' | Newline Whitespace* '*' ) ~[\r\n]*;

// Fragment rules


SCALE_FACTORS
    : [TGMKk_%cmunpfa]
    ;

WS
    : ( Whitespace
        | Newline '+'?
        | '\\'
      )+
     -> channel(HIDDEN);

// Field Spearator is space, tab, punctuation, or continuation character
// Except ()=:
fragment FieldSeparator
    : Whitespace+
//    | [.,/#!$%^&*;{}-_`~]
    ;

fragment Digits
    : [0-9] ([0-9_]* [0-9])?
    ;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;

//fragment Continuation
//    : [\\]
//    | '+'
//    ;

fragment Newline
    : [\r\n\f]
    ;

fragment Whitespace
    : [ \t]
    ;

fragment Digit
    : [0-9]
    ;

fragment UppercaseLetter
    : [A-Z_]
    ;

fragment Letter
    : [a-zA-Z_]
    ;

fragment IdentifierEscapeSequence
    : '\\' [.,/#!$%^&*;:{}=\-_`~() btnfr"'\\<>]
    ;

fragment EscapeSequence
    : '\\' [.,/#!$%^&*;:{}=\-_`~() btnfr"'\\]
    ;

fragment PreDefinedQuantities
    : ('A' | 'MMF' | 'V' | 'Wb' | 'C' | 'W' | 'U')
    ;

fragment ScaleFactors
    : [TGMKk_%cmunpfa]
    ;

fragment ExponentPart
    : [eE] [+-]? Digits
    ;
