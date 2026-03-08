class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = homepage
        self.forwardStack = []
        self.backStack = []
        
    def visit(self, url: str) -> None:
        self.backStack.append(self.current)
        self.current = url
        self.forwardStack = []        

    def back(self, steps: int) -> str:
        while steps > 0 and self.backStack:
            self.forwardStack.append(self.current)
            self.current = self.backStack.pop()
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forwardStack:
            self.backStack.append(self.current)
            self.current = self.forwardStack.pop()
            steps -= 1
        return self.current
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)