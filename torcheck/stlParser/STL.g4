grammar STL;

prog :   formula NEWLINE                 # textFormula
    | formula                            # plainFormla
//    |   PARAMETERS EQ expr NEWLINE      # assign
    |   NEWLINE                         # blank
    ;

formula : LPAR formula op=(AND|OR) formula  RPAR           # AndOr
	|	 NOT formula                                       # Not
//	|    expr op=(GT|GE|LT|LE|E) expr                        # Atom
	|    var op=(GE|LE) expr                               # Atom
	|    LPAR formula RPAR                                 # parensFormula
//	|    op =(TRUE|FALSE)                                  # trueFalse
//	|	 LPAR formula RPAR U  interval LPAR formula RPAR   # U
    |	 LPAR formula U  interval formula RPAR             # U
	|    F  interval LPAR formula RPAR                     # F
	|	 G  interval LPAR formula RPAR                     # G
	;

var: X UNDERSCORE NATURAL  # atomicPredicate
    ;

interval : LBRAT  expr COMMA  expr RBRAT # timeBounds
    |  LBRAT expr COMMA INF RBRAT        # rightUnbound
    |                                    # emptyTimeBounds
	;

expr:   NUMBER                              # number
    |   MINUS NUMBER                        # negNumber
    |   NATURAL                               # natural
    |   MINUS NATURAL                         # negNatural
//    |   op=(PARAMETERS|SERIES)              # id
//    |   LPAR expr RPAR                      # parensExpr
//    | expr op=(MULT|DIV|PLUS|MINUS) expr      # AlgOp
    ;

// PARAMETERS:     [a-z]+ ;
// SERIES  :       [A-Z] ([A-Z] | [0-9])* ;

NATURAL : [0-9]+ ;
NUMBER : NATURAL+ ('.' NATURAL+) ;




LPAR    :       '(';
RPAR    :       ')';
COMMA   :       ',';
LBRAT   :       '[';
RBRAT   :       ']';
U       :	'until';
F       :	'eventually';
G       :	'always';
INF     :   'inf';

// TRUE	:	'True';
// FALSE	:	'False';

// PLUS	:	'+';
MINUS	:	'-';
// MULT	:	'*';
UNDERSCORE : '_';
// DIV	:	'/';

AND	:	'and';
OR	:	'or';
NOT	:	'not';

EQ	:	'=';
// NEQ	:	'!=';
// GT	:	'>';
GE	:	'>=';
// LT	:	'<';
LE	:	'<=';
// E	:	'==';

X   :   'x';




// $<Terminal

//INTEGER	:	'0'..'9'+
//	;

// NUMBER :
//	:   ('0'..'9')+ ('.')* ('0'..'9')* EXPONENT?
//	|   '.' ('0'..'9')+ EXPONENT?
//	|   ('0'..'9')+ EXPONENT
//	;


// fragment
// EXPONENT : ('e'|'E') ('+'|'-')? ('0'..'9')+ ;



// ID	:	('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*
//	;

NEWLINE	:	( '\r'| '\n' )
	;

// $>


// $<White space

COMMENT
    :   ('//' ~('\n'|'\r')*)->channel(HIDDEN)
    ;

/* Ignore white space characters, except from newline */
WS
    :   (' ' | '\t' | NEWLINE )->channel(HIDDEN)
    ;
// $>