#include <iostream> //include library for input and output
#include <string> //include library for strings

int main () // return_type function_id (params)
{
    // single line comment

    /*
    multiple 
    line 
    comment
    */

    // integers
    int aVar = 2720;
    int bVar(32);
    int cVar; // not recommended | just start it from 0

    // floats/doubles
    float myFirstFloat = 3.14;
    double myFirstDouble = 3.14;

    // char/strings
    char myChar = 'A';
    char mySymbol = '*';

    std::string fun = "fun!";

    std::cout << "aVar: " << aVar << std::endl;
    std::cout << "bVar: " << bVar << std::endl;
    std::cout << "cVar: " << cVar << std::endl;
    std::cout << "myFirstFloat: " << myFirstFloat << std::endl;
    std::cout << "myFirstDouble: " << myFirstDouble << std::endl;
    std::cout << "myChar: " << myChar << std::endl;

    return 0;
}
