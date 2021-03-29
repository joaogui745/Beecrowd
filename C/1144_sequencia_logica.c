/* 
Programa:   Seuqência Lógica.
Objetivo:   Continuar a sequencia. 
Entrada :   Numero de sequencias
Saida:      A Sequencia.
*/

#include <stdio.h>
#include <math.h>

int main(){
	int numero, i;
	scanf("%d", &numero);
	i = 1;

	while (i <= numero){
		printf("%d %d %d\n", i, (int) pow(i, 2), (int) pow(i, 3));
		printf("%d %d %d\n", i, (int) pow(i, 2) + 1, (int) pow(i, 3) + 1);
		i++;
	}
	return 0;
}
