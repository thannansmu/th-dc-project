from element import Element
from html_templates import main_template
import random
import string

#splits formula into premises and conclusion and creates element objects
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

    if (len(prems) > 1):
        prems = prems.split(".")
    
    #add conclusion to premise list so that it can also be parsed
    if (len(conc) > 1):
        prems.append(conc)
    
    letter_count = 0
    already_used_letters = []
    already_negative = []
    
    symbol_list = ["->", "<->", "/\\", "\/"] 
    
    for p, prem in enumerate(prems):
        #Remove spaces
        prem = prem.replace(" ", "")
        #find single letters
        for i, c in enumerate(prem):
            if i == 0 and prem[i] == "~" and prem[1].isalpha() and prem[1] not in already_used_letters:
                element_list.append(Element(prem[1]))
                already_used_letters.append(prem[1])
                letter_count += 1
            
            elif i > 0 and prem[i - 1] == "~" and c.isalpha() and prem[i - 1] + c not in already_negative:
                if (c not in already_used_letters):
                    element_list.append(Element(c))
                    already_used_letters.append(c)
                    letter_count += 1
                
                new_element2 = Element(prem[i - 1] + c)
                element_list.append(new_element2)
                already_negative.append(prem[i - 1] + c)
            
            elif c.isalpha() == True and c not in already_used_letters:
                new_element = Element(c)
                element_list.append(new_element)
                already_used_letters.append(c)
                letter_count += 1
    
        #find phrases in ()
        left_indexes = []
        right_indexes = []
        total_indexes = []
        
        for i,c in enumerate(prem):
            if i == 0 and c == "~" and prem[1] == "(" and prem not in already_negative:
                print("here")
                if ")" in prem:
                    tempElement = Element(prem[:prem.index(")") + 1])
                    element_list.append(tempElement)
                else:
                    tempElement = Element(prem)
                    element_list.append(tempElement)
                already_negative.append(prem)
            
            elif i > 1 and c == "~" and prem[i + 1] == "(" and prem[i:prem.index(")")] not in already_negative:
                if ")" in prem:
                    tempElement = Element(prem[i:prem.index(")") + 1])
                    element_list.append(tempElement)
                else:
                    tempElement = Element(prem)
                    element_list.append(tempElement)
                already_negative.append(prem[i:prem.index(")") + 1])
               
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
        
    for prem in prems:  
        flag = False              
        for el in element_list:
            if prem == el.text:
                flag = True
        
        if (flag == False):
            element_list.append(Element(prem))

    return element_list, letter_count

#creates the columns of the truth table and assigns truth values
def create_columns(element_list, letter_count):
    already_used_elements = []
    row_amount = 2 ** letter_count
    amount_true_false = row_amount
    
    for e, element in enumerate(element_list):
        #check if element already has assigned truth values
        flag = True
        if (len(element.text) == 1):
            count = amount_true_false / 2
            for i in range(row_amount):
                if count == 0:
                    if flag == True:
                        flag = False
                    else:
                        flag = True
                    count += amount_true_false / 2
                
                element.append_truth_value(flag)
                count -= 1
            
            amount_true_false /= 2
            
        else:
            new_element_text = element.text
            if (len(new_element_text) > 0):
                for i in reversed(range(e)):
                    new_element_text = new_element_text.replace(element_list[i].text, str(i))
            
                #Split by symbol
                symbol = ""
                if "~" in new_element_text:
                    new_element_text = [new_element_text[0], new_element_text[1:]]
                if "/\\" in new_element_text:
                    new_element_text = new_element_text.split("/\\")
                    symbol = "/\\"
                elif "\/" in new_element_text:
                    new_element_text = new_element_text.split("\/")
                    symbol = "\/"
                elif "<->" in new_element_text:
                    new_element_text = new_element_text.split("<->")
                    symbol = "<->"
                elif "->" in new_element_text:
                    new_element_text = new_element_text.split("->")
                    symbol = "->"
                
                # print(new_element_text)
                new_element_text[0] = new_element_text[0].replace("(", "").replace(")", "")
                new_element_text[1] = new_element_text[1].replace("(", "").replace(")", "")
                
                if (new_element_text[0] == "~"):
                    element1 = "~"
                else:
                    element1 = element_list[int(new_element_text[0])]
                    
                element2 = element_list[int(new_element_text[1])]
                for i in range(row_amount):
                    if element1 == "~":
                        for j in range(row_amount):
                            if element2.truth_values[j] == True:
                                element.truth_values.append(False)
                            else:
                                element.truth_values.append(True)
                    
                    if symbol == "/\\":
                        for j in range(row_amount):
                            if element1.truth_values[j] == True and element2.truth_values[j] == True:
                                element.truth_values.append(True)
                            else:
                                element.truth_values.append(False)
                
                    elif symbol == "\/":
                        for j in range(row_amount):
                            if element1.truth_values[j] == True or element2.truth_values[j] == True:
                                element.truth_values.append(True)
                            else:
                                element.truth_values.append(False)
                
                    elif symbol == "<->":
                        for j in range(row_amount):
                            if element1.truth_values[j] == element2.truth_values[j]:
                                element.truth_values.append(True)
                            else:
                                element.truth_values.append(False)
                
                    elif symbol == "->":
                        for j in range(row_amount):
                            if element1.truth_values[j] == True and element2.truth_values[j] == True:
                                element.truth_values.append(True)
                            elif element1.truth_values[j] == False and element2.truth_values[j] == True:
                                element.truth_values.append(True)
                            elif element1.truth_values[j] == False and element2.truth_values[j] == False:
                                element.truth_values.append(True)
                            else:
                                element.truth_values.append(False)
        already_used_elements.append(element)
        
        
    return element_list

#main function that calls the other ones
def assign_truth_values(input):
    element_list, letter_count = parse_formula(input)    
    #sort elements so they can be displyed in order of length in the table
    element_list.sort(key=lambda x: len(x.text))
    element_list = create_columns(element_list, letter_count)
    write_html(element_list)    

#generates id for truth table url (mainly for website version)
def generate_url_id():
    id = ""
    for i in range(10):
        letters_and_numbers = string.ascii_letters + "1234567890"
        random_character = random.choice(letters_and_numbers)
        id += random_character

    return id

#writes truth table to html file
def write_html(element_list):
    text = "<tr>"
    for element in element_list:
        text += "<td>{0}</td>".format(element.text)
    text += "</tr>\n"
    for i in range(len(element_list[0].truth_values)):
        text += "<tr>"
        for j in range(len(element_list)):
            text += "<td>{0}</td>".format(element_list[j].truth_values[i])
        text += "</tr>\n"
    
    temp = main_template.format(text)
    with open("Templates/table.html", "w") as f:
        f.write(temp)
    