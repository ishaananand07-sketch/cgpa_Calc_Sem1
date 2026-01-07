g=int(input("Enter group(1/2): "))
def gp(perc):
    if perc>=91:
        return 10
    elif perc>=81:
        return 9
    elif perc>=71:
        return 8
    elif perc>=61:
        return 7
    elif perc>=51:
        return 6
    elif perc>=41:
        return 5
    else:
        return 0

def lac():
    credits=4
    lacese=float(input("Enter lac endsem marks (outoff 60): "))
    lacise=float(input("Enter lac insem marks (outoff 20): "))
    lactw=float(input("Enter lac term work (outoff 60): "))
    lactw=(lactw/60*25)
    laccie=float(input("Enter lac cie+attendendance (outoff 20): "))
    lactotal=lacese+lacise+lactw+laccie
    lacperc=(lactotal/125)*100
    print("Total marks obtained in LAC:",lactotal,"outoff 125")
    print("Percentage obtained in LAC:",lacperc,"%")
    lacgp=gp(lacperc)
    print("Grade point obtained in LAC:",lacgp)
    print("Total Credits for LAC: ",credits)
    print()
    return (lacgp*credits)
    
def cst():
    credits=2
    cstese=float(input("Enter cst endsem marks (outoff 60): "))
    cstise=float(input("Enter cst insem marks (outoff 20): "))
    cstcie=float(input("Enter cst cie+attendendance (outoff 20): "))
    csttotal=cstese+cstise+cstcie
    cstperc=(csttotal/100)*100
    print("Total marks obtained in CST:",csttotal,"outoff 100")
    print("Percentage obtained in CST:",cstperc,"%")
    cstgp=gp(cstperc)
    print("Grade point obtained in CST:",cstgp)
    print("Total Credits for CST: ",credits)
    print() 
    return (cstgp*credits)
    

def cstl():
    credits=1
    cstltw=float(input("Enter cst term work (outoff 100): "))
    cstltw=(cstltw/100*25)
    cstltotal=cstltw
    cstlperc=(cstltotal/25)*100
    print("Total marks obtained in CSTL:",cstltotal,"outoff 25")
    print("Percentage obtained in CSTL:",cstlperc,"%")
    cstlgp=gp(cstlperc)
    print("Grade point obtained in CSTL:",cstlgp) 
    print("Total Credits for CSTL: ",credits)
    print() 
    return (cstlgp*credits)
    

def cgd():
    credits=2
    cgdese=float(input("Enter cgd endsem marks (outoff 60): "))
    cgdise=float(input("Enter cgd insem marks (outoff 20): "))
    cgdcie=float(input("Enter cgd cie+attendendance (outoff 20): "))
    cgdtotal=cgdese+cgdise+cgdcie
    cgdperc=(cgdtotal/100)*100
    print("Total marks obtained in CGD:",cgdtotal,"outoff 100")
    print("Percentage obtained in CGD:",cgdperc,"%")
    cgdgp=gp(cgdperc)
    print("Grade point obtained in CGD:",cgdgp)
    print("Total Credits for CGD: ",credits)
    print() 
    return (cgdgp*credits)
    

def cgdl():
    credits=1
    cgdltw=float(input("Enter cgdl term work (outoff 70): "))
    cgdltw=(cgdltw/70*25)
    cgdltotal=cgdltw
    cgdlperc=(cgdltotal/25)*100
    print("Total marks obtained in CGDL:",cgdltotal,"outoff 25")
    print("Percentage obtained in CGDL:",cgdlperc,"%")
    cgdlgp=gp(cgdlperc)
    print("Grade point obtained in CGDL:",cgdlgp)
    print("Total Credits for CGDL: ",credits)
    print() 
    return (cgdlgp*credits) 
    

def cpps():
    credits=2
    cppsese=float(input("Enter cpps endsem marks (outoff 60): "))
    cppsise=float(input("Enter cpps insem marks (outoff 20): "))
    cppscie=float(input("Enter cpps cie+attendendance (outoff 20): "))
    cppstotal=cppsese+cppsise+cppscie
    cppsperc=(cppstotal/100)*100
    print("Total marks obtained in CPPS:",cppstotal,"outoff 100")
    print("Percentage obtained in CPPS:",cppsperc,"%")
    cppsgp=gp(cppsperc)
    print("Grade point obtained in CPPS:",cppsgp)
    print("Total Credits for CPPS: ",credits)
    print() 
    return (cppsgp*credits)
    

def cppsl():
    credits=1
    cppsltw=float(input("Enter cppsl term work (outoff 100): "))
    cppsltw=(cppsltw/100*25)
    cppsltotal=cppsltw
    cppslperc=(cppsltotal/25)*100
    print("Total marks obtained in CPPSL:",cppsltotal,"outoff 25")
    print("Percentage obtained in CPPSL:",cppslperc,"%")
    cppslgp=gp(cppslperc)
    print("Grade point obtained in CPPSL:",cppslgp)
    print("Total Credits for CPPSL: ",credits)
    print() 
    return (cppslgp*credits)
    

def ese():
    credits=2
    esee=float(input("Enter ese endsem marks (outoff 60): "))
    eseie=float(input("Enter ese insem marks (outoff 20): "))
    esecie=float(input("Enter ese cie+attendendance (outoff 20): "))
    esetotal=esee+eseie+esecie
    eseperc=(esetotal/100)*100
    print("Total marks obtained in ESE:",esetotal,"outoff 100")
    print("Percentage obtained in ESE:",eseperc,"%")
    esegp=gp(eseperc)
    print("Grade point obtained in ESE:",esegp)
    print("Total Credits for ESE: ",credits)
    print() 
    return (esegp*credits)
    

def iidtl():
    credits=1
    iidltw=float(input("Enter iidtl term work (outoff 60): "))
    iidltotal=iidltw/60*50            
    iidlperc=(iidltotal/50)*100
    print("Total marks obtained in IIDTL:",iidltotal,"outoff 60")
    print("Percentage obtained in IIDTL:",iidlperc,"%")
    iidlgp=gp(iidlperc)
    print("Grade point obtained in IIDTL:",iidlgp)
    print("Total Credits for IIDTL: ",credits)
    print() 
    return (iidlgp*credits)
    

def ss():
    credits=2
    sstw=float(input("Enter ss term work (outoff 40): "))
    sstw=(sstw/40*25)
    sscie=float(input("Enter ss cie+attendendance (outoff 25): "))
    sstotal=sstw+sscie
    ssperc=(sstotal/50)*100
    print("Total marks obtained in SS:",sstotal,"outoff 50")
    print("Percentage obtained in SS:",ssperc,"%")
    ssgp=gp(ssperc)
    print("Grade point obtained in SS:",ssgp)
    print("Total Credits for SS: ",credits)
    print() 
    return (ssgp*credits)
    

def cca():
    credits=1
    ccatw=float(input("Enter cca term work (outoff 25): "))
    ccatotal=ccatw
    ccaperc=(ccatotal/25)*100
    print("Total marks obtained in CCA:",ccatotal,"outoff 25")
    print("Percentage obtained in CCA:",ccaperc,"%")
    ccagp=gp(ccaperc)
    print("Grade point obtained in CCA:",ccagp)
    print("Total Credits for CCA: ",credits)
    print() 
    return (ccagp*credits)  
    
print()

if g==2:
    s1=lac()
    s2=cst()
    s3=cstl()
    s4=cgd()
    s5=cgdl()
    s6=cpps()
    s7=cppsl()
    s8=ese()
    s9=iidtl()
    s10=ss()
    s11=cca()
    total_credits=19
    total_points=s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11
    cgpa=total_points/total_credits
    print("Your CGPA is:",round(cgpa,2))