class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dici={}
        temp=97
        for i in key:
            if i!=" " and i not in dici:
                dici[i]=chr(temp)
                temp+=1
        print(dici)
        ans=""
        for i in message:
            if i==" ":
                ans+=" "
            else:
                ans+=dici[i]
        return ans