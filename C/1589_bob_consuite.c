// Bob conduite
#include <stdio.h>

int main(){
	int i, C1, C2, minimo, casos;
	scanf("%d", &casos);
	for (i = 0; i < casos; i++){
		scanf("%d %d", &C1, &C2);
	    minimo = ((2 * C1) + (2 * C2)) / 2;
	    printf("%d\n", minimo);
	    return 0;
	}
}