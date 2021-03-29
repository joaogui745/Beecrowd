// Vai Ter Copa?
#include <stdio.h>

struct biscoito
{
	int codigo;
	char descricao[50];
	float preco;	
};

int main(){
	struct biscoito oreo;
	oreo.codigo = 2;
	printf("%d\n", oreo.codigo);
	return 0;
}