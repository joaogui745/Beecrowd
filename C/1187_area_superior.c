// Área Superior
//Abaixo da Diagonal Secundária
#include <stdio.h>
#define tamanho_matriz 12

double soma(double matrix[tamanho_matriz][tamanho_matriz]){
	int linha, coluna;
	double soma = 0;
	for (linha = 0; linha < ((tamanho_matriz - 1) / 2); linha++){
		for (coluna = linha + 1; coluna < (tamanho_matriz - (linha + 1)); coluna++){
			soma += matrix[linha][coluna];
		}
	}
	return soma;
}

double media(double matrix[tamanho_matriz][tamanho_matriz]){
	int linha, coluna, qtd;
	double soma = 0;
	for (linha = 0; linha < ((tamanho_matriz - 1) / 2); linha++){
		for (coluna = linha + 1; coluna < (tamanho_matriz - (linha + 1)); coluna++){
			soma += matrix[linha][coluna];
			qtd++;
		}
	}
	return soma / qtd;
}



int main(){
	// Variáveis
	int linha, coluna; 
	char operacao;
	double matrix[tamanho_matriz][tamanho_matriz];
	scanf("%c", &operacao);


	// Preenchimento da matriz
	for (linha = 0; linha < tamanho_matriz; linha++){
		for (coluna = 0; coluna < tamanho_matriz; coluna++){
			scanf("%lf", &matrix[linha][coluna]);
		}
	}

	//Chamada da operação desejada
	if (operacao == 'S'){
		printf("%.1f\n", soma(matrix));
	}
	else {
		printf("%.1f\n", media(matrix));
	}
	return 0;
} 