class Element:
    def __init__(self, text):
        self.text = text
        self.truth_values = []
    
    def append_truth_value(self, value):
        self.truth_values.append(value)
    
    
    