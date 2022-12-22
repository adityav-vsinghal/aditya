GrossIncome = int(input("Enter a gross income($)"))
noofdependents = int(input("Enter number of dependents"))
Standarddeduction=10000
Dependentdeduction=3000
Taxableincome = GrossIncome - Standarddeduction - ((Dependentdeduction)*(noofdependents)) 
TaxRate= 20/100
Tax= (Taxableincome)*(TaxRate)
print ("Your income tax is           ,",Tax)
