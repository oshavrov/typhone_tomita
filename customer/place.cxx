#encoding "utf-8"
#GRAMMAR_ROOT S

CallPlace -> Word<wff=/уу/>;

S -> CallPlace interp(CustomerPlace.Place);
