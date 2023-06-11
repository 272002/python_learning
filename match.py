from difflib import SequenceMatcher

def lcm(str1,str2):
    seqMatch = SequenceMatcher(None,str1,str2)
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))
    
    if (match.size!=0):
        print(str1[match.a : match.a + match.size])
    else:
        print("NO") 

lcm("geekfs","geekofgeeks")
