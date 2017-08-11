?program: expr*

?expr: boolean
     | assign
     | call
     | ifcond
     | forloop
     | whileloop
     | irange
     | array
     | function
     | "{" expr* "}"     -> block
     | expr "+" expr     -> add
     | array "+" array   -> add
     | assertion
     | tryrescue
//     | casecond

?tryrescue: "try" expr "rescue" expr [ "else" expr ] -> tryrescue

?function: "fn" "(" signature* ")" expr              -> function
?signature: (name ":" name ("," name ":" name)*)     -> signature

?array: "[" arrayitem* "]"
?arrayitem: expr ("," expr)*

?call: name "(" assoc* ")"
?assoc: name ":" expr ("," name ":" expr)*

?irange: term "to" term [ "step" term ]              -> irange
?forloop: "for" name "in" expr expr                  -> forloop
?ifcond: "if" boolean expr [ "else" expr ]           -> ifcond
?whileloop: "while" boolean expr                     -> whileloop

//?casecond: "case" name "is" "{" (regex|expr) expr ((regex|expr) expr)* "}" [ "else" expr ]
//?regex: /\/[^\/]+?\//

?assign: name "=" expr

?assertion: "assert" boolean                         -> assertion

?boolean: cmp ((AND|OR) cmp)*

?cmp: term
    | term "<" term     -> cmp_lt
    | term ">" term     -> cmp_gt
    | term "<=" term    -> cmp_lteq
    | term ">=" term    -> cmp_gteq
    | term "==" term    -> cmp_eq
    | term "<>" term    -> cmp_neq

?term: factor
    | term "+" factor   -> add
    | term "-" factor   -> sub

?factor: pow
    | factor "*" pow    -> mul
    | factor "/" pow    -> div
    | factor "//" pow   -> floor
    | factor "%" pow    -> mod

?pow: atom
    | pow "^" atom      -> pow

?atom: INTEGER          -> integer
    | DECIMAL           -> decimal
    | name              -> name
    | STRING            -> string
    | "-" atom          -> negation
    | "true"            -> true
    | "false"           -> false
    | "nil"             -> nil
    | "[" expr "]"      -> array
    | "(" expr ")"

?name: NAME

COMMENT: /\#[^\n]*/
NAME: ( LETTER | "@" LETTER) ("_"|"-"|"?"|"!"|LETTER|DIGIT )*
DECIMAL: INTEGER "." DIGIT+
AND: "and"
OR: "or"
NOT: "not"

%import common.WS               -> WHITESPACE
%import common.ESCAPED_STRING   -> STRING
%import common.LETTER           -> LETTER
%import common.SIGNED_INT       -> INTEGER
%import common.DIGIT            -> DIGIT

%ignore WHITESPACE
%ignore COMMENT
