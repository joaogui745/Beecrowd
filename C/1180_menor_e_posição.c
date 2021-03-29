#include <stdio.h>

int main(){
	int tamanho_vetor, i, menor = 1000000, indice;
	scanf("%d", &tamanho_vetor);
	int vetor[tamanho_vetor];
	for (i = 0; i < tamanho_vetor; i++){
		scanf("%d", &vetor[i]);
		if (menor > vetor[i]){
			menor = vetor[i];
			indice = i;
		}
	}
	printf("Menor valor: %d\nPosicao: %d", menor, indice);
	return 0;
}