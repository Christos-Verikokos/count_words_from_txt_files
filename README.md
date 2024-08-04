# count_words_from_txt_files
Search for user-specified words within the contents of files, using paths provided in a specified list file.

Improve exercise 10-10 from "Python crash course" book:
Searching for Specific Words in Multiple Files
Description:

* Write a program that reads a list of file paths from a default text file or given by user,
  if is not extist file show appropriate message.
* Ask the user which words to search for. If user doesn't type any words or type empty
  registrations, show appropriate erros message.
* For each file path, open the file and search for words specified by the user
  and count it.
* Print the file name and number of times where each word appears.

Steps:

Create a file containing file paths:
Create a text file (e.g., file_paths.txt) and list the paths of several text files to search within.
Write the program:
Read the list of file paths from the default file_paths.txt file or given by user.
Prompt the user to enter words to search for.
For each word, open each file and search for the word within the file.
Print the name of the file and the lines containing the word.
