# function to remove the word "dang" and identify its index in the message
def filter_messages(messages):
    
    # list to collect censored messages
    messages_censored = []
    
    # list to collect count of censored word per message
    occurences = []
    
    # word to censor
    censor = "dang"
    
    # message by message
    for i in range(len(messages)):

        # extract the current message into a sentence
        sentence = messages[i]
        
        # split the sentence into single words
        words = sentence.split()
            
        # variable to track count of censor per message
        count = 0
        
        # list with words without censored word
        words_censored = []

        # go word by word
        for j in range(len(words)):
            
            # save current word
            word = words[j]
            

            # check current word for censor
            if word == censor:
                # increase cout by 1 
                count += 1
            else:
                # add word to words
                words_censored.append(word)
        
        # add count of current sentence to occurences
        occurences.append(count)
        
        # join words into sentence
        sentence_censored = " ".join(words_censored)
        
        # add censored messages to messages censored
        messages_censored.append(sentence_censored)

    return messages_censored, occurences    
        

    #print(occurences)

    #print(messages_censored)





def main():
    messages = ["dang it", "let's keep on moving"]
    filter_messages(messages)

main()
