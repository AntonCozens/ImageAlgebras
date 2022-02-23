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
from list_and_set import *

class Format:  
    Indent = 0
    Pad = 112

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

def Excite(i: Image) -> list[Image]:
    print(('-' * Format.Indent) + 'Excite  ----|')
    Format.Indent = Format.Indent + 1
    result = [i]
    if i.Op == Op.C:
        result = Excite(i.L) + Excite(i.R)
    Format.Indent = Format.Indent - 1
    return result

def ExciteSeq(i: Image) -> list[Image]:
    print(('-' * Format.Indent) + 'ExciteSeq  ----|')
    Format.Indent = Format.Indent + 1
    if i.Op == Op.S:
        result = [i.L] + ExciteSeq(i.R)
    else:
        result = [i]
    Format.Indent = Format.Indent - 1
    return result

def ExciteAll(image: Image) -> list[list[Image]]:
    print(('-' * Format.Indent) + 'ExciteAll  ----|')
    Format.Indent = Format.Indent + 1
    excited = []
    for opt in Excite(image):
        excited = excited + [ExciteSeq(opt)]
    Format.Indent = Format.Indent - 1
    return excited

def Transmitters(sequents : list[Image]) -> list[Image]:
    print(('-' * Format.Indent) + 'Transmitters  ----|')
    Format.Indent = Format.Indent + 1
    p = sequents[0]
    result = []
    if p.Op == Op.E:
        print(('-' * Format.Indent) + ' T: ' + str(p))
        result = result + [p]
    Format.Indent = Format.Indent - 1
    return result

def Inputs(images : list[Image]) -> list[Image]:
    print('    ' + ('-' * Format.Indent) + 'Inputs  ----|')
    p = images[0]
    result = []
    if p.Op == Op.Q:
        result = result + [p]
    return result


# Substitution.
# i - Image
# s - Substitution Image
# v - Variable Image
def Sub(i: Image, s: Image, v: Image) -> Image:
    print('    ' + ('-' * Format.Indent) + 'Sub  ----|')
    if i != v:
        return i
    if str(v) == str(i):
        return s
    if i.Op == Op.Q:
        if str(i.R) == str(v):
            return i
        return Image(i.L, i.Op, Image(I, Op.E, I))
    return Image(Sub(i.L, s, v), i.Op, Sub(i.L, s, v))

def Quieten(head: Image, var: Image, tail: list[Image]) -> Image:
    print('    ' + ('-' * Format.Indent) + 'Quieten  ----|')
    result = I
    if head.Op == Op.E and var.Op == Op.Q:
        # match channels.
        if head.L == var.L:
            for p in tail:
                result = Image(result, Op.S, Image(Sub(tail, head.R, var.R), Op.S, result))
            return result
    for i in tail:
        result = Image(head, Op.S, result)
    return head

def Reduce(image: Image) -> Image:
    print(('-' * Format.Indent) + 'Reduce  ----|')
    Format.Indent = Format.Indent + 1
    result = image
    excited = ExciteAll(image)
    # for option in excited:
    #     print('---- Choice Sequence')
    #     for seq in option:
    #         print(str(seq))
    #     print('----')
    transmitters = []
    for option in excited:
        transmitters = transmitters + Transmitters(option)
    return result
    print("transmitters")
    for t in transmitters:
        print(str(t))
    if transmitters == []:
        return image
    trigger = transmitters[0]
    newImages = []
    print("Options / Choices")
    choices = Excite(image)
    for option in choices:
        print(str(option))
        newImages = newImages + [Quieten(option, trigger.R, Inputs(ExciteSeq(option)))]
    print('New Options / Choies')
    for newOption in newImages:
        print(str(newOption))

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
RunSubTest(I, I, ICI, I)

image = Image(IQI, Op.S, Image(IQI, Op.S, IQI))
exp = Image(ICI, Op.S, Image(ICI, Op.S, ICI))
RunSubTest(image, I, ICI, exp)
# quit()

def ExciteTest(image: Image) -> None:
    print(str(image) + ' ->')
    for i in Excite(image):
        print(str(i))
    print('-' * 60)

ExciteTest(I)
ExciteTest(ICI)
ExciteTest(ISI)
ExciteTest(IEI)
ExciteTest(IQI)
image = Image(I, Op.C, ICI)
ExciteTest(image)
image = Image(ICI, Op.C, I)
ExciteTest(image)
image = Image(ICI, Op.C, ICI)
ExciteTest(image)
image = Image(ISI, Op.C, ICI)
ExciteTest(image)
image = Image(ICI, Op.C, ISI)
ExciteTest(image)
image = Image(ISI, Op.C, ISI)
ExciteTest(image)
image = Image(IEI, Op.C, IQI)
ExciteTest(image)
image = Image(IQI, Op.C, IEI)
ExciteTest(image)
image = Image(IQI, Op.S, IEI)
ExciteTest(image)
image = Image(IQI, Op.E, IEI)
ExciteTest(image)
image = Image(IQI, Op.Q, IEI)
ExciteTest(image)

def ExciteSeqTest(image: Image) -> None:
    print(str(image) + ' ->')
    for i in ExciteSeq(image):
        print(str(i))
    print('-' * 60)

ExciteSeqTest(I)
ExciteSeqTest(ICI)
ExciteSeqTest(ISI)
ExciteSeqTest(IEI)
ExciteSeqTest(IQI)
image = Image(I, Op.C, ICI)
ExciteSeqTest(image)
image = Image(ICI, Op.S, I)
ExciteSeqTest(image)
image = Image(ICI, Op.S, ICI)
ExciteSeqTest(image)
image = Image(ISI, Op.S, ICI)
ExciteSeqTest(image)
image = Image(ICI, Op.S, ISI)
ExciteSeqTest(image)
image = Image(ISI, Op.S, ISI)
ExciteSeqTest(image)
image = Image(IEI, Op.S, IQI)
ExciteSeqTest(image)
image = Image(IQI, Op.S, IEI)
ExciteSeqTest(image)
image = Image(IQI, Op.S, IEI)
ExciteSeqTest(image)
image = Image(IQI, Op.E, IEI)
ExciteSeqTest(image)
image = Image(IQI, Op.Q, IEI)
ExciteSeqTest(image)

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

def TransmittersTest(images: list[Image]) -> None:
    for i in images:
        print(str(i))
    transmitters = Transmitters(images)
    x = 1
    for act in transmitters:
        print('Out ' + str(x) + ' -> ' + str(act))
        x = x + 1
    print('-' * 60)

imageL = Image(IQI, Op.S, I)
imageR = Image(IEI, Op.S, Image(ICI, Op.S, I))
image = Image(imageL, Op.C, imageR)
images = [imageL, imageR, image]
TransmittersTest(images)

imageL = Image(IQI, Op.E, I)
imageR = Image(IEI, Op.E, Image(ICI, Op.S, I))
image = Image(imageL, Op.E, imageR)
images = [imageL, imageR, image]
TransmittersTest(images)

def InputsTest(images: list[Image]) -> None:
    print('InputsTest ----|')
    for i in images:
        print(str(i))
    inputs = Inputs(images)
    x = 1
    for act in inputs:
        print('In ' + str(x) + ' -> ' + str(act))
        x = x + 1
    print('-' * 60)

imageL = Image(IQI, Op.S, I)
imageR = Image(IEI, Op.S, Image(ICI, Op.S, I))
image = Image(imageL, Op.C, imageR)
images = [imageL, imageR, image]
InputsTest(images)

imageL = Image(IQI, Op.Q, I)
imageR = Image(IEI, Op.Q, Image(ICI, Op.S, I))
image = Image(imageL, Op.Q, imageR)
images = [imageL, imageR, image]
InputsTest(images)

def QuietenTest(o: Image, li: Image, ri: list[Image]):
    print(str(o))
    print(str(li))
    RI = I
    for i in ri:
        RI = Image(i, Op.S, RI)
    print(str(RI))
    quiet = Quieten(o, li, ri)
    print('-> ' + str(quiet))
    print('*' * 60)

print('Start: QuietenTests')

o = Image(ICI, Op.E, ICI)
li = Image(ICI, Op.Q, IQI)
QuietenTest(o, li, [ISI])

o = Image(ICI, Op.E, ISI)
li = Image(ICI, Op.Q, IQI)
QuietenTest(o, li, [IQI])

o = Image(ICI, Op.E, ISI)
li = Image(ISI, Op.Q, IQI)
QuietenTest(o, li, [IQI])

o = Image(ICI, Op.E, ISI)
li = Image(ICI, Op.Q, IQI)
ri = Image(IQI, Op.S, Image(IQI, Op.S, IQI))
QuietenTest(o, li, [ri])

o = Image(ICI, Op.E, ICI)
li = Image(ICI, Op.Q, ISI)
ri = Image(IQI, Op.S, Image(IQI, Op.S, IQI))
QuietenTest(o, li, [ri])

o = Image(ICI, Op.E, ICI)
li = Image(ICI, Op.C, ISI)
ri = Image(IQI, Op.S, Image(IQI, Op.S, IQI))
QuietenTest(o, li, [ri])

print("Start: ExciteAllTests")

def ExciteAllTest(image: Image) -> None:
    print('ExciteAllTest +  ----|')
    print(str(image))
    for opt in ExciteAll(image):
        print('----')
        for seq in opt:
            print('    ' + str(seq))

ExciteAllTest(ICI)

image = Image(ICI, Op.C, Image(ICI, Op.C, I))
ExciteAllTest(image)
image = Image(IQI, Op.C, Image(ICI, Op.C, I))
ExciteAllTest(image)
image = Image(IQI, Op.C, Image(ISI, Op.C, IEI))
ExciteAllTest(image)
ExciteAllTest(YL)
ExciteAllTest(YR)

# print(str(Reduce(Image(YL, Op.C, YR))))

print('Experiment IV: Vision 1, YL to YR')
print('Begin:  ' + '#' * Format.Pad)
Format.Indent = 0
print('input:  ' + str(YL))
print('Output: ' + str(Reduce(YL)))
print('ExOput: ' + str(YR))
print('End:    ' + '#' * Format.Pad + '\r\n')

print('Experiment IV: Vision 1, YR to YL')
print('#' * 60)
print(str(YR))
print('Actual:   ' + str(Reduce(YR)))
print('Expected: ' + str(YL))
