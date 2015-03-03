from Tkinter import *
from ttk import *

def calculate():
    try:
        ln = loans.get()
        i = intr.get()
        yr = years.get()
        final = compound(ln, i, yr)
        pay = round(final/yr/12, 2)
        sal = round(pay*10*12, 2)

        interestPaid = final - ln
        total.set("$"+str(round(final, 2)))
        payment.set("$"+str(pay))
        salary.set("$"+str(sal))
        interest.set("$"+str(round(interestPaid, 2)))
    except ValueError:
        pass

def compound(t, apr, y):
	if y == 0:
		return t
	else:
		return compound(t+(t*(apr*.01)), apr, y-1)


root = Tk()
root.title("Student Loan Repayment Calculator")

t = Frame(root, padding="10")
t.pack()


loans = IntVar(t)
years = IntVar(t)
intr = DoubleVar(t)
total = StringVar(t)
interest = StringVar(t)
payment = StringVar(t)
salary = StringVar(t)



label0 = Label(t, text="Calculate your future student loan payment", padding="0 0 0 10")
label0.pack()

rFrame = LabelFrame(t, padding="10")
rFrame.pack(side=RIGHT, padx=15)

label1 = Label(t, text="Total student loan debt")
label1.pack()

loansEntry = Entry(t, width=10, textvariable=loans)
loansEntry.pack()

label2 = Label(t, text="Combined average Annual Percentage Rate")
label2.pack()

percSpin = Spinbox(t, from_=0.0, to=20.0, format='%3.1f', increment=0.1, width=4, textvariable=intr)
percSpin.pack()

label3 = Label(t, text="Repayment Completion Goal (in years)")
label3.pack()

yearCombo = Combobox(t, values="3 5 8 10 20 30", textvariable=years)
yearCombo.pack()

calcButton = Button(t, text="Calculate", command=calculate)
calcButton.pack()



payLabel = Label(rFrame, text="Monthly Payment")
payLabel.pack()

payVar = Label(rFrame, textvariable=payment)
payVar.pack()

salaryLabel = Label(rFrame, text="Needed Annual Salary")
salaryLabel.pack()

salaryVar = Label(rFrame, textvariable=salary)
salaryVar.pack()

totalLabel = Label(rFrame, text="Total Amount Paid")
totalLabel.pack()

totalVar = Label(rFrame, textvariable=total)
totalVar.pack()

intLabel = Label(rFrame, text="Total Interest Paid")
intLabel.pack()

intVar = Label(rFrame, textvariable=interest)
intVar.pack()

mainloop()