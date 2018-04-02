#include "MoeLecture.h"

void MoeLecture::Main()
{
    //Chapter001();
    //Chapter002();
}

void MoeLecture::Question()
{
    //Question01_01();
    //Question01_02();
    //Question02_01();
    Question02_02();
}

void MoeLecture::Chapter001()
{
    char name[100];
    char lang[100];

    std::cout<<"What are your name? ";
    std::cin>>name;
    std::cout<<"What study language? ";
    std::cin>>lang;

    std::cout<<"My name is "<<name<<std::endl;
    std::cout<<"I study language is "<<lang<<std::endl;
}

void MoeLecture::Chapter002()
{
    // int num         = 1020;
    // int &numRef     = num;

    // numRef          = 3047;
    // std::cout<<"Value : "<<num<<std::endl;
    // std::cout<<"Ref : "<<numRef<<std::endl;

    // std::cout<<std::endl;

    // std::cout<<"Value : "<<&num<<std::endl;
    // std::cout<<"Ref : "<<&numRef<<std::endl;


    // int num         = 12;
    // int *ptr        = &num;
    // int **dptr      = &ptr;

    // int &ref        = num;
    // int *(&pref)    = ptr;
    // int **(&dpref)  = dptr;

    // std::cout<<ref<<std::endl;
    // std::cout<<*pref<<std::endl;
    // std::cout<<**dpref<<std::endl;

    int val1 = 10;
    int val2 = 20;

    SwapByRef( val1, val2 );

    std::cout<<val1<<std::endl;
    std::cout<<val2<<std::endl;
}

void MoeLecture::SwapByRef( int &num1, int &num2 )
{
    int temp = num1;
    num1 = num2;
    num2 = temp;
}


void MoeLecture::Question01_01()
{
    int number = 0;
    while( true )
    {
        std::cout<<"Select Question (1 ~ 4): ";
        std::cin>>number;

        switch( number )
        {
            case 1: Question01_01_1(); break;
            case 2: Question01_01_2(); break;
            case 3: Question01_01_3(); break;
            case 4: Question01_01_4(); break;

            default: return;
        }
    }
}

void MoeLecture::Question01_01_1()
{
    int sum = 0;
    int inputNum = 0;
    for( int i = 0; i < 5; i++ )
    {
        std::cout<<"[ "<< i <<" ] input number : ";
        std::cin>>inputNum;

        sum += inputNum;
    }

    std::cout<<std::endl;
    std::cout<<"Total Sum : "<<sum<<std::endl;
}

void MoeLecture::Question01_01_2()
{
    char name[1024];
    char phoneNumber[1024];

    std::cout<<"Input your name : ";
    std::cin>>name;
    std::cout<<"Input your phone number : ";
    std::cin>>phoneNumber;

    std::cout<<std::endl;
    std::cout<<"your name : "<<name<<std::endl;
    std::cout<<"your phone number : "<<phoneNumber<<std::endl; 
}

void MoeLecture::Question01_01_3()
{
    int num = 0;
    bool isEnd = false;
    while( false == isEnd )
    {
        std::cout<<"Input number : ";
        std::cin>>num;

        if( 0 > num )
        {
            isEnd = true;
            continue;
        }

        for( int i = 1; i < 10; i++ )
        {
            std::cout<<num<<" * "<<i<<" = "<<num * i<<std::endl;
        }
    }
}

void MoeLecture::Question01_01_4()
{
    int num = 0;
    bool isEnd = false;
    while( false == isEnd )
    {
        std::cout<<"Input price : ";
        std::cin>>num;

        if( 0 > num )
        {
            isEnd = true;
            continue;
        }
        
        int pay = 50 + (num * 0.12);

        std::cout<<"this month pay : "<<pay<<std::endl;
    }
}

void MoeLecture::Question01_02()
{
    int num1 = 20, num2 = 30;
    std::cout<<num1<<' '<<num2<<std::endl;
    Question01_02_Swap( &num1, &num2 );    
    std::cout<<num1<<' '<<num2<<std::endl<<std::endl;

    char ch1 = 'A', ch2 = 'Z';
    std::cout<<ch1<<' '<<ch2<<std::endl;
    Question01_02_Swap( &ch1, &ch2 );    
    std::cout<<ch1<<' '<<ch2<<std::endl<<std::endl;

    double dnum1 = 1.1111, dnum2 = 5.5555;
    std::cout<<dnum1<<' '<<dnum2<<std::endl;
    Question01_02_Swap( &dnum1, &dnum2 );    
    std::cout<<dnum1<<' '<<dnum2<<std::endl<<std::endl;
}

void MoeLecture::Question01_02_Swap(int *num1, int *num2)
{
    int temp = *num1;
    *num1 = *num2;
    *num2 = temp;
}

void MoeLecture::Question01_02_Swap(char *ch1, char *ch2)
{
    char temp = *ch1;
    *ch1 = *ch2;
    *ch2 = temp;
}

void MoeLecture::Question01_02_Swap(double *dnum1, double *dnum2)
{
    double temp = *dnum1;
    *dnum1 = *dnum2;
    *dnum2 = temp;
}

void MoeLecture::Question02_01()
{
    Question02_01_1();
    Question02_01_2();
}

void MoeLecture::Question02_01_1()
{
    std::cout<<"Question02_01_1()"<<std::endl;

    int value = 10;

    Q02_01_1_AddValue( value );
    Q02_01_1_ChangeMark( value );

    std::cout<<value<<std::endl;
}

void MoeLecture::Q02_01_1_AddValue( int &value )
{
    value++;
}

void MoeLecture::Q02_01_1_ChangeMark( int &value )
{
    value = value * -1;
}

void MoeLecture::Question02_01_2()
{
    std::cout<<"Question02_01_2()"<<std::endl;

    int num1 = 5;
    int *ptr1 = &num1;
    int num2 = 10;
    int *ptr2 = &num2;

    std::cout<<"Value1 : "<<*ptr1<<", Val1REF : "<<ptr1<<std::endl;
    std::cout<<"Value2 : "<<*ptr2<<", Val2REF : "<<ptr2<<std::endl;

    std::cout<<std::endl;
    std::cout<<std::endl;    

    Q02_01_2_SwapPointer( ptr1, ptr2 );

    std::cout<<"Value1 : "<<*ptr1<<", Val1REF : "<<ptr1<<std::endl;
    std::cout<<"Value2 : "<<*ptr2<<", Val2REF : "<<ptr2<<std::endl;
}

void MoeLecture::Q02_01_2_SwapPointer( int *&ptr1, int *&ptr2 )
{
    int *temp = ptr1;
    ptr1 = ptr2;
    ptr2 = temp;
}

void MoeLecture::Question02_02()
{
    const int num = 12;
    const int *ptr = &num;
    const int *&ptrRef = ptr;


    std::cout<<num<<std::endl;
    std::cout<<*ptr<<std::endl;
    std::cout<<*ptrRef<<std::endl;
}