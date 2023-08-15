def category(object_coords):
    object_coords['action_detection'] = 0
    object_coords['action_category'] = 'NaN'
    for i in range(len(object_coords)):        
        if object_coords['name'][i] == 'person':
            object_coords['action_detection'][i] = 1
            object_coords['action_caategory'][i] = 'person detected'
        else:
            continue
    return object_coords