#include <stdio.h>
#include <stdlib.h>

int* reverter(int lista[], int tamanho, int posicao) {
    static int* novaLista = NULL;
    
    if (posicao == 0) {
        novaLista = (int*)malloc(tamanho * sizeof(int));
    }
    
    if (posicao >= tamanho) {
        return novaLista;
    }
    
    novaLista[tamanho - 1 - posicao] = lista[posicao];
    return reverter(lista, tamanho, posicao + 1);
}
void modulo(){
int lista[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int tamanho = sizeof(lista) / sizeof(lista[0]);
    
    int* listaInvertida = reverter(lista, tamanho, 0);
    
    printf("Lista invertida: ");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", listaInvertida[i]);
    }
    printf("\n");
    
    free(listaInvertida);
}

int main() {
    modulo();
    return 0;
}