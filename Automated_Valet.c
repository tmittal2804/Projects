#include <stdio.h>
#include <string.h>
#include <time.h>

// Parking Lot Size
#define ROWS 3
#define COLS 5

// Colour Codes
#define RED     "\033[1;31m"
#define GREEN   "\033[1;32m"
#define YELLOW  "\033[1;33m"
#define CYAN    "\033[1;36m"
#define RESET   "\033[0m"
#define CLEAR   "\033[2J\033[1;1H"

// Vehicle Storage Structure
struct Slot {
    int occupied;
    char vehicleType[10];   // Car / Bike / EV
    char numberPlate[15];
    time_t entryTime;
};



struct Slot parking[ROWS][COLS];
// ------------------------------
// Show Parking Grid (2D)
// ------------------------------
void showParking() {
    printf(CLEAR);
    printf(CYAN "\n======= PARKING LOT (2-D VIEW) =======\n\n" RESET);

    for(int r = 0; r < ROWS; r++) {
        for(int c = 0; c < COLS; c++) {
            if(parking[r][c].occupied) {
                char shortPlate[4];
                strncpy(shortPlate, parking[r][c].numberPlate, 3);
                shortPlate[3] = '\0';
                printf(RED "[%3s]" RESET "  ", shortPlate);
            } else {
                printf(GREEN "[   ]" RESET "  ");
            }
        }
        printf("\n");
    }

    printf("\n" YELLOW "Legend:" RESET
           "  " GREEN "[   ] Empty" RESET
           "   " RED "[ABC] Occupied" RESET "\n");
}



// ------------------------------
// Park a Vehicle
// ------------------------------
void parkVehicle() {
    char type[10], plate[15];

    printf("\nEnter Vehicle Type (Car/Bike/EV): ");
    scanf("%s", type);
    printf("Enter Number Plate: ");
    scanf("%s", plate);

    // Search nearest empty slot
    for(int r=0; r<ROWS; r++) {
        for(int c=0; c<COLS; c++) {
            if(!parking[r][c].occupied) {
                parking[r][c].occupied = 1;
                strcpy(parking[r][c].vehicleType, type);
                strcpy(parking[r][c].numberPlate, plate);
                parking[r][c].entryTime = time(NULL);

                printf(GREEN "\nVehicle successfully parked!" RESET "\n");
                printf("Slot: Row %d  Column %d\n", r+1, c+1);
                return;
            }
        }
    }

    printf(RED "\nParking Full! No space available.\n" RESET);
}



// ------------------------------
// Retrieve a Vehicle + Billing
// ------------------------------
void retrieveVehicle() {
    int r, c;

    printf("\nEnter Row and Column of vehicle: ");
    scanf("%d %d", &r, &c);

    r--; c--;

    if(r < 0 || r >= ROWS || c < 0 || c >= COLS) {
        printf(RED "Invalid slot!\n" RESET);
        return;
    }

    if(!parking[r][c].occupied) {
        printf(YELLOW "That slot is already empty!\n" RESET);
        return;
    }

    time_t now = time(NULL);
    double minutes = difftime(now, parking[r][c].entryTime) / 60.0;

    if(minutes < 1) minutes = 1; // minimum 1 minute charge

    int bill = (int)minutes * 10; // Rs 10 per minute

    printf(GREEN "\nVehicle Retrieved Successfully!" RESET "\n");
    printf("Vehicle: %s\n", parking[r][c].vehicleType);
    printf("Plate:   %s\n", parking[r][c].numberPlate);
    printf("Time Parked: %.1f minutes\n", minutes);
    printf("Total Bill: ₹%d\n", bill);

    parking[r][c].occupied = 0;
}



// ------------------------------
// Parking Analytics
// ------------------------------
void analytics() {
    int used = 0, total = ROWS * COLS;

    for(int r=0; r<ROWS; r++)
        for(int c=0; c<COLS; c++)
            if(parking[r][c].occupied) used++;

    printf(CYAN "\n------- PARKING ANALYTICS -------\n" RESET);
    printf("Total Slots: %d\n", total);
    printf("Occupied:    %d\n", used);
    printf("Free:        %d\n", total - used);
    printf("Occupancy:   %.2f%%\n", (used * 100.0) / total);
}



// ------------------------------
// Main Menu Loop
// ------------------------------
int main() {
    int choice;

    while(1) {
        printf(CYAN "\n======= AUTOMATED VALET SYSTEM =======\n" RESET);
        printf("1. Park a Vehicle\n");
        printf("2. Retrieve a Vehicle\n");
        printf("3. Show Parking Grid\n");
        printf("4. Analytics\n");
        printf("5. Exit\n");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1: parkVehicle(); break;
            case 2: retrieveVehicle(); break;
            case 3: showParking(); break;
            case 4: analytics(); break;
            case 5: printf("Goodbye!\n"); return 0;
            default: printf(RED "Invalid choice! Try again.\n" RESET);
        }
    }

    return 0;
}