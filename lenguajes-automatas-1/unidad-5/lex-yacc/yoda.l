
%%
"el"    {yylval=0; return(ARTICULO);}
"la"    {yylval=1; return(ARTICULO);}
"gato"  {yylval=2; return(SUSTANTIVO);}
"perro" {yylval=3; return(SUSTANTIVO);}
"mujer" {yylval=4; return(SUSTANTIVO);}
"hombre"    {yylval=5; return(SUSTANTIVO);}
"computadora"   {yylval=6; return(SUSTANTIVO);}
"robot" {yylval=7; return(SUSTANTIVO);}
"hizo"  {yylval=8; return(VERBO);}
"mordio"    {yylval=9; return(VERBO);}
"come"  {yylval=10; return(VERBO);}
"programa"  {yylval=11; return(VERBO);}
"ve"    {yylval=12; return(VERBO);}
"estudia"   {yylval=13; return(VERBO);}
"el alumno" {yylval=14; return(SUJETO);}
"la alumna" {yylval=15; return(SUJETO);}
"la computadora"    {yylval=16; return(SUJETO);}
"programacion"  {yylval=17; return(OBJETO);}
"pastel"    {yylval=18; return(OBJETO);}
"platano"   {yylval=19; return(OBJETO);}
"robots"    {yylval=20; return(OBJETO);}
"sitios web"    {yylval=21; return(OBJETO);}
"&"     {return('&');}
"\n"    {return('\n');}
%%