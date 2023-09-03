def char(string):
    char = string[0]
    string = string.replace(char, '$')
    string = char + string[1:]
    return string

string = 'restart'
print(char(string))