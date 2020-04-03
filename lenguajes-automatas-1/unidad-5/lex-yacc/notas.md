Gramática BNF para el lenguaje "Yoda"

Esta gramática recibe una frase de entrada con la estructura: SVO (Sujeto,
Verbo, Predicado)

<frase> ::= <sujeto> <verbo> <objeto>   
<sujeto> ::= <artículo> <sustantivo> | La persona   
<artículo> ::= el | la | los | las | uno | unos | un | ...   
<sustantivo> ::= gato | perro | hombre | mujer | computadora | robot   
<verbo> ::= hizo | corrió | comió | programó | enseñó   
<objeto> ::= <artículo> <sustantivo> | dos memorias   
