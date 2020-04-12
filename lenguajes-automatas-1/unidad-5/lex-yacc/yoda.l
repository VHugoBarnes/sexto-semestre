%%
"el"    {yylval=1; return(ARTICULO);}
"la"    {yylval=2; return(ARTICULO);}
"gato"  {yylval=3; return(SUSTANTIVO);}
"perro" {yylval=4; return(SUSTANTIVO);}
"mujer" {yylval=5; return(SUSTANTIVO);}
"hombre"    {yylval=6; return(SUSTANTIVO);}
"computadora"   {yylval=7; return(SUSTANTIVO);}
"robot" {yylval=8; return(SUSTANTIVO);}
"hizo"  {yylval=9; return(VERBO);}
"mordio"    {yylval=10; return(VERBO);}
"come"  {yylval=11; return(VERBO);}
"programa"  {yylval=12; return(VERBO);}
"el alumno" {yylval=13; return(SUJETO);}
"la alumna" {yylval=14; return(SUJETO);}
"la computadora"    {yylval=15; return(SUJETO);}
"programacion"  {yylval=16; return(OBJETO);}
"pastel"    {yylval=17; return(OBJETO);}
"platano"   {yylval=18; return(OBJETO);}
%%