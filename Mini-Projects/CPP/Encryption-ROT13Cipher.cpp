#include<iostream>
#include<string>

// Encrypt input message using
// ROT 13 Cipher
uint8_t shift = 13;

// ROT 13 Cipher is special 
// Caesar cipher in which 
// letters are shifted by 13 places
inline std::string ROT13Cipher(std::string inputText)
{
    std::string outputText ;
    for(uint_fast16_t i=0; i<inputText.size();++i)
    {
        if(tolower(inputText[i])-'a' < shift+1)
            outputText.append(1,inputText[i]+shift);
        else
            outputText.append(1,inputText[i]-shift);
    }
    return outputText;
}

int main()
{
    std::string inputText;
    std::cout << "Enter input text: " ;
    std::getline(std::cin,inputText);
    std::cout << ROT13Cipher(inputText);
    return 0;
}