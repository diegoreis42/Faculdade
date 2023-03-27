/* Made by Diego Reis 27/03/2023
*/

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

// Armazena:
// Vetor de inteiros
// Tamanho do vetor
// Valor do erro: 1, 2 ou 3; especificados na funçao trataErro
typedef struct tReturn {
  int *vet;
  int tam;
  int erro;
}tReturn;

tReturn* alocaReturn(){
  tReturn *rep = (tReturn*) malloc(sizeof(tReturn));

  return rep;
}


int *getVet(tReturn *rep){
  return rep->vet;
}

int getTam(tReturn *rep){
  return rep->tam;
}

int getErro(tReturn *rep){
  return rep->erro;
}

// recebe tReturn rep->erro;
void trataErro(int erro){
  if(erro == 1)
    printf("Erro ao abrir o arquivo\n");
  else if(erro == 2)
    printf("Erro ao ler do arquivo\n");
  else
    printf("Erro ao alocar memória\n");
}

// Le arquivo contendo sequencia de inteiros
// Primeiro valor eh o tamanho da sequencia
// Retorna: tReturn contendo o vetor, tamanho, e tipo de erro(se houver)
tReturn* leArquivo(char nomeArquivo[]){
  tReturn *rep = alocaReturn();
  FILE *fptr = fopen(nomeArquivo, "r");
// Checa erro ao abrir o arquivo
  if(fptr == NULL){
    rep->erro = 1;
    return rep;
  }
// Checa erro ao alocar memoria
  if(rep == NULL){
    rep->erro = 3;
    return rep;
  }


  fscanf(fptr, "%d", &rep->tam);
  rep->vet = (int*) malloc(sizeof(int) * (rep->tam));
  
  for(int i = 0; i < (rep->tam); i++){
    // Checa erro ao ler o arquivo
    if(fscanf(fptr, "%d", &rep->vet[i]) != 1){
        rep->erro = 2;
        return rep;
    }

  }
  return rep;
}
/*  Algoritmo de ordenaçao Bubble sort
 * -------------------------------------
 *  Pior caso -> O(n^2)
 *  Melhor caso -> O(n^2)
 * */

int bolha(int *vet, int tam){
  int aux, counter = 0;
  for(int i = 0; i < tam; i++){
    for(int j = 1; j < tam; j++){
      if(vet[j] < vet[j - 1]){
        aux = vet[j - 1];
        vet[j - 1] = vet[j];
        vet[j] = aux;
      }
      counter++;
    }
  }

    return counter;
}

/*  Algoritmo de ordenaçao Smart Bubble sort
 * ------------------------------------------
 *  Pior caso -> O(n^2)
 *  Melhor caso -> O(n)
 *  Explicaçao
 * ------------------------------------------
 *  Como maior numero da parte desordenada sempre
 *  vai ser posto na posiçao correta, eh desneces-
 *  sario checar os valores apos ele, por isto o
 *  tam - i. Alem disso, ele checa se o vetor ja
 *  esta ordenado.
 * */
int bolhaInteligente(int *vet, int tam){

  int aux, counter = 0;
  bool swaped = false;

  for(int i = 0; i < tam; i++){
    for(int j = 1; j < tam - i; j++){
      if(vet[j] < vet[j - 1]){
        aux = vet[j - 1];
        vet[j - 1] = vet[j];
        vet[j] = aux;
        swaped = true;
      }
      counter++;
    }
    if(swaped == false)
      break;
  }


return counter;
}


void imprimeVet(int *vet, int tam){
  for(int i = 0; i < tam; i++){
    printf("%d\n", vet[i]);
  }
}
