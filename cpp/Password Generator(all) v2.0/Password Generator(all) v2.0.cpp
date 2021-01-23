#include <iostream>
#include <fstream>
#include <conio.h>
#include <string>
#include <sstream>
/* It takes  ~10 seconds for one line of  the 8 line code*/
using namespace std;

ofstream file;

int main()
{
    cout<<"Hello User! Welcome to this very small program that is capable of creating a lot of data!";
    cout<<endl<<"Note : You may press Ctrl+C to stop and exit the program at anytime.";
    cout<<endl<<"Now, to start with,";
    string a="1";
    while (a=="1")
    {
        string fileoutputs="";
        int n;
        int x=0;
        char c1=32;
        char c2=32;
        char c3=32;
        char c4=32;
        char c5=32;
        char c6=32;
        char c7=32;
        char c8=32;
        char c9=32;
        char c10=32;
        char c11=32;
        char c12=32;
        char c13=32;
        char c14=32;
        char c15=32;
        char c16=32;
        char c17=32;
        char c18=32;
        char c19=32;
        char c20=32;
        char c21=32;
        char c22=32;
        char c23=32;
        char c24=32;
        char c25=32;
        char c26=32;
        char c27=32;
        char c28=32;
        char c29=32;
        char c30=32;
        char c31=32;
        char c32=32;
        stringstream ss;

        cout<<endl<<"Enter the number of characters you want (8-32): ";
        cin>>n;
        fileoutputs.reserve((n*857375)+857375);

        while((n<8)||(n>32))
        {
            cout<<endl<<"Sorry, User!!"<<endl<<"This program is not capable of handling such an input."<<endl<<"Please enter between (8-32) to continue to run the program"<<endl<<"Otherwise enter (0) to end the program:";
            cin>>n;
            if (n==0)
            {
                break;
            }
        }
        if ((n>=8)||(n<=32))
        {
            ss<<n;
            string m=ss.str()+"_character_password_dictionary.txt";
            file.open(m.c_str());
        }

        while((c32<127)&&(8<=n<=32))
        {
            if((n==32)&&(c32<127))
            {
                fileoutputs+=c32+c31+c30+c29+c28+c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c32<<c31<<c30<<c29<<c28<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==31)&&(c31<127))
            {
                fileoutputs+=c31+c30+c29+c28+c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c31<<c30<<c29<<c28<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==30)&&(c30<127))
            {
                fileoutputs+=c30+c29+c28+c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c30<<c29<<c28<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==29)&&(c29<127))
            {
                fileoutputs+=c29+c28+c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c29<<c28<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==28)&&(c28<127))
            {
                fileoutputs+=c28+c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c28<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==27)&&(c27<127))
            {
                fileoutputs+=c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==26)&&(c26<127))
            {
                fileoutputs+=c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==25)&&(c25<127))
            {
                fileoutputs+=c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==24)&&(c24<127))
            {
                fileoutputs+=c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==23)&&(c23<127))
            {
                fileoutputs+=c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==22)&&(c22<127))
            {
                fileoutputs+=c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==21)&&(c21<127))
            {
                fileoutputs+=c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==20)&&(c20<127))
            {
                fileoutputs+=c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==19)&&(c19<127))
            {
                fileoutputs+=c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==18)&&(c18<127))
            {
                fileoutputs+=c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==17)&&(c17<127))
            {
                fileoutputs+=c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==16)&&(c16<127))
            {
                fileoutputs+=c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==15)&&(c15<127))
            {
                fileoutputs+=c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==14)&&(c14<127))
            {
                fileoutputs+=c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==13)&&(c13<127))
            {
                fileoutputs+=c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==12)&&(c12<127))
            {
                fileoutputs+=c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==11)&&(c11<127))
            {
                fileoutputs+=c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==10)&&(c10<127))
            {
                fileoutputs+=c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==9)&&(c9<127))
            {
                fileoutputs+=c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==8)&&(c8<127)&&(x<=6634204312890625))
            {
                fileoutputs.append(c8+c7+c6+c5+c4+c3+c2+c1+"\n");
                if(x%857375==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else
            {
                break;
            }
            x=x+1;
            if((c1>=32)and(c1<126))
            {
                c1=c1+1;
            }
            else if(c1==126)
            {
                c1=c1-94;
                c2=c2+1;
            }
            if(c2==127)
            {
                c2=c2-95;
                c3=c3+1;
            }
            if(c3==127)
            {
                c3=c3-95;
                c4=c4+1;
            }
            if(c4==127)
            {
                c4=c4-95;
                c5=c5+1;
            }
            if(c5==127)
            {
                c5=c5-95;
                c6=c6+1;
            }
            if(c6==127)
            {
                c6=c6-95;
                c7=c7+1;
            }
            if(c7==127)
            {
                c7=c7-95;
                c8=c8+1;
            }
            if(c8==127)
            {
                c8=c8-95;
                c9=c9+1;
            }
            if(c9==127)
            {
                c9=c9-95;
                c10=c10+1;
            }
            if(c10==127)
            {
                c10=c10-95;
                c11=c11+1;
            }
            if(c11==127)
            {
                c11=c11-95;
                c12=c12+1;
            }
            if(c12==127)
            {
                c12=c12-95;
                c13=c13+1;
            }
            if(c13==127)
            {
                c13=c13-95;
                c14=c14+1;
            }
            if(c14==127)
            {
                c14=c14-95;
                c15=c15+1;
            }
            if(c15==127)
            {
                c15=c15-95;
                c16=c16+1;
            }
            if(c16==127)
            {
                c16=c16-95;
                c17=c17+1;
            }
            if(c17==127)
            {
                c17=c17-95;
                c18=c18+1;
            }
            if(c18==127)
            {
                c18=c18-95;
                c19=c19+1;
            }
            if(c19==127)
            {
                c19=c19-95;
                c20=c20+1;
            }
            if(c20==127)
            {
                c20=c20-95;
                c21=c21+1;
            }
            if(c21==127)
            {
                c21=c21-95;
                c22=c22+1;
            }
            if(c22==127)
            {
                c22=c22-95;
                c23=c23+1;
            }
            if(c23==127)
            {
                c23=c23-95;
                c24=c24+1;
            }
            if(c24==127)
            {
                c24=c24-95;
                c25=c25+1;
            }
            if(c25==127)
            {
                c25=c25-95;
                c26=c26+1;
            }
            if(c26==127)
            {
                c26=c26-95;
                c27=c27+1;
            }
            if(c27==127)
            {
                c27=c27-95;
                c28=c28+1;
            }
            if(c28==127)
            {
                c28=c28-95;
                c29=c29+1;
            }
            if(c29==127)
            {
                c29=c29-95;
                c30=c30+1;
            }
            if(c30==127)
            {
                c30=c30-95;
                c31=c31+1;
            }
            if(c31==127)
            {
                c31=c31-95;
                c32=c32+1;
            }
        }
        void close();
        cout<<"Do you want to make some more dictionaries, or do you want to skip it for today?(Enter 1 for Yes||0 for No): ";
        cin>>a;
    }

    cout<<endl<<"Thank you, User for using this program!!(Press anything to end the program)"<<endl;

    getch();

    return 0;
}
