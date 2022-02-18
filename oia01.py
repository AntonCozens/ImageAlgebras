from oia import (
    Image,
    Op
) 

I = Image("", Op.I,  "")
ICI = Image(I, Op.C,  I)
ICI_CI = Image(ICI, Op.C,  I)
IC_ICI = Image(I, Op.C,  ICI)

print("ICI")