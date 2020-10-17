#include <stdio.h>
#include <ctype.h>
void main()
{   int ch, m1, top = -1, k, i, m, j, n1, n2, n3, stack[50], num, u;
    char b[50], a[50], pfs[50], st[50], a1 = '+', a2 = '-';
    char a3 = '*', a4 = '/', a5 = '%', a6 = '^', c, temp;
    do{   top = -1;
        printf("\t\nMenu\n1.Infix to Postfix conversion");
        printf("\t\n2.Evaluation\n3.Exit");
        printf("\nEnter your choice:");
        scanf("%d", &ch);
        if (ch == 1)
        {   printf("Enter the infix expression : ");
            scanf(" %s", a);
            for (i = 0, k = 0; a[i] != '\0'; i++)
            {   m = (int)a[i];
                if (a[i] == a6)
                {   top++;
                    st[top] = a[i];}
                else if (a[i] == '%' || a[i] == '*' || a[i] == '/')
                {   for (j = top; j > -1; j--)
                    {   if (st[j] == a2 || st[j] == a1 || st[j] == '(')
                        {   top++;
                            st[top] = a[i];
                            break;}
                        else
                        {   pfs[k] = st[j];
                            k++;
                            st[j] = a[i];
                            break;}
                    }
                    if (top == -1)
                    {   top++;
                        st[top] = a[i];}
                }
                else if (a[i] == '+' || a[i] == '-')
                {   for (j = top; j > -1; j--)
                    {   if (st[j] == '*' || st[j] == '/' || st[j] == '%' || st[j] == '+' || st[j] == '-' || st[j] == '^')
                        {pfs[k] = st[j];
                            k++;
                            top--;}
                        else
                        {   top++;
                            st[top] = a[i];
                            break;}  
                    }
                    if (top == -1)
                    {   top++;
                        st[top] = a[i];}
                }
                else if (m == 40)
                {   top++;
                    st[top] = a[i];}
                else if (a[i] == ')')
                {   for (j = top; j > -1; j--)
                    {   if (st[j] == '(')
                         {   top--;
                            break;}
                        else
                        {   pfs[k] = st[j];
                            k++;
                            top--;}}
                }
                else
                {   pfs[k] = a[i];
                    k++;}
            }
            if (top != -1)
            {   for (i = top; i != -1; i--)
                {   pfs[k] = st[i];
                    k++;
                    top--;}
            }
            pfs[k] = '\0';
            printf("Output=%s", pfs);
            printf("\n");
        }
        else if (ch == 2)
        {   top = -1;
            printf("\nEnter the expression:");
            scanf("%s", b);
            while (b[i] != '\0')
            {   c = b[i];
                if (c >= '0' && c <= '9')
                {   int num;
                    num = (int)c - 48;
                    top++;
                    stack[top] = num;}
                else if (isalpha(c))
                {   printf("\nEnter the value of %c:", c);
                    scanf(" %d", &m1);
                    stack[++top] = m1;}
                else
                {   n2 = stack[top--];
                    n1 = stack[top--];
                    switch (c){
                    case '^':
                    {   n3 = 1;
                        for (u = 0; u < n2; u++)
                        { n3 = n3 * n1;}
                        break; }
                    case '+':
                    {n3 = n2 + n1;
                        break;}
                    
                    case '-':
                    {   n3 = n1 - n2;
                        break;}
                    case '*':
                    {   n3 = n1 * n2;
                        break;}
                    case '/':
                    {   n3 = n1 / n2;
                        break;}
                    case '%':
                    {   n3 = n1 % n2;
                        break;}}
                    stack[++top] = n3;
                }i++;
            }printf("\nThe result of expression %s is %d\n\n", b, stack[top--]);
        }
    } while (ch < 3);
}
