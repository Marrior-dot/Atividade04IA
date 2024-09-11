#include <stdio.h>

int reverter(int lista[], int novaLista[], int posNovaLista, int posAntigaLista){
    if(posAntigaLista == 0){
        //int *listaDeRetorno[sizeof(novaLista)/sizeof(novaLista[0])] = {};
        //for (int i = 0; i < sizeof(novaLista)/sizeof(novaLista[0]); i++)
        //{
        //    listaDeRetorno[i] = novaLista[i];
        //}
        //
        //return *listaDeRetorno;
        return *novaLista;
    }
    novaLista[posNovaLista] = lista[posAntigaLista];
    //printf("%d", *novaLista);
    //printf("%d", posAntigaLista);
    posNovaLista++;
    posAntigaLista--;

    return reverter(lista, novaLista, posNovaLista, posAntigaLista);
}

int main(int argc, char const *argv[])
{
    int lista[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int *listaRef = &lista;
    printf("%d", *listaRef);
    int *novaLista[] = {};
    //printf("%d", reverter(lista, novaLista, 0, 8));
    return 0;
}
