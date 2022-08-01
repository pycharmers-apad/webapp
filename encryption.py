import json

class encryption(object):
    def __init__(self,username,password):
        self.uname_en,self.u_undrfl,self.u_ovrfl=self.customEncrypt(username,3,1)
        self.password_en,self.p_undrfl,self.p_ovrfl=self.customEncrypt(password,3,1)

    def customEncrypt(self,usr_str,N=3,D=1,*args):   ##Task 1
        rev_usr_str=usr_str[::-1]
        encrypt_lst=[]
        ovr_flow_lst=[]  ##Incase the value goes above 126 (ASCII limit)
        undr_flow_lst=[]  ##Incase the value goes below 34 (Ignoring ASCII value of '!' and ' ')
        
        try:
            overflow_encrypt=args[1][::-1]    ###Optional argument to see if overflow has happened
            underflow_encrypt=args[0][::-1]   ###Optional argument to see if underflow has happened
        except:
            pass

        for i in range(0,len(rev_usr_str)):
            ascii_val_org=ord(rev_usr_str[i])
            ovr_flow_flag=0
            undr_flow_flag=0
            ascii_val=ascii_val_org+(D*N)
            
            if(ascii_val>126):
                ovr_flow_flag=1                ###Flag to indicate overflow, i.e. greater than 126
                ascii_val=ascii_val%126+34     ### If the ascii value is greater than 126, it will not encrypt it. So we force it to fall within our ASCII range of 34 & 126
            
            elif(ascii_val<34):
                undr_flow_flag=1                ###Flag to indicate undeflow, i.e lesser than 34
                ascii_val=ascii_val+34         ### If the ascii value is lesser than 34, it won't encrypt it. So we force it to fall within our ASCII range of 34 & 126
                    
            try:                                    ####Checks to see if an overflow, underflow flag is given to the character within the string
                if overflow_encrypt[i]==1 or underflow_encrypt[i]==1:
                    ascii_val=self.overflow_underflow_encrypt(ord(rev_usr_str[i]),N,D,overflow_encrypt[i],underflow_encrypt[i])
            except:
                pass

            encrypt_lst.append(ascii_val)
            undr_flow_lst.append(undr_flow_flag)
            ovr_flow_lst.append(ovr_flow_flag)
            
            encrypt_val=''.join(chr(i) for i in encrypt_lst)
        return encrypt_val,undr_flow_lst,ovr_flow_lst
    
    def customDecrypt(self):
        self.uname_de,self.u_undrfl_de,self.u_ovrfl_de=self.customEncrypt(self.uname_en,3,-1,self.u_undrfl,self.u_ovrfl)
        self.password_de,self.p_undrfl_de,self.p_ovrfl_de=self.customEncrypt(self.password_en,3,-1,self.p_undrfl,self.p_ovrfl)
        return {'username':self.uname_de,'password':self.password_de}


    def overflow_underflow_encrypt(string,N,D,overflow_encrypt,underflow_encrypt):  ##Exception when the ranges fall out of our ASCII range (34-126)
        if overflow_encrypt==1:
            return string+(D*N)-34+126
        elif underflow_encrypt==1:
            return string+(D*N)-34
    
    def get_encrypted_creds(self):
        return self.uname_en,self.password_en