## 3. Optional arguments ##

def tokenize(text_string, special_characters, clean=False):
    if clean:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
    else:
        story_tokens = text_string.split(" ")
    return(story_tokens)

tokenized_story = []
tokenized_vocabulary = []
misspelled_words = []
tokenized_story = tokenize(story_string, clean_chars,True)
tokenized_vocabulary = tokenize(vocabulary, clean_chars, True)
for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)

## 5. Practice: creating a more compact spell checker ##

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters, clean=False):
    cleaned_text = text_string
    if clean:
        cleaned_text = clean_text(text_string, special_characters)
    tokens = cleaned_text.split(" ")
    return(tokens)
    
def spell_check(vocabulary_file, text_file, special_characters = [",",".","'",";","\n"]):
    misspelled_words = []
    file_v = open(vocabulary_file,'r').read()
    file_t = open(text_file,'r').read()
    tokenized_vocabulary = tokenize(file_v,special_characters, True)
    tokenized_text = tokenize(file_t,special_characters, True)
    for tt in tokenized_text:
        if tt not in tokenized_vocabulary and tt is not '':
            misspelled_words.append(tt)
    return(misspelled_words)
    
final_misspelled_words = []
final_misspelled_words = spell_check("dictionary.txt","story.txt")
print(final_misspelled_words)

## 7. Syntax errors ##

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    text = open(text_file).read()
    
    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)
    
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)

## 9. TypeError and ValueError ##

forty_two = 42
forty_two + "42"

float("guardians")

## 11. Traceback ##

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    # Add ending parentheses.
    text = open(text_file).read()
    
    # Fix indentation.
    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)
    
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)