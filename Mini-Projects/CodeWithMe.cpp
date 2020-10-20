#include <iostream>
#include <ctime>

void WelcomeMessage(int level)
{   std::cout << "...\nWelcome to CodeWithMe...\n\n";
    std::cout << "\n\nYou are a agent and solve and crack the code to seek secret information... " << level;
    
}
bool Game(int level)
{
    WelcomeMessage(level);

    // Generate Code
    const int a = rand() % level + level;
    const int b = rand() % level + level;
    const int c = rand() % level + level;
    
    const int Sum = a + b + c;
    const int Product = a * b * c;


    // Print Sum and Product to the terminal
    std::cout << "+ There are 3 numbers in the code";
    std::cout << "\n+ The Addition of all the digits is: " << Sum;
    std::cout << "\n+ The Multiplication of all the digits is: " << Product << std::endl;

    // Gte the code from the agent
    int A, B, C;
    std::cin >> A >> B >> C;

    int GuessS = A + B + C;
    int GuessP = A * B * C;

    // Check the correctness of the code entered
    if (GuessS == Sum && GuessP == Product)
    {
        std::cout << "\n*** Well done !You have successfully passed a level.Great Going ***";
        return true;
    }
    else
    {
        std::cout << "\n*** Oops ! Wrong Code....Try again! ***";
        return false;
    }
}

int main()
{
    srand(time(NULL)); // create new random sequence
    
    int intialLevel = 1;
    int const highestLevel = 4;

    while (intialLevel <= highestLevel) // Loop game until all levels completed
    {
        bool maxLevelReached = PlayGame(intialLevel);
        std::cin.clear(); // Clears any errors
        std::cin.ignore(); // Discards the buffer

        if (maxLevelReached) 
        {
            ++intialLevel;
        }
    }
    std::cout << "\n*** Great work agent! You have successfully cleared all the levels.You did it ***\n";
    return 0;
}
