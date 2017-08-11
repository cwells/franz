?program: expr*

?expr: boolean
     | assign
     | call
     | ifcond
     | forloop
     | whileloop
     | irange
     | function
     | "{" expr* "}"     -> block
     | expr "+" expr     -> add
     | assertion
     | tryrescue
//     | array
//     | array "+" array   -> add

?assign: name "=" expr

?tryrescue: "try" expr "rescue" expr [ "else" expr ] -> tryrescue

?function: "fn" "(" signature* ")" expr              -> function
?signature: (name ":" name ("," name ":" name)*)     -> signature

//?array: "[" arrayitem* "]"
//?arrayitem: expr ("," expr)*

?call: name "(" assoc* ")"
?assoc: name ":" expr ("," name ":" expr)*

?irange: term "to" term [ "step" term ]              -> irange
?forloop: "for" name "in" expr expr                  -> forloop
?ifcond: "if" boolean expr [ "else" expr ]           -> ifcond
?whileloop: "while" boolean expr                     -> whileloop
?assertion: "assert" boolean                         -> assertion

?boolean: cmp ((AND|OR) cmp)*

?cmp: term
    | cmp "<" term       -> cmp_lt
    | cmp ">" term       -> cmp_gt
    | cmp "<=" term      -> cmp_lteq
    | cmp ">=" term      -> cmp_gteq
    | cmp "==" term      -> cmp_eq
    | cmp "<>" term      -> cmp_neq

?term: factor
    | term "+" factor    -> add
    | term "-" factor    -> sub

?factor: pow
    | factor "*" pow     -> mul
    | factor "/" pow     -> div
    | factor "//" pow    -> floor
    | factor "%" pow     -> mod

?pow: atom
    | pow "^" atom       -> pow

?atom: INTEGER           -> integer
    | DECIMAL            -> decimal
    | name               -> name
    | STRING             -> string
    | "-" atom           -> negation
    | "true"             -> true
    | "false"            -> false
    | "nil"              -> nil
    | "[" arrayitem* "]" -> array
    | "(" expr ")"

?arrayitem: expr ("," expr)* -> arrayitem
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
