#include <stdlib.h>
#include <stdio.h>
#include <errno.h>


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
  int tam = sizeof(rep->vet) / sizeof(int);

  return tam;
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
  int *aux = NULL;
  tReturn *rep = alocaReturn();
  FILE *fptr = fopen(nomeArquivo, "r");

  switch (errno) {
    
    case ENOENT:
      rep->erro = 1;
      break;
    case EILSEQ:
      rep->erro = 2;
      break;
    case ENOMEM:
      rep->erro = 3;
      break;
    default:
      break;
  }

  fscanf(fptr, "%d", &rep->tam);
  rep->vet = (int*) malloc(sizeof(int) * (rep->tam));
  
  for(int i = 0; i < (rep->tam); i++){
    fscanf(fptr, "%d", aux);
    rep->vet[i] = (*aux);
  }
  return rep;
}


int bolha(int *vet, int tam){}

int bolhaInteligente(int *vet, int tam){}

void imprimeVet(int *vet, int tam){
  for(int i = 0; i < tam; i++){
    printf("%d\n", vet[i]);
  }
}
