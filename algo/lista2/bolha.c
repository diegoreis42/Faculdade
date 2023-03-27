#include <stdlib.h>
#include <stdio.h>


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

void trataErro(int erro){
  if(erro == 1)
    printf("Erro ao abrir o arquivo\n");
  else if(erro == 2)
    printf("Erro ao ler do arquivo\n");
  else
    printf("Erro ao alocar memória\n");
}

tReturn* leArquivo(char nomeArquivo[]){
  tReturn *rep = alocaReturn();
  FILE *fptr = fopen(nomeArquivo, "r");

  if(fptr == NULL){
    rep->erro = 1;
    return rep;
  }

  if(rep == NULL){
    rep->erro = 3;
    return rep;
  }


  fscanf(fptr, "%d", &rep->tam);
  rep->vet = (int*) malloc(sizeof(int) * (rep->tam));
  
  for(int i = 0; i < (rep->tam); i++){
    if(fscanf(fptr, "%d", &rep->vet[i]) != 1){
        rep->erro = 2;
        return rep;
    }

  }
  return rep;
}


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

int bolhaInteligente(int *vet, int tam){

  int aux, counter = 0, n = tam;
  for(int i = 0; i < tam; i++){
    for(int j = 1; j < n; j++){
      if(vet[j] < vet[j - 1]){
        aux = vet[j - 1];
        vet[j - 1] = vet[j];
        vet[j] = aux;
      }
      counter++;
    }
    n--;
  }


return counter;
}


void imprimeVet(int *vet, int tam){
  for(int i = 0; i < tam; i++){
    printf("%d\n", vet[i]);
  }
}
