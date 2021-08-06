# Rabin-Karp Algortihm for pattern searching

def search(text, pattern, q,base):
    lp=len(pattern)
    lt=len(text)
    p=0
    t=0
    h=1
    
    for i in range(lp-1):
        h=(h*base)%q
        
    # calculating hash value of pattern
    # and first window of text
    for i in range(lp):
        p=(base*p+ord(pattern[i]))%q
        t=(base*t+ord(pattern[i]))%q
    
    for i in range(0, lt-lp+1):
        # if hash of window of text and hash of pattern
        # match, then check each character
        if p==t:
            for j in range(lp):
                if text[i+j]!=pattern[j]:
                    break
                else:
                    j+=1
            if j==lp:
                print("Pattern found at index "+ str(i))
        # calculate hash for the next window
        if i<lt-lp:
            t=((base*(t-ord(text[i])*h))+ ord(text[i+lp]))%q
            # modular arithmetic
            if t<0:
                t=t+q
        
    
text=input()
pattern=input()
q=101 # prime number
# no of characters in the input alphabet
base=256
search(text, pattern, q, base)

'''
Time Complexity: It takes O(m) preprocessing time, 
and its matching time is O((n-m+1)*m) in the worst case,
where m is the size of the pattern and
n is the size of the text.
In average case, we expect few valid shifts—perhaps some 
constant c of them. In this case, the expected matching time
of the algorithm is O((n-m+1)+ cm), plus the time required 
to process spurious hits.
'''
