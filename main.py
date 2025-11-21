import cmath
import re
import math
def prase_number(s):
    match=re.match(r'(\d+\.?\d*)\s*[∠]\s*(-?\d+\.?\d*)',s)
    if match:
        r=float(match.group(1))
        theta_180=float(match.group(2))
        theta=math.radians(theta_180)
        return cmath.rect(r,theta)
    return None
def prase_complex(s):
    s=s.replace(" ","")
    z=prase_number(s)
    if z is not None:
        return z
    return complex(s)
def polar(s):
    r,theta=cmath.polar(s)
    return f"{r:.4f} ∠{math.degrees(theta):.2f}°"


if __name__=='__main__':
    z1_str=input("enter z1:")
    z2_str=input("enter z2:")
    op=input('运算:')
    z1=prase_complex(z1_str)
    z2=prase_complex(z2_str)

    if op=='+':
        result=z1+z2
    elif op=='-':
        result=z1-z2
    elif op=='*':
        result=z1*z2
    elif op=='/':
        result=z1/z2
    else:
        print("no support calculate")
    print("代数形式："f"{result.real:.3f} {'+' if result.imag>=0 else '-'} j{abs(result.imag):.3f}")
    print("polar:",polar(result))
    print("y")

