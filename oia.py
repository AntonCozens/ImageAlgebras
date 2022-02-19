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
# Whwn talking about images rge terms li and ri will be used as follows:
#
# li o ri
#
from urllib.parse import non_hierarchical
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
    if i.Op == Op.C:
        return CSplit(i.L) + CSplit(i.R)
    return [i]

def SSplit(i: Image) -> list[Image]:
    if i.Op == Op.S:
        return SSplit(i.L) + SSplit(i.R)
    return [i]

def Excite(image: Image) -> list[list[Image]]:
    images = []
    return CSplit(image)

def ActOut(images : list[Image]) -> list[Image]:
    sending = []
    for i in images:
        if i.Op == Op.E:
            sending = sending + [i.L]
    return sending

def ActIn(images : list[Image]) -> list[Image]:
    receiving = []
    for i in images:
        if i.Op == Op.Q:
            receiving = receiving + [i.L]
    return receiving

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
print(str(YL))

print("YL -----:")
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

def CSplitTest(image: Image) -> None:
    print(str(image) + ' ->')
    for i in CSplit(image):
        print(str(i))
    print('-' * 60)

CSplitTest(I)
CSplitTest(ICI)
CSplitTest(ISI)
CSplitTest(IEI)
CSplitTest(IQI)
image = Image(I, Op.C, ICI)
CSplitTest(image)
image = Image(ICI, Op.C, I)
CSplitTest(image)
image = Image(ICI, Op.C, ICI)
CSplitTest(image)
image = Image(ISI, Op.C, ICI)
CSplitTest(image)
image = Image(ICI, Op.C, ISI)
CSplitTest(image)
image = Image(ISI, Op.C, ISI)
CSplitTest(image)
image = Image(IEI, Op.C, IQI)
CSplitTest(image)
image = Image(IQI, Op.C, IEI)
CSplitTest(image)
image = Image(IQI, Op.S, IEI)
CSplitTest(image)
image = Image(IQI, Op.E, IEI)
CSplitTest(image)
image = Image(IQI, Op.Q, IEI)
CSplitTest(image)

def SSplitTest(image: Image) -> None:
    print(str(image) + ' ->')
    for i in SSplit(image):
        print(str(i))
    print('-' * 60)

SSplitTest(I)
SSplitTest(ICI)
SSplitTest(ISI)
SSplitTest(IEI)
SSplitTest(IQI)
image = Image(I, Op.C, ICI)
SSplitTest(image)
image = Image(ICI, Op.S, I)
SSplitTest(image)
image = Image(ICI, Op.S, ICI)
SSplitTest(image)
image = Image(ISI, Op.S, ICI)
SSplitTest(image)
image = Image(ICI, Op.S, ISI)
SSplitTest(image)
image = Image(ISI, Op.S, ISI)
SSplitTest(image)
image = Image(IEI, Op.S, IQI)
SSplitTest(image)
image = Image(IQI, Op.S, IEI)
SSplitTest(image)
image = Image(IQI, Op.S, IEI)
SSplitTest(image)
image = Image(IQI, Op.E, IEI)
SSplitTest(image)
image = Image(IQI, Op.Q, IEI)
SSplitTest(image)

def ExciteTest(image: Image) -> None:
    print(str(image) + ' ->')
    excited = Excite(image)
    print(excited)
    x = 1
    for option in excited:
        print('Option ' + str(x) + ' ->')
        print(str(option))
        x = x + 1
    print('-' * 60)


ExciteTest(I)
ExciteTest(ICI)
image = Image(I, Op.C, Image( I, Op.C, Image(I, Op.C, ICI)))
ExciteTest(image)
image = Image(IQI, Op.C, Image( I, Op.C, Image(I, Op.S, ICI)))
ExciteTest(image)
imageL = Image(IQI, Op.S, I)
imageR = Image(IEI, Op.S, Image(ICI, Op.S, I))
image = Image(imageL, Op.C, imageR)
ExciteTest(image)

def ActOutTest(images: list[Image]) -> None:
    for i in images:
        print(str(i))
    actout = ActOut(images)
    x = 1
    for act in actout:
        print('Out ' + str(x) + ' -> ' + str(act))
        x = x + 1
    print('-' * 60)

imageL = Image(IQI, Op.S, I)
imageR = Image(IEI, Op.S, Image(ICI, Op.S, I))
image = Image(imageL, Op.C, imageR)
images = [imageL, imageR, image]
ActOutTest(images)

imageL = Image(IQI, Op.E, I)
imageR = Image(IEI, Op.E, Image(ICI, Op.S, I))
image = Image(imageL, Op.E, imageR)
images = [imageL, imageR, image]
ActOutTest(images)

def ActInTest(images: list[Image]) -> None:
    for i in images:
        print(str(i))
    actin = ActIn(images)
    x = 1
    for act in actin:
        print('In ' + str(x) + ' -> ' + str(act))
        x = x + 1
    print('-' * 60)

imageL = Image(IQI, Op.S, I)
imageR = Image(IEI, Op.S, Image(ICI, Op.S, I))
image = Image(imageL, Op.C, imageR)
images = [imageL, imageR, image]
ActInTest(images)

imageL = Image(IQI, Op.Q, I)
imageR = Image(IEI, Op.Q, Image(ICI, Op.S, I))
image = Image(imageL, Op.Q, imageR)
images = [imageL, imageR, image]
ActInTest(images)
