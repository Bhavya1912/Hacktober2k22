#include<iostream>
void showrule()
{
    printf("\t\t\t\t\t\t\t\tGame : Rock Paper Scissor\n \t\n\n\n\nEnter r for Rock\nEnter p for Paper\nEnter s for Scissor\n\n\n");
}
void showinfo(char c1,char c2)
{
printf("player1 chose: %c\nplayer2 chose: %c\n ",c1,c2);
}
void design()
{
    printf("\n ****************************************");
}
int main() {
showrule();

char p1,p2;
printf("Enter Your Choice Player 1 and Player 2 Respectively\n");
scanf("%c %c",&p1,&p2);
showinfo(p1,p2);
design();
switch(p1)
{
    case 'r':
    if(p2=='p')
    printf("\n  Hurray !! player 2 wins");
    else if (p2=='s')
    printf("\n   Hurray!!player 1 wins");
    break ;
    case 'p':
    if(p2=='s')
    printf("\n   Hurray!!player 2 wins");
    else if (p2=='r')
    printf("\n   Hurray!!player 1 wins ");
    break ;
    case 's':
    if(p2=='r')
    printf("\n   Hurray!!player 2 wins");
    else if (p2=='p')
    printf("\n   Hurray!!player 1 wins");
    break ;
    default :
    printf("\nEnter Valid Choice !! For Rock Enter r For paper Enter p For Scissor Enter s Thanks for visiting ");
    break;
}
if((int)p1==(int)p2)
{
        printf("\nOh! Its Draw ... You Both Choses The Same");
}
design();
    return 0;
}
