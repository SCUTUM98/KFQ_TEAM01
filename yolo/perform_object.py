from yolov5.utils.general import non_max_suppression

def perform_object(image_tensor, conf_thres, model):
    results = model.forward(image_tensor)[0]
    results = non_max_suppression(results, conf_thres=conf_thres)
    
    return results