from tkinter import *
import sqlite3

root=Tk()
root.title("Students Records")
root.geometry("400x600")


conn = sqlite3.connect("Records.db")

c = conn.cursor()
'''
c.execute("""CREATE TABLE students_Records(
          Student_Name text,
          Father_Name text,
          Roll_No text,
          Department text,
          Section text,
          Phone_Number integer
          )""")
'''
SN=Entry(width=5)
SN.grid(row=0,column=1,padx=10,pady=10,ipadx=100)

FN=Entry(width=5)
FN.grid(row=1,column=1,padx=10,pady=10,ipadx=100)

RN=Entry(width=5)
RN.grid(row=2,column=1,padx=10,pady=10,ipadx=100)

Dp=Entry(width=5)
Dp.grid(row=3,column=1,padx=10,pady=10,ipadx=100)

SC=Entry(width=5)
SC.grid(row=4,column=1,padx=10,pady=10,ipadx=100)

PN=Entry(width=5)
PN.grid(row=5,column=1,padx=10,pady=10,ipadx=100)

#Selection of id
SELECT_Entry=Entry(width=5)
SELECT_Entry.grid(row=8,column=1,padx=10,pady=10,ipadx=100)
SELECT_Entry_Label=Label(root,text="Enter id to select:")
SELECT_Entry_Label.grid(row=8,column=0,padx=10,pady=10)


def Insert():
    conn = sqlite3.connect("Records.db")

    c = conn.cursor()
    c.execute("INSERT INTO students_Records VALUES(:S_N,:F_N,:R_N,:D_P,:S_C,:P_N)",
            {
                "S_N":SN.get(),
                "F_N":FN.get(),
                "R_N":RN.get(),
                "D_P":Dp.get(),
                "S_C":SC.get(),
                "P_N":PN.get()
             })



    conn.commit()

    conn.close()



    SN.delete(0,END)
    FN.delete(0,END)
    RN.delete(0,END)
    Dp.delete(0,END)
    SC.delete(0,END)
    PN.delete(0,END)




def Update():
    conn = sqlite3.connect("Records.db")

    c = conn.cursor()
    record_id=SELECT_Entry.get()
    #print(record_id)
    c.execute("""UPDATE students_Records SET
              Student_Name=:S_N,
              Father_Name=:F_N,
              Roll_No=:R_N,
              Department=:D_P,
              Section=:S_C,
              Phone_Number=:P_N
              WHERE oid = :oid""",
                {
                'S_N':SNE.get(),
                'F_N':FNE.get(),
                'R_N':RNE.get(),
                'D_P':DpE.get(),
                'S_C':SCE.get(),
                'P_N':PNE.get(),
                'oid':record_id
                  })



    conn.commit()

    conn.close()
    SELECT_Entry.delete(0,END)

    editer.destroy()
    
    
def delete_record():
    conn=sqlite3.connect("Records.db")
    c=conn.cursor()
    c.execute("DELETE FROM Students_Records WHERE oid="+SELECT_Entry.get())
    conn.commit()
    conn.close()
    SELECT_Entry.delete(0,END)
def Update_record():
    global editer
    editer=Tk()
    editer.title('Record Update')
    editer.geometry("400x400")
    
    conn=sqlite3.connect("Records.db")
    c=conn.cursor()
    record_id=SELECT_Entry.get()
    c.execute("SELECT * FROM Students_Records WHERE oid="+record_id)
    records=c.fetchall()
    #print(records)
    
    global SNE
    global FNE
    global RNE
    global DpE
    global SCE
    global PNE
    
    SNE=Entry(editer,width=5)
    SNE.grid(row=0,column=1,padx=10,pady=10,ipadx=100)

    FNE=Entry(editer,width=5)
    FNE.grid(row=1,column=1,padx=10,pady=10,ipadx=100)

    RNE=Entry(editer,width=5)
    RNE.grid(row=2,column=1,padx=10,pady=10,ipadx=100)

    DpE=Entry(editer,width=5)
    DpE.grid(row=3,column=1,padx=10,pady=10,ipadx=100)

    SCE=Entry(editer,width=5)
    SCE.grid(row=4,column=1,padx=10,pady=10,ipadx=100)

    PNE=Entry(editer,width=5)
    PNE.grid(row=5,column=1,padx=10,pady=10,ipadx=100)

    for result in records:
        SNE.insert(0,result[0])
        FNE.insert(0,result[1])
        RNE.insert(0,result[2])
        DpE.insert(0,result[3])
        SCE.insert(0,result[4])
        PNE.insert(0,result[5])
            
    SNL=Label(editer,text="Student Name:")
    SNL.grid(row=0,column=0,padx=10,pady=10)
    FNL=Label(editer,text="Father's Name:")
    FNL.grid(row=1,column=0,padx=10,pady=10)
    RNL=Label(editer,text="Roll No:")
    RNL.grid(row=2,column=0,padx=10,pady=10)
    DPL=Label(editer,text="Department:")
    DPL.grid(row=3,column=0,padx=10,pady=10)
    SCL=Label(editer,text="Section:")
    SCL.grid(row=4,column=0,padx=10,pady=10)
    PNL=Label(editer,text="Phone Number:")
    PNL.grid(row=5,column=0,padx=10,pady=10)

    save_btn=Button(editer,text="Save",height=1,borderwidth=3,command=Update)
    save_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=110)

    conn.commit()
    conn.close()
    
def Query():
    conn=sqlite3.connect("Records.db")
    c=conn.cursor()
    c.execute("SELECT *,oid FROM Students_Records")
    results=c.fetchall()
    #print(results)
    prints_records=""
    for result in results:
        prints_records+= str(result[0])+" "+str(result[-1])+"\n"
    show=Label(root,text=prints_records)
    show.grid(row=11,column=0,columnspan=2)
    


Btn_Insert=Button(root,text="Insert Data",height=1,borderwidth=3,command=Insert)
Btn_Insert.grid(row=6,column=0,columnspan=2,ipadx=110,padx=10,pady=10)

Btn_Query=Button(root,text="Show data",height=1,borderwidth=3,command=Query)
Btn_Query.grid(row=7,column=0,columnspan=2,ipadx=111,padx=10,pady=5)


#Delete botton
delete_btn=Button(root,text="Delete",height=1,borderwidth=3,command=delete_record)
delete_btn.grid(row=9,column=0,columnspan=2,ipadx=111,padx=10,pady=5)

#Update botton
Update_btn=Button(root,text="Update",height=1,borderwidth=3,command=Update_record)
Update_btn.grid(row=10,column=0,columnspan=2,ipadx=111,padx=10,pady=5)


SNL=Label(root,text="Student Name:")
SNL.grid(row=0,column=0,padx=10,pady=10)
FNL=Label(root,text="Father's Name:")
FNL.grid(row=1,column=0,padx=10,pady=10)
RNL=Label(root,text="Roll No:")
RNL.grid(row=2,column=0,padx=10,pady=10)
DPL=Label(root,text="Department:")
DPL.grid(row=3,column=0,padx=10,pady=10)
SCL=Label(root,text="Section:")
SCL.grid(row=4,column=0,padx=10,pady=10)
PNL=Label(root,text="Phone Number:")
PNL.grid(row=5,column=0,padx=10,pady=10)



conn.commit()

conn.close()







root.mainloop()
