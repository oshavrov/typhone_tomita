#encoding "utf-8"
#GRAMMAR_ROOT S

CallPlace -> 'уу' | 'улан-удэ' | 'якутия' | 'якутск' | 'ykt' | 'як';

S -> CallPlace interp(CustomerPlace.Place);
