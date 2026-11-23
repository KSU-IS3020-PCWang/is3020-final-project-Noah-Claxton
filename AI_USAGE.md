# AI Improvement Record

## Original Development

For my IS 3020 final project, I chose to create a Football Equipment Inventory Tracker because I wanted to build something related to my experience working in football operations. Keeping track of helmets, shoulder pads, jerseys, and other equipment is an important part of
keeping a program running. I started by identifying the main problems I wanted the application to solve, including tracking equipment, assigning gear to players, recording returns, and identifying damaged items. I planned to use Python concepts from class, such as functions, loops, dictionaries, conditionals, and CSV files. I also used ChatGPT during the planning and initial code development stages. ChatGPT helped review my proposal and tested a version of the Python application that I created.

## AI Tools Used

The main AI tool I used was OpenAI ChatGPT. I used it to help reviwe the Python application, explain parts of the code, troubleshoot questions about running the program in PyCharm, and grammar correct project documentation.


## Improvements Requested

After deciding on the original application features, I asked ChatGPT to help include several additional functions. The first improvement was making the maintenance list a required feature. I wanted an easy way to identify equipment marked as needing repair or replacement instead of searching through the entire inventory. This was also suggested by my teacher, however I saw it late and decided to add it. The second improvement was a player lookup feature. This would allow an operations directer or someone from their team to enter a player's name or number and see all equipment currently assigned to that player. The third improvement was an end-of-season report. This report would identify equipment that had not been returned and show which players were responsible for those items. I also requested that the additional code stay within the Python concepts I had learned in IS 3020 rather than using advanced programming techniques.


## Changes Accepted

1. Maintenance List

The maintenance list identifies equipment marked as "Needs Repair" or "Replace." I accepted this feature because equipment condition is important in football, and staff should be able to find items requiring attention quickly. The feature uses a loop to check equipment records and conditional statements to identify items based on their condition.

2. Player Equipment Lookup

The player lookup allows a user to search for a player and view the equipment currently assigned to them. I accepted this change because it makes equipment tracking easier, especially when several items are assigned to the same player. The function searches the inventory records and displays items that match the player's information.

3. End-of-Season Report

The end-of-season report displays equipment that is still checked out. I accepted this change because collecting and accounting for equipment is an important responsibility at the end of a football season. The report checks the assignment status of equipment and displays items that have not been returned. This will eliminate not knowing where equipment is or if it has been returned or not. 

## Changes Rejected or Revised

One important decision was to keep the application simple rather than expanding it into a more advanced system. I wanted the project to remain appropriate for the Python concepts covered in IS 3020. I kept the command-line menu instead of adding a graphical interface. I also stayed with CSV file storage instead of using a database. These decisions made the application easier to understand and kept the focus on the main equipment management features.

## What I Learned

This project helped me better understand how the Python concepts we learned in class can be combined to create a useful application. Instead of writing a program that only performs one task, I worked with a system that allows users to choose different actions through a menu. I learned more about how dictionaries can organize equipment information and how lists can hold multiple records. I also saw how functions make a larger program easier to organize by separating tasks such as adding equipment, searching for items, and recording returns. Another important part was learning how CSV files allow information to be saved and loaded between sessions. When I first ran the application in PyCharm, it displayed a message saying that no inventory file was found. I learned that this was expected because the program was designed to begin with an empty inventory when the CSV file did not exist. Using ChatGPT also showed me why reviewing AI-generated code is important. Even when AI provides a working example, I still need to understand what each function does, how the information is stored, and how different parts of the program work together. Overall, the project helped me connect my experience in football operations with the programming concepts we covered in IS 3020.
