/* 
Programa:	Distância Entre Dois Pontos.
Objetivo:	Calcular a distância entre 2 pontos.
Entrada :	4 Números Reais.
Saida: 		A distância real.
*/

#include <stdio.h>
#include <math.h>

int main(){
	float P1[2], P2[2], distancia;

	scanf("%f %f", &P1[0], &P1[1]);
	scanf("%f %f", &P2[0], &P2[1]);

	distancia = sqrt(pow(P2[0] - P1[0], 2) + pow(P2[1] - P1[1], 2));

	printf("%.4f\n", distancia);

	return 0;
}
