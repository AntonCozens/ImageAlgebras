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

# Binding Variables
def BV(i):
    if i.Op == Op.I:
        return []
    if i.Op == Op.Q:
        return [i.R]
    return BV(i.L) + BV(i.R)

# Binding Variables Tests
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
# IQI_Q_ICI__S_IQI = Image(I_Q_ICI, Op.S, IQI)

print("T1: " + str(str(I) == "I"))
print("T2: " + str(BV(I) == []))
print("T3: " + str(str(ICI) == "(I+I)"))
print("T4: " + str(BV(ICI) == []))
print("T5: " + str(str(ISI) == "(I.I)"))
print("T6: " + str(BV(ISI) == []))
print("T7: " + str(str(IQI) == "(I?I)"))
print("T8: " + str(BV(IQI) == [I]))
print("T9: " + str(str(IQ_ICI) == "(I?(I+I))"))
print("T10: " + str(BV(IQ_ICI) == [ICI]))
print("T11: " + str(str(IQI_Q_ISI) == "((I?I)?(I.I))"))
print("T12: " + str(BV(IQI_Q_ISI) == [ISI]))

def FV(i):
     if i.Op == Op.I:
         return [Op.I]
#     if i.Op == Op.S:
#         FVL = FV(i.L)
#         FVR = FV(i.R)
#         # Assume we have a?b.p
#         if i.L.Op == Op.Q: 
#             return FV(i.L) - FV(i.R)
#     return list_to_set([i.L, i.R])
    
# print (FV(Image("", Op.I,  "")))
# I = Image("", Op.I,  "")
# print (["I: "] + FV(Image(I, Op.C,  I)))
# print (["C: "] + FV(Image(I, Op.C,  Image(I, Op.C,  I))))
# print (["S: "] + FV(Image(I, Op.S,  Image(I, Op.S,  I))))
# print (["E: "] + FV(Image(I, Op.E,  Image(I, Op.E,  I))))
# print (["Q: "] + FV(Image(I, Op.Q,  Image(I, Op.Q,  I))))

# Substitution.
# i - Image
# s - Substitution Image
# v - Variable Image
def Sub(i: Image, s: Image, v: Image) -> Image:
    if i == I:
        return I
    if str(v) == str(i):
        return s
    if i.Op == Op.Q:
        if str(i.R) == str(v):
            return i
        return Image(i.L, i.Op, I)
    return i
    if i.Op == Op.Q:
        if b == I:
            return i
        if s == I:
            return i
        if str(b) == str(i.L.R):
            return i
        return (Sub(i.L, b, s), Op.Q, Sub(i.R, b, s))
    if i.L == I:
        newL = I
    else:
        newL = Image(Sub(i.L, b, s))
    if i.R == I:
        newR = I
    else:
        newR = Image(Sub(i.R, b, s))
    return Image(newL, i.Op, newR)

print('\\' * 60)
print('Substitution')
print('/' * 60) 

def RunSub(old: Image, sub: Image, var: Image) -> None:
    print("old: " + str(old))
    print("sub: " + str(old) + '[' + str(sub) + '/' + str(var) + ']')
    print("new: " + str(Sub(old, sub, var)))
    print("-" * 60)

old = I
sub = I
var = I
RunSub(old, sub, var)

print("TS1: " + str( str(Sub(I, I, I)) == str(I) ))
print("TS2: " + str( str(Sub(I, ICI, I)) == str(I) ))
print("TS3: " + str( str(Sub(I, I, ISI)) == str(I) ))
print("TS4: " + str( str(Sub(I, ICI, IQI)) == str(I) ))
print("TS5: " + str( str(Sub(IQI_Q_ICI__S_ISI, ICI, ISI)) == str(IQI_Q_ICI__S_ISI) ))
print("TS6: " + str( str(Sub(IQI_Q_ICI__S_ISI, ISI, ICI)) == str(IQI_Q_ICI__S_ISI) ))
print("TS7: " + str( str(Sub(IQI_Q_ICI__S_ISI, IQI, ISI)) == str(IQI_Q_ICI__S_IQI) ))

# print("TS3: " + str( str(Sub(ICI, ISI, ICI)) == str(ICI) )) 
# print("TS4: " + str( str(Sub(ICI, I, ISI)) == str(ICI) ))
# print("TS5: " + str( str(Sub(ICI, ISI, I)) == str(ICI) ))
# print("TS6: " + str( str(Sub(IQ_ICI, ICI, ISI)) == str(IQ_ICI) ))
# print("TS7: " + str( str(Sub(IQ_ICI, ICI, ISI)) == str(IQ_ICI) ))
# print("TS8: " + str( str(Sub(ICI_C_ICI, ICI, ISI)) == str(ISI_C_ISI) ))
# print("TS9: " + str( str(Sub(IQI_S_ICI, ICI, ISI)) == str(IQI_S_ISI) ))
# print("TS10: " + str( str(Sub(IQ_ICI__S_ICI, ICI, ISI)) == str(IQ_ICI__S_ICI) ))
# print("TS11: " + str( str(Sub(IQ_ICI__S_ISI, ISI, ICI)) == str(IQ_ICI__S_ICI) ))


def Red(i: Image) -> Image:
    return i

# print("TR1: " + str( str(Red(I)) == str(I) ))
