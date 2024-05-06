def generator_numbers(text: str):

    # pattern = r'\d{*}\.\d{*}'
    
    # i = re.findall(pattern, text)   
    
    i = [ 1.00, 2.5, 3.3, 0.1]

    print(i)

    for n in i:
        yield n #float(n)

        