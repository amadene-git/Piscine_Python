import array

class TinyStatistician:
    
    def bubble_sort(self, x):
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
        return xcpy

    def my_sqrt(self, num, root = 2, n_dec = 20):
        nat_num = 1
        while nat_num**root <= num:
            result = nat_num
            nat_num += 1

        for d in range(1, n_dec+1):
            increment = 10 ** -d
            count = 1
            before = result

            while (before + increment * count)**root <= num:
                result = before + increment*count
                count += 1
        
        return result

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
        xcpy = self.bubble_sort(x)
                
        
        if len(x) % 2 == 1:
            return float(xcpy[(len(x) + 1) // 2 - 1])

        
        return float((xcpy[len(x) // 2 - 1] + xcpy[len(x) // 2]) / 2)
            

    def quartiles(self, x):
        if not isinstance(x, list) and not isinstance(x, array):
            return None
        if len(x) == 0:
            return None
        
        xcpy = self.bubble_sort(x)
        
        
        if (len(x) + 3) % 4 != 0:
            q1 = float((xcpy[(len(x) + 3) // 4 - 1] + xcpy[(len(x) + 3) // 4]) / 2)
        else:
            q1 = float(xcpy[(len(x) + 3) // 4 - 1])
        
        if (3 * len(x) + 1) % 4 != 0:
            q3 = float((xcpy[(3 * len(x) + 1) // 4 - 1] + xcpy[(3 * len(x) + 1) // 4]) / 2)
        else:
            q3 = float(xcpy[(3 * len(x) + 1) // 4 - 1])

        
        return { "Q1": q1, "Q3": q3}

    def var(self, x):
        if not isinstance(x, list) and not isinstance(x, array):
            return None
        if len(x) == 0:
            return None
        
        xcpy = self.bubble_sort(x)


        v = 0
        m = self.mean(x)
        for i in xcpy:
            if i < m:
                v += (m - i) ** 2
            else:
                v += (i - m) ** 2 
        
        return v / len(x)


    def std(self, x):
        if not isinstance(x, list) and not isinstance(x, array):
            return None
        if len(x) == 0:
            return None
        
        return self.my_sqrt(self.var(x))


if __name__ == '__main__':
    tstat = TinyStatistician()
    a =  [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    print("Expected result: 82.4")
    print()
    print(tstat.median(a))
    print("Expected result: 42.0")
    print()
    print(tstat.quartiles(a))
    print("Expected result: [10.0, 59.0]")
    print()
    print(tstat.var(a))
    print("Expected result: 12279.439999999999")
    print()
    print(tstat.std(a))
    print("Expected result: 110.81263465868862")