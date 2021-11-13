from element import Element
import random
import string

# input = input("Enter formula: ")

def parse_formula(input):
    #split formula
    formula = input.replace(" ", "").split("∴")
    element_list = [Element(formula[1])]
    
    prems = formula[0]
    conc = formula[1]

    prems = prems.split(".")
    for prem in prems:
        element_list.append(Element(prem))
    
    letter_count = 0
    already_used_letters = []
    for prem in prems:
        #Remove spaces
        prem = prem.replace(" ", "")
        #find single letters
        for c in prem:
            if c.isalpha() == True and c not in already_used_letters:
                new_element = Element(c)
                element_list.append(new_element)
                already_used_letters.append(c)
        #find phrases in ()
        left_indexes = []
        right_indexes = []
        total_indexes = []
        
        for i,c in enumerate(prem):
            if c == "(":
                left_indexes.append(i)
                total_indexes.append(i)
            elif c == ")":
                right_indexes.append(i)
                total_indexes.append(i)
        
        for i in left_indexes:
            count = 0
            total_index = total_indexes.index(i)
            
            for j in range(total_index + 1, len(total_indexes)):
                current_in_total = total_indexes[j]
                if current_in_total in left_indexes:
                    count += 1
                
                elif current_in_total in right_indexes:
                    if count > 0:
                        count -= 1
                    
                    else:
                        new_element = Element(prem[i + 1:current_in_total])
                        element_list.append(new_element)
                        break
    
    
def generate_url_id():
    id = ""
    for i in range(10):
        letters_and_numbers = string.ascii_letters + "1234567890"
        random_character = random.choice(letters_and_numbers)
        id += random_character

    return id


parse_formula("(P -> Q) -> (Q -> R) ∴ Q")




