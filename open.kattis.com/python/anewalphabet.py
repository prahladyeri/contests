symbols = ["@", "8", '(', '|)', '3', '#', '6', '[-]', '|', '_|', '|<', '1', '[]\/[]']
symbols += ['[]\[]', '0', '|D', '(,)', '|Z', '$', "']['", '|_|', '\/', '\/\/', '}{', '`/', '2']


ss = input()
ss = ss.lower()
out = ""
for c in ss:
    o = ord(c)
    if o>=97 and o<=122:
        out += symbols[o-97]
    else:
        out += c
        
print(out)