class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = "Home"

    def visit(self, page):
        self.back_stack.append(self.current)
        self.current = page
        self.forward_stack.clear()
        print("Visited:", self.current)

    def back(self):
        if not self.back_stack:
            print("No pages to go back")
            return
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        print("Back to:", self.current)

    def forward(self):
        if not self.forward_stack:
            print("No pages to go forward")
            return
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        print("Forward to:", self.current)


browser = Browser()
browser.visit("Google")
browser.visit("YouTube")
browser.visit("GitHub")

browser.back()
browser.back()
browser.forward()
