class Fraction:
    def __init__(self, num=0, den=1):

        self.n = num
        self.d = den
        if self.d == 0:
            print("zero")

    def add(self, fraction_obj):
        if self.n == 0 or fraction_obj.n == 0:
            return



    def multiply(self, fraction_obj):
        pass

    def print(self):
        pass

    def smaller_fraction(self):
        if self.n == 0:
            return
        divisor = min(self.d,self.n)
        dividend = max(self.d,self.n)
        rem = -1
        hcf = -1
        while rem != 0:
            multi = divisor * (dividend // divisor)
            rem = dividend - multi
            if rem == 0:
                hcf = divisor
                break
            dividend = divisor
            divisor = rem

        self.n = self.n // hcf
        self.d = self.d // hcf

    def print(self):
        print("{}/{}".format(self.n,self.d))





if __name__ == "__main__":
    nu1 = int(input())
    de1 = int(input())
    num1 = Fraction()

    # nu2 = int(input())
    # de2 = int(input())
    # num2 = Fraction(nu2, de2)


    num1.smaller_fraction()
    num1.print()

    # num1.add(num2)
    # num1.multiply(num2)
    # num1.print()
    # num2.print()
