#
# OIA: Open Image Algebras
#
# Coding for Life / Coding for Pleasure
#  
# Author: Anton Cozens
# Email: anton.cozens@gmail.com
#
# Licence: (Y) 2022.
#
# "Nulla est homini causa philosphandi,
#  nisi ut beatus sit."
#
#          St. Augustine.
#
#
# Experiment IV. 2022-02-18
# 
# Implementation of H
# 
# H = (I?(I+I)).I!(I+I).(I+I)
# 
#            .
#           / \
#          /   \
#         /     \
#        ?       .
#       / \     / \
#      I  I+I  /   \
#             /     \
#            !      I+I
#           / \
#          I  I+I
#
from list_and_set import *  

class Op:
    I = "I"
    C = "+"
    S = "."
    E = "!"
    Q = "?"

class Image:
    def __init__(self, L, Op, R):
        self._Op = Op
        self._L = L
        self._R = R
    @property
    def Op(self):
        return self._Op
    @property
    def L(self):
        return self._L
    @property
    def R(self):
        return self._R
    def __str__(self):
        if self._Op == Op.I:
            return "I"
        return "(" + str(self.L) + self.Op + str(self.R) + ")"

def CSplit(i: Image) -> list[Image]:
    return [i]

def SSplit(i: Image) -> list[Image]:
    return i

def Excite(il: list[Image]) -> Image:
    return I

def Quieten(ill: list[list[Image]], s: Image, v: Image) -> Image:
    return I

# Substitution.
# i - Image
# s - Substitution Image
# v - Variable Image
def Sub(i: Image, s: Image, v: Image) -> Image:
    if i != v:
        return i
    if str(v) == str(i):
        return s
    if i.Op == Op.Q:
        if str(i.R) == str(v):
            return i
        return Image(i.L, i.Op, Image(I, Op.E, I))
    return Image(Sub(i.L, s, v), i.Op, Sub(i.L, s, v))

def RunSub(old: Image, sub: Image, var: Image):
    new = Sub(old, sub, var)
    print("old: " + str(old))
    print("sub: " +'[' + str(sub) + '/' + str(var) + ']')
    print("new: " + str(new))
    print("-" * 60)
    return new

def RunSubTest(old: Image, sub: Image, var: Image, exp: Image):
    print("exp: " + str(exp))
    # try:
    new = RunSub(old, sub, var)
    # except:
    #     print('Oops!')
    print(str(str(new) == str(exp)))
    print("=" * 60)

OI = Op.I
I = Image(Image("", OI, ""), OI, Image("", OI, ""))
ICI = Image(I, Op.C, I)
H = Image(Image(I ,Op.Q , ICI), Op.S, Image(Image(I, Op.E, ICI), Op.S, ICI))
YL = Image(Image(Image(I, Op.E, H), Op.S, H), Op.C, H)
YR = Image(H, Op.C, Image(Image(I, Op.E, H), Op.S, H))

print("YL -----:")
print(str(YL))
print("YR -----:")
print(str(YR))

print('\\' * 60)
print('Substitution')
print('/' * 60)

RunSubTest(YL, H, ICI, YR)
RunSubTest(YR, H, ICI, YL)

# Scaffolding.
ISI = Image(I, Op.S, I)
IEI = Image(I, Op.E, I)
IQI = Image(I, Op.Q, I)
IQ_ICI = Image(I, Op.Q, ICI)
IQ_ISI = Image(I, Op.Q, ISI)
IQI_Q_ISI = Image(IQI, Op.Q, ISI)
ICI_C_ICI = Image(ICI, Op.C, ICI)
ISI_C_ISI = Image(ISI, Op.C, ISI)
IQI_S_ICI = Image(IQI, Op.C, ICI)
IQI_S_ISI = Image(IQI, Op.C, ISI)
IQI_ICI = Image(IQI, Op.C, ICI)
IQ_ICI__S_ICI = Image(IQI_ICI, Op.S, ICI) 
IQ_ICI__S_ISI = Image(IQI_ICI, Op.S, ISI) 
IQI_Q_ICI__S_ISI = Image(IQI_ICI, Op.Q, ISI)
IQI_Q_ICI__S_IQI = Image(IQI_ICI, Op.Q, IQI)

IQI_Q_ICI__S_IQI = Image(IQI_ICI, Op.Q, IQI)

RunSubTest(YL, I, I, YL)
RunSubTest(YL, ICI, I, YL)
RunSubTest(YL, ISI, ICI, YL)

# Redefine.
H = Image(Image(I ,Op.Q , ISI), Op.S, Image(Image(I, Op.E, ICI), Op.S, ICI))
EXP = Image(Image(Image(I, Op.E, H), Op.S, H), Op.C, H)

RunSubTest(I, I, I, I)
RunSubTest(I, ICI, I, ICI)

RunSubTest(YL, ISI, ICI, EXP)