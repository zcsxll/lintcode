# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        # sorted(intervals, key=self.get_key)
        ts = []
        for i in intervals:
            # print(i.start, i.end)
            ts.append((i.start, 's'))
            ts.append((i.end, 'e'))
        ts = sorted(ts, key=self.get_key)
        # print(ts)
        cnt = 0
        ret = 0
        for t in ts:
            if t[1] == 's':
                cnt += 1
                if ret < cnt:
                    ret = cnt
            else:
                cnt -= 1
        return ret

    def get_key(self, a):
        return a[0]

if __name__ == '__main__':
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    intervals = [Interval(2, 7)]
    ret = Solution().minMeetingRooms(intervals)
    print(ret)