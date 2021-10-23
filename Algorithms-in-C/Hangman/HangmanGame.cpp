
#include <iostream>
#include <cstdlib>
#include <stdlib.h>
#include <ctime>
#include <string>
using namespace std;

//---------------------------------------Initialization of Data for playing against CPU--------------------------------

//----------------------------------------------Class for Creation of LLs----------------------------------------------
class LinkedList
{
public:
	int tracker = 0;//tracks the length of linked list, used in generation a random number
	struct node
	{
		node* next = NULL;
		string data;
	}
	*head, * tail;
	LinkedList() {//If not initialised it throws an exception
		head = NULL;
		tail = NULL;
	}
	void createNode(string value) {
		node* temp = new node;
		temp->data = value;
		temp->next = NULL;
		if (head == NULL) {
			head = temp;
			tail = temp;
			temp = NULL;
		}
		else {
			tail->next = temp;
			tail = temp;
		}
		tracker++;
	}


	void display() {
		node* temp = new node;
		temp = head;
		cout << endl;
		cout << "[ ";
		while (temp != NULL) {
			cout << temp->data << " ";
			temp = temp->next;
		}
		cout << "]";
	};

	void insertEnd(string value) {
		node* temp = new node;
		temp->data = value;
		temp->next = NULL;
		tail->next = temp;
		tail = temp;
		tracker++;
	}
	void insertStart(string value) {
		node* temp = new node;
		temp->data = value;
		temp->next = head;
		head = temp;
		tracker++;
	}
	void insertAt(string value, int pos) {
		node* temp = new node;
		node* cur = new node;
		node* pre = new node;

		temp->data = value;
		cur = head;
		for (int i = 0; i < pos; i++) {
			pre = cur;
			cur = cur->next;
		}
		pre->next = temp;
		temp->next = cur;
		tracker++;
	};

	void deleteEnd() {
		node* cur = new node;
		node* pre = new node;
		cur = head;
		while (cur->next != NULL) {
			pre = cur;
			cur = cur->next;
		}
		tail = pre;
		pre->next = NULL;
		delete cur;
		tracker--;
	}
	void deleteStart() {
		node* temp = new node;
		temp = head;
		head = head->next;
		delete temp;
		tracker--;
	}
	void deleteAt(int pos) {
		node* cur = new node;
		node* pre = new node;

		cur = head;
		for (int i = 0; i < pos; i++) {
			pre = cur;
			cur = cur->next;
		}
		pre->next = cur->next;
		tracker--;
	};

	string giveValue(int pos) {//gets a value from the list based on 'pos' postion
		node* temp = new node;
		temp = head;
		for (int i = 0; i < pos; i++) {
			temp = temp->next;
		}
		return temp->data;
	}

	int exist(string theWord) {
		node* temp = new node;
		temp = head;
		int search = -1;
		while (temp != NULL) {
			if (temp->data == theWord) {
				search++;
				temp = temp->next;
			}
			else {
				temp = temp->next;
			}
		}
		return search;
	}

	string searchWord() {
		system("CLS");
		string searchedWord;
		if (head == NULL) {
			cout << "THE LIST IS EMPTY\n";
		}
		else {
			node* temp = new node;
			temp = head;
			cout << "ENTER THE WORD YOU WANT TO SEARCH: \n";
			cin >> searchedWord;
			int searchIndex = -1;
			int arrayofIndex[50];

			int i = 1;
			while (temp != NULL) {
				if (temp->data == searchedWord) {
					searchIndex++;
					arrayofIndex[searchIndex] = i;
					temp = temp->next;
					i++;
				}
				else {
					temp = temp->next;
					i++;
				}


			}
			if (searchIndex == -1) {
				cout << "THE GIVEN WORD " << searchedWord << " DOES NOT EXIST\n";
			}
			else {
				cout << "THE WORD '" << searchedWord << "' EXISTS AT THE FOLLOWING POSITION(S):\n";
				for (int i = 0; i <= searchIndex; i++) {
					cout << arrayofIndex[i] << "\t";
				}
				cout << "\n";
			}
			return searchedWord;
		}
	}
};
//--------------------------------------------------Initialization of Functions-------------------------------------------
void player();
void gameplay(string);
int check(char, string, string&);
bool pass(string);
void userEngagement(LinkedList);
//--------------------------------------------------Initialization of Global Variables-------------------------------------
char userInput;
int maxTries, wrongChoices = 0, difficulty, category, arrcategory, playoradmin;
string word;
string password = "admin", userPasswordInput;


//----------------------------------------------------Main Program-------------------------------------------------------
int main() {
	//WELCOMES THE PLAYER
	string welcome = "\n    :::: Welcome To HANGMAN ::::\n    A Project By:\n   Hassan Tariq \n\nLoading...\n";
	for (int i = 0; i < welcome.size(); i++) {
		for (int j = 0; j < 40000000; j++);
		cout << welcome[i];
	}
	for (int r = 1; r <= 20; r++)
	{
		for (int q = 0; q <= 100000000; q++);
		printf("%c", 177);
	}
	//-------------------------------Default initialization of some Categories as Linked Lists-----------------------------
	LinkedList continents;
	LinkedList animals;
	LinkedList colors;
	LinkedList countries;
	LinkedList fruits;

	continents.createNode("africa");
	continents.insertEnd("antarctica");
	continents.insertEnd("asia");
	continents.insertEnd("australia");
	continents.insertEnd("europe");
	continents.insertEnd("northamerica");
	continents.insertEnd("southamerica");

	animals.createNode("lion");
	animals.insertEnd("tiger");
	animals.insertEnd("whale");
	animals.insertEnd("dog");
	animals.insertEnd("cat");

	colors.createNode("blue");
	colors.insertEnd("red");
	colors.insertEnd("black");
	colors.insertEnd("green");

	countries.createNode("pakistan");
	countries.insertEnd("india");
	countries.insertEnd("austraila");
	countries.insertEnd("afghanistan");
	countries.insertEnd("france");

	fruits.createNode("apple");
	fruits.insertEnd("orange");
	fruits.insertEnd("mango");
	fruits.insertEnd("kiwi");
	fruits.insertEnd("durian");
	fruits.insertEnd("banana");
	//---------------------------------------------------------------------------------------------------------------------
	cout << "\n-RULES\n--------------------------------- \n-Each Letter is represented by a star (*)\n-Write in small case\n-Only type one letter per Entry\n---------------------------------\n";
	do {
		cout << "\n                                                  ::HANGMAN::\n\nChoose [1] to Play Game\nChoose [2] for admin access\nChoose [3] to Exit\nEnter your input : ";
		cin >> playoradmin;
		if (!cin) cin.clear();  // recover from errors
		//cin.ignore(numeric_limits <streamsize> ::max(), '\n');  // get rid of the ENTER key 
		switch (playoradmin)
		{
		case 1: {
			system("CLS");

			cout << "\nPlease Select Difficulty :\n[1] For Easy\n[2] For Medium\n[3] For Hard\n";
			//Validates User Input
			do {
				cout << "\nChoose from options 1-3 \n";
				cout << "Input Your Difficulty : ";
				cin >> difficulty;
			} while ((difficulty < 1) || (difficulty > 3));

			//Sets Game Difficulty
			if (difficulty == 1) {
				maxTries = 8;
			}
			else if (difficulty == 2) {
				maxTries = 5;
			}
			else {
				maxTries = 3;
			}
			cout << "\nYou have " << maxTries << " tries to Guess\n";

			//Initialization of the word to be guessed 
			cout << "[1] You wanna play against other player or \n[2] Select from a Category\nEnter your Input : ";
			cin >> category;
			//Player Enters the word
			if (category == 1) {
				cout << "Player may enter the secret word : ";
				cin >> word;
			}
			//Word is randomly selected from a Category (That user Chooses)
			else {
				cout << "\nSelect Category :\n[1] For Country Names\n[2] For Fruits\n[3] For Animals\n[4] For Continents Name\n[5] For Colors\n";
				//User Input Validation
				do {
					cout << "\nChoose between 1-5\n";
					cout << "\nInput Your Choice : ";
					cin >> arrcategory;
				} while ((arrcategory < 1) || (arrcategory > 5));
				srand(time(NULL));

				//Selects a random word from users choosen category...by generation a random number (inbound the lists length, i.e being tracked)
				//and then uses giveValue function to return data at that position
				if (arrcategory == 1) {
					int n = rand() % (countries.tracker);
					word = countries.giveValue(n);
				}
				else if (arrcategory == 2) {
					int n = rand() % (fruits.tracker);
					word = fruits.giveValue(n);
				}
				else if (arrcategory == 3) {
					int n = rand() % (animals.tracker);
					word = animals.giveValue(n);
				}
				else if (arrcategory == 4) {
					int n = rand() % (continents.tracker);
					word = continents.giveValue(n);
				}
				else if (arrcategory == 5) {
					int n = rand() % (colors.tracker);
					word = colors.giveValue(n);
				}
				else {

				}
			}

			//Makes a string compromised of *'s equal to the lenght of the word
			string hidden(word.length(), '*');
			gameplay(hidden);
			system("pause");//Waits till user presses any key
			system("CLS");
			/*cin.ignore();
			cin.get();
			return 0;*/
			break;
		}
		case 2: {
			system("CLS");
			//ADMIN WELCOME SCREEN
			cout << "                                         ";
			string adminWelcome = "ADMIN ACESS--SECURITY LEVEL = HIGH !";
			for (int i = 0; i < adminWelcome.size(); i++) {
				for (int j = 0; j < 40000000; j++);
				cout << adminWelcome[i];
			}
			//---------------------
			cout << "\nENTER PASSWORD TO GAIN ACCESS : ";
			cin >> userPasswordInput;
			//CHECKS USER PASSWORD 
			if (pass(userPasswordInput)) {
				system("CLS");
				int user;
				do {
					system("CLS");
					cout << "                                         ::::MAIN ADMIN SECTION::::\n";
					cout << "[1] To Access Data Records\n[2] To Change Password\n[3] To Exit";
					cout << "\nEnter Your Choice : ";
					cin >> user;
					switch (user)
					{
					case 1: {
						system("CLS");
						int ui;
						cout << "                                         ::::::DATA ACCESS MENU::::::";
						do {
							cout << "\n[1] To Access Default Data Records\n[2] To Exit";
							cout << "\nInput your choice : ";
							cin >> ui;
							switch (ui)
							{
							case 1: {
								system("CLS");
								int ui2;
								cout << "                                         ::::::::DEFAULT DATA MENU::::::::";
								do {
									cout << "\nChoose : \n[1] For Animals\n[2] For Continents\n[3] For Countries\n[4] For Colors\n[5] For Fruits\nEnter 0 TO EXIT ";
									cout << "\nInput Your Choice : ";
									cin >> ui2;
									switch (ui2)
									{
									case 1:
										system("CLS");
										cout << "|||Animals|||";
										userEngagement(animals);
										system("CLS");
										cout << "                                         ::::::::DEFAULT DATA MENU::::::::";
										break;
									case 2:
										system("CLS");
										cout << "|||Continents|||";
										userEngagement(continents);
										system("CLS");
										cout << "                                         ::::::::DEFAULT DATA MENU::::::::";
										break;
									case 3:
										system("CLS");
										cout << "|||Countries|||";
										userEngagement(countries);
										system("CLS");
										cout << "                                         ::::::::DEFAULT DATA MENU::::::::";
										break;
									case 4:
										system("CLS");
										cout << "|||Colors|||";
										userEngagement(colors);
										system("CLS");
										cout << "                                         ::::::::DEFAULT DATA MENU::::::::";
										break;
									case 5:
										system("CLS");
										cout << "|||Fruits|||";
										userEngagement(fruits);
										system("CLS");
										cout << "                                         ::::::::DEFAULT DATA MENU::::::::";
										break;
									default:
										cout << "\nPlease choose btw 1-5 OR 0 \n";
										break;
									}
								} while (ui2 != 0);
								system("CLS");
								cout << "                                         ::::::DATA ACCESS MENU::::::";
								;								break;
							}
							default:
								cout << "Please choose btw 1 or 2 \n";
								break;
							}
						} while (ui != 2);
						system("CLS");
					}
							break;
					case 2: {//User can change password
						string nPassword;
						cout << "\nEnter Your New Password : ";
						cin >> nPassword;
						password = nPassword;
						cout << "--------------------\n--PASSWORD CHANGED--\n--------------------\n";
						break;
					}
					default:
						cout << "\nPlease choose btw 1-3 : \n";
						break;
					}
				} while (user != 3);
				system("CLS");
			}
			else
			{
				cout << "\n!!!!WRONG PASSWORD!!!\nExiting ADMIN ACCESS";
				string adminExit = ". . .";
				for (int i = 0; i < adminExit.size(); i++) {
					for (int j = 0; j < 500000000; j++);
					cout << adminExit[i];
				}
				system("CLS");
			}
			break;
		}
		case 3:
			cout << "\n";
			break;
		default:
			cout << "\n\nPlease choose btw 1-3";
			break;
		}
	} while (playoradmin != 3);
	cout << "\n\n\nEXITING PROGRAM";
	string exit = "....";
	for (int i = 0; i < exit.size(); i++) {
		for (int j = 0; j < 300000000; j++);
		cout << exit[i];
	}

}

//Function to check if the letter entered matches one in the guessword and revealing it if YES
int check(char userInput, string actualWord, string & hidden) {
	int same = 0;
	int len = actualWord.length();
	for (int i = 0; i < len; i++) {
		if (userInput == hidden[i]) { //If the word has already been guessed
			return 0;
		}
		if (userInput == actualWord[i]) {
			hidden[i] = userInput;
			same++;
		}
	}
	return same;
}

//Main function that Carries the Gameplay Mechanics of the game
void gameplay(string hidden) {
	system("CLS");
	while (wrongChoices < maxTries) {
		cout << "\n" << hidden;
		cout << "\n----------------------\nGuess a Letter : ";
		cin >> userInput;

		if (check(userInput, word, hidden) == 0) {
			cout << "\nThis Letter isn't in the Word!\n";
			wrongChoices++;
		}
		else {
			cout << "\nYou Found a LETTER! \n";
		}

		cout << "\nYou have " << maxTries - wrongChoices << " guesses left.\n";
		if (word == hidden) {
			cout << "\n :::::: CONGRATULATIONS ::::::";
			cout << "\nWord was : " << word << "\n";
			cout << "You Won!\n";
			break;
		}
	}
	if (wrongChoices == maxTries) {
		cout << "\n :::::: YOU LOST ::::::: ";
		cout << "\nThe word was : \n" << word;
	}
}

//Function to check if password is correct
bool pass(string pass) {
	if (pass == password) {
		return true;
	}
	else
	{
		return false;
	}
}

//Function to handle workings of Users engagement with the records
void userEngagement(LinkedList give) {
	int ui3;
	do {
		cout << "\nChoose Operation:\n[1] To Display Data\n[2] To Add a Record\n[3] To Delete a Record\n[4] To Search a Record\n[0] To Exit\n";
		cout << "Input Your Choice : ";
		cin >> ui3;
		switch (ui3)
		{
		case 1: {
			give.display();
			cout << endl;
			cout << "------------------";
			break;
		}
		case 2: {
			string theWord;
			cout << "Enter the Word that you want to Add: ";
			cin >> theWord;
			int yes = give.exist(theWord);
			if (yes ==0) {
				cout << "\nWord already Exists.";
			}
			else {
				give.insertEnd(theWord);
			}
			cout << endl;
			//system("CLS");
			break;
		}
		case 3: {
			cout << "\n-----------------";
			give.display();
			cout << "\n-----------------\n";
			cout << endl;
			int pos;
			cout << "Enter the position of the word that you want to delete: \n";
			cin >> pos;
			give.deleteAt(pos - 1);
			cout << endl;
			break;
		}
		case 4:
		{
			give.searchWord();
			cout << endl;
			break;
		}
		default:
			cout << "\nPlease choose from the given options.";
			break;
		}
	} while (ui3 != 0);
}