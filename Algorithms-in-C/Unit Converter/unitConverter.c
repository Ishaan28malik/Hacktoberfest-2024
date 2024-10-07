#include <stdio.h>

// Function prototypes
void temperatureConversion();
void distanceConversion();
void weightConversion();

int main() {
    int choice;
    
    do {
        // Menu
        printf("\n--- Unit Converter ---\n");
        printf("1. Temperature Conversion\n");
        printf("2. Distance Conversion\n");
        printf("3. Weight Conversion\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                temperatureConversion();
                break;
            case 2:
                distanceConversion();
                break;
            case 3:
                weightConversion();
                break;
            case 4:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while (choice != 4);

    return 0;
}

// Temperature Conversion
void temperatureConversion() {
    int choice;
    float temp, convertedTemp;

    printf("\n--- Temperature Conversion ---\n");
    printf("1. Celsius to Fahrenheit\n");
    printf("2. Fahrenheit to Celsius\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    if (choice == 1) {
        printf("Enter temperature in Celsius: ");
        scanf("%f", &temp);
        convertedTemp = (temp * 9 / 5) + 32;
        printf("%.2f Celsius = %.2f Fahrenheit\n", temp, convertedTemp);
    } else if (choice == 2) {
        printf("Enter temperature in Fahrenheit: ");
        scanf("%f", &temp);
        convertedTemp = (temp - 32) * 5 / 9;
        printf("%.2f Fahrenheit = %.2f Celsius\n", temp, convertedTemp);
    } else {
        printf("Invalid choice!\n");
    }
}

// Distance Conversion
void distanceConversion() {
    int choice;
    float distance, convertedDistance;

    printf("\n--- Distance Conversion ---\n");
    printf("1. Kilometers to Miles\n");
    printf("2. Miles to Kilometers\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    if (choice == 1) {
        printf("Enter distance in kilometers: ");
        scanf("%f", &distance);
        convertedDistance = distance * 0.621371;
        printf("%.2f kilometers = %.2f miles\n", distance, convertedDistance);
    } else if (choice == 2) {
        printf("Enter distance in miles: ");
        scanf("%f", &distance);
        convertedDistance = distance / 0.621371;
        printf("%.2f miles = %.2f kilometers\n", distance, convertedDistance);
    } else {
        printf("Invalid choice!\n");
    }
}

// Weight Conversion
void weightConversion() {
    int choice;
    float weight, convertedWeight;

    printf("\n--- Weight Conversion ---\n");
    printf("1. Kilograms to Pounds\n");
    printf("2. Pounds to Kilograms\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    if (choice == 1) {
        printf("Enter weight in kilograms: ");
        scanf("%f", &weight);
        convertedWeight = weight * 2.20462;
        printf("%.2f kilograms = %.2f pounds\n", weight, convertedWeight);
    } else if (choice == 2) {
        printf("Enter weight in pounds: ");
        scanf("%f", &weight);
        convertedWeight = weight / 2.20462;
        printf("%.2f pounds = %.2f kilograms\n", weight, convertedWeight);
    } else {
        printf("Invalid choice!\n");
    }
}
