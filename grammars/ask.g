?program: expr*

?expr: cmp
     | assign
     | assoc
     | ifcond
     | forloop
     | whileloop
     | irange
     | funcdef
     | "{" expr* "}"     -> block
     | expr "+" expr     -> add
     | assertion
     | tryrescue
     | yield_expr
     | return_expr

?assign: name "=" expr

?tryrescue: "try" expr "rescue" expr [ "else" expr ] -> tryrescue

?funcdef: ("fn"|"ⲗ") "(" signature* ")" expr         -> funcdef
?signature: (name ":" name ("," name ":" name)*)     -> signature

?assoc: (name|string) ":" expr                       -> assoc

?irange: expr "to" expr [ "step" expr ]              -> irange
?forloop: "for" name "in" expr expr                  -> forloop
?ifcond: "if" expr expr [ "else" expr ]              -> ifcond
?whileloop: "while" expr expr                        -> whileloop
?assertion: "assert" expr                            -> assertion
?yield_expr: "yield" expr                            -> yield_expr
?return_expr: "return" expr                          -> return_expr


?cmp: term
    | cmp ("and"|"or") term -> cmp_log
    | cmp "<" term          -> cmp_lt
    | cmp ">" term          -> cmp_gt
    | cmp "<=" term         -> cmp_lteq
    | cmp ">=" term         -> cmp_gteq
    | cmp "==" term         -> cmp_eq
    | cmp "<>" term         -> cmp_neq

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
    | string             -> string
    | "-" atom           -> negation
    | "true"             -> true
    | "false"            -> false
    | "nil"              -> nil
    | name "(" args* ")" -> call
    | "[" arrayitem* "]" -> array
    | "(" expr ")"

?args: expr ("," expr)*      -> args
?arrayitem: expr ("," expr)* -> arrayitem

?name: NAME
?string: STRING

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
