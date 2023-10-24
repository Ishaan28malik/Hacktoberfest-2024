#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>
#include <string.h>


void gotoxy(int, int);
void menu();
void add();
void view();
void search();
void modify();
void deleterec();
void addExamResult();
void viewExamResults();
void searchExamResult();
void modifyExamResult();
void deleteExamResult();

struct student
{
    char name[30];
    char mobile[20];
    int rollno;
    char course[30];
    char branch[30];
    int year;
};

struct exam
{
    int rollno;
    int marks;
};

void gotoxy(int x, int y)
{
    COORD c;
    c.X = x;
    c.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}

int main()
{
    gotoxy(15, 8);
    printf("<--:Examination Management System:-->");
    gotoxy(19, 15);
    printf("Press any key to continue.");
    getch();
    menu();
    return 0;
}

void menu()
{
    int choice;
    system("cls");
    gotoxy(10, 3);
    printf("<--:MENU:-->");
    gotoxy(10, 5);
    printf("Enter appropriate number to perform the following task.");
    gotoxy(10, 7);
    printf("1 : Add Student Record.");
    gotoxy(10, 8);
    printf("2 : View Student Records.");
    gotoxy(10, 9);
    printf("3 : Search Student Record.");
    gotoxy(10, 10);
    printf("4 : Modify Student Record.");
    gotoxy(10, 11);
    printf("5 : Delete Student Record.");
    gotoxy(10, 12);
    printf("6 : Add Exam Result.");
    gotoxy(10, 13);
    
    printf("7 : View Exam Results.");
    gotoxy(10, 14);
    printf("8 : Search Exam Result.");
    gotoxy(10, 15);
    printf("9 : Modify Exam Result.");
    gotoxy(10, 16);
    printf("10 : Delete Exam Result.");
    gotoxy(10, 17);
    printf("11 : Exit.");
    gotoxy(10, 20);
    printf("Enter your choice: ");
    scanf("%d", &choice);
    switch (choice)
    {
    case 1:
        add();
        break;

    case 2:
        view();

        break;

    case 3:
        search();
        break;

    case 4:
        modify();
        break;

    case 5:
        deleterec();
        break;

    case 6:
        addExamResult();
        break;

    case 7:
        viewExamResults();
        break;

    case 8:
        searchExamResult();
        break;

    case 9:
        modifyExamResult();
        break;

    case 10:
        deleteExamResult();
        break;

    case 11:
        exit(1);
        break;

    default:
        gotoxy(10, 22);
        printf("Invalid Choice.");
    }
}

void add()
{
    FILE *fp;
    struct student std;
    char yes = 'y';
    system("cls");

    fp = fopen("record.csv", "a+");
    if (fp == NULL)
    {
        gotoxy(10, 5);
        printf("Error opening file");
        exit(1);
    }
    fflush(stdin);
    while (yes == 'y')
    {
        gotoxy(10, 3);
        printf("<--:ADD RECORD:-->");
        gotoxy(10, 5);
        printf("Enter details of student.");
        gotoxy(10, 7);
        printf("Enter Name : ");
        gets(std.name);
        gotoxy(10, 8);
        printf("Enter Mobile Number : ");
        gets(std.mobile);
        gotoxy(10, 9);
        printf("Enter Roll No : ");
        scanf("%d", &std.rollno);
        fflush(stdin);
        gotoxy(10, 10);
        printf("Enter Course : ");
        gets(std.course);
        gotoxy(10, 11);
        printf("Enter Branch : ");
        gets(std.branch);
        gotoxy(10, 12);
        printf("Enter Year : ");
        scanf("%d", &std.year);
        fprintf(fp, "%s,%s,%d,%s,%s,%d\n", std.name, std.mobile, std.rollno, std.course, std.branch, std.year);
        fflush(fp);
        gotoxy(10, 15);
        printf("Want to add another record? Then press 'y' else 'n'.");
        fflush(stdin);
        yes = getch();
        system("cls");
        fflush(stdin);
    }
    fclose(fp);
    gotoxy(10, 18);
    printf("Press any key to continue.");
    getch();
    menu();
}

void view()
{
    FILE *fp;
    struct student std;
    system("cls");
    gotoxy(10, 3);
    printf("<--:VIEW RECORD:-->");
    gotoxy(10, 5);
    printf("S.No   Name of Student       Mobile No      Roll No        Course                  Branch                                Year");
    gotoxy(10, 6);
    printf("------------------------------------------------------------------------------------------------------------------------------");
    fp = fopen("record.csv", "r");
    if (fp == NULL)
    {
        gotoxy(10, 8);
        printf("Error opening file.");
        exit(1);
    }

    int i = 1, j = 8;
    while (fscanf(fp, "%[^,],%[^,],%d,%[^,],%[^,],%d\n", std.name, std.mobile, &std.rollno, std.course, std.branch, &std.year) != EOF)
    {
        gotoxy(10, j);
        printf("%-7d%-22s%-15s%-15d%-24s%-40s%-6d\n", i, std.name, std.mobile, std.rollno, std.course, std.branch, std.year);
        i++;
        j++;
    }

    fclose(fp);
    gotoxy(10, j + 3);
    printf("Press any key to continue.");
    getch();
    menu();
}

void search()
{
    FILE *fp;
    struct student std;
    int n;
    system("cls");
    gotoxy(10, 3);
    printf("<--:SEARCH RECORD:-->");
    gotoxy(10, 5);
    printf("Enter roll no. of the student : ");
    fflush(stdin);
    scanf("%d", &n);
    fp = fopen("record.csv", "r");
    if (fp == NULL)
    {
        gotoxy(10, 6);
        printf("Error opening file");
        exit(1);
    }

    int found = 0;
    while (fscanf(fp, "%[^,],%[^,],%d,%[^,],%[^,],%d\n", std.name, std.mobile, &std.rollno, std.course, std.branch, &std.year) != EOF)
    {
        if (n == std.rollno)
        {
            gotoxy(10, 8);
            printf("Name : %s", std.name);
            gotoxy(10, 9);
            printf("Mobile Number : %s", std.mobile);
            gotoxy(10, 10);
            printf("Roll No : %d", std.rollno);
            gotoxy(10, 11);
            printf("Course : %s", std.course);
            gotoxy(10, 12);
            printf("Branch : %s", std.branch);
            gotoxy(10, 13);
            printf("Year : %d", std.year);
            found = 1;
            break;
        }
    }
    if (!found)
    {
        gotoxy(10, 8);
        printf("Record not found!");
    }

    fclose(fp);
    gotoxy(10, 16);
    printf("Press any key to continue.");
    getch();
    menu();
}

void modify()
{
    int rollNo;
    FILE *fp, *ft;
    struct student std;
    system("cls");
    gotoxy(10, 3);
    printf("<--:MODIFY RECORD:-->");
    gotoxy(10, 5);
    printf("Enter roll number of student to modify: ");
    fflush(stdin);
    scanf("%d", &rollNo);
    fp = fopen("record.csv", "r");
    if (fp == NULL)
    {
        gotoxy(10, 6);
        printf("Error opening file");
        exit(1);
    }
    ft = fopen("temp.csv", "w");
    if (ft == NULL)
    {
        gotoxy(10, 6);
        printf("Error opening file");
        exit(1);
    }
    int found = 0;
    while (fscanf(fp, "%[^,],%[^,],%d,%[^,],%[^,],%d\n", std.name, std.mobile, &std.rollno, std.course, std.branch, &std.year) != EOF)
    {
        if (rollNo == std.rollno)
        {
            gotoxy(10, 7);
            printf("Enter name: ");
            fflush(stdin);
            gets(std.name);
            gotoxy(10, 8);
            printf("Enter mobile number : ");
            gets(std.mobile);
            gotoxy(10, 9);
            printf("Enter roll no : ");
            scanf("%d", &std.rollno);
            fflush(stdin);
            gotoxy(10, 10);
            printf("Enter Course : ");
            gets(std.course);
            gotoxy(10, 11);
            printf("Enter Branch : ");
            gets(std.branch);
            gotoxy(10, 12);
            printf("Enter Year : ");
            scanf("%d", &std.year);
            found = 1;
        }
        fprintf(ft, "%s,%s,%d,%s,%s,%d\n", std.name, std.mobile, std.rollno, std.course, std.branch, std.year);
    }

    fclose(fp);
    fclose(ft);

    remove("record.csv");
    rename("temp.csv", "record.csv");

    if (!found)
    {
        gotoxy(10, 7);
        printf("Record not found!");
    }

    gotoxy(10, 16);
    printf("Press any key to continue.");
    getch();
    menu();
}

void deleterec()
{
    int rollNo;
    FILE *fp, *ft;
    struct student std;
    system("cls");
    gotoxy(10, 3);
    printf("<--:DELETE STUDENT RECORD:-->");
    gotoxy(10, 5);
    printf("Enter roll number of student to delete record: ");
    fflush(stdin);
    scanf("%d", &rollNo);
    fp = fopen("record.csv", "r");
    if (fp == NULL)
    {
        gotoxy(10, 6);
        printf("Error opening file");
        exit(1);
    }
    ft = fopen("temp.csv", "w");
    if (ft == NULL)
    {
        gotoxy(10, 6);
        printf("Error opening file");
        exit(1);
    }

    int found = 0;
    while (fscanf(fp, "%[^,],%[^,],%d,%[^,],%[^\n],%d\n", std.name, std.mobile, &std.rollno, std.course, std.branch, &std.year) != EOF)
    {
        if (rollNo != std.rollno)
        {
            fprintf(ft, "%s,%s,%d,%s,%s", std.name, std.mobile, std.rollno, std.course, std.branch);
        }
        else
        {
            found = 1;
        }
    }

    fclose(fp);
    fclose(ft);

    remove("record.csv");
    rename("temp.csv", "record.csv");

    if (!found)
    {
        gotoxy(10, 7);
        printf("Record not found!");
    }

    gotoxy(10, 10);
    printf("Press any key to continue.");
    getch();
    menu();
}

void addExamResult()
{
    FILE *fp;
    struct exam result;
    char another = 'y';
    system("cls");

    fp = fopen("exam_results.csv", "a+");
    if (fp == NULL)
    {
        gotoxy(10, 5);
        printf("Error opening file");
        exit(1);
    }

    fflush(stdin);
    while (another == 'y')
    {
        gotoxy(10, 3);
        printf("<--:ADD EXAM RESULT:-->");
        gotoxy(10, 5);
        printf("Enter Exam Result Details.");
        gotoxy(10, 7);
        printf("Enter Roll No: ");
        scanf("%d", &result.rollno);
        gotoxy(10, 8);
        printf("Enter Marks: ");
        scanf("%d", &result.marks);
        fprintf(fp, "%d,%d\n", result.rollno, result.marks);
        fflush(fp);
        gotoxy(10, 11);
        printf("Want to add another exam result? Then press 'y' else 'n'.");
        fflush(stdin);
        another = getch();
        system("cls");
        fflush(stdin);
    }
    fclose(fp);
    gotoxy(10, 14);
    printf("Press any key to continue.");
    getch();
    menu();
}

void viewExamResults()
{
    FILE *fp;
    struct exam result;
    system("cls");
    gotoxy(10, 3);
    printf("<--:VIEW EXAM RESULTS:-->");
    gotoxy(10, 5);
    printf("S.No   Roll No   Marks");
    gotoxy(10, 6);
    printf("-----------------------");
    fp = fopen("exam_results.csv", "r");
    if (fp == NULL)
    {
        gotoxy(10, 8);
        printf("Error opening file.");
        exit(1);
    }

    int i = 1, j = 8;
    while (fscanf(fp, "%d,%d\n", &result.rollno, &result.marks) != EOF)
    {
        gotoxy(10, j);
        printf("%-7d%-10d%-6d\n", i, result.rollno, result.marks);
        i++;
        j++;
    }

    fclose(fp);
    gotoxy(10, j + 3);
    printf("Press any key to continue.");
    getch();
    menu();
}

void searchExamResult()
{
    FILE *fp;
    struct exam result;
    int rollNo;
    system("cls");
    gotoxy(10, 3);
    printf("<--:SEARCH EXAM RESULT:-->");
    gotoxy(10, 5);
    printf("Enter roll no. of the student: ");
    fflush(stdin);
    scanf("%d", &rollNo);
    fp = fopen("exam_results.csv", "r");
    if (fp == NULL)
    {
        gotoxy(10, 6);
        printf("Error opening file");
        exit(1);
    }

    int found = 0;
    while (fscanf(fp, "%d,%d\n", &result.rollno, &result.marks) != EOF)
    {
        if (rollNo == result.rollno)
        {
            gotoxy(10, 8);
            printf("Roll No: %d", result.rollno);
            gotoxy(10, 9);
            printf("Marks: %d", result.marks);
            found = 1;
            break;
        }
    }

    if (!found)
    {
        gotoxy(10, 8);
        printf("Record not found!");
    }

    fclose(fp);
    gotoxy(10, 14);
    printf("Press any key to continue.");
    getch();
    menu();
}

void modifyExamResult()
{
    int rollNo;
    FILE *fp, *ft;
    struct exam result;
    system("cls");
    gotoxy(10, 3);
    printf("<--:MODIFY EXAM RESULT:-->");
    gotoxy(10, 5);
    printf("Enter roll number of student to modify exam result: ");
    fflush(stdin);
    scanf("%d", &rollNo);
    fp = fopen("exam_results.csv", "r");
    if (fp == NULL)
    {
        gotoxy(10, 6);
        printf("Error opening file");
        exit(1);
    }
    ft = fopen("temp.csv", "w");
    if (ft == NULL)
    {
        gotoxy(10, 6);
        printf("Error opening file");
        exit(1);
    }
    int found = 0;
    while (fscanf(fp, "%d,%d\n", &result.rollno, &result.marks) != EOF)
    {
        if (rollNo == result.rollno)
        {
            gotoxy(10, 7);
            printf("Enter new marks: ");
            scanf("%d", &result.marks);
            fprintf(ft, "%d,%d\n", result.rollno, result.marks);
            found = 1;
        }
        else
        {
            fprintf(ft, "%d,%d\n", result.rollno, result.marks);
        }
    }

    fclose(fp);
    fclose(ft);

    remove("exam_results.csv");
    rename("temp.csv", "exam_results.csv");

    if (!found)
    {
        gotoxy(10, 7);
        printf("Record not found!");
    }
    else
    {
        gotoxy(10, 7);
        printf("Record modified successfully.");
    }

    gotoxy(10, 14);
    printf("Press any key to continue.");
    getch();
    menu();
}

void deleteExamResult()
{
    int rollNo;
    FILE *fp, *ft;
    struct exam result;
    system("cls");
    gotoxy(10, 3);
    printf("<--:DELETE EXAM RESULT:-->");
    gotoxy(10, 5);
    printf("Enter roll number of student to delete exam result: ");
    fflush(stdin);
    scanf("%d", &rollNo);
    fp = fopen("exam_results.csv", "r");
    if (fp == NULL)
    {
        gotoxy(10, 6);
        printf("Error opening file");
        exit(1);
    }
    ft = fopen("temp.csv", "w");
    if (ft == NULL)
    {
        gotoxy(10, 6);
        printf("Error opening file");
        exit(1);
    }

    int found = 0;
    while (fscanf(fp, "%d,%d\n", &result.rollno, &result.marks) != EOF)
    {
        if (rollNo != result.rollno)
        {
            fprintf(ft, "%d,%d\n", result.rollno, result.marks);
        }
        else
        {
            found = 1;
        }
    }

    fclose(fp);
    fclose(ft);

    remove("exam_results.csv");
    rename("temp.csv", "exam_results.csv");

    if (!found)
    {
        gotoxy(10, 7);
        printf("Record not found!");
    }

    gotoxy(10, 14);
    printf("Press any key to continue.");
    getch();
    menu();
}
