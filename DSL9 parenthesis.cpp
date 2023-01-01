/*In any language program mostly syntax error occurs due to unbalancing delimiter such as 
(),{},[]. Write C++ program using stack to check whether given expression is well 
parenthesized or not*/

#include<iostream>
#include<stdlib.h>
#include<string.h>
using namespace std;


    int TOP=-1;
    char stack[50];
    void push(char x)
    {
        TOP++;
        stack[TOP]=x;
    }
    void pop(char t)
    {
        if(t=='}')
        {
            if(stack[TOP]=='{')
            TOP--;

        }
        else if(t==')')
        {
            if(stack[TOP]=='(')
            TOP--;
        }
        else if(t==']')
        {
             if(stack[TOP]=='[')
            TOP--;
        }
    
    }


void display()
{
    int i;
    if(TOP==-1)
    cout<<"\nStack is Empty\n Given expression is well parenthesised...\n";
    else
    {
        cout<<"\nStack is NOT Empty\n Given expression NOT is well parenthesised...\n";
    }
}
int main()
{
    char exp[50],x,t;
    int len,i;
    cout<<"\nYour infix expression is =";
    cin>>exp;
    cout<<"\nYour infix expression is ="<<exp;
    len=strlen(exp);
    for(i=0;i<len;i++)
    {
        if((exp[i]=='{')||(exp[i]=='(')||(exp[i]=='['))
        {
            x=exp[i];
            push(x);
        }
        else if((exp[i]=='}')||(exp[i]==')')||(exp[i]==']'))
        {
            t=exp[i];
            pop(t);

        }
        display();
        return 0;
    }
}
