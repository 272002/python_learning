for i in range(3):
    p = 0
    q = 0
    r = 0
    s = 0
    psd = input("Enter a password ")
     
    if i < 3:
        if len(psd) > 0 and len(psd) < 5:
            
            for j in range(0,len(psd)):
                
                if ord(psd(j)) >= 48 and ord(psd(j)) <= 57:
                    p = int(1)  # numbers
                if ord(psd(j)) >= 65 and ord(psd(j)) <= 90:
                    q = int(1)  # Capital Alphabets
                if ord(psd(j)) >= 97 and ord(psd(j)) <= 122:
                    r = int(1)  # small alphabets
                if ord(psd(j)) >= 33 and ord(psd(j)) <= 47 or ord(psd(j))  == 64 :
                    s = int(1)   # special symbols
    
    if p == 1 and q == 1 and r == 1 and s == 1:
        print('valid password')
    else:
        continue