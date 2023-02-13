import array

class TinyStatistician:
    
    def mean(self, x):
        if not isinstance(x, list) and not isinstance(x, array):
            return None
        if len(x) == 0:
            return None

        length = len(x)
        total = 0
        for i in range(length):
            if not isinstance(x[i], int) and not isinstance(x[i], float):
                raise Exception(f"Error '{x[i]}' Not a Number")
            total += x[i]
        return float(total / length)
    
    def median(self, x):
        if not isinstance(x, list) and not isinstance(x, array):
            return None
        if len(x) == 0:
            return None
        xcpy = x
        length = len(x)
        while length > 0:
            for i in range(length - 1):
                if not isinstance(xcpy[i], int) and not isinstance(xcpy[i], float):
                    raise Exception(f"Error '{x[i]}' Not a Number")                
                if xcpy[i] > xcpy[i + 1]:
                    tmp = xcpy[i]
                    xcpy[i] = xcpy[i + 1]
                    xcpy[i + 1] = tmp
            length -= 1 
        return xcpy[len(x) // 2]
            

    def quartiles(self, x):
        if not isinstance(x, list) and not isinstance(x, array):
            return None
        if len(x) == 0:
            return None
        xcpy = x
        length = len(x)
        while length > 0:
            for i in range(length - 1):
                if not isinstance(xcpy[i], int) and not isinstance(xcpy[i], float):
                    raise Exception(f"Error '{x[i]}' Not a Number")                
                if xcpy[i] > xcpy[i + 1]:
                    tmp = xcpy[i]
                    xcpy[i] = xcpy[i + 1]
                    xcpy[i + 1] = tmp
            length -= 1 
        return (xcpy[len(x) // 4], xcpy[-len(x) // 4])        

    def 



if __name__ == '__main__':
    lol = TinyStatistician()
    tab = [1,2,3,4,5,6,7,8,9,10]
    print(lol.quartiles([0,1, 2 ,3,4, 5,  6,7, 8  ,9]))