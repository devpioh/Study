#include "stdafx.h"

class CoffeeBean;

int main()
{
    std::cout<<"Hello Cpp!!"<<std::endl;

    CoffeeBean *coffee = new CoffeeBean();

    coffee->Display();

    delete coffee;

    return 0;
}