// Dividindo Círculos
#include <stdio.h>
#include <math.h>

long long int n_choose_x(int n, int x){
	if (x == 1){
		return n;
	}
	else{
		return n * n_choose_x(n-1, x-1);
	}
}


int main(){
	long long int n, partes;
	scanf("%lld", &n);
	partes = 1 + (n_choose_x(n, 2) / tgamma(3)) + (n_choose_x(n, 4) / tgamma(5));
	printf("%lld\n", partes); 
	return 0;
}