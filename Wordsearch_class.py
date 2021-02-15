class Wordsearch():
    def __init__(self,filename):
        """Input grid from text file"""

        file=open(filename,'r')
        grid=''
        for line in file:
            grid+=line
        file.close()

        grid=grid.split('\n')
        height=len(grid)
        width=len(grid[0])

        # Check if rows same length
        minw=min(len(row) for row in grid)
        maxw=max(len(row) for row in grid)
        if minw!=maxw:
            print("Note: Different row lengths!")
            width=maxw
            # Ensure all rows same length by adding blank spaces
            for i in range(height):
                if len(grid[i])<width:
                    grid[i]+=' '*(width-len(grid[i]))

        # Ensure square grid
        if height>width:
            for i in range(height):
                grid[i]+=' '*(height-width)
            width+=1
        elif width>height:
            for i in range(width-height):
                grid.append(' '*width)
                height+=1
                
        self.grid=grid
        self.height=height
        self.width=width
        self.directions=self._MakeDirections()
        
    def _MakeDirections(self):            
        # Generate lines in other directions from forward direction
        forward=self.grid[:]
        height,width=self.height,self.width
        downward=[]
        for i in range(height):
            line=''
            coords=[]
            for j in range(width):
                line+=forward[j][i]
                coords.append((j,i))
            downward.append((line,coords))

        upright=[]
        # upper triangle
        for i in range(height):
            line=''
            coords=[]
            j=0
            while j<=i:
                line+=forward[i-j][j]
                coords.append((i-j,j))
                j+=1
            upright.append((line,coords))
        # lower triangle
        for k in range(1,width):
            line=''
            coords=[]
            j=0
            while j+k<=(width-1):
                line+=forward[(height-1)-j][j+k]
                coords.append(((height-1)-j,j+k))
                j+=1
            upright.append((line,coords))
            
        downright=[]
        # upper triangle
        for k in reversed(range(1,width)):
            line=''
            coords=[]
            i=0
            while i+k<=(width-1):
                line+=forward[i][i+k]
                coords.append((i,i+k))
                i+=1
            downright.append((line,coords))
        # lower triangle
        for i in range(height):
            line=''
            coords=[]
            j=0
            while i+j<=height-1:
                line+=forward[i+j][j]
                coords.append((i+j,j))
                j+=1
            downright.append((line,coords))

        # Now add coords to forward direction
        for i in range(height):
            coords=[]
            for j in range(width):
                coords.append((i,j))
            forward[i]=(forward[i],coords)

        def opposite(direction):
            opp_dir=[]
            for row in direction:
                rev_line=''
                rev_coords=[]
                for i in reversed(range(len(row[0]))):
                    rev_line+=row[0][i]
                    rev_coords.append(row[1][i])
                opp_dir.append((rev_line,rev_coords))
            return opp_dir
            
        backward=opposite(forward)
        upward=opposite(downward)
        downleft=opposite(upright)
        upleft=opposite(downright)

        self.gridcoords=forward

        directions={'forward':forward,'backward':backward,'upward':upward,'downward':downward,
                    'diagNE':upright,'diagSW':downleft,'diagSE':downright,'diagNW':upleft}
    
        return directions

    def Find(self,word):
        """Returns index [Row,Column] of word start and end"""

        found=False
        for direction in self.directions.values():
            for row in direction:
                line,coord=row[0],row[1]
                location=line.find(word)
                if location>=0:
                    found=True
                    step=len(word)-1
                    start=coord[location]
                    end=coord[location+step]
                    return [start,end]
        if not found:
            print(word,"cannot be found!")
            return None

    def Show(self):
        for row in self.grid:
            print(row)
        return self.grid



