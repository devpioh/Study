#include <iostream>

class MoeLecture
{
    public:
    void Main();
    void Question();
    
    private:
    void Chapter001();
    void Chapter002();

    private:
    void SwapByRef( int &num1, int &num2 );

    private:
    void Question01_01();
    void Question01_01_1();
    void Question01_01_2();
    void Question01_01_3();
    void Question01_01_4();

    void Question01_02();
    void Question01_02_Swap(int *num1, int *num2);
    void Question01_02_Swap(char *ch1, char *ch2);
    void Question01_02_Swap(double *dnum1, double *dnum2);

    void Question02_01();
    void Question02_01_1();
    void Q02_01_1_AddValue( int &value );
    void Q02_01_1_ChangeMark( int &value );
    void Question02_01_2();
    void Q02_01_2_SwapPointer( int *&ptr1, int *&ptr2 );

    void Question02_02();

};