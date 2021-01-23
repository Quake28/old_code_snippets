def hcf(x,y):
    if x<y:
        smaller=x
    elif x>y:
        smaller=y
    for i in range (1,smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf=i
    return hcf

def lcm(x,y):
    return int(x*y/(hcf(x,y)))

def main():
    x=int(input("Enter numerator :"))
    y=int(input("Enter denominator :"))
    print("Simplest form is ",int(x/(hcf(x,y))),"/",int(y/(hcf(x,y))),".")
    print("The HCF for the two numbers is ",hcf(x,y),".")
    print("The LCM for the two numbers is ",lcm(x,y),".")

main()
