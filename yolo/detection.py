def check_coordinates(x1,y1,x2,y2, road_coordinates):
    for i in range(len(road_coordinates)):
        rx1 = road_coordinates['X1'][i]
        ry1 = road_coordinates['Y1'][i]
        rx2 = road_coordinates['X2'][i]
        ry2 = road_coordinates['Y2'][i]
        state = 0
        
        if rx1 <= x1 <= rx2 and ry1 <= y1 <= ry2:
            state = 1
    
    return state

def category(object_coords, road_coordinates):
    for i in range(len(object_coords)):
        # set coordinates
        px1 = object_coords['X1'][i]
        py1 = object_coords['Y1'][i]
        px2 = object_coords['X2'][i]
        py2 = object_coords['Y2'][i]
        
        state = check_coordinates(px1, py1, px2, py2, road_coordinates) # check road boundary
        
        # if object is on the road
        if state == 1:
            if object_coords['Class_Name'][i] == 'person':
                for j in range(len(object_coords)):
                    # set coordinates
                    bx1 = object_coords['X1'][j]
                    by1 = object_coords['Y1'][j]
                    bx2 = object_coords['X2'][j]
                    by2 = object_coords['Y2'][j]

                    # bicycle and motocycle detection
                    if object_coords['Class_Name'][j] in ['bicycle', 'motorcycle']:
                        if bx1 <= px1 <= bx2 and by1 <= py1 <= by2:
                            object_coords.at[j, 'action_detection'] = 1
                            object_coords.at[j, 'action_category'] = f'{object_coords["Class_Name"][j]} detected with person'
                            if object_coords['Class_Name'][j] == 'bicycle':
                                object_coords.at[j, 'event_type'] = 'B01'
                            else:
                                object_coords.at[j, 'event_type'] = 'B02'
                        elif bx1 <= px2 <= bx2 and by1 <= py2 <= by2:
                            object_coords.at[j, 'action_detection'] = 1
                            object_coords.at[j, 'action_category'] = f'{object_coords["Class_Name"][j]} detected with person'
                            if object_coords['Class_Name'][j] == 'bicycle':
                                object_coords.at[j, 'event_type'] = 'B01'
                            else:
                                object_coords.at[j, 'event_type'] = 'B02'

                    # person detection which printed on vehicle
                    elif object_coords['Class_Name'][j] in ['car', 'truck', 'bus']:
                        if bx1 <= px1 <= bx2 and by1 <= py1 <= by2:
                            print('on the vehicle')
                            continue # nothing happened
                        elif bx1 <= px2 <= bx2 and by1 <= py2 <= by2:
                            print('on the vehicle')
                            continue # nothing happened

                    # person detected
                    else:
                        object_coords.at[i, 'action_detection'] = 1
                        object_coords.at[i, 'action_category'] = 'person detected'
                        object_coords.at[i, 'event_type'] = 'P01'

            # fire detected
            elif object_coords['Class_Name'][i] in ['fire', 'smoke', 'car fire']:
                object_coords.at[i, 'action_detection'] = 1
                
                # fire detected
                if object_coords['Class_Name'][i] == 'fire':
                    object_coords.at[i, 'action_category'] = 'fire detected'
                    object_coords.at[i, 'event_type'] = 'F01'
                
                # smoke detected
                elif object_coords['Class_Name'][i] == 'smoke':
                    object_coords.at[i, 'action_category'] = 'smoke detected'
                    object_coords.at[i, 'event_type'] = 'F02'
                
                # car fire detected
                elif object_coords['Class_Name'][i] == 'car fire':
                    object_coords.at[i, 'action_category'] = 'car fire detected'
                    object_coords.at[i, 'event_type'] = 'F03'

            # animals detected
            elif object_coords['Class_Name'][i] in ['cat', 'deer', 'dog', 'racoon', 'wild_boar']:
                object_coords.at[i, 'action_detection'] = 1
                # cat & dog detected
                if object_coords['Class_Name'][i] in ['cat', 'dog']:
                    object_coords.at[i, 'action_category'] = 'animal detected(cat/dog)'
                    object_coords.at[i, 'event_type'] = 'A01'
                
                # deer & elk detected
                elif object_coords['Class_Name'][i] == 'deer':
                    object_coords.at[i, 'action_category'] = 'animal detected(deer/elk)'
                    object_coords.at[i, 'event_type'] = 'A02'
                
                # racoon detected
                elif object_coords['Class_Name'][i] == 'racoon':
                    object_coords.at[i, 'action_category'] = 'animal detected(racoon)'
                    object_coords.at[i, 'event_type'] = 'A03'
                
                # wild boar & pig detected
                elif object_coords['Class_Name'][i] == 'wild_boar':
                    object_coords.at[i, 'action_category'] = 'animal detected(wild_boar/pig)'
                    object_coords.at[i, 'event_type'] = 'A04'
    
    return object_coords
