#memory timing helper v1.01
from tkinter import *
import tkinter as tk

def refresh(self):
    self.destroy()
    self.__init__()

r = tk.Tk()
r.minsize(640,480)
r.title('Memory Speed Settings')
default_bg = r.cget("bg")

#Define Variables
text_tCL = tk.StringVar()
text_tRCD = tk.StringVar()
text_tRP = tk.StringVar()
text_tRAS = tk.StringVar()
text_tRC = tk.StringVar()
text_tT =  tk.StringVar()
text_aCL = tk.StringVar()
text_aRCD = tk.StringVar()
text_aRP = tk.StringVar()
text_tSpeed = tk.StringVar()
#Define int Variables
tCL = 0
tRCD= 0
tRP = 0
tRAS= 0
tRC = 0
tT  = 0
aCL = 0
aRCD= 0
aRP = 0

refreshscreen = 0
Label(r, text='Memory Speed Settings Calculator ',anchor=tk.E, bg=default_bg, height=2, width=40, bd=3, font=("Arial", 12, "bold"), cursor="hand2", fg="black", padx=0,pady=0).grid(row=1,column=0,columnspan=4)
Label(r, text='Default',anchor=tk.E, bg=default_bg, height=2, width=14, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="black", padx=0,pady=0).grid(row=2,column=0)
Label(r, text='New',anchor=tk.E, bg=default_bg, height=2, width=14, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="black", padx=0,pady=0).grid(row=2,column=1)
Label(r, text='Calculated',anchor=tk.E, bg=default_bg, height=2, width=14, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="black", padx=0,pady=0).grid(row=2,column=3)

pc1 = Label(r,text="tCL" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc2 = Label(r,text="tRCD" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc3 = Label(r,text="tRP" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc4 = Label(r,text="tRAS" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc5 = Label(r,text="tRC" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc6 = Label(r,text="tWR" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc7 = Label(r,text="tRFC" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc8 = Label(r,text="T" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc9 = Label(r,text="tRRD" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc10= Label(r,text="tWTR" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc11= Label(r,text="tRPT" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc12= Label(r,text="tFAW" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
pc13= Label(r,text="tCWL" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="green", padx=0, pady=0)
#placholders
c1 = Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="blue", padx=0, pady=0)
c2 = Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="blue", padx=0, pady=0)
c3 = Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="blue", padx=0, pady=0)
c4 = Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="red", padx=0, pady=0)
c5 = Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="red", padx=0, pady=0)
c6 = Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="red", padx=0, pady=0)
c7 = Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="red", padx=0, pady=0)
c8 = Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="blue", padx=0, pady=0)
c9 = Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="red", padx=0, pady=0)
c10= Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="red", padx=0, pady=0)
c11= Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="red", padx=0, pady=0)
c12= Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="red", padx=0, pady=0)
c13= Label(r,text="-" ,anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10), cursor="hand2", fg="red", padx=0, pady=0)
Label(r, text='tCL ',anchor=tk.E, bg=default_bg, height=2, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="red", padx=1,pady=1).grid(row=3)
Label(r, text='tRCD',anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="blue", padx=0, pady=0).grid(row=4)
Label(r, text='tRP',anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="blue", padx=0, pady=0).grid(row=5)
Label(r, text='tRAS',anchor=tk.E,bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="blue", padx=0, pady=0).grid(row=6)
Label(r, text='tRC',anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="blue", padx=0, pady=0).grid(row=7)
Label(r, text='T',anchor=tk.E, bg=default_bg, height=1, width=5, bd=3, font=("Arial", 10, "bold"), cursor="hand2", fg="blue", padx=0, pady=0).grid(row=8)
pc1.grid(row=3,column=3)
c1.grid(row=3,column=4)
pc2.grid(row=4,column=3)
c2.grid(row=4,column=4)
pc3.grid(row=5,column=3)
c3.grid(row=5,column=4)
pc4.grid(row=6,column=3)
c4.grid(row=6,column=4)
pc5.grid(row=7,column=3)
c5.grid(row=7,column=4)
pc6.grid(row=8,column=3)
c6.grid(row=8,column=4)
pc7.grid(row=9,column=3)
c7.grid(row=9,column=4)
pc8.grid(row=10,column=3)
c8.grid(row=10,column=4)
pc9.grid(row=11,column=3)
c9.grid(row=11,column=4)
pc10.grid(row=12,column=3)
c10.grid(row=12,column=4)
pc11.grid(row=13,column=3)
c11.grid(row=13,column=4)
pc12.grid(row=14,column=3)
c12.grid(row=14,column=4)
pc13.grid(row=15,column=3)
c13.grid(row=15,column=4)
def update_window(event=None):
    e1 = Entry(r,bd=2,width=2,textvariable = text_tCL)
    e2 = Entry(r,bd=2,width=2,textvariable = text_tRCD)
    e3 = Entry(r,bd=2,width=2,textvariable = text_tRP)
    e4 = Entry(r,bd=2,width=2,textvariable = text_tRAS)
    e5 = Entry(r,bd=2,width=2,textvariable = text_tRC)
    e6 = Entry(r,bd=2,width=2,textvariable = text_tT)
    e1.grid(row=3, column=1, sticky="W")
    e2.grid(row=4, column=1, sticky="W")
    e3.grid(row=5, column=1, sticky="W")
    e4.grid(row=6, column=1, sticky="W")
    e5.grid(row=7, column=1, sticky="W")
    e6.grid(row=8, column=1, sticky="W")
    #add new column
    f1 = Entry(r,bd=2,width=2,textvariable = text_aCL)
    f2 = Entry(r,bd=2,width=2,textvariable = text_aRCD)
    f3 = Entry(r,bd=2,width=2,textvariable = text_aRP)
    f1.grid(row=3, column=2, sticky="W")
    f2.grid(row=4, column=2, sticky="W")
    f3.grid(row=5, column=2, sticky="W")
#***** Add code to calulate from alter code ******
    #show entered tCL
    #init to ZERO (will be reset on recal for c_ ints)
    tRCD=tRP=tRAS=tRC=tCL=0   
    tempn = text_tRCD.get()     
    if tempn.isdigit() : tRCD=int(tempn)
    tempn = text_tRP.get()
    if tempn.isdigit() : tRP=int(tempn)
    tempn = text_tRAS.get()
    if tempn.isdigit() : tRAS=int(tempn)
    tempn = text_tRC.get()
    if tempn.isdigit() : tRC=int(tempn)
    tempn = text_tCL.get()
    if tempn.isdigit() : tCL=int(tempn)
    #Altered Values
    aCL = aRP = aRCD = 0;
    tempn = text_aCL.get()
    if tempn.isdigit() : aCL=int(tempn)
    tempn = text_aRP.get()
    if tempn.isdigit() : aRP=int(tempn)
    tempn = text_aRCD.get()     
    if tempn.isdigit() : aRCD=int(tempn)
    tempn = text_tT.get()     
    if tempn.isdigit() : atT=int(tempn)
    #Assign c_ overclock variables to zero
    c_tRAS = c_tRC = c_tRP = c_tRCD = c_tCL = c_tWR = c_tRFC = c_tRRDf = c_tWTR = c_tRRD = c_tWTR = c_tRPT = c_tCWL = 0
    if aCL> 0 :   c_tCL  = aCL
    if aRP > 0 :  c_tRP  = aRP
    if aRCD > 0 : c_tRCD = aRCD
    #Update Values
    if c_tCL > 0 :  c1.config(text = str(c_tCL))
    if c_tRCD > 0 : c2.config(text = str(c_tRCD))
    if c_tRP > 0 :  c3.config(text = str(c_tRP))

    #Display Command rate
    tempn = text_tT.get()
    
    if tempn.isdigit() : c8.config(text = tempn)

    #Calculate OC tRAS
    if c_tCL>0 and c_tRCD>0 and c_tRP>0 :
       #c_tRAS = c_tRCD + c_tRP + c_tCL
       #There isn't an actual formula for TRAS but tRCD + tCL + X(a delay to precharge) so we need to know the individual chips X
       #So original X = (Original TRAS - (RCD+CL)) then divide by oringinal CL and multiply by new CL and later round up
       c_tRRDf = (((tRAS - (tCL+tRCD))/tCL) * aCL)
       c_tRAS = int(aCL + aRCD + c_tRRDf + 0.4) # + 0.4 for round up on after CL RCD delay
       c4.config(text = str(c_tRAS))
       if c_tRRDf > 0 :
           c_tRRD = int(c_tRRDf)
           c_tWTR = c_tRRD + 1
           c9.config(text = str(c_tRRD)) #tRDD
           c10.config(text = str(c_tWTR)) # tRRD must be < tWTR normal to add 1
           
    # tRC = tRAS (Row Address/Access Strobe/Select ) + tRP (Row/RAS Precharge) 
    if c_tRAS > 0 and c_tRP >0 : c_tRC = c_tRAS + c_tRP
    #Display any calcualated result for c_tRC
    if c_tRC > 0 : c5.config(text = str(c_tRC))
    #Caclulate tWR force Even
    if c_tRRD > 0 and c_tWTR > 0 : c_tWR = c_tWTR + c_tRRD
    if (float(c_tWR / 2.0) - int(c_tWR / 2)) > 0 and (atT /2) >= 1.0: c_tWR += 1 # make tWR even if tWR not Even and setting is T2
    if c_tWR > 0 : 
        c6.config(text = str(c_tWR))
        c12.config(text = str(c_tRRD * 4)) #tFAW
        c_tRPT = c_tWR - c_tRRD #c_tRPT
        c11.config(text = str(c_tRPT))
  
    #Calculate tRFC
    #because if defaults worked we would not be working out manual values further more this *equation is a litle BS as c_tRFC varies with
    #memory density BUT the maximum amount of  "Refresh commands is limited to 9 × tREFI (see Figure 57). A maximum of 8 
    #addi-tional Refresh commands can be issued in advance (“pulled in”), with each one reducing the number of regu-
    #regular Refresh commands required later by one" Hynix data sheet so
    #This cacluates much higher that the BIOS and I would say the foumula is very conservative!
    if c_tRC > 0 : c_tRFC = 8 * c_tRC
    if c_tRFC > 0 : c7.config(text = str(c_tRFC))


    #final setting 10 tCL (set tCWL=tCL if tCL is even and tCWL= tCL-1 by one clk if tCL is odd) 
    if (float(c_tCL / 2.0) - int(c_tCL / 2)) > 0 : c_tCWL = c_tCL - 1
    else : c_tCWL = c_tCL
    if c_tCWL > 0 : c13.config(text = str(c_tCWL))
    if refreshscreen == 1:
       button = tk.Button(r, text='Update', width=14, command=update_window)
       button.grid(row=30, column=2)
 

if refreshscreen == 0:
   refreshscreen = 1
   update_window()
    
r.mainloop()


