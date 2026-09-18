mätarinställning_idag=int(input("Mätarinställning idag?"))
mätarinställning_för_ett_år_sedan=int(input("0m ett år sedan"))
antal_körda_mil=mätarinställning_idag-mätarinställning_för_ett_år_sedan
print("antal körda mil", antal_körda_mil)
antal_liter_bensin= int(input ("antal  liter bensin"))
förbrukning_bensin= antal_liter_bensin / antal_körda_mil
print 