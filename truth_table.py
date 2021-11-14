from element import Element
import random
import string

# input = input("Enter formula: ")

def parse_formula(input):
    #split formula
    formula = input.replace(" ", "").split("∴")
    element_list = []
    
    if len(formula) > 1:
        prems = formula[0]
        conc = formula[1]
    else:
        prems = formula
        conc = ""

    print(prems)
    prems = prems[0].split(".")
    
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
    
    #Add prems and conclusion to element list
    for prem in prems:
        element_list.append(Element(prem))
    
    element_list.append(Element(conc))
    
    return element_list, letter_count


def create_columns(element_list, letter_count):
    row_amount = 2 ** letter_count
    amount_true_false = row_amount
    for e, element in enumerate(element_list):
        flag = True
        if (len(element.text) == 1):
            for i in range(row_amount):
                if i < amount_true_false % (amount_true_false / 2) == 0:
                    if flag == True:
                        flag = False
                    else:
                        flag = True
                
                element.append_truth_value(flag)
            
            amount_true_false /= 2
            
        else:
            for i in range(e, len(element_list) + 1):       #Figure this out
                element.text = element.text.replace(element_list[-i].text, str(i - 1))
            
            #Split by symbol                /\  \/  ->  <-> ~
            symbol = ""
            if "/\\" in element.text:
                element.text = element.text.split("/\\")
                symbol = "/\\"
            elif "\/" in element.text:
                element.text = element.text.split("\/")
                symbol = "\/"
            elif "<->" in element.text:
                element.text = element.text.split("<->")
                symbol = "<->"
            elif "->" in element.text:
                element.text = element.text.split("->")
                symbol = "->"
            
            element1 = element_list[int(element.text[0])]
            element2 = element_list[int(element.text[1])]
            for i in range(row_amount):
                if symbol == "/\\":
                    for j in range(len(element1.truth_values)):
                        if element1.truth_values[j] == True and element2.truth_values[j] == True:
                            element.truth_values.append(True)
                        else:
                            element.truth_values.append(False)
                    
                elif symbol == "\/":
                    for j in range(len(element1.truth_values)):
                        if element1.truth_values[j] == True or element2.truth_values[j] == True:
                            element.truth_values.append(True)
                        else:
                            element.truth_values.append(False)
                        
                elif symbol == "<->":
                    for j in range(len(element1.truth_values)):
                        if element1.truth_values[j] == element2.truth_values[j]:
                            element.truth_values.append(True)
                        else:
                            element.truth_values.append(False)
                            
                elif symbol == "->":
                    for j in range(len(element1.truth_values)):
                        if element1.truth_values[j] == True and element2.truth_values[j] == True:
                            element.truth_values.append(True)
                        elif element1.truth_values[j] == False and element2.truth_values[j] == True:
                            element.truth_values.append(True)
                        elif element1.truth_values[j] == False and element2.truth_values[j] == False:
                            element.truth_values.append(True)
                        else:
                            element.truth_values.append(False)
                
                
            
            
                
                
    
        
def assign_truth_values(input):
    element_list, letter_count = parse_formula(input)      
    create_columns(element_list, letter_count)
    
    
def generate_url_id():
    id = ""
    for i in range(10):
        letters_and_numbers = string.ascii_letters + "1234567890"
        random_character = random.choice(letters_and_numbers)
        id += random_character

    return id


assign_truth_values("(P -> Q) \/ (R -> S)")







