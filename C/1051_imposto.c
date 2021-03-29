/* 
Programa:	Imposto de renda.
Objetivo:	Calcular o imposto de um salário.
Entrada :	Salario (float)
Saida: 		Imposto (.4 Float)
*/

#include <stdio.h>

float calcula_imposto(int i, float salario){
	switch (i){
		case 1:
			salario = (salario - 2000) * 0.08;
			return salario;
		case 2:
			salario = (salario - 3000) * 0.18 + calcula_imposto(1, 3000);
        	return salario;
        case 3:
        	salario = (salario - 4500) * 0.28 + calcula_imposto(2, 4500);
        	return salario;
        default:
        	return 0;
	}
}

int main(){

	float salario, imposto;
	int indice;
	
	scanf("%f", &salario);

	if (salario < 2000.01){
		indice = 0;
	}
	else if (salario < 3000.01){
		indice = 1;
	}
	else if (salario <= 4500){
		indice = 2;
	}
	else {
		indice = 3;
	}

	imposto = calcula_imposto(indice, salario);

	if (imposto == 0){
		printf("Isento\n");
	}
	else {
		printf("R$ %.f\n", imposto);
	}

	return 0;
}
