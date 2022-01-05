for testCase in range(int(input())):
    c,d=map(int, input().split())
    l=list(map(str, input().split()))
    ctotal,dtotal=0,0
    l=[10 if (x=='10')or(x=='J')or(x=='Q')or(x=='K') else x for x in l]
    a,b=l[0],l[1]
    if a=='A' and ((c==10) or (c==20)):
        ctotal = 21
    if a != 'A':
        ctotal=c + int(a)
        
    if b=='A' and ((d==10) or (d==20)):
        dtotal = 21
    elif b != 'A':
        dtotal=d + int(b)
    
    if ctotal == 21 and dtotal != 21:
        print('Win')
    elif ctotal == dtotal:
        print('Tie')
    elif ctotal !=21 and dtotal == 21:
        print('Lose')
