from oia import *

print('Image Examples')

def PrintExample(imageString: str) -> None:
    print(imageString)
    print(str(eval(imageString)))

imageString = 'Image(I, Op.C, I)'
PrintExample(imageString)
imageString = 'Image(Image(I, Op.C, I), Op.C, I)'
PrintExample(imageString)
imageString = 'Image(I, Op.C, Image(I, Op.C, I))'
PrintExample(imageString)
imageString = 'Image(I, Op.C, Image(I, Op.C, Image(I, Op.C, I)))'
PrintExample(imageString)
imageString = 'Image(I, Op.C, Image(I, Op.C, Image(I, Op.C, Image(I, Op.C, I))))'
PrintExample(imageString)
imageString = 'Image(IQI, Op.C, Image(IQI, Op.C, Image(IQI, Op.C, Image(IQI, Op.C, I))))'
PrintExample(imageString)

I1 = Image(I, Op.E, ICI)
I2 = Image(I1, Op.S, I1)
imageString = 'Image(I2, Op.C, Image(IQI, Op.C, Image(IQI, Op.C, Image(IQI, Op.C, I))))'
PrintExample(imageString)
result = Excite(eval(imageString))
print(str(result[0]))
sequents = ExciteSeq(result[0])
print(sequents[0])
transmitters = Transmitters(sequents)
print(transmitters[0])

#
# Check the dissabmbly of H.
#
print('Check splitting of H')
print(H)
print(Excite(H))
print(ExciteSeq(Excite(H)[0]))
print(Transmitters(ExciteSeq(Excite(H)[0])))

#
# Check the dissabmbly of I!H.H.
#
print('Check splitting of HP')
HP = Image(Image(I, Op.E, H), Op.S, H)
print(HP)
print(Excite(HP))
print(ExciteSeq(Excite(HP)[0]))
print(Transmitters(ExciteSeq(Excite(HP)[0]))[0])