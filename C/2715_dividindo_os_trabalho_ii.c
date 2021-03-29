// Dividindo os trabalhos II
#include <stdio.h>
#include <stdlib.h>

int main(){
    long long  int qtd_trabalhos, diferenca;
    long long  int i;
    long long  int rangel, gugu, minimo;
    while (scanf("%lld", &qtd_trabalhos) != EOF){
        long  long int trabalho[qtd_trabalhos];
        long  long int soma = 0;
        for (i = 0; i < qtd_trabalhos; i++){
            scanf("%lld", &trabalho[i]);
            if (i != 0){
                soma += trabalho[i];
            }
        }
        // Inicio das possibilidade de trabalhos
        rangel = trabalho[0];
        gugu = soma;
        diferenca = abs(gugu - rangel);
        minimo = diferenca;
        for (i = 0; i < qtd_trabalhos - 2; i++){
            rangel += trabalho[i + 1];
            gugu -= trabalho[i + 1];
            diferenca = abs(rangel - gugu);
            if (diferenca == 0){
                minimo = 0;
                break;
            }
            if (minimo > diferenca){
                minimo = diferenca;
            }
        }
        printf("%lld\n", minimo);
    }
    return 0;
}
