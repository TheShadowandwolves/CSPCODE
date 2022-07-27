import csp


while True:
    text = input('=> ')
    result, error = csp.run('<stdin>',text)
    
    if error:
        print(error.as_string())
    else:
        print(result)
         
