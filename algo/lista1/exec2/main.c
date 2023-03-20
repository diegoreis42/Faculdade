#include <stdio.h>
#include "arquivo.h"

int main()
{
    //VARIÁVEIS
    int opcao = 0;
    int qtd;
    int res;
    int seed;
    char nome[50];
    int *vet = NULL;

    do {
        //menu
        printf("\nEscolha uma opcao: \n");
        printf("1. Gravar números aleatórios\n");
        printf("2. Ler arquivo\n");
        printf("3. Sair\n");

        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite a quantidade de dados desejada: ");
                scanf("%d", &qtd);
                printf("\nInforme o nome do arquivo de saida: ");
                scanf("%s", nome);
                printf("\nInforme a semente: ");
                scanf("%d", &seed);
                res = geraArquivo(nome, qtd, seed);
                if (res == -1)
                    printf("\nFalha ao gerar arquivo de numeros aleatorios.\n");
                else
                    printf("\nArquivo de numeros aleatorios gerado com seucesso\n");
                break;

            case 2:
            printf("\nInforme o nome do arquivo de entrada: ");
            scanf("%s", nome);
            leArquivo(nome);
            break;

            case 3:
                break;

        }
    } while (opcao != 3);

    return 0;
}
