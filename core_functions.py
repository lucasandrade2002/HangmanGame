
def getWords():
    
    with open(r"C:\workspace\palavras_jogoForca.txt", mode="r", encoding="utf-8") as file:
        
        words_updated = []
        words = file.readlines()
        
        for w in words:
            words_updated.append(w.strip(" \n"))
            
    file.close()
    return words_updated

def getAttemptUser(word_chosen, letter):
      
        hasChar = False
        
        for el in word_chosen:
            
            if str.lower(el) == str.lower(letter):
                hasChar = True
             
        return hasChar