class XmasSearch:
    def __init__(self):
        self.lines = []
        self.count = 0
        self.words = ["XMAS", "SAMX"]
        self.length = 4
        
    def fits_horizontaly(self, i, j):
        return j <= len(self.lines[i].strip()) - self.length
    
    def fits_verticaly(self, i, j):
        return i <= len(self.lines) - self.length
        
    def horizontal(self, i, j):
        if self.fits_horizontaly(i, j):
            word = self.lines[i][j:j+self.length]
            return word in self.words
        return False
    
    def vertical(self, i, j):
        if self.fits_verticaly(i, j):
            word = ""
            for ii in range(self.length):
                word += self.lines[i+ii][j]
            return word in self.words
        return False
    
    def right_cross(self, i, j):
        if self.fits_horizontaly(i, j) and self.fits_verticaly(i, j):
            word = ""
            for ii in range(self.length):
                for jj in range(self.length):
                    if ii == jj:
                        word += self.lines[i+ii][j+jj]
            return word in self.words
        return False
    
    def left_cross(self, i, j):
        if j >= self.length - 1 and self.fits_verticaly(i, j):
            word = ""
            for ii in range(self.length):
                for jj in range(self.length):
                    if ii == jj:
                        word += self.lines[i+ii][j-jj]
            return word in self.words
        return False
             
    def search(self, lines):
        self.lines = lines
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i].strip())):
                if self.vertical(i, j):
                    self.count += 1
                if self.horizontal(i, j):
                    self.count += 1
                if self.right_cross(i, j):
                    self.count += 1
                if self.left_cross(i, j):
                    self.count += 1
        return self.count


if __name__ == "__main__":
    with open("04.txt", "r") as input_file:
        lines = input_file.readlines()
        lines = [line.strip() for line in lines]
    result = XmasSearch().search(lines)
    print(f"Result: {result}")
            