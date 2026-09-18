mätarinställning=int(input('mätarinställningen i dag?'))
mäterinställning_för_ett_år_sedan=int(input( "mätarinställning om år sedan?"))
antal_köra_mil=mätarinställning - mäterinställning_för_ett_år_sedan
print('antal körda mil:' , antal_köra_mil , "mil")
bensin=int(input("antal liter bensin"))
förbrukning= bensin / antal_köra_mil
print (' antal_köra_mil / , bensin, ')