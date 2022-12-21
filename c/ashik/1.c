#include <stdio.h>
float ids(float vgs, float vds, float vt)
{
    //  vgs - gate source voltage
    //  vds - drain source voltage
    //  vt - threshold voltage
    int sum;
    if(vds<(vgs-vt))   // linear region
    {
        return ((vgs-vt)*vds)-(vds*vds/2);
    }
    else {
        return (vgs-vt)*(vgs-vt)/2;
    }
}

int main()
{
    float vt = 1;
    float id[7];    // Array storing current values
    float vgs = 3.5;
    printf("Case 1: Vgs = %.2fV\n",vgs);

    for(int i=0; i<=6; i++)
    {
        id[i] = ids(vgs, i, vt);
        printf("Vds =  %d    Ids = %.2f", i, id[i]);
        printf("\n");
    }
    float id2[7];    // Array storing current values for Vgs = 4V
    vgs = 4;
    printf("\nCase 2: Vgs = %.2fV\n",vgs);

    for(int i=0; i<=6; i++)
    {
        id2[i] = ids(vgs, i, vt);
        printf ("Vds =  %d    Ids = %.2f", i, id2[i]);
        printf("\n");
    }

     return 0;
}