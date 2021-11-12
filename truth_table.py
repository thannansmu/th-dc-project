from element import Element

input = input("Enter formula: ")

def parse_formula(input):
    element_list = []
    #split formlua
    formula = input.split("∴")
    prems = formlua[0]
    conc = formlua[1]

    prems = prems.split(".")
    
    letter_count = 0
    already_used_letters = []
    for prem in prems:
        #find single letters
        for c in prem:
            if c.isalpha() == True and c not in already_used_letters:
                new_element = Element(c)
                element_list.append(new_element)
                already_used_letters.append(c)
        #find phrases in ()
        #go though each ()
        #get whole phrase
        
        
        
        
        
        
        

    
    
    









