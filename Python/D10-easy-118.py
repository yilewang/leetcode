### leetcode D10


def generate(numRows):
        grp = [[1]]*numRows
        grp[0] = [1]
        if numRows > 1:
            grp[1] = [1,1]
            for i in range(2,numRows, 1):
                count = len(grp[i-1])
                space = []
                for cc in range(len(grp[i-1])):
                    try:
                        nu = grp[i-1][cc] + grp[i-1][cc+1]
                    except:
                        break
                    space.append(nu)
                grp[i] = space
                grp[i].insert(0, 1)
                grp[i].append(1)

        return grp


print(generate(1))