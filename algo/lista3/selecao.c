#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int geraAleatorios(char *nomeArquivo, int qtd, int semente){
  srand(semente);
  FILE *fptr = fopen(nomeArquivo, "w");
  
  if(fptr == NULL){
    return 1;
  }
  for(int i = 0; i < qtd; i++){
    fprintf(fptr, "%d\n", rand() % 1000);
  }

  fclose(fptr);
  return 0;
}


int* leArquivo(char *nomeArquivo, int qtd){
  int *vet = (int*) malloc(qtd * sizeof(int));
  FILE *fptr = fopen(nomeArquivo, "r");

  if(fptr == NULL){
    return NULL;
  }

  for(int i = 0; i < qtd; i++){
    if(fscanf(fptr, "%d", &vet[i]) != 1)
      return NULL; 
  }

  fclose(fptr);
  return vet;
}

int encontraMenor(int inicio, int fim, int *vet){
  int menor = vet[inicio], minPos;

  for(int i = inicio; i < fim; i++){
    if(vet[i] <= menor){
      minPos = i;
      menor = vet[i];
    }
  }

  return minPos;
}

void selecao(int *vet, int tam){
  int marcador = 0, menor, aux;

  while(marcador < tam - 1){
    menor = encontraMenor(marcador + 1, tam, vet); // retorna a posiçao do menor valor
    if(vet[menor] < vet[marcador]){
      aux = vet[menor];
      vet[menor] = vet[marcador];
      vet[marcador] = aux;
    }
    marcador++;  
  }
}


void insercao(int *vet, int tam){
  int marcador, aux, pos;

  for(marcador = 1; marcador < tam; marcador++){
    pos = marcador - 1;
    aux = vet[marcador];

    while(aux < vet[pos] && pos >= 0){
      vet[pos + 1] = vet[pos];
      pos--;
    }

    vet[pos + 1] = aux;
  }
}


void buscaBinaria(int *vet, int inicio, int fim, int valor, int *res){
  res[1]++;
  if(inicio <= fim){
    // evita overflow da media tradicional
    int meio = floor((inicio + fim) / 2);
    
    if(vet[meio] == valor){
      res[0] = 1;
      return;
    }

    if(vet[meio] > valor)
      buscaBinaria(vet, inicio, meio - 1, valor, res);

    if(vet[meio] < valor)
      buscaBinaria(vet, meio + 1, fim, valor, res);
  }

  else{
    res[0] = 0;
    return;
  }
}

void imprimeVet(int *vet, int tam){
  for(int i = 0; i < tam; i++){
    printf("%d ", vet[i]);
  }
  printf("\n");
}


