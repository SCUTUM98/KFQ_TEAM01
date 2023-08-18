def category(object_coords):
    for i in range(len(object_coords)):        
        if object_coords['Class_Name'][i] == 'person':
            for j in range(len(object_coords)):
                if object_coords['Class_Name'][j] in ['bicycle', 'motorcycle']:
                    px1 = object_coords['X1'][i]
                    py1 = object_coords['Y1'][i]
                    px2 = object_coords['X2'][i]
                    py2 = object_coords['Y2'][i]
                    bx1 = object_coords['X1'][j]
                    by1 = object_coords['Y1'][j]
                    bx2 = object_coords['X2'][j]
                    by2 = object_coords['Y2'][j]
                    
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
                else:
                    object_coords.at[i, 'action_detection'] = 1
                    object_coords.at[i, 'action_category'] = 'person detected'
                    object_coords.at[i, 'event_type'] = 'P01'
        elif object_coords['Class_Name'][i] in ['fire', 'smoke', 'car fire']:
            object_coords.at[i, 'action_detection'] = 1
            if object_coords['Class_Name'][i] == 'fire':
                object_coords.at[i, 'action_category'] = 'fire detected'
                object_coords.at[i, 'event_type'] = 'F01'
            elif object_coords['Class_Name'][i] == 'smoke':
                object_coords.at[i, 'action_category'] = 'smoke detected'
                object_coords.at[i, 'event_type'] = 'F02'
            elif object_coords['Class_Name'][i] == 'car fire':
                object_coords.at[i, 'action_category'] = 'car fire detected'
                object_coords.at[i, 'event_type'] = 'F03'
        elif object_coords['Class_Name'][i] in ['cat', 'deer', 'dog', 'racoon', 'wild_boar']:
            object_coords.at[i, 'action_detection'] = 1
            if object_coords['Class_Name'][i] in ['cat', 'dog']:
                object_coords.at[i, 'action_category'] = 'animal detected(cat/dog)'
                object_coords.at[i, 'event_type'] = 'A01'
            elif object_coords['Class_Name'][i] == 'deer':
                object_coords.at[i, 'action_category'] = 'animal detected(deer/elk)'
                object_coords.at[i, 'event_type'] = 'A02'
            elif object_coords['Class_Name'][i] == 'racoon':
                object_coords.at[i, 'action_category'] = 'animal detected(racoon)'
                object_coords.at[i, 'event_type'] = 'A03'
            elif object_coords['Class_Name'][i] == 'wild_boar':
                object_coords.at[i, 'action_category'] = 'animal detected(wild_boar/pig)'
                object_coords.at[i, 'event_type'] = 'A04'
    return object_coords
