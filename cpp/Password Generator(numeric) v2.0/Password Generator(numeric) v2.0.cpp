#include <iostream>
#include <fstream>
#include <conio.h>
#include <string>
#include <sstream>
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
        int64_t x=0;
        char c1=48;
        char c2=48;
        char c3=48;
        char c4=48;
        char c5=48;
        char c6=48;
        char c7=48;
        char c8=48;
        char c9=48;
        char c10=48;
        char c11=48;
        char c12=48;
        char c13=48;
        char c14=48;
        char c15=48;
        char c16=48;
        char c17=48;
        char c18=48;
        char c19=48;
        char c20=48;
        char c21=48;
        char c22=48;
        char c23=48;
        char c24=48;
        char c25=48;
        char c26=48;
        char c27=48;
        char c28=48;
        char c29=48;
        char c30=48;
        char c31=48;
        char c32=48;
        stringstream ss;

        cout<<endl<<"Enter the length of the passwords you want (1-32): ";
        cin>>n;

        while((n<1)||(n>32))
        {
            cout<<endl<<"Sorry, User!!"<<endl<<"This program is not capable of handling such an input."<<endl<<"Please enter between (8-32) to continue to run the program"<<endl<<"Otherwise enter (0) to end the program:";
            cin>>n;
            if (n==0)
            {
                break;
            }
        }
        if ((n>=1)||(n<=32))
        {
            ss<<n;
            string m=ss.str()+"_character(numeric_only)_password_dictionary.txt";
            file.open(m.c_str());
        }

        while((c32<58)&&(8<=n<=32))
        {
            if((n==32)&&(c32<58))
            {
                fileoutputs+=c32+c31+c30+c29+c28+c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c32<<c31<<c30<<c29<<c28<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==31)&&(c31<58))
            {
                fileoutputs+=c31+c30+c29+c28+c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c31<<c30<<c29<<c28<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==30)&&(c30<58))
            {
                fileoutputs+=c30+c29+c28+c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c30<<c29<<c28<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==29)&&(c29<58))
            {
                fileoutputs+=c29+c28+c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c29<<c28<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==28)&&(c28<58))
            {
                fileoutputs+=c28+c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c28<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==27)&&(c27<58))
            {
                fileoutputs+=c27+c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c27<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==26)&&(c26<58))
            {
                fileoutputs+=c26+c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c26<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==25)&&(c25<58))
            {
                fileoutputs+=c25+c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c25<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==24)&&(c24<58))
            {
                fileoutputs+=c24+c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c24<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==23)&&(c23<58))
            {
                fileoutputs+=c23+c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c23<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==22)&&(c22<58))
            {
                fileoutputs+=c22+c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c22<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==21)&&(c21<58))
            {
                fileoutputs+=c21+c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c21<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==20)&&(c20<58))
            {
                fileoutputs+=c20+c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c20<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==19)&&(c19<58))
            {
                fileoutputs+=c19+c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c19<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==18)&&(c18<58))
            {
                fileoutputs+=c18+c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c18<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==17)&&(c17<58))
            {
                fileoutputs+=c17+c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c17<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==16)&&(c16<58))
            {
                fileoutputs+=c16+c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c16<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==15)&&(c15<58))
            {
                fileoutputs+=c15+c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c15<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==14)&&(c14<58))
            {
                fileoutputs+=c14+c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c14<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==13)&&(c13<58))
            {
                fileoutputs+=c13+c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c13<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==12)&&(c12<58))
            {
                fileoutputs+=c12+c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c12<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==11)&&(c11<58))
            {
                fileoutputs+=c11+c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c11<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==10)&&(c10<58))
            {
                fileoutputs+=c10+c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c10<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==9)&&(c9<58))
            {
                fileoutputs+=c9+c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c9<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==8)&&(c8<58))
            {
                fileoutputs+=c8+c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c8<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==7)&&(c7<58))
            {
                fileoutputs+=c7+c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c7<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==6)&&(c6<58))
            {
                fileoutputs+=c6+c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c6<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==5)&&(c5<58))
            {
                fileoutputs+=c5+c4+c3+c2+c1+"\n";
                if(x%10000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c5<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==4)&&(c4<58))
            {
                fileoutputs+=c4+c3+c2+c1+"\n";
                if(x%1000==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c4<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==3)&&(c3<58))
            {
                fileoutputs+=c3+c2+c1+"\n";
                if(x%100==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c3<<c2<<c1<<"\n";
                }
            }
            else if((n==2)&&(c2<58))
            {
                fileoutputs+=c2+c1+"\n";
                if(x%10==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c2<<c1<<"\n";
                }
            }
            else if((n==1)&&(c1<58))
            {
                fileoutputs+=c1+"\n";
                if(x%1==0)
                {
                    file<<fileoutputs;
                    fileoutputs.clear();
                    cout<<c1<<"\n";
                }
            }
            else
            {
                break;
            }
            x=x+1;
            if((c1>=48)and(c1<57))
            {
                c1=c1+1;
            }
            else if(c1==57)
            {
                c1=c1-9;
                c2=c2+1;
            }
            if(c2==57)
            {
                c2=c2-9;
                c3=c3+1;
            }
            if(c3==57)
            {
                c3=c3-9;
                c4=c4+1;
            }
            if(c4==57)
            {
                c4=c4-9;
                c5=c5+1;
            }
            if(c5==57)
            {
                c5=c5-9;
                c6=c6+1;
            }
            if(c6==57)
            {
                c6=c6-9;
                c7=c7+1;
            }
            if(c7==57)
            {
                c7=c7-9;
                c8=c8+1;
            }
            if(c8==57)
            {
                c8=c8-9;
                c9=c9+1;
            }
            if(c9==57)
            {
                c9=c9-9;
                c10=c10+1;
            }
            if(c10==57)
            {
                c10=c10-9;
                c11=c11+1;
            }
            if(c11==57)
            {
                c11=c11-9;
                c12=c12+1;
            }
            if(c12==57)
            {
                c12=c12-9;
                c13=c13+1;
            }
            if(c13==57)
            {
                c13=c13-9;
                c14=c14+1;
            }
            if(c14==57)
            {
                c14=c14-9;
                c15=c15+1;
            }
            if(c15==57)
            {
                c15=c15-9;
                c16=c16+1;
            }
            if(c16==57)
            {
                c16=c16-9;
                c17=c17+1;
            }
            if(c17==57)
            {
                c17=c17-9;
                c18=c18+1;
            }
            if(c18==57)
            {
                c18=c18-9;
                c19=c19+1;
            }
            if(c19==57)
            {
                c19=c19-9;
                c20=c20+1;
            }
            if(c20==57)
            {
                c20=c20-9;
                c21=c21+1;
            }
            if(c21==57)
            {
                c21=c21-9;
                c22=c22+1;
            }
            if(c22==57)
            {
                c22=c22-9;
                c23=c23+1;
            }
            if(c23==57)
            {
                c23=c23-9;
                c24=c24+1;
            }
            if(c24==57)
            {
                c24=c24-9;
                c25=c25+1;
            }
            if(c25==57)
            {
                c25=c25-9;
                c26=c26+1;
            }
            if(c26==57)
            {
                c26=c26-9;
                c27=c27+1;
            }
            if(c27==57)
            {
                c27=c27-9;
                c28=c28+1;
            }
            if(c28==57)
            {
                c28=c28-9;
                c29=c29+1;
            }
            if(c29==57)
            {
                c29=c29-9;
                c30=c30+1;
            }
            if(c30==57)
            {
                c30=c30-9;
                c31=c31+1;
            }
            if(c31==57)
            {
                c31=c31-9;
                c32=c32+1;
            }
        }
        void close();
        cout<<"Your password dictionary of "<<n<<" numbers is completed!\nIf you want to create more dictionaries then please type in the password length (1-32),\nOr type in 0 to exit the program : ";
        cin>>n;
    }

    cout<<endl<<"Thank you, User for using this program!!(Press anything to end the program)"<<endl;

    getch();

    return 0;
}
