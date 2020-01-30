import json
cipher = "em fmzwfqvsycqkstg"

#finds likely keys for a Caesar cipher
def getProb(char,cipher):

    #remove spaces and make lower case
    cipher = cipher.replace(" ", "").lower()
    cipher = cipher.replace(",","")
    cipher = cipher.replace(".","")
    cipher = cipher.replace("!","")
    cipher = cipher.replace("?","")
    cipher = cipher.replace(":","")

    #array of character frequencies
    char_freq_array = [0.080, 0.015,0.030,0.040, 0.130,0.020,0.015,0.060,0.065,0.005,0.005,0.035,0.030,0.070,0.080,0.020,0.002,0.065,0.060,0.090,0.030,0.010,0.015,0.005,0.020,0.002]

    probability = 0

    #convert chars to ints
    a_int = 97
    char = char - 97
    
    for index in range(0,26):

        #gets correct letter probability
        array_index = (index-char)%26       

        #does formula for cracking caesar
        prob_of_char = char_freq_array[array_index]
        freq_in_text= cipher.count(chr(index+a_int))/len(cipher)
        probability += freq_in_text*prob_of_char
        
    return probability

#adds key and probability to dictionary.
prob_dict = {}
total_prob = 0
for i in range(97,123):
    prob= getProb(i, cipher)
    prob_dict[prob] = i -97
    total_prob+=prob

print(json.dumps(prob_dict, sort_keys=True))
print(total_prob)








