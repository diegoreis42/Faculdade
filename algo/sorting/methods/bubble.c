#include <stdio.h>
#include <stdlib.h>

void swap(int* xp, int* yp){
  int temp = *xp;
  *xp = *yp;
  *yp = temp;
}

void bubbleSort(int *vet, int size){
  /* Algoritmo mais simples de ordenaçao
   * compara cada elemento a todos os outros
   * e os troca de lugar (swap) caso um for maior
   * que o outro
   *
   * --- Complexidade ---
   *  Pior caso => O(n^2)
   *  Melhor caso => 0(n)
   */

  for(int i = 0; i < size - 1; i++){
    for(int j = 0; j < size - i - 1; j++){
      if(vet[j] > vet[j + 1])
        swap(&vet[j], &vet[j + 1]);
    }
  }
}
