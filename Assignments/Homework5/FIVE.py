
def SHR(n, x):
    temp = ""
    for i in range(len(n)):
        temp += "0"
    cap = len(x)
    i = n-1
    while temp < cap:
        temp += x[i]
        i += 1
    return temp

def XOR(a,b):
    c = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            c += "0"
        else:
            c += "1"

def Sigma0(n, x):
    Rotated = XOR(ROTR(1,x), ROTR(8,x))
    shifted = XOR(Rotated, SHR(7,x))
    return shifted

def Sigma1(x):
    Rotated = XOR(ROTR(19,x), ROTR(61,x))
    shifted = XOR(Rotated, SHR(6,x))
    return shifted

def ROTR(n,x):
    temp = (n * -1) % len(x)
    res = x[temp :] + x[ : temp]
    return res

def BuildW(M):
    W = []
    for t in range(80):
        if t <= 15:
            # Buffers the first 15 Ws
            W[t] = M[t:(t+1)*64]
        else:
            # SImplifiied addition, should be its own script beacuse after each addition 
            # Mod 2^64 needs to be done but for visual purposes i did this.
            W[t] = (Sigma1(W[t-2]) + W[t-7] + Sigma0(W[t-15]) + W[t-16]) % 2**64

def DefineW(t):
    Out = f"W{t} = $\sigma_1^{{512}}(W_{{{t-2}}})+W_{{{t-7}}}+ \sigma_0^{{512}}(W_{{{t-15}}}) + W_{{{t-16}}}$"
    print(Out)

if __name__ == "__main__":
    M = ""
    # BuildW(M)
    DefineW(16)
    DefineW(17)
    DefineW(18)
    DefineW(19)
