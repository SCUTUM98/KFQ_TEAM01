import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import math
from scipy.spatial import ConvexHull

def get_angle(point, center_x, center_y):
    x, y = point
    return math.atan2(y - center_y, x - center_x)

def create_polygon(poly_list):
    polygon = Polygon(poly_list)
    print(polygon)
    
    return polygon

# check coordinates order
# Is all points can be connected?
def check_polylist(poly_df):
    poly_list = []
    for i in range(len(poly_df)):
        new_points = [(poly_df['X1'][i], poly_df['Y1'][i]), (poly_df['X2'][i], poly_df['Y1'][i]), (poly_df['X1'][i], poly_df['Y2'][i]), (poly_df['X2'][i], poly_df['Y2'][i])]
        poly_list.extend(new_points)
    #print(f'poly_list: {len(poly_list)}')
    
    # Convex hull 생성
    hull = ConvexHull(poly_list)
    
    # 기준점 설정
    center_x, center_y = poly_list[hull.vertices[0]]
    #print(f'center: {center_x, center_y}')
    
    # 각도에 따라 점들을 시계 방향으로 정렬
    sorted_polygon = [poly_list[vertex] for vertex in hull.vertices]
    #sorted_polygon = sorted(hull.vertices, key=lambda vertex: get_angle(poly_list[vertex], center_x, center_y))
    #print(f'sorted_polygon: {len(sorted_polygon)}')
    #print(sorted_polygon)
    
    # 시계 방향으로 정렬된 정점을 가져옴
    #convex_hull_points = [poly_list[vertex] for vertex in sorted_polygon]
    #print(f'convex_hull_points: {len(convex_hull_points)}')
    
    #polygon = Polygon(convex_hull_points)
    polygon = Polygon(sorted_polygon)
    
    return polygon

def object_polylist(x1, y1, x2, y2):
    poly_list = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
    #print(f'poly_list: {len(poly_list)}')
    
    polygon = Polygon(poly_list)
    
    return polygon