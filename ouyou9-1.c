#include <stdio.h>
int main(void)
{
    int number = 0, a = 0, b = 1;
    while(1){
        number++;
        if (b * 2 != number)continue;
        b = b * 2;
        printf("数字%dを発見しました。\n", number);
        a++;
        if (a == 20)break;
    }
    return 0;
}