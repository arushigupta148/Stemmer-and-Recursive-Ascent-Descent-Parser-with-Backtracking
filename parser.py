Aux=['can','may','will','do']
Det=['a','an','the','that','these','those']
Adj=['large','small']
Pronoun=['he','she','they','you']
ProperNoun=['mary','john','denver','houston','boston','beijing']
Noun=['book','flight','can','water','boy','box','floor','flight','apple','banana','computer','work','home']
Verb=['do','work','book','hold','spend','open','call','have','eat']
Prep=['in','on','at','from','to','near']
Conj=['and','or','but']
VBD=['is','are','am']
CD=['1','2','3','4','5','6','7','8','9','10','11','12']
RB=['am','pm']
array=['a','an','the','that','these','those','large','small','he','she','they','you','mary','john','denver','houston','boston','beijing','book','flight','can','water','boy','box','floor','flight','apple','banana','computer','work','home','do','work','book','hold','spend','open','call','have','eat','in','on','at','from','to','near','and','or','but','is','are','am','1','2','3','4','5','6','7','8','9','10','11','12','am','pm']

import sys

def stemmer(input2):
    token=[]
    
    newinput=[]
    lines=[]
    line=1
    for text in input2:
        if "\n" in text:
            temp=text.split("\n")
            newinput.append(temp[0])
            lines.append(line)
            line+=1
            lines.append(line)
            newinput.append(temp[1])
        elif "." in text:
            temp=text.split(".")
            if temp[0].isalpha():
                newinput.append(temp[0])
                lines.append(line)
                newinput.append(".")
                lines.append(line)
            else:
                newinput.append(text)
                lines.append(line)
        else:
            newinput.append(text)
            lines.append(line)
    
    for t in newinput:        
        t=t.lower()        
        while len(t)>0:
            if t in array:
                token.append(t)
                break
            elif t==".":
                token.append(t)
                break
            else:
                t=t[:-1]

    types=[]
    for tok in token:
        if tok.isdigit():
            if "." in newinput[token.index(tok)]:
                types.append("DOUBLE")
            else:
                types.append("INT")
        elif tok.isalpha():
            types.append("STRING")
        else:
            types.append("OP")
    types.append("ENDFILE")
    
    #print newinput
    #print types
    #print lines
    #print token
    return token[:-1]
        
def leveler(x):
    global level
    op = ""
    for i in range(level):
        op += "| "
    print op+x

def parser(input1):
    global count
    count=0
    t=input1[count]
    stack=[]
    
    
    #BOTTOM UP PARSER
    def Q0(t): #S   
          global level
          level = 0
          leveler("S")
          temp = R0(t)
          temp1=""
          if temp == "":
              temp1=R1(t)
              if temp1=="":
                  temp2 = R2(t)
                  if temp2=="":
                      temp3=R3(t)
                  
          if temp!="":
              global count
              if count==(len(input1)-1):
                  return t
              count+=1
              t=input1[count]
              if temp1!="":
                  return t
              return t
          elif temp2!="":
              return t
          elif temp3!="":
              return t
          else:
              return ""
        
    def Q1(t): #NP
          global level
          prev = level
          level += 1
          leveler("NP")
          temp = R4(t)
          if temp == "":
              temp2 = R5(t)
              if temp2=="":
                  temp3=R6(t)
                  if temp3=="":
                      temp4=R7(t)
                      if temp4=="":
                          temp5=R8(t)
                          if temp5=="":
                                  temp7=R11(t)
                                  if temp7=="":
                                      temp8=R12(t)
          if temp!="":
              if t in Prep:
                  temp6=R10(t)
                  if temp6!="":
                      return t
              return t
          elif temp2!="":
              if t in Prep:
                  temp6=R10(t)
                  if temp6!="":
                      return t
              return t
          elif temp3!="":
              if t in Prep:
                  temp6=R10(t)
                  if temp6!="":
                      return t
              return t
          elif temp4!="":
              if t in Prep:
                  temp6=R10(t)
                  if temp6!="":
                      return t
              return t
          elif temp5!="":
              if t in Prep:
                  temp6=R10(t)
                  if temp6!="":
                      return t
              return t
          elif temp7!="": 
              if t in Prep:
                  temp6=R10(t)
                  if temp6!="":
                      return t
              return t
          elif temp8!="": 
              if t in Prep:
                  temp6=R10(t)
                  if temp6!="":
                      return t
              return t
          else:
              return ""
          
    
    def Q2(t): #VP
          global level
          global count
          level += 1
          prev=level
          leveler("VP")
          temp4=""
          temp2=""
          temp=R18(t)
          if temp == "":
                  temp3=R23(t)
                  if temp3=="":
                          temp5=R25(t)
                          if temp5=="":
                              temp4=R24(t)    
          if temp!="": #Verb
                if count==(len(input1)-1):
                  return t
                count+=1
                t=input1[count]            
                lis=['a','an','the','that','these','those','large','small','he','she','they','you','mary','john','denver','houston','boston','beijing','book','flight','can','water','boy','box','floor','flight','apple','banana','computer','work','home','1','2','3','4','5','6','7','8','9','10','11','12']
                if t in lis:
                    level=prev
                    prev=level
                    temp=R19(t) #NP
                    if temp!="": #NP
                         if count==(len(input1)-1):
                             return t
                         count+=1
                         t=input1[count]
                         if t in Prep:
                             level=prev
                             temp2 = R20(t)
                             if temp2!="": #PP
                                 return t            
                elif t in Prep: #PP
                    level=prev
                    temp2 = R20(t)
                    if temp2 != "":
                     return t
                elif temp4!="":
                    return t
                return t
          elif temp3!="":
                if temp4!="":
                    return t
                return t
          elif temp5!="":
                if temp4!="":
                    return t
                return t
          else:
              return ""
    
    def Q3(t): #Nominal
          global level
          level += 1
          leveler("Nominal")
          temp1=R15(t)
          if temp1=="":
              temp2=R16(t)
              if temp1=="":
                  temp3=R17(t)
                  
          if temp1!="":
               return t
          elif temp!="":
               return t
          elif temp3!="": 
               return t
          else:
               return ""
               
    def Q4(t): #PP
          global level
          level += 1
          leveler("PP")
          temp = R13(t)
          if temp!="": #Prep NP
              global count
              if count==(len(input1)-1):
                  return t
              count+=1
              t=input1[count]
              temp2=R14(t)
              if temp2!="": #PP
                  return t
              return t
          else:
              return ""
    
    def Q5(t): #Det
          if t in Det:
               global level
               level += 1
               leveler("Det")
               level += 1
               leveler(t)
               return t
          return ""
    
    def Q6(t): #Adj
          if t in Adj:
               global level
               level += 1
               leveler("Adj")
               level += 1
               leveler(t)
               return t
          return ""
    
    def Q7(t): #ProperNoun
          if t in ProperNoun:
               global level
               level += 1
               leveler("ProperNoun")
               level += 1
               leveler(t)
               return t
          return ""
    
    def Q8(t): #Aux
          if t in Aux:
               global level
               level += 1
               leveler("Aux")              
               level += 1
               leveler(t)
               return t
          return ""
    
    def Q9(t): #Noun
          if t in Noun:
               global level
               level += 1
               leveler("Noun")
               level += 1
               leveler(t)
               return t
          return ""
    
    def Q10(t): #Pronoun
           if t in Pronoun:
               global level
               level += 1
               leveler("Pronoun")
               level += 1
               leveler (t)
               return t
           return ""
    
    def Q11(t): #Verb
           if t in Verb:
               global level
               level += 1
               leveler("Verb")
               level += 1
               leveler(t)
               return t
           return ""
    
    def Q12(t): #Prep
           if t in Prep:
               global level
               level += 1
               leveler("Prep")
               level += 1
               leveler(t)
               return t
           return ""
    
    def Q13(t): #Conj
           if t in Conj:
               global level
               level += 1
               leveler("Conj")
               level += 1
               leveler(t)
               return t
           return ""
    
    def Q14(t): #VBD
           if t in VBD:
               global level
               level += 1
               leveler("VBD")
               level += 1
               leveler(t)
               return t
           return ""
    
    def Q15(t): #CD
           if t in CD:
               global level
               level += 1
               leveler("CD")
               level += 1
               leveler(t)
               return t
           return ""
    
    def Q16(t): #RB
           if t in RB:
               global level
               level += 1
               leveler("NP")
               level += 1
               leveler(t)
               return t
           return ""
           
           
           
           
    #TOP TO DOWN PARSER
    def R0(t): #S - NP VP
          global level
          level = 0
          temp=Q1(t)
          if temp!="":
              global count
              if count==(len(input1)-1):
                  return t
              count+=1
              t=input1[count]
              level = 0
              temp2=Q2(t)
              if temp2!="":
                  return t
          return ""
           
    def R1(t): #S - NP VP PP
          global level
          level = 0
          temp=Q4(t)
          if temp!="":
              return t
          return ""

    def R2(t): #S - AUX NP VP
          global level
          level = 0
          temp=Q8(t)
          if temp!="":
              global count
              if count==(len(input1)-1):
                  return t
              count+=1
              t=input1[count]
              temp2=Q1(t)
              level=0
              if temp!="":
                  if count==(len(input1)-1):
                      return t
                  count+=1
                  t=input1[count]
                  temp3=Q2(t)
                  level=0
                  if temp3!="":
                      return t
          return ""
    
    def R3(t): #S - VP
          global level
          level=0
          temp=Q2(t)
          if temp!="":
              return t
          return ""
    
    def R4(t): #NP - PRONOUN
          global level
          temp=Q10(t)
          if temp!="":
              return t
          return ""
    
    def R5(t): #NP - PROPER-NOUN
          global level
          temp=Q7(t)
          if temp!="":
              return t
          return ""
      
    def R6(t): #NP - DET NOMINAL
          global level
          prev = level
          temp = Q5(t)
          if temp != "":
              global count
              if count==(len(input1)-1):
                  return t
              count+=1
              t=input1[count]
              level = prev
              temp = Q3(t)
              if temp != "":
                  return t
          return ""
    
    def R7(t): #NP - DET ADJ NOUN
          global level
          prev=level
          temp=Q5(t)
          if temp!="":
              global count
              if count==(len(input1)-1):
                  return t
              count+=1
              t=input1[count]
              level = prev
              temp = Q6(t)
              if temp != "":
                  if count==(len(input1)-1):
                      return t
                  count+=1
                  t=input1[count]
                  level = prev
                  temp = Q9(t)
                  if temp != "":
                      return t
          return ""
    
    def R8(t): #NP - ADJ NOUN
          global level
          prev=level
          temp=Q6(t)
          if temp!="":
                  global count
                  if count==(len(input1)-1):
                      return t
                  count+=1
                  t=input1[count]
                  level = prev
                  temp = Q9(t)
                  if temp != "":
                      return t
          return ""
    
    def R10(t): #NP - PP
          global level
          prev=level
          temp=Q4(t)
          if temp!="":
              return t
          return ""
    
    def R11(t): #NP - NOUN
          global level
          temp=Q9(t)
          if temp!="":
               return t
          return ""
    
    def R12(t): #NP - CD RB
          global level
          prev=level
          temp=Q15(t)
          if temp!="":
               global count
               if count==(len(input1)-1):
                  return t
               count+=1
               t=input1[count]
               level = prev
               temp = Q16(t)
               if temp != "":
                   return t
          return ""
    
    def R13(t): #PP - PREP NP 
           global level
           prev=level
           temp = Q12(t)
           if temp!="": #Prep
              global count
              if count==(len(input1)-1):
                  return t
              count+=1
              t=input1[count]
              level=prev
              temp2=Q1(t)
              if temp2!="": #NP
                   return t
           return ""
    
    def R14(t): #PP - PREP NP PP
           global level
           prev=level
           temp = Q4(t)
           if temp!="": #PP
                return t
           return ""
    
    def R15(t): #NOMINAL - NOUN
           global level
           prev=level
           temp = Q9(t)
           if temp!="":
               return t
           return ""
    
    def R16(t): #NOMINAL - NOMINAL NOUN
           global level
           prev=level
           temp = Q3(t)
           if temp!="":
               global count
               if count==(len(input1)-1):
                  return t
               count+=1
               t=input1[count]
               level=prev
               temp=Q9(t)
               if temp!="": #Noun
                   return t
           return ""
    
    def R17(t): #NOMINAL - NOMINAL PP
           global level
           prev=level
           temp = Q3(t)
           if temp!="":
               global count
               if count==(len(input1)-1):
                  return t
               count+=1
               t=input1[count]
               level=prev
               temp=Q4(t)
               if temp!="":
                   return t
           return ""
    
    def R18(t): #VP - VERB
           global level
           temp=Q11(t)
           if temp!="":
               return t
           return ""
    
    def R19(t): #VP - NP
           global level
           temp=Q1(t)
           if temp!="":
               return t
           return ""
    
    def R20(t): #VP - PP
           global level
           temp=Q4(t)
           if temp!="":
               return t
           return ""
    
    def R22(t): #VP - VP PP
           global level
           prev=level
           temp=Q2(t)
           if temp!="":
               global count
               if count==(len(input1)-1):
                  return t
               count+=1
               t=input1[count]
               level=prev
               temp2=Q4(t)
               if temp2!="":
                   return t
           return ""
    
    def R23(t): #VP - AUX VP
           global level
           prev=level
           temp=Q8(t)
           if temp!="":
               global count
               if count==(len(input1)-1):
                  return t
               count+=1
               t=input1[count]
               level=prev
               temp2=Q2(t)
               if temp2!="":
                   return t
           return ""
    
    def R24(t): #VP - VP CONJ VP
           global level
           prev=level
           temp=Q2(t)
           if temp!="":
               global count
               if count==(len(input1)-1):
                  return t
               count+=1
               t=input1[count]
               level=prev
               temp2=Q13(t)
               if temp2!="":
                   if count==(len(input1)-1):
                       return t
                   count+=1
                   t=input1[count]
                   level=prev
                   temp3=Q2(t)
                   if temp3!="":
                       return t
           return ""
    
    def R25(t): #VP - VBD VP
           global level
           prev=level
           temp=Q14(t)
           if temp!="":
               global count
               if count==(len(input1)-1):
                  return t
               count+=1
               t=input1[count]
               level=prev
               temp2=Q2(t)
               if temp2!="":
                   return t
           return ""
       
    Q0(t)
    


input3="The boy opened the\nbox on the floor."
#input3="John is eating at work."
input2=input3.split(" ")
input1=stemmer(input2)
print input1
parser(input1)
