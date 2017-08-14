import csv
import matplotlib.path as mplPath
import numpy as np
import json
        
class portal:
    def __init__(self,name, lat, lon):
        self.name = name
        self.lat = float(lat)-40
        self.lon = float(lon)-116
    def __repr__(self):
        return '{}'.format(self.name)
    def __str__(self):
        return '{}'.format(self.name)

class field:
    def __init__(self,base1,base2,end):
        self.base1 = base1
        self.base2 = base2
        self.end = end
        self._portal_list = [base1,base2,end]
    def __repr__(self):
        return '<Field {}, {}, {}>'.format(self.base1, self.base2, self.end)
    def contains_portal(self,portal):
        verts = []
        for item in self._portal_list:
            verts += [[item.lat,item.lon]]
        bbPath = mplPath.Path(np.array(verts))
        if bbPath.contains_point(np.array([portal.lat,portal.lon])):
            return True
    def contains_portals(self,portal_list):
        portals_in_triangle = []
        for item in portal_list:
            if self.contains_portal(item) and self.end.name != item.name:
                portals_in_triangle += [item]
        return portals_in_triangle
    def best_subfield(self,portal_list):
        subfield_contains_number = 0
        # 设置最优field顶点为候选po列表第一位
        best_end = portal_list[0]
        portals_in_best_field = []
        for portal in portal_list:
            if not self.contains_portal(portal): continue
            new_field = field(self.base1,self.base2, portal)
            portal_in_field = new_field.contains_portals(portal_list)
            if len(portal_in_field) > subfield_contains_number:
                subfield_contains_number = len(portal_in_field)
                best_end = portal
                portals_in_best_field = portal_in_field
        return (field(self.base1,self.base2,best_end), portals_in_best_field)

class best_plan:
    def __init__(self,base1,base2,end,portal_list):
        self.base1 = base1
        self.base2 = base2
        self.end = end
        self._starter_field = field(base1,base2,end)
        self._portal_list = portal_list
        self.waypoints = [end]
        self.total_ap = 0
        self.total_field = 0
        self.total_link = 0
    def calculate(self):
        calculate_result = self._starter_field.best_subfield(self._portal_list)
        (self._starter_field,self._portal_list) =calculate_result
        self.waypoints += [self._starter_field.end]
        if len(self._portal_list) > 0:
        # 如果计算出来是有结果的，而且field下面还有候选po，递归查找子field
            self.calculate()

        else:
            self.waypoints.reverse()
            self.total_link = 3 * (len(self.waypoints) + 1)
            self.total_field = 3 * len(self.waypoints) + 1
            self.total_ap = 313 * self.total_link + 1250 * self.total_field
    def _get_line(self,portal1,portal2):
        return {'color':'#a24ac3',
            'type':'polyline',
            'latLngs': [
                {'lat':portal1.lat+40,'lng':portal1.lon+116},
                {'lat':portal2.lat+40,'lng':portal2.lon+116},
                    ]}
    def print_result(self):
        plan_dict = [self._get_line(self.base1,self.base2)]
        for point in self.waypoints:
            plan_dict += [self._get_line(self.base1,point)]
            plan_dict += [self._get_line(self.base2,point)]
        print("""计算完成，路点总数{}, 路点如下{},总AP {}
{}
        """.format(len(self.waypoints),self.waypoints,self.total_ap,json.dumps(plan_dict)))

            
        
        
def is_portal_in_field(portal,field):
    """https://stackoverflow.com/questions/2049582/how-to-determine-if-a-point-is-in-a-2d-triangle
    float sign (fPoint p1, fPoint p2, fPoint p3)
    {
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
    }
    
    bool PointInTriangle (fPoint pt, fPoint v1, fPoint v2, fPoint v3)
    {
        bool b1, b2, b3;
    
        b1 = sign(pt, v1, v2) < 0.0f;
        b2 = sign(pt, v2, v3) < 0.0f;
        b3 = sign(pt, v3, v1) < 0.0f;
    
        return ((b1 == b2) && (b2 == b3));
    }
    """
    return field.contains_portal(portal)

def get_portal_by_name(name,portal_list):
    id = 0
    for item in portal_list:
        if item.name == name:
            item = portal_list.pop(id)
            return item, portal_list
        id += 1
    raise NameError('{} portal not found'.format(name))

if __name__ == '__main__':
    BASE1 = '新华门'
    BASE2 = '国家大剧院'
    END = '天安门广场－远眺国家博物馆'
    portals = []
    with open('portals.csv','r',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader :
            data = {
                    'name':row[0],
                    'lat':row[1],
                    'lon':row[2],
                    }
            new_portal = portal(**data)
            portals += [new_portal]
            
    (BASE1, portals) = get_portal_by_name(BASE1,portals)
    (BASE2, portals) = get_portal_by_name(BASE2,portals)
    (best_end, portals) = get_portal_by_name(END,portals)
#    这一段代码在尝试找一个能盖住最多po的field，但并不实用，可以直接指定一个po
#    best_end = None
#    most_portal_in_field = 0
#    for portal in portals :
#        largest_field = field(BASE1,BASE2,portal)
#        portal_number_in_field = len(largest_field.contains_portals(portals))
#        if portal_number_in_field > most_portal_in_field:
#            best_end = portal
#            most_portal_in_field = portal_number_in_field
    new_best_plan = best_plan(BASE1,BASE2,best_end, portals)
    new_best_plan.calculate()
    new_best_plan.print_result()
    # print(len(IN_CIRCLE))
