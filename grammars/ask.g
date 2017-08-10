?program: expr*

?expr: boolean
     | assign
     | call
     | ifcond
     | forloop
     | irange
     | array
     | function
     | "{" expr* "}"     -> block
     | expr "+" expr     -> add
     | array "+" array   -> add
//     | casecond

?function: "fn" "(" params* ")" expr
?params: (arrayitem ":" name ("," arrayitem ":" name)*)    -> params

?array: "[" arrayitem* "]"
?arrayitem: expr ("," expr)*

?call: name "(" assoc* ")"
?assoc: name ":" expr ("," name ":" expr)*

?irange: term "to" term [ "step" term ]     -> irange

?forloop: "for" name "in" expr expr

?ifcond: "if" boolean expr [ "else" expr ]

//?casecond: "case" name "is" "{" (regex|expr) expr ((regex|expr) expr)* "}" [ "else" expr ]
//?regex: /\/[^\/]+?\//

?assign: name "=" expr

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

?factor: atom
    | factor "*" atom   -> mul
    | factor "/" atom   -> div

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
