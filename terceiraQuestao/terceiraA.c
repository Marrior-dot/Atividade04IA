#include <stdio.h>


int produto(int lista[], int esq, int dir){
    if (esq == dir){
        return 1;
    }
    return lista[esq] * produto(lista, esq+1, dir);
}

void chamarModulo(){
    int teste1[] = {2, 5, 1, 2, 3};
    int teste2[] = {1, 2, 3, 4, 5};
    printf("Resposta teste 1: %d\n", produto(teste1, 0, sizeof(teste1)/sizeof(teste1[0])));
    printf("Resposta teste 2: %d\n", produto(teste2, 0, sizeof(teste2)/sizeof(teste2[0])));
}

int main(int argc, char const *argv[])
{
    chamarModulo();
    return 0;
}




