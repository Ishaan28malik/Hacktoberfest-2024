#include <stdio.h>
#include <stdlib.h>

int isLeapYear(int year) {
    return ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0));
}

int isValidDate(int day, int month, int year) {
    if (year < 1 || month < 1 || month > 12 || day < 1)
        return 0;

    int daysInMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    if (isLeapYear(year))
        daysInMonth[2] = 29;

    return day <= daysInMonth[month];
}

void calculateAge(int present_date, int present_month, int present_year, int birth_date, int birth_month, int birth_year) {
   if (!isValidDate(present_date, present_month, present_year) || !isValidDate(birth_date, birth_month, birth_year)) {
        printf("Invalid input date.\n");
        return;
    }
       
   if (birth_date > present_date) {
        present_date = present_date + 30;
        present_month = present_month - 1;
    }

    if (birth_month > present_month) {
        present_year = present_year - 1;
        present_month = present_month + 12;
    }
  
   int final_date = present_date - birth_date;
   int final_month = present_month - birth_month;
   int final_year = present_year - birth_year;
  
   printf("Your Age -> Years: %d Months: %d Days: %d", final_year, final_month, final_date);
}

int main() {
    int present_date, present_month, present_year;
    int birth_date, birth_month, birth_year;

    printf("Enter the current date (DD MM YYYY): ");
    scanf("%d %d %d", &present_date, &present_month, &present_year);

    printf("Enter your birth date (DD MM YYYY): ");
    scanf("%d %d %d", &birth_date, &birth_month, &birth_year);
  
   calculateAge(present_date, present_month, present_year, birth_date, birth_month, birth_year);
   
   return 0;
}
