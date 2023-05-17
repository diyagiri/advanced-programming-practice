msg=input("Enter the secret message:")
def comparealpha(val):
    if ord(val)==32:
        return chr(32)
    else:
        letter=[chr(x) for x in range(97,123)]
        for i in range(len(letter)):
            ans=letter[i-3]
        if val.islower():
            return ans.lower()
        else:
            return ans.upper()
secmsg=list((map(comparealpha,msg)))
print("".join(secmsg))