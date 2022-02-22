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
transmitters = Outputs(sequents)
print(transmitters[0])
