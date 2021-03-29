// Construindo Casas
#include <stdio.h>
#include <math.h>

int main(){
	double A, B, C;
	int lado;
	scanf("%lf %lf %lf", &A, &B, &C);
	while (A != 0){
		lado = (int) sqrt((A * B * 100) / C);
	    printf("%d\n", lado);
	    scanf("%lf %lf %lf", &A, &B, &C);
	}
}
