int* produtoLista(int lista[], int x, int esq, int dir) {
    if (esq == dir) {
        return lista;
    }
    lista[esq] = lista[esq] * x;
    return produtoLista(lista, x, esq + 1, dir);
}

void modulo(){
    int var1[] = {10,2,55,2};
    int *var1Produto = produtoLista(var1, 10, 0, 5);
    int count = sizeof(var1Produto)/sizeof(int);

    printf("Lista multiplicada: ");
    for (int i = 0; i < 4; i++)
    {
        printf("%d ",var1Produto[i]);
    }
}

int main(int argc, char const *argv[])
{
   
    modulo();
    return 0;
}
