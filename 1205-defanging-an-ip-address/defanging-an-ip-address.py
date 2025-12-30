class Solution:
    def defangIPaddr(self, address: str) -> str:
        add1 = address.replace(".","[.]")
        return add1
        