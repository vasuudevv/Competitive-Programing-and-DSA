n = N
        m = len(trust)2

        d= [0]n
        v= [0]m

        for a,b in trust
            v.append(a)
            d[b-1]+=1
            
        ma=max(d)
        maxi=d.index(ma)+1
        if maxi not in v
            return maxi
        else
            return -1