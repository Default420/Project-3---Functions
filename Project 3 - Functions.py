# -*- coding: utf-8 -*-
"""Copy of Applied Tech. Project 3 - Question copy_v1.1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W234RE_8veTPPxz1OmrWR5ot-jBYooFs

### Instructions

#### Goal of the Project

This project is designed for you to practice and solve the activities that are based on the concepts covered in the following lessons:

 1.  While Loop, Data-Type Conversion and Conditional Statements.

 2.  Improving The Algorithm

---

#### Getting Started

Follow the steps described below to solve the project:

1. Click on the link provided below to open the Colab file for this project.
   
   https://colab.research.google.com/drive/1qaEa3FobEJKvDKnxPxWoFzd267ZjJmQd

2. Create the duplicate copy of the Colab file. Here are the steps to create the duplicate copy:

    - Click on the **File** menu. A new drop-down list will appear.

      <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/0_file_menu.png' width=500>

    - Click on the **Save a copy in Drive** option. A duplicate copy will get created. It will open up in the new tab on your web browser.

      <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/1_create_colab_duplicate_copy.png' width=500>

     - After creating the duplicate copy of the notebook, please rename it in the **YYYY-MM-DD_StudentName_Project3** format.

3. Now, write your code in the prescribed code cells.

---

#### Activity 1: Increment a Number by 50.

Write a function to increment a number by 50.

For example: if the number entered is 12 then expected output is: 12 + 50 = 62.

Follow the steps given below to achieve the desired result:

- **Step 1:** Ask the user to enter a number. Convert the data type of user input to integer and then store it in a variable `num`.

- **Step 2:** Create a function (using the `def` keyword) and name it `increment()` which takes one input, `n`.

- **Step 3:** Inside the function, add the input parameter `n` with `50` using the `+` operator and store the result in a variable `result`.

- **Step 4:** Print the result in the output using the `return` keyword. If you don't write the `return` statement, then this function will only add the numbers but won't give any output.

- **Step 5:** Call the `increment()` function (outside the function) and pass the variables `num` (the variable which holds the user input) as an input to this function.
"""

# Step 1: Ask the user to enter the first number as an integer and then store it in a variable num.
num = int(input("Enter the first number: "))

# Step 2: Create a function and name it 'increment()' which takes one input 'n'.
def increment(n):

  # Step 3: Add the input parameter 'n' with 50 using the '+' operator and store the result in a variable.
  result = n + 50

  # Step 5: Print the result in the output using the 'return' keyword.
  return result

# Step 5: Call the 'increment()' function and pass the variable 'num' as an input.
print("The result of incrementing the number by 50 is:", increment(num))

"""---

#### Activity 2: Multiplication of Two Numbers

Write a function to print the multiplication of two numbers.

For example, if `num_1 = 5` and `num2 = 15`, then result = 5 * 15 = 75

Follow the steps given below to achieve the desired result:

  - **Step 1:** Ask the user to enter the first number. Convert the data type of user input to integer using the `int()` function and then store it in a variable `num_1`.

  - **Step 2:** Ask the user to enter the second number. Convert the data type of user input to integer using the `int()` function and then store it in a variable `num_2`.

  - **Step 3:** Create a function (using the `def` keyword) and name it `multiplier()` which takes two inputs, `num1` and `num2`.

  - **Step 4:** Inside the function, multiply the input parameters `num1` and `num2` using the `*` operator and store the result in a variable `result`.

  - **Step 5:** Print the result in the output using the `return` keyword. If you don't write the `return` statement, then this function will only add the numbers but won't give any output.

  - **Step 6:** Now call the `multiplier()` function (outside the function) and pass the variables `num_1` and `num_2` (the variable which holds the user input) as an input to this function.
"""

# Step 1: Ask the user to enter the first number as an integer and then store it in a variable 'num_1'.
num_1 = int(input("Enter the first number: "))

# Step 2: Ask the user to enter the second number as an integer and then store it in a variable 'num_2'.
num_2 = int(input("Enter the second number: "))

# Step 3: Create a function and name it 'multiplier()' which takes two inputs, 'num1' and 'num2'.
def multiplier(num1, num2):

  # Step 4: Multiply the input parameters using the '*' operator and store the result in a variable.
  result = num1 * num2

  # Step 5: Print the result in the output using the 'return' keyword.
  return result

# Step 6: Call the 'multiplier()' function and pass the variables 'num_1' and 'num_2' as an input.
print("The result of multiplying the two numbers is:", multiplier(num_1, num_2))

"""---

### Submitting the Project

Follow the steps described below to submit the project.

1. After finishing the project, click on the **Share** button on the top right corner of the notebook. A new dialog box will appear.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/2_share_button.png' width=500>

2. In the dialog box, click on the **Copy link** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/3_copy_link.png' width=500>


3. The link of the duplicate copy (named as **YYYY-MM-DD_StudentName_Project3**) of the notebook will get copied

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/4_copy_link_confirmation.png' width=500>

4. Go to your dashboard and click on the **My Projects** option.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/5_student_dashboard.png' width=800>

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/6_my_projects.png' width=800>

5. Click on the **View Project** button for the project you want to submit.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/7_view_project.png' width=800>

6. Click on the **Submit Project Here** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/8_submit_project.png' width=800>

7. Paste the link to the project file named as **YYYY-MM-DD_StudentName_Project3** in the URL box and then click on the **Submit** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/9_enter_project_url.png' width=800>

---
"""