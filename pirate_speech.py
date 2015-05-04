import urllib

def read_text():
    quotes = open("C:\Users\jbarragan\Python\movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    change_pirate_speech(contents_of_file)

def change_pirate_speech(text_to_check):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
    
    
