def category(object_coords):
    object_coords['action'] = 'NaN'
    for i in range(len(object_coords)):        
        if object_coords['name'][i] == 'person':
            object_coords['action'][i] = 'person detected'
        else:
            continue
    return object_coords