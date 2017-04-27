function problem7(nNum)
bLoop = 1;
k = 3;
index = 2;

if(nNum == 1)
    k = 2;
    index = 1;
    fprintf('%6.f is the %6.fnd Prime Number\n', k, index)
    bLoop = 0;
end

while(bLoop == 1)
    k = k+2;
    bPrime = 1;
    
    for j=2:k/2
        if(mod(k, j) == 0)
            bPrime = 0;
        end
    end
    
    if(bPrime == 1)
        index = index + 1;
        fprintf('%6.f is the %6.fnd Prime Number\n', k, index)
    end
    
    if(nNum == index)
        bLoop = 0;
    end
end