%{
# include <stdio.h>
# include <ctype.h>

char *tokens[] = {"el", "la", "gato", "perro", "mujer", "hombre", "computadora", "robot", \
 "hizo", "mordio", "come", "programa", "ve", "estudia", "el alumno", "la alumna", "la computadora", \
 "programacion", "pastel", "platano", "robots", "sitios web"};
char cadenasujeto[100],cadenaverbo[100],cadenaobjeto[100];

void iniciarpartes ()
{
    /* Inicializa las tres cadenas que mantienen los punteros 
    en varios componentes acomulados de una oracion*/
    int i;
    for (i=0; i < 100; i++){
        cadenasujeto[i] = cadenaverbo[i] = cadenaobjeto[i] = '0';
    }        
}
%}

%start lista

%token ARTICULO SUSTANTIVO VERBO SUJETO OBJETO

%%
lista:   {iniciarpartes();}
    |lista frase '\n'
        { iniciarpartes();
          printf("\nSiguiente frase por favor!\n\n");
        }
    |lista error '\n'
        { yyerror("Error de sintaxis. Saliendo..."); exit(1);}
    ;


frase:   '&'
            {printf("Final de las entradas, saliendo..."); exit(1);}
    |   sujeto verbo objeto
            { printf("\n\nYoda dice: %s %s %s\n", cadenaobjeto, cadenasujeto, cadenaverbo);
            }
    ;

sujeto:   ARTICULO SUSTANTIVO 
                { printf("Regla 1: %s %s", tokens[$1], tokens[$2]);
                  strcpy(cadenasujeto, tokens[$1]);
                  strcat(cadenasujeto, " ");
                  strcat(cadenasujeto, tokens[$2]);
                }
    |   SUJETO
                { printf("Regla 5: %s", tokens[$1]);
                  strcpy(cadenasujeto, tokens[$1]);
                }
    ;

verbo:   VERBO
                { printf("Regla 4: %s", tokens[$1]);
                  strcpy(cadenaverbo, tokens[$1]);
                }
    ;

objeto:   ARTICULO SUSTANTIVO
                { printf("Regla 5: %s %s", tokens[$1], tokens[$2]);
                  strcpy(cadenaobjeto, tokens[$1]);
                  strcat(cadenaobjeto, " ");
                  strcat(cadenaobjeto, tokens[$2]);
                }
    |   OBJETO
                { printf("Regla 5: %s", tokens[$1]);
                  strcpy(cadenaobjeto, tokens[$1]);
                }
    ;
%%
#include "lex.yy.c"



main(){
    return(yyparse() );

    }

yyerror(s)
    char *s;
{
    fprintf(stderr, "%s\n",s);

}