#include <stdio.h>

int main(){
	int identificacao, horas_trabalhadas;
	float salario, taxa;

	scanf("%d %d %f", &identificacao, &horas_trabalhadas, &taxa);

	salario = taxa * horas_trabalhadas;

	printf("NUMBER = %d\n", identificacao);
	printf("SALARY = U$ %.2f\n", salario);

	return 0;
}