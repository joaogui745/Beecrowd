// Desviando de Árvores de Natal
#include <stdio.h>
#include <stdlib.h>

int main(){
	int linha, coluna, qtd_linhas, vetor_linhas[3], delta_s, indice;
	while (1){
		scanf("%d", &qtd_linhas);
		if (qtd_linhas == 0){
			break;
		}
		int vapo = 0;
	    int delta_s = 1;
		for (linha = 0; linha < qtd_linhas; linha++){
			int soma = 0;
			for (coluna = 0; coluna < 3; coluna++){
				scanf("%d", &vetor_linhas[coluna]);
				if (vetor_linhas[coluna] == 0){
					indice = coluna;
				}
				soma += vetor_linhas[coluna];
			}
			if (soma != 0){
				vapo += abs(delta_s - indice);
				delta_s = indice;
			}
		}
		printf("%d\n", vapo);
	}
	return 0;
}

