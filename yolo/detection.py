def category(object_coords):
    for i in range(len(object_coords)):        
        if object_coords['Class_Name'][i] == 'person':
            object_coords['action_detection'][i] = 1
            object_coords['action_category'][i] = 'person detected'
        elif object_coords['Class_Name'][i] == 'Fire':
            object_coords['action_detection'][i] = 1
            object_coords['action_category'][i] = 'fire detected'
        elif object_coords['Class_Name'][i] in ['cat', 'deer', 'dog', 'racoon', 'wild_boar']:
            object_coords['action_detection'][i] = 1
            object_coords['action_category'][i] = f'animal detected({object_coords["Class_Name"][i]})'
        else:
            continue
    return object_coords