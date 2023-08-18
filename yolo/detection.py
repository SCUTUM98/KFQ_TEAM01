def category(object_coords):
    for i in range(len(object_coords)):        
        if object_coords['Class_Name'][i] == 'person': # detect person
            for j in range(len(object_coords)):
                if object_coords['Class_Name'][j] in ['bicycle', 'motorcycle']: # check person is riding bike or motorbike
                    # set coordinate of person and bike/motorbike
                    px1 = object_coords['X1'][i]
                    py1 = object_coords['Y1'][i]
                    px2 = object_coords['X2'][i]
                    py2 = object_coords['Y2'][i]
                    bx1 = object_coords['X1'][j]
                    by1 = object_coords['Y1'][j]
                    bx2 = object_coords['X2'][j]
                    by2 = object_coords['Y2'][j]
                    
                    # compare coordinate
                    if bx1 <= px1 <= bx2 and by1 <= py1 <= by2:
                        object_coords['action_detection'][j] = 1
                        object_coords['action_category'][j] = f'{object_coords["Class_Name"][j]} detected with person'
                        object_coords['event_type'][j] = 'B01'
                    elif bx1 <= px2 <= bx2 and by1 <= py2 <= by2:
                        object_coords['action_detection'][j] = 1
                        object_coords['action_category'][j] = f'{object_coords["Class_Name"][j]} detected with person'
                        object_coords['event_type'][j] = 'B01'
                    else:
                        continue
                else:
                    object_coords['action_detection'][i] = 1
                    object_coords['action_category'][i] = 'person detected'
                    object_coords['event_type'][i] = 'P01'
        elif object_coords['Class_Name'][i] in ['fire', 'smoke', 'car fire']:
            object_coords['action_detection'][i] = 1
            if object_coords['Class_Name'][i] == 'fire':
                object_coords['action_category'][i] = 'fire detected'
                object_coords['event_type'] = 'F01'
            elif object_coords['Class_Name'][i] == 'smoke':
                object_coords['action_category'][i] = 'smoke detected'
                object_coords['event_type'] = 'F02'
            elif object_coords['Class_Name'][i] == 'car fire':
                object_coords['action_category'][i] = 'car fire detected'
                object_coords['event_type'] = 'F03'
            else:
                continue
        elif object_coords['Class_Name'][i] in ['cat', 'deer', 'dog', 'racoon', 'wild_boar']:
            object_coords['action_detection'][i] = 1
            if object_coords['Class_Name'][i] in ['cat', 'dog']:
                object_coords['action_category'][i] = 'animal detected(cat/dog)'
                object_coords['event_type'] = 'A01'
            elif object_coords['Class_Name'][i] == 'deer':
                object_coords['action_category'][i] = 'animal detected(deer/elk)'
                object_coords['event_type'] = 'A02'
            elif object_coords['Class_Name'][i] == 'racoon':
                object_coords['action_category'][i] = 'animal detected(racoon)'
                object_coords['event_type'] = 'A03'
            elif object_coords['Class_Name'][i] == 'wild_boar':
                object_coords['action_category'][i] = 'animal detected(wild_boar/pig)'
                object_coords['event_type'] = 'A04'
            else:
                continue
        else:
            continue
    return object_coords