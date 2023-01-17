# Challenge 45


def analyse_string(s):
    res = {}
    
    specials = r"""#$%&'()*+,-./:;<=>?@[]^`{|}~"""
    res['special character'] = sum(s.count(spec) for spec in specials)
    
    words = s.split()
    res['words'] = len(words)
    
    res['total characters'] = sum(len(word) for word in words)
    
    return res


txt = 'Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".'

print(analyse_string(txt))



'''
Challenge #45:

Day 45: Words & Special Characters

Write a function called analysestring that returns the number of special 
characters (#$%&'()*+,-./:;<=>?@[]^`{|}~), words, and, total characters 
(all letters and special characters minus whitespaces) in a string. 
Return everything in a dictionary format:

{“special character”: “number”, “words”: “number”, “total characters”: “number”}

Use the string below as an argument:

“Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".
'''

