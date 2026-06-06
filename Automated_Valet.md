# 🚗 Automated Valet Parking System (C)

## Overview

The Automated Valet Parking System is a console-based parking management application developed in C. It simulates a real-world parking lot using a 2D grid structure and provides features such as vehicle parking, retrieval, billing, parking visualization, and occupancy analytics.

The project demonstrates the use of data structures, arrays, structures, file organization, and time-based calculations in C programming.

---

## Features

### Vehicle Parking

* Park Cars, Bikes, and EVs.
* Automatically assigns the nearest available parking slot.
* Stores vehicle details and entry time.

### 2D Parking Grid Visualization

* Displays the parking lot as a 2D grid.
* Empty slots are shown separately from occupied slots.
* Occupied slots display a short version of the vehicle number plate.

### Automated Billing

* Calculates parking duration using system time.
* Generates parking charges automatically.
* Current billing rate: ₹10 per minute.

### Vehicle Retrieval

* Retrieve a vehicle using its parking slot.
* Displays parking duration and total bill.
* Frees the slot after retrieval.

### Parking Analytics

* Total parking slots.
* Occupied slots.
* Available slots.
* Parking occupancy percentage.

---

## Technologies Used

* C Programming
* Structures
* 2D Arrays
* String Handling
* Time Library (`time.h`)
* ANSI Terminal Colors

---

## How to Run

### Compile

```bash
gcc Automated_Valet.c -o Automated
```

### Execute

```bash
./Automated
```

For Windows:

```bash
parking.exe
```

---

## Menu Options

```text
1. Park a Vehicle
2. Retrieve a Vehicle
3. Show Parking Grid
4. Analytics
5. Exit
```

---

## Sample Workflow

1. Select "Park a Vehicle".
2. Enter vehicle type and number plate.
3. System assigns the nearest available slot.
4. View the parking grid.
5. Retrieve the vehicle.
6. Receive parking bill.
7. Check analytics dashboard.

---

## Learning Outcomes

This project helped in understanding:

* Structures in C
* Multi-dimensional arrays
* Real-time data handling
* Time-based calculations
* Console application development
* Problem-solving using C

---

## Future Improvements

* File handling for persistent storage
* User authentication
* Vehicle search by number plate
* Dynamic parking capacity
* Different billing rates for Cars, Bikes, and EVs
* Graphical User Interface (GUI)

---

