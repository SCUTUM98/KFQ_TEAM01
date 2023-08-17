def category(object_coords):
    object_coords['action_detection'] = 0
    object_coords['action_category'] = 'NaN'
    for i in range(len(object_coords)):        
        if object_coords['name'][i] == 'person':
            object_coords['action_detection'][i] = 1
            object_coords['action_category'][i] = 'person detected'
        elif object_coords['name'][i] == 'Fire':
            object_coords['action_detection'][i] = 1
            object_coords['action_category'][i] = 'fire detected'
        elif object_coords['name'][i] == 'Cat' or 'Deer' or 'Dog' or 'Racoon' or 'WildBoar':
            object_coords['action_detection'][i] = 1
            object_coords['action_category'][i] = f'animal detected({object_coords["name"][i]})'
        else:
            continue
    return object_coords