?program: expr*

?expr: logic
     | assign
     | assign_add
     | assign_sub
     | assign_mul
     | assign_div
     | assign_floor
     | assign_mod
     | assign_if
     | assign_many
     | assign_many_if
     | assoc
     | ifcond
     | forloop
     | whileloop
     | dowhile
     | irange
     | funcdef
     | "{" expr* "}"     -> block
     | expr "+" expr     -> add
     | assertion
     | tryrescue
     | break_expr
     | include_file

?include_file: "include" expr                        -> include_file

?assign: name "=" expr
?assign_add: name "+=" expr
?assign_sub: name "-=" expr
?assign_mul: name "*=" expr
?assign_div: name "/=" expr
?assign_mod: name "%=" expr
?assign_floor: name "//=" expr
?assign_if: name "?=" expr
?assign_many: "(" name ("," name)+ ")" "=" "(" expr ("," expr)+ ")"
?assign_many_if: name_list "?=" rval_list

?rval_list: ( "(" expr ("," expr)+ ")" | name )
?name_list: ( "(" name ("," name)+ ")" )

?tryrescue: "try" expr "rescue" expr [ "else" expr ] -> tryrescue

?funcdef: ("fn"|"ⲗ") "(" signature* ")" expr         -> funcdef
?signature: (name ":" name ("," name ":" name)*)     -> signature
?assoc: (name|string) ":" expr                       -> assoc

?irange: expr "to" expr [ "step" expr ]
    | "[" expr "to" expr [ "step" expr ] "]"         -> irange
?forloop: "for" name "in" expr expr                  -> forloop
?ifcond: "if" expr expr [ "else" expr ]              -> ifcond
?whileloop: "while" expr expr                        -> whileloop
?dowhile: "do" expr "while" expr                     -> dowhile
?assertion: "assert" expr                            -> assertion
// ?yield_expr: "yield" expr                            -> yield_expr
?break_expr: "break" expr*                           -> break_expr

?logic: cmp
    | logic "and" cmp        -> cmp_and
    | logic "or" cmp         -> cmp_or

?cmp: term
    | cmp "<" term           -> cmp_lt
    | cmp ">" term           -> cmp_gt
    | cmp "<=" term          -> cmp_lteq
    | cmp ">=" term          -> cmp_gteq
    | cmp "==" term          -> cmp_eq
    | cmp ("<>"|"!=") term   -> cmp_neq

?term: factor
    | term "+" factor        -> add
    | term "-" factor        -> sub

?factor: pow
    | factor "*" pow         -> mul
    | factor "/" pow         -> div
    | factor "//" pow        -> floor
    | factor "%" pow         -> mod

?pow: atom
    | pow "^" atom                  -> pow
    | pow "[" expr "]"              -> subscript
    | pow "[" expr? colon expr? "]" -> slice

?atom: INTEGER               -> integer
    | DECIMAL                -> decimal
    | name                   -> name
    | string                 -> string
    | "-" atom               -> negation
    | "true"                 -> true
    | "false"                -> false
    | "nil"                  -> nil
    | "(" expr ")"           -> expr
    | "return" expr          -> return_expr
    | "yield" expr           -> yield_expr
    | "[" arrayitem* "]"     -> array
    | name "(" args* ")"     -> call
    | name "(" args* ")" "->" name ("->" name)* -> chain
//    | call

// ?call: name "(" args* ")"
?colon: ":" -> colon
?args: expr ("," expr)*       -> args
?arrayitem: expr ("," expr)*  -> arrayitem

?name: NAME
?string: STRING

COMMENT: /\#[^\n]*/
NAME: ( (LETTER|"_") | "@" LETTER) ("-"|"_"|"?"|"!"|"%"|"$"|LETTER|DIGIT )*
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
