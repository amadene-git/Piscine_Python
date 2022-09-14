# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

print("module_{module:0>2}, ex_{ex:0>2} : {dec1:.2f}, {int1:.2e}, {dec2:.2e} ".format(module=kata[0], ex=kata[1], dec1=kata[2], int1=kata[3], dec2=kata[4]))