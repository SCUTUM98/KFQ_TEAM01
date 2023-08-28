import pandas as pd
from shapely.geometry import Point
from create_polygon import object_polylist

def check_polygon(polygon, object_coords):
    x1_list = object_coords['X1'].tolist()
    y1_list = object_coords['Y1'].tolist()
    x2_list = object_coords['X2'].tolist()
    y2_list = object_coords['Y2'].tolist()

    corners = []
    for x1, y1, x2, y2 in zip(x1_list, y1_list, x2_list, y2_list):
        corners.append((x1, y1))
        corners.append((x1, y2))
        corners.append((x2, y1))
        corners.append((x2, y2))
    for corner in corners:
        x, y = corner
        if polygon.contains(Point(x, y)):
            return 1
    
    return 0

def polygon_contains(polygon, x1, y1, x2, y2):
    corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
    
    for corner in corners:
        x, y = corner
        if polygon.contains(Point(x, y)):
            return 1
    return 0

def category(object_coords, polygon):
    human_detect = ['P01']
    bike_detect = ['B01', 'B02']
    fire_detect = ['F01', 'F02', 'F03']
    animal_detect = ['A01', 'A02', 'A03', 'A04']
    obstacle_detect = ['S01', 'S02', 'S03', 'S04', 'S05']
    
    for i in range(len(object_coords)):
        # set coordinates
        px1 = object_coords['X1'][i]
        py1 = object_coords['Y1'][i]
        px2 = object_coords['X2'][i]
        py2 = object_coords['Y2'][i]
        
        state = check_polygon(polygon, object_coords)
        #state = check_coordinates(px1, py1, px2, py2, road_coordinates)
        print(f'state: {state}')
        
        # if object is on the road
        if state == 1:
            if object_coords['Class_Name'][i] == 'person':
                for j in range(len(object_coords)):
                    # set coordinates
                    bx1 = object_coords['X1'][j]
                    by1 = object_coords['Y1'][j]
                    bx2 = object_coords['X2'][j]
                    by2 = object_coords['Y2'][j]
                    
                    tmp_polygon = object_polylist(bx1, by1, bx2, by2)
                    is_combine = polygon_contains(tmp_polygon, px1, py1, px2, py2)
                    # bicycle and motocycle detection
                    if object_coords['Class_Name'][j] in ['bicycle', 'motorcycle']:
                        if is_combine == 1:
                            object_coords.at[j, 'action_detection'] = 1
                            object_coords.at[j, 'action_category'] = f'{object_coords["Class_Name"][j]} detected with person'
                            if object_coords['Class_Name'][j] == 'bicycle':
                                object_coords.at[j, 'event_type'] = bike_detect[0]
                            else:
                                object_coords.at[j, 'event_type'] = bike_detect[1]
                        else:
                            continue

                    # person detection which printed on vehicle
                    elif object_coords['Class_Name'][j] in ['car', 'truck', 'bus']:
                        if is_combine == 1:
                            print('on the vehicle')
                            continue # nothing happened
                        else:
                            continue

                    # person detected
                    else:
                        object_coords.at[i, 'action_detection'] = 1
                        object_coords.at[i, 'action_category'] = 'person detected'
                        object_coords.at[i, 'event_type'] = human_detect[0]

            # fire detected
            elif object_coords['Class_Name'][i] in ['fire', 'smoke', 'car fire']:
                object_coords.at[i, 'action_detection'] = 1
                
                # fire detected
                if object_coords['Class_Name'][i] == 'fire':
                    object_coords.at[i, 'action_category'] = 'fire detected'
                    object_coords.at[i, 'event_type'] = fire_detect[0]
                
                # smoke detected
                elif object_coords['Class_Name'][i] == 'smoke':
                    object_coords.at[i, 'action_category'] = 'smoke detected'
                    object_coords.at[i, 'event_type'] = fire_detect[1]
                
                # car fire detected
                elif object_coords['Class_Name'][i] == 'car fire':
                    object_coords.at[i, 'action_category'] = 'car fire detected'
                    object_coords.at[i, 'event_type'] = fire_detect[2]

            # animals detected
            elif object_coords['Class_Name'][i] in ['cat', 'deer', 'dog', 'racoon', 'wild_boar']:
                object_coords.at[i, 'action_detection'] = 1
                # cat & dog detected
                if object_coords['Class_Name'][i] in ['cat', 'dog']:
                    object_coords.at[i, 'action_category'] = 'animal detected(cat/dog)'
                    object_coords.at[i, 'event_type'] = animal_detect[0]
                
                # deer & elk detected
                elif object_coords['Class_Name'][i] == 'deer':
                    object_coords.at[i, 'action_category'] = 'animal detected(deer/elk)'
                    object_coords.at[i, 'event_type'] = animal_detect[1]
                
                # racoon detected
                elif object_coords['Class_Name'][i] == 'racoon':
                    object_coords.at[i, 'action_category'] = 'animal detected(racoon)'
                    object_coords.at[i, 'event_type'] = animal_detect[2]
                
                # wild boar & pig detected
                elif object_coords['Class_Name'][i] == 'wild_boar':
                    object_coords.at[i, 'action_category'] = 'animal detected(wild_boar/pig)'
                    object_coords.at[i, 'event_type'] = animal_detect[3]
            
            # obstacle detected
            elif object_coords['Class_Name'][i] in ['tree', 'rock', 'box', 'tire', 'drum']:
                object_coords.at[i, 'action_detection'] = 1
                # tree detected
                if(object_coords['Class_Name'][i] == 'tree'):
                    object_coords.at[i, 'action_category'] = 'obstacle detected(tree)'
                    object_coords.at[i, 'event_type'] = obstacle_detect[0]
                
                # rock detected
                elif(object_coords['Class_Name'][i] == 'rock'):
                    object_coords.at[i, 'action_category'] = 'obstacle detected(rock)'
                    object_coords.at[i, 'event_type'] = obstacle_detect[1]
                
                elif(object_coords['Class_Name'][i] in ['tree', 'box', 'tire', 'drum']):
                    for j in range(len(object_coords)):
                        bx1 = object_coords['X1'][j]
                        by1 = object_coords['Y1'][j]
                        bx2 = object_coords['X2'][j]
                        by2 = object_coords['Y2'][j]
                        
                        tmp_polygon = object_polylist(bx1, by1, bx2, by2)
                        is_combine = polygon_contains(tmp_polygon, px1, py1, px2, py2)
                        print(f'tire on vehicle: {is_combine}')
                        
                        if object_coords['Class_Name'][j] in ['car', 'truck', 'bus', 'bicycle', 'motorcycle']:
                            if is_combine == 1:
                                print('on the vehicle')
                                continue # nothing happened
                        else:
                            # tree detected
                            if(object_coords['Class_Name'][i] == 'tree'):
                                object_coords.at[i, 'action_category'] = 'obstacle detected(tree)'
                                object_coords.at[i, 'event_type'] = obstacle_detect[0]
                            
                            # box detected
                            elif(object_coords['Class_Name'][i] == 'box'):
                                object_coords.at[i, 'action_category'] = 'obstacle detected(box)'
                                object_coords.at[i, 'event_type'] = obstacle_detect[2]
                            
                            # tire detected
                            elif(object_coords['Class_Name'][i] == 'tire'):
                                object_coords.at[i, 'action_category'] = 'obstacle detected(tire)'
                                object_coords.at[i, 'event_type'] = obstacle_detect[3]
                
                            # drum detected
                            elif(object_coords['Class_Name'][i] == 'drum'):
                                object_coords.at[i, 'action_category'] = 'obstacle detected(drum)'
                                object_coords.at[i, 'event_type'] = obstacle_detect[4]
                                
                            else:
                                continue    
    return object_coords
