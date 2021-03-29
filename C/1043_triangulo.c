/* 
Programa:	Triângulo
Objetivo:	Verificar a existência do triângulo e calcular seu perímetro, ou a área do trapézio
Entrada :	3 Tamanhos dos lados do triângulo
Saida: 		Perímetro do triângulo ou área do trapézio
*/

#include <stdio.h>

int main(){
	float A, B, C, perimetro, area;
	scanf("%f %f %f", &A, &B, &C);

	if (C < B + A && B < A + C && A < B + C){
		perimetro = A + B + C;
		printf("Perimetro = %.1f\n", perimetro);
	}
	else{
		area = ((A + B) * C) / 2.0;
		printf("Area = %.1f\n", area);
	}
	return 0;
} 