#include <stdio.h>
#include "aleatorios.h"

int main()
{
    //VARIÁVEIS
    int opcao = 0;
    int qtd;
    int num;
    int res;
    int seed;
    int *vet = NULL;

    do {
        //menu
        printf("\nEscolha uma opcao: \n");
        printf("1. Gerar números aleatórios\n");
        printf("2. Buscar um numero\n");
        printf("3. Sair\n\n");
        
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite a quantidade de dados desejada: ");
                scanf("%d", &qtd);
                printf("Digite a semente: ");
                scanf("%d", &seed);
                vet = geraAleatorio(qtd, seed);
                break;

            case 2:
                if (vet != NULL) {
                    printf("Digite o elemento buscado: ");
                    scanf("%d", &num);
                    res = buscaElemento(vet, qtd, num);
                    if (res == -1)
                        printf("\nElemento não existe no vetor\n");
                    else
                        printf("\nElemento encontrado na posicao %d vetor\n", res);
                    break;
                }
                else
                    printf("\nVoce deve gerar os numeros aleatorios primeiro.\n");

            case 3:
                break;

        }
    } while (opcao != 3);

    libera_vetor(vet);

    return 0;
}
