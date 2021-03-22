class ComplexNumber:
    def __init__(self, re, img):
        self.re = re
        self.img = img

    def __add__(self, other):
        re_new = self.re+other.re
        img_new = self.img+other.img
        return {'Re':re_new,'Img':img_new}

    def __sub__(self, other):
        re_new = self.re-other.re
        img_new = self.img-other.img
        return {'Re':re_new,'Img':img_new}

    def __mul__(self, other):
        re_new = self.re*other.re - self.img*other.img
        img_new = self.re*other.img + self.img*other.re
        return {'Re':re_new,'Img':img_new}


z_1 = ComplexNumber(12, 5)
z_2 = ComplexNumber(4, -5)
z = z_1 - z_2

print(z)
