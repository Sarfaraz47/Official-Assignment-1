{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Calculate Area of a Circle"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Write a Python program which accepts the radius of a circle from the user and compute the area.\n",
    "###### Program Console Sample Output 1:\n",
    "###### Input Radius: 0.5\n",
    "###### Area of Circle with radius 0.5 is 0.7853981634"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the radius of a circle:0.5\n",
      "Area of a circle with radius 0.5 is 3.142\n"
     ]
    }
   ],
   "source": [
    "radius = float(input(\"Enter the radius of a circle:\"))\n",
    "pi = 3.142\n",
    "Area = pi*radius*2\n",
    "print(f\"Area of a circle with radius {radius} is {Area}\")"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Check Number either positive, negative or zero"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Write a Python program to check if a number is positive, negative or zero\n",
    "###### Program Console Sample Output 1:\n",
    "###### Enter Number: -1\n",
    "##### Negative Number Entered\n",
    "###### Program Console Sample Output 2:\n",
    "##### Integer: 3\n",
    "##### Positive Number Entered\n",
    "###### Program Console Sample Output 3:\n",
    "##### Integer: 0\n",
    "###### Zero Entered"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the given number: -1\n",
      "Negative number entered\n"
     ]
    }
   ],
   "source": [
    "number = float(input(\"Enter the given number: \"))\n",
    "if number < 0:\n",
    "    print(\"Negative number entered\")\n",
    "elif number > 0: \n",
    "    print(\"Positive number entered\")\n",
    "elif number == 0:\n",
    "    print(\"Zero entered\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the given number: 3\n",
      "Positive number entered\n"
     ]
    }
   ],
   "source": [
    "number = int(input(\"Enter the given number: \"))\n",
    "if number < 0: \n",
    "    print(\"Negative number entered\")\n",
    "elif number > 0: \n",
    "    print(\"Positive number entered\")\n",
    "elif number == 0: \n",
    "    print(\"Zero entered\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the given number: 0\n",
      "Zero entered\n"
     ]
    }
   ],
   "source": [
    "number = int(input(\"Enter the given number: \"))\n",
    "if number < 0:\n",
    "    print(\"Positive number entered\")\n",
    "elif number > 0:\n",
    "    print(\"Negative number entered\")\n",
    "elif number == 0:\n",
    "    print(\"Zero entered\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Divisibility Check of two numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Write a Python program to check whether a number is completely divisible by another number. Accept two integer values form the user\n",
    "##### Program Console Sample Output 1:\n",
    "###### Enter numerator: 4\n",
    "###### Enter Denominator: 2\n",
    "##### Number 4 is Completely divisible by 2\n",
    "###### Program Console Sample Output 2:\n",
    "##### Enter numerator: 7\n",
    "\n",
    "##### Enter Denominator: 4\n",
    "###### Number 7 is not Completely divisible by 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the numerator: 4\n",
      "Enter the denominator: 2\n",
      "4 is completely divisible by 2\n"
     ]
    }
   ],
   "source": [
    "numerator = int(input(\"Enter the numerator: \"))\n",
    "denominator = int(input(\"Enter the denominator: \"))\n",
    "if numerator % denominator == 0: \n",
    "    print(f\"{numerator} is completely divisible by {denominator}\")\n",
    "else:\n",
    "    print(f\"{numerator} is not completely divisble by {denominator}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the numerator: 7\n",
      "Enter the denominator: 4\n",
      "7 is not completely divisible by 4\n"
     ]
    }
   ],
   "source": [
    "numerator = int(input(\"Enter the numerator: \"))\n",
    "denominator = int(input(\"Enter the denominator: \"))\n",
    "if numerator % denominator == 0:\n",
    "    print(f\"{numerator} is completely divisible by{denominator}\")\n",
    "else:\n",
    "    print(f\"{numerator} is not completely divisible by {denominator}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Calculate Volume of a sphere"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Write a Python program to get the volume of a sphere, please take the radius as input from user"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Program Console Output:\n",
    "##### Enter Radius of Sphere: 1\n",
    "###### Volume of the Sphere with Radius 1 is 4.18"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter radius of sphere: 1\n",
      "volume of sphere with radius 1.0 is 4.19\n"
     ]
    }
   ],
   "source": [
    "radius = float(input(\"Enter radius of sphere: \"))\n",
    "pi = 3.142\n",
    "volume_of_sphere = 4/3 * pi * radius**3\n",
    "volume_of_sphere = round(volume_of_sphere,2)\n",
    "print(f\"volume of sphere with radius {radius} is {volume_of_sphere}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Copy string n times\n",
    "#### Write a Python program to get a string which is n (non-negative integer) copies of a given string.\n",
    "##### Program Console Output:\n",
    "##### Enter String: Hi\n",
    "###### How many copies of String you need: 4\n",
    "###### 4 Copies of Hi are HiHiHiHi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter string: Hi\n",
      "How many copies of string you need: 4\n",
      "4 copies of Hi are HiHiHiHi\n"
     ]
    }
   ],
   "source": [
    "a = input(\"Enter string: \")\n",
    "b = int(input(\"How many copies of string you need: \")) \n",
    "print(f\"{b} copies of {a} are {a*b}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Check if number is Even or Odd\n",
    "### Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user\n",
    "#### Program Console Output 1:\n",
    "##### Enter Number: 4\n",
    "###### 4 is Even\n",
    "#### Program Console Output 2:\n",
    "##### Enter Number: 9\n",
    "###### 9 is Odd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number: 4\n",
      "4 is even\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"enter the number: \"))\n",
    "if a == 4: \n",
    "    print(f\"{a} is even\")\n",
    "elif a == 3:\n",
    "    print(f\"{a} is odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number: 9\n",
      "9 is odd\n"
     ]
    }
   ],
   "source": [
    "b = int(input(\"enter the number: \"))\n",
    "if b == 2:\n",
    "    print(f\"{b} is even\")\n",
    "elif b == 9:\n",
    "    print(f\"{b} is odd\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. Vowel Tester\n",
    "### Write a Python program to test whether a passed letter is a vowel or not\n",
    "#### Program Console Output 1:\n",
    "##### Enter a character: A\n",
    "###### Letter A is Vowel\n",
    "#### Program Console Output 2:\n",
    "##### Enter a character: e\n",
    "###### Letter e is Vowel\n",
    "#### Program Console Output 2:\n",
    "##### Enter a character: N\n",
    "###### Letter N is not Vowel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter any leeter: a\n",
      "letter a is vowel\n"
     ]
    }
   ],
   "source": [
    "vowels = (input(\"enter any leeter: \"))\n",
    "if vowels == 'a' or vowels == 'e' or vowels == 'i' or vowels == 'o' or vowels == 'u':\n",
    "    print(f\"letter {vowels} is vowel\")\n",
    "else:\n",
    "    print(f\"letter{vowels} is not vowel\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter any letter: e\n",
      "letter e is vowel\n"
     ]
    }
   ],
   "source": [
    "vowels = (input(\"enter any letter: \"))\n",
    "if vowels == 'a' or vowels == 'e' or vowels == 'i' or vowels == 'o' or vowels == 'u':\n",
    "    print(f\"letter {vowels} is vowel\")\n",
    "else:\n",
    "    print(f\"letter {vowels} is not a vowel\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter any letter: N\n",
      "letter N is not a vowel\n"
     ]
    }
   ],
   "source": [
    "vowels = (input(\"enter any letter: \"))\n",
    "if vowels == 'a' or vowels == 'e' or vowels == 'i' or vowels == 'o' or vowels == 'u':\n",
    "    print(f\"letter {vowels} is vowel\")\n",
    "else:\n",
    "    print(f\"letter {vowels} is not a vowel\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8. Triangle area\n",
    "### Write a Python program that will accept the base and height of a triangle and compute the area\n",
    "###### Reference:\n",
    "https://www.mathgoodies.com/lessons/vol1/area_triangle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the base of a triangle: 8\n",
      "enter the height of a triangle: 7\n",
      "The Area oa a triangle is 28.0\n"
     ]
    }
   ],
   "source": [
    "base = int(input(\"enter the base of a triangle: \"))\n",
    "height = int(input(\"enter the height of a triangle: \"))\n",
    "A= base*height/2\n",
    "print(f\"The Area oa a triangle is {A}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9. Calculate Interest\n",
    "### Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years\n",
    "#### Program Console Sample 1:\n",
    "##### Please enter principal amount: 10000\n",
    "###### Please Enter Rate of interest in %: 0.1\n",
    "###### Enter number of years for investment: 5\n",
    "###### After 5 years your principal amount 10000 over an interest rate of 0.1 % will be 16105.1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the principal amount: 1000\n",
      "enter rate of interest: 0.1\n",
      "enter number of years of investment: 5\n",
      "After 5 years your principal amount 1000 over an interest rate of 0.1% will be 1000.01\n"
     ]
    }
   ],
   "source": [
    "p = int(input(\"enter the principal amount: \"))\n",
    "r = float(input(\"enter rate of interest: \"))\n",
    "t = int(input(\"enter number of years of investment: \"))\n",
    "rate = r * 100\n",
    "i = p * (1 + (rate/100) ** t)    #interest formula\n",
    "i = round(i,2)\n",
    "print(f\"After {t} years your principal amount {p} over an interest rate of {r}% will be {i}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Reference:\n",
    "https://en.wikipedia.org/wiki/Euclidean_distance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter co-ordinate for x1: 2\n",
      "enter co-ordinate for x2: 4\n",
      "enter co-ordinate for y1: 4\n",
      "enter co-ordinate for y2; 4\n",
      "the distance between point (2.0, 4.0) and (4.0, 4.0) is: 2\n"
     ]
    }
   ],
   "source": [
    "x1 = float(input(\"enter co-ordinate for x1: \"))\n",
    "x2 = float(input(\"enter co-ordinate for x2: \"))\n",
    "y1 = float(input(\"enter co-ordinate for y1: \"))\n",
    "y2 = float(input(\"enter co-ordinate for y2; \"))\n",
    "d = ((y1-x1)**2 + (y2-x2)**2)**.5   #euclidean distance formula between point (x1, y1) and (x2, y2).\n",
    "distance = round(d,)\n",
    "print(f\"the distance between point {x1, y1} and {x2, y2} is: {distance}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 11. Feet to Centimeter Converter\n",
    "### Write a Python program to convert height in feet to centimetres.\n",
    "##### Program Console Sample 1:\n",
    "###### Enter Height in Feet: 5\n",
    "###### There are 152.4 Cm in 5 ft\n",
    "###### Reference:\n",
    "https://www.rapidtables.com/convert/length/feet-to-cm.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the value of height in feet: 5\n",
      "There are 152.4 cm in 5 ft\n"
     ]
    }
   ],
   "source": [
    "height = int(input(\"enter the value of height in feet: \"))\n",
    "value = height * 30.48\n",
    "print(f\"There are {value} cm in {height} ft\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 12. BMI Calculator\n",
    "### Write a Python program to calculate body mass index\n",
    "##### Program Console Sample 1:\n",
    "###### Enter Height in Cm: 180\n",
    "###### Enter Weight in Kg: 75\n",
    "###### Your BMI is 23.15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the value of height180\n",
      "emter the value of mass75\n",
      "Your BMI is 23.15\n"
     ]
    }
   ],
   "source": [
    "height = float(input(\"enter the value of height\"))\n",
    "mass = int(input(\"emter the value of mass\"))\n",
    "a = height /100\n",
    "value = round(mass /a**2,2)\n",
    "print(f\"Your BMI is {value}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 13. Sum of n Positive Integers\n",
    "### Write a python program to sum of the first n positive integers\n",
    "#### Program Console Sample 1:\n",
    "###### Enter value of n: 5\n",
    "###### Sum of n Positive integers till 5 is 15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the value: 5\n",
      "Sum of n integer numbers till 5 is 15.0\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"enter the value: \"))\n",
    "a = n * (n+1)/2\n",
    "print(f\"Sum of n integer numbers till {n} is {a}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 14. Digits Sum of a Number\n",
    "### Write a Python program to calculate the sum of the digits in an integer\n",
    "#### Program Console Sample 1:\n",
    "##### Enter a number: 15\n",
    "###### Sum of 1 + 5 is 6\n",
    "#### Program Console Sample 2:\n",
    "##### Enter a number: 1234\n",
    "###### Sum of 1 + 2 + 3 + 4 is 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Integer Value:2222\n",
      "Sum of digits are: 8\n"
     ]
    }
   ],
   "source": [
    "n = input(\"Enter Integer Value:\")\n",
    "sum = 0\n",
    "for d in n:\n",
    "    sum+=int(d)\n",
    "print(f\"Sum of digits are:\",sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
