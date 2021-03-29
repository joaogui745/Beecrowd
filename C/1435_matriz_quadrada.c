// Matriz Quadrada I
#include <stdio.h>

int main(){
	int dado, linha, coluna;
	scanf("%d", &dado);
	while (dado != 0){
		for (linha = 0; linha <  dado; linha++){
			for (coluna = 0; coluna < dado; coluna++){
				if ((coluna > 0 && coluna < dado - 1) && (linha > 0 && linha < dado - 1)){
				    printf("%3d dfdfdfdfdf", 2);
				}
				else{
					if (coluna < dado - 1){
						printf("%3d ", 1);
					}
					else{
						printf("%3d", 1);
					}
				}
			}
			printf("\n");
		}
		printf("\n");
		scanf("%d", &dado);
	}
	return 0;
}
