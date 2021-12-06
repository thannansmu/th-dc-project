#element class
class Element:
    #init function
    def __init__(self, text):
        self.text = text
        self.truth_values = []
    
    #appends truth value to element
    def append_truth_value(self, value):
        self.truth_values.append(value)
    