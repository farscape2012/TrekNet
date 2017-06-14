# Definition for a point.
class Point2D(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def maxPoints(self, points):
        """ sort an array using quick sort algorithm
        :type points: Point2D object
        :rtype: int 
        Note:
            Time complexity: best case On^2)
            Space complexity: O(n) 
        """
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i+1, l):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y:
                    # points overlap
                    same += 1
                    continue
                if points[i].x == tx:
                    slope = 'i'
                else:
                    slope = (points[i].y-ty) * 1.0 /(points[i].x-tx)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
    return m
