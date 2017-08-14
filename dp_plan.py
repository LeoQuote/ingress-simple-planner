# -*- coding:utf-8 -*-

from six import print_
import csv
import json
import math


class Portal(object):

    def __init__(self, name, x, y, *args):
        self.name = name
        self.x = float(x) - 40
        self.y = float(y) - 116
        self.prev_portal = None
        self.level = 1

    def __str__(self):
        return '{name}({x}, {y})'.format(
            x=str(self.x)[:8], y=str(self.y)[:8], name=self.name
        )

    def in_triangle(self, t1, t2, t3):
        # https://stackoverflow.com/questions/2049582/how-to-determine-if-a-point-is-in-a-2d-triangle
        def sign(p1, p2, p3):
            return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y) > 0
        return sign(self, t1, t2) == sign(self, t2, t3) == sign(self, t3, t1)

    def line_distance(self, t1, t2):
        # https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line#Line_defined_by_two_points
        x0, y0, x1, y1, x2, y2 = self.x, self.y, t1.x, t1.y, t2.x, t2.y
        return math.fabs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) \
            / math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)


def gen_line(p1, p2):
    return {'color': '#a24ac3',
            'type': 'polyline',
            'latLngs': [
                {'lat': p1.x + 40, 'lng': p1.y + 116},
                {'lat': p2.x + 40, 'lng': p2.y + 116},
            ]}


def calc_plan(base1, base2, portals):
    """
    按离底边从近到远的顺序计算每个po的最大层数
    """
    calc_done = set()
    for portal in sorted(portals, key=lambda x: x.line_distance(base1, base2)):
        for p in calc_done:
            if p.in_triangle(portal, base1, base2) and p.level + 1 > portal.level:
                portal.level = p.level + 1
                portal.prev_portal = p

        calc_done.add(portal)

    print_result(portals)


def print_result(portals):
    portals.sort(key=lambda p: p.level)

    plan_data = [gen_line(base1, base2)]
    p = portals[-1]

    print_('层数:', p.level,
           'AP:', 1250 * (3 * p.level - 2) + 313 * (3 * p.level - 1))

    while p.prev_portal:
        print_(p, ' <- ', end='')
        plan_data += [gen_line(base1, p)]
        plan_data += [gen_line(base2, p)]
        p = p.prev_portal

    print_(p)
    plan_data += [gen_line(base1, p)]
    plan_data += [gen_line(base2, p)]
    print_(json.dumps(plan_data))


if __name__ == '__main__':
    ps = [Portal(*row) for row in csv.reader(open('portals.csv'))]
    base1 = ps[24]
    base2 = ps[47]
    ps.remove(base1)
    ps.remove(base2)
    calc_plan(base1, base2, ps)
