def bank_foiz(S,p):
    k = 0
    result = 0
    while result < 2*S:
       k = k+0.00001
       result = S*(((p+100)/100)**k)
    d=dict()
    d['oy']=k
    d['pul']=result
    return d
    #print("O'tgan oy: "+str(k)+"  Bankdagi pul miqdori: "+str(result))