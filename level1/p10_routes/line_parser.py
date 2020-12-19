from dataclasses import dataclass
import unittest


@dataclass
class TracerouteNode:
    ip: str
    hostname: str
    rt_time: int
    hidden: bool = False


def parse_traceroute_line_linux(line: str) -> TracerouteNode:
    if line.__contains__('*'):
        return TracerouteNode('', '', 0, True)
    line = line.replace(' !X', '')
    s = line.split(' ')
    print(s)
    hostname = s[3]
    ip = s[4][1:-1]
    rtts = [s[6], s[9], s[12]]
    rtt = sum([float(f) for f in rtts]) / 3
    # do napisania
    return TracerouteNode(ip, hostname, round(rtt))


class TestSum(unittest.TestCase):

    def test_1(self):
        line = ' 4  58.56.126.176.ip4.epix.net.pl (176.126.56.58)  6.639 ms  6.876 ms  7.112 ms'
        rt = parse_traceroute_line_linux(line)
        self.assertEqual(rt.ip, '176.126.56.58', '')
        self.assertEqual(rt.hostname, '58.56.126.176.ip4.epix.net.pl', '')

    def test_2(self):
        line = ' 2  10.54.0.1 (10.54.0.1)  3.095 ms  3.939 ms  4.126 ms'
        rt = parse_traceroute_line_linux(line)
        self.assertEqual(rt.ip, '10.54.0.1', '')
        self.assertEqual(rt.hostname, '10.54.0.1', '')

    def test_3(self):
        line = ' 8  109.wsi.edu.pl (91.200.38.109)  19.322 ms !X  21.340 ms !X  21.580 ms !X'
        rt = parse_traceroute_line_linux(line)
        self.assertEqual(rt.ip, '91.200.38.109', '')
        self.assertEqual(rt.hostname, '109.wsi.edu.pl', '')

    def test_4(self):
        line = ' 7  * * *'
        rt = parse_traceroute_line_linux(line)
        self.assertEqual(rt.ip, '', '')
        self.assertEqual(rt.hostname, '', '')
        self.assertEqual(rt.hidden, True, '')


if __name__ == '__main__':
    unittest.main()
