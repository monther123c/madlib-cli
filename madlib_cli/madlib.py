import re

## Main method
def User_service():

    print('''☆☆☆ Welcome to Madlib Creation Game ☆☆☆
☆☆☆ Madlib is a game where you decide the parts of the story ☆☆☆
☆☆☆ You will be asked to input multiple values for the game ☆☆☆
☆☆☆ Make your answers creative to make the game entertaining ☆☆☆
''')
    reuseable_text = read_template("assets/make_me_a_video_game_template.txt")
    text , words = parse_template(reuseable_text)
    print(words)
    filled_tuple = list()
    for word in words:
        filled_tuple.append(input(f"\ninsert a {word}\n"))
    with open("make_me_a_video_game_output.txt",'w') as file:
        temp = merge(text,(tuple)(filled_tuple))
        file.write(temp) 
        print(temp)
        
## Reading the file content 
def read_template(path):
    '''Reads the template from the provided path.
    -Returns:
     The file content if the path is vaild
                    OR
     Raise an error if the path is not vaild                         
     '''
    try:
        with open (path ,"r")as file:
            return file.read()
    except:
        raise FileNotFoundError    


## saving the words inside '{}' and then replacing them with an empty '{}    
def parse_template(text):
    '''Takes a String (Could be a line or more)
    returns :
    - New text that has filtered to remove the any words between {} in it 
    - The words that we removed from the original text
    '''
    words  = re.findall('{(.*?)}', text)
    textnew = re.sub('{.+?}', '{}', text)  
    return textnew,(tuple)(words)  

## merging the empty template with the user words 
def merge (empty_text,words:tuple):
    '''Takes a template and merges it with the provided tuple of words
    returns:
    - The merged template with the words
    '''
    return empty_text.format(*words)