from pathlib import Path


#Function that search specific one or more words each text and print results.
def word_count(path,words):
    text = Path(path)
    try:
        contents = text.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"File not found with path: {path}.")
    else:
        if words:
            file_name = path.split('/')[-1]
            print(f"- '{file_name}' contains of the following words according to:")
            for word in words:
                times = contents.lower().count(f" {word} ")
                print(f"   The word '{word}' exists {times} times.") 

#Words given by the user.
def given_words_by_user():
    given_words = []
    print("Tell me which words you want to be counted in the texts. To exit, type 'e' (end): ")
    given_count = 1
    while True:
        temp = input(f"Word {given_count}: ")
        
        if temp == 'e':
            break
        elif temp:
            given_words.append(temp.strip())
            given_count += 1
        else: 
            print("Type a word.")
    if not given_words:
        print("You didn't type any words for search. I can't search.")
    else:
        return  given_words

#Names of text files  are taken from file that it contains the paths of them and inserted in a list.
def main_file(container_filename='/Users/macbook/Documents/python projects/pcc doc/temp/improve 10-10/paths.txt'):    
    pathsfile = Path(container_filename)
    try:
        contents_pathsfile = pathsfile.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("The file is not exist. You can't go to the next step")
        return False
    else:
        return contents_pathsfile.splitlines()

main_file_path = input("Type file's path that it contains paths of searching:\notherwise press enter for searching by default file.")

if not main_file_path:  #Whether the user has not typed any path. Continued by default path.
    file_names = main_file()
    words_list = given_words_by_user()
      
    for filename in file_names:
            word_count(filename,words_list)      
else:                   #Whether the user has typed any path and existed
    file_names = main_file(main_file_path)
    if file_names:
        words_list = given_words_by_user()
        for filename in file_names:
            word_count(filename,words_list)



    



