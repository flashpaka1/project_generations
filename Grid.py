class Grid:
    rows = 5
    columns = 5
    boundsX = [rows]
    boundsY = [columns]


    def printStr(self):
        for i in self.rows:
            for j in self.columns:
                print(self.boundsX[i])