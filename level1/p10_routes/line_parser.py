from dataclasses import dataclass
import unittest


@dataclass
class TracerouteNode:
    ip: str
    hostname: str
    rt_time: int
    hidden: bool = False

    @staticmethod
    def hidden_node():
        return TracerouteNode('hidden', 'hidden', 0, True)


def parse_traceroute_line_linux(line: str) -> TracerouteNode:
    line = line.strip()
    try:
        if line.__contains__('*'):
            return TracerouteNode('', '', 0, True)
        line = line.replace(' !X', '')
        s = line.split(' ')
        print(s)
        hostname = s[2]
        ip = s[3][1:-1]
        rtt = float(s[5])
    except:
        print(f'error parsing line: [{line}]')
        return TracerouteNode.hidden_node()
    return TracerouteNode(ip, hostname, round(rtt))


def parse_traceroute_line_windows(line: str):
    ip = ''
    hostname = 'not specified'
    rt_time = 1

    if not line.__contains__('*'):
        x = line.split(' ')

        if x[-1].__contains__('[') and x[-1].__contains__(']'):
            ip = x[-1][1:-1]
            hostname = x[-2]
        else:
            ip = x[-1]
        if not x[6].__contains__('<'):
            try:
                avg = int(x[6]) + int(x[12]) + int(x[18])
            except:
                rt_time = 666

    else:
        return TracerouteNode('hidden', 'hidden', 0, True)
    return TracerouteNode(ip, hostname, rt_time)


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
