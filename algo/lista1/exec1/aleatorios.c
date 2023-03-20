#include <stdio.h>
#include <stdlib.h>



int * geraAleatorio(int qtd, int seed){
  srand(seed);

  int *vet = (int*) malloc(qtd * sizeof(int));

  for(int i = 0; i < qtd; i++){
    vet[i] = rand() % qtd + 1;
    printf("%d-", vet[i]);
  }
  printf("\n");

return vet;
}


int buscaElemento(int *vet, int qtd, int num){

  for (int i = 0; i < qtd; i++) {
    if(vet[i] == num)  
      return i;
  }

  return -1;
}


void libera_vetor(int *vet){
  free(vet);
}
