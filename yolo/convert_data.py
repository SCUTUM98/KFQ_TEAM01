import cv2
import pandas as pd

def collect_data(results, frame, mapping, results_df, captured_time):
    # Process the results and draw bounding boxes on the frame
    for detections in results:
        if detections is not None:
            for x1, y1, x2, y2, conf, cls in detections:
                # resize image size to 640x640
                input_size = (640,640)
                original_height, original_width, _ = frame.shape
                
                # coordinate correction cause img has resized to 640,640
                x1 = int(x1 * (original_width / input_size[0]))
                y1 = int(y1 * (original_height / input_size[1]))
                x2 = int(x2 * (original_width / input_size[0]))
                y2 = int(y2 * (original_height / input_size[1]))
                
                class_name = mapping[int(cls)]
                label = f"Class: {class_name}, Confidence: {conf:.2f}"
                color = (0, 0, 255)  # Green color for bounding box
                thickness = 3
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)
                
                # Append detection results to the DataFrame
                row = [captured_time, class_name, conf, x1, y1, x2, y2, 0, 'NaN', 'NaN']
                results_df.loc[len(results_df)] = row
                
    return results_df

def collect_coordinates(results, frame, mapping, road_coordinates, sidewalk_coordinates):
    for detections in results:
        if detections is not None:
            for x1, y1, x2, y2, conf, cls in detections:
                input_size = (640,640)
                original_height, original_width, _ = frame.shape
                x1 = int(x1 * (original_width / input_size[0]))
                y1 = int(y1 * (original_height / input_size[1]))
                x2 = int(x2 * (original_width / input_size[0]))
                y2 = int(y2 * (original_height / input_size[1]))
                
                class_name = mapping[int(cls)]
                
                if(class_name in ['car', 'truck', 'bus']):
                    row = [x1, y1, x2, y2, class_name]
                    road_coordinates.loc[len(road_coordinates)] = row
                elif(class_name == 'person'):
                    row = [x1, y1, x2, y2, class_name]
                    sidewalk_coordinates.loc[len(sidewalk_coordinates)] = row
                    
    return road_coordinates, sidewalk_coordinates