# 88_Project-Electricity-Bill-Calculator_Ru-26-01632_1D_Mudit-Sahu
Program to Calculate Electricity Bill Using Slab-Wise Rates
1. Understand the Problem Statement and Define the Problem Clearly
Problem Statement
The aim is to write a program that calculates an electricity bill based on the number of electricity units consumed by a consumer.

The total electricity bill is calculated using:

Slab-wise rates: Different electricity rates are charged for different ranges of units consumed.

Fixed charge: A fixed amount added to the electricity bill.

Tax: A percentage of tax applied to the bill amount.

Finally, the program displays a formatted electricity bill showing the units consumed, energy charges, fixed charges, tax, and total amount payable.

Input
- Number of electricity units consumed.

Output
Consumer's electricity consumption.

Energy charges.

Fixed charges.

Tax amount.

Total electricity bill.

Assumed Slab-Wise Rates
For this program, assume the following electricity rates:

Units consumed

Rate per unit

0–100 units

₹2

101–200 units

₹3

201–300 units

₹5

Above 300 units

₹7

Fixed charge = ₹50

Tax = 5% of the subtotal.

2. Develop the Solution Using Proper Logic and Programming Concepts
A. Algorithm
Start the program.

Input the number of electricity units consumed.

Calculate energy charges according to the slab-wise rates.

Add the fixed charge of ₹50.

Calculate 5% tax on the subtotal.

Add the tax to the subtotal.

Display the formatted electricity bill.

Stop the program.

B. Calculation Logic
The electricity charges are calculated progressively:

First 100 units: 100 × ₹2 = ₹200

Next 100 units: 100 × ₹3 = ₹300

Next 100 units: 100 × ₹5 = ₹500

Above 300 units: Remaining units × ₹7

Formula:

Subtotal
=
Energy Charges
+
Fixed Charge
Subtotal=Energy Charges+Fixed Charge
Tax
=
Subtotal
×
5
100
Tax=Subtotal× 
100
5
​
 
Total Bill
=
Subtotal
+
Tax
Total Bill=Subtotal+Tax