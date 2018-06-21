def troca(s,velho,novo):
    s = list(s)
    x = 0
    y = 0
    a = False 
    if not a:
        while (x < len(s)):
            while (y <= len(s)):
                if s[x:y] == list(velho):
                    s[x:y] = novo
                y += 1
            y = 0
            x+= 1
        Done = True
    s = ''.join(s) 
    return print("Frase:",s)
