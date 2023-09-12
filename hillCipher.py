
#the hill cipher part..enciphering here 2*2 matrix here......sorry only 4 words allowed here

def hill_cipher_encrypt(pt,key):

    pt_array=list(pt)
    res=""


    pt_matrix=[[0 for i in range(2)] for i in range(2)]

    k=0
    for i in range(2):
        for j in range(2):
            pt_matrix[i][j]=ord(pt_array[k])-97
            k+=1
  
    #now the plain text matrix is ready
    #now the multiplication part

    result=[[0 for i in range(2)] for i in range(2)]

    for i in range(2):
        for j in range(2):
            result[i][j]=0
            for k in range(2):
                result[i][j]+=(pt_matrix[i][k]*key[k][j])

    # matrix mul is successfull
    
    for i in range(2):
        for j in range(2):
            result[i][j]=result[i][j]%26+97

    for i in range(2):
        for j in range(2):
            res=res+chr(result[i][j])

    return res


################################################################################
#mod of the key matrix should be realtively prime to 26
def invert(det):
    i=1
    neg=False
    
    if(det<0):
        det=det*(-1)
        neg=True

        
    res=0
    run=True
    
    while(run):
        if(((det*i)-1)%26==0):
            res=i
            run=False
        i+=1

    if(neg==True):
        res=res*(-1)
        
    return res
        
        
def  hill_cipher_decrypt(ct,key):
    
    ct_matrix=[[0 for i in range(2)] for i in range(2)]
    ct_array=list(ct)

    k=0
    for i in range(2):
        for j in range(2):
            ct_matrix[i][j]=ord(ct_array[k])-97
            k+=1

   # good
    

    det=(key[0][0]*key[1][1])-(key[0][1]*key[1][0])
    

    inverse=invert(det)

    #print(inverse) good


    adj=[[key[1][1],-key[0][1]],[-key[1][0],key[0][0]]] #transpose is also done

    

    for i in range(2):
        for j in range(2):
             adj[i][j]=adj[i][j]*(inverse)

    #now the multiplication part
    result=[[0 for i in range(2)] for i in range(2)]
         
    for i in range(2):
        for j in range(2):
            result[i][j]=0
            for k in range(2):
                result[i][j]+=(ct_matrix[i][k]*adj[k][j])

            
    for i in range(2):
        for j in range(2):
            result[i][j]=result[i][j]%26+97
    res=""
         
    for i in range(2):
        for j in range(2):
            res=res+chr(result[i][j])

    return res
##################################################################
def hill_attack(ct_array,pt_array):

    print(ct_array)
    print(pt_array)
    
    det=(pt_array[0][0]*pt_array[1][1])-(pt_array[0][1]*pt_array[1][0])
    print(det)

    
    det_inv=invert(det)
    print(det_inv)

    adj=[[pt_array[1][1],-pt_array[0][1]],[-pt_array[1][0],pt_array[0][0]]] #transpose is also done

    print(adj)

    for i in range(2):
        for j in range(2):
             adj[i][j]=adj[i][j]*(det_inv)

    print(adj)

    
    result=[[0,0],[0,0]]
         
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j]+=(adj[i][k]*ct_array[k][j])

    print(result)

            
    for i in range(2):
        for j in range(2):
            result[i][j]=result[i][j]%26

    print(result)

########################################################################
    

if __name__=="__main__":

    pt=str(input("enter the plain text   "))

    key=[[0 for i in range(2)] for i in range(2)]
    array_2=[]
    
    print("now enter the key matrix(2*2) remember its det should be relatively prime to 26")
    for i in range(2):
           for j in range(2):
               key[i][j]=int(input("enter "+str(i)+str(j)+" "))

# code for any size input................
    if((len(pt))%4!=0):
        for i in range(4-(len(pt)%4)):
            pt=pt+"x"

    iterations=len(pt)//4

    array=[]
    j=0
    k=4
    for i in range(iterations):
        array.append(pt[j:k])
        j=k
        k=k+4
########################################################
    for l in range(len(array)):
        result=hill_cipher_encrypt(array[l],key)
        array[l]=result
        
    final=""
    for i in array:
        final=final+i

    print("the encrypted text is" ,
          final)
#########################################################
    j=0
    k=4
    for i in range(iterations):
        array_2.append(final[j:k])
        j=k
        k=k+4

    final_2=""   
    l=0
    for l in range(len(array_2)):
        result=hill_cipher_decrypt(array_2[l],key)
        array_2[l]=result

    for i in array_2:
        final_2=final_2+i

    print("the decrypted text is ",
          final_2)
################################################################# now for the decryption part
    
    #final is the encrypted text...the following fn will print the key

    option=str(input("do u want to attack the hill cipher(2*2)(y/n)"))
    if(option=='y'):
            #the first four words are enough
            ct_array=[]
            pt_array=[]
            
            j=0
            for i in range(2):
                pt_sub=[]
                ct_sub=[]
                pt_sub.append(ord(pt[j])-97)
                pt_sub.append(ord(pt[j+1])-97)
                ct_sub.append(ord(final[j])-97)
                ct_sub.append(ord(final[j+1])-97)
                pt_array.append(pt_sub)
                ct_array.append(ct_sub)
                j+=2
                

            hill_attack(ct_array,pt_array)
                


    

    
