import re    
def is_number_regex(s):
    """ Returns True is string is a number. """
    if re.match("^\d+?\.\d+?$", s) is None:
        return s.isdigit()
    return True
    
print(is_number_regex('6'))   
print(is_number_regex('6.1'))  
print(is_number_regex("a"))
    
def url_path_to_dict(path):
    pattern = (r'^'
               r'((?P<schema>.+?)://)?'
               r'((?P<user>.+?)(:(?P<password>.*?))?@)?'
               r'(?P<host>.*?)'
               r'(:(?P<port>\d+?))?'
               r'(?P<path>/.*?)?'
               r'(?P<query>[?].*?)?'
               r'$'
               )
    regex = re.compile(pattern)
    m = regex.match(path)
    d = m.groupdict() if m is not None else None
    return d

for key, value in url_path_to_dict('http://a:b@example.com:890/path/wah@t/foo.js?foo=bar&bingobang=&king=kong@kong.com#foobar/bing/bo@ng?bang').items():
    print(key, '->', value)

def get_address():
    import re
    a = input()
    pattern = r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"
    number_re = re.compile(pattern)
    if number_re.match(a):
        print ("Email of correct:")
        print (a) 
    else:
        print ("Error:")
        print (a)

get_address()
