/* 
Programa:   Experiências.
Objetivo:   Apresentar o total, o tipo e o percentual de cobaias. 
Entrada :   Casos com combaias.
Saida:      O total, o tipo e o percentual de cobaias.
*/

#include <stdio.h>

int indice(char letra){
    if (letra == 'C'){
        return 0;
    }
    else if (letra == 'R'){
        return 1;
    }
    else{
        return 2;
    }
}

int main(){
    int j, qtd, casos, total = 0, animais[] = {0,0,0};
    char letra, nomes[][8] = {"coelhos", "ratos", "sapos"};
    scanf("%d", &casos);
    
    for (j = 0; j < casos; j++){
        scanf("%d %c", &qtd, &letra);
        total += qtd;
        animais[indice(letra)] += qtd;
    }

    printf("Total: %d cobaias\n", total);
    for (j = 0; j < 3; j++){
        printf("Total de %s: %d\n", nomes[j], animais[j]);
    }
    for (j = 0; j < 3; j++){
        printf("Percentual de %s: %.2f %%\n", nomes[j], (animais[j] * 100.0) / total);
    }

    return 0;
}