import os
import json
from typing import List, Dict

class LabelMe:
    def __init__(self):
        pass

    def convert_to_lb(self, input_files: List[str], ontology_mapping: Dict[str, str], image_mapping: Dict[str, str]) -> List[Dict]:
        """
        Convert LabelMe JSON files to Labelbox NDJSON format.
        
        :param input_files: List of LabelMe JSON file paths to be converted.
        :param ontology_mapping: Dictionary mapping LabelMe class names to Labelbox class names.
        :param image_mapping: Dictionary mapping LabelMe filenames to Labelbox globalKeys.
        :return: List of dictionaries in NDJSON format.
        """
        ndjson_data = []

        for json_file in input_files:
            with open(json_file, 'r') as file:
                data = json.load(file)
                
            filename = data['imagePath']
            global_key = image_mapping.get(filename)

            if not global_key:
                print(f"No global key found for {filename}, skipping this file.")
                continue

            for shape in data['shapes']:
                shape_type = shape['shape_type']
                label = shape['label']
                mapped_label = ontology_mapping.get(label, label)
                points = shape['points']
                flags = shape.get('flags', {})

                if shape_type == "rectangle":
                    xmin = min(point[0] for point in points)
                    ymin = min(point[1] for point in points)
                    xmax = max(point[0] for point in points)
                    ymax = max(point[1] for point in points)
                    bbox = {
                        'top': ymin,
                        'left': xmin,
                        'height': ymax - ymin,
                        'width': xmax - xmin
                    }
                    annotation = {
                        'name': 'bounding_box',
                        'bbox': bbox,
                        'dataRow': {'globalKey': global_key},
                        'classifications': [{'value': k} for k, v in flags.items() if v]
                    }
                    ndjson_data.append(annotation)
                elif shape_type == "polygon":
                    annotation = {
                        'name': 'polygon',
                        'polygon': {
                            'points': points
                        },
                        'dataRow': {'globalKey': global_key},
                        'classifications': [{'value': k} for k, v in flags.items() if v]
                    }
                    ndjson_data.append(annotation)
                elif shape_type == "point":
                    annotation = {
                        'name': 'point',
                        'point': {
                            'x': points[0][0],
                            'y': points[0][1]
                        },
                        'dataRow': {'globalKey': global_key},
                        'classifications': [{'value': k} for k, v in flags.items() if v]
                    }
                    ndjson_data.append(annotation)

        return ndjson_data

    def convert_from_lb(self, data_row_json: List[Dict]) -> str:
        """
        Convert Labelbox NDJSON data to LabelMe JSON format.
        
        :param data_row_json: List of dictionaries in NDJSON format.
        :return: A string representing LabelMe JSON format.
        """
        labelme_data = {}

        for data_row in data_row_json:
            global_key = data_row['dataRow']['globalKey']
            labelme_data.setdefault('imagePath', global_key)
            labelme_data.setdefault('shapes', [])
            shape = {}

            if data_row['name'] == 'bounding_box':
                bbox = data_row['bbox']
                points = [
                    [bbox['left'], bbox['top']],
                    [bbox['left'] + bbox['width'], bbox['top']],
                    [bbox['left'] + bbox['width'], bbox['top'] + bbox['height']],
                    [bbox['left'], bbox['top'] + bbox['height']]
                ]
                shape = {
                    'label': data_row['name'],
                    'points': points,
                    'shape_type': 'rectangle',
                    'flags': {c['value']: True for c in data_row.get('classifications', [])}
                }
            elif data_row['name'] == 'polygon':
                shape = {
                    'label': data_row['name'],
                    'points': data_row['polygon']['points'],
                    'shape_type': 'polygon',
                    'flags': {c['value']: True for c in data_row.get('classifications', [])}
                }
            elif data_row['name'] == 'point':
                shape = {
                    'label': data_row['name'],
                    'points': [[data_row['point']['x'], data_row['point']['y']]],
                    'shape_type': 'point',
                    'flags': {c['value']: True for c in data_row.get('classifications', [])}
                }
            
            labelme_data['shapes'].append(shape)
        
        labelme_data['flags'] = {}
        labelme_data['imageData'] = None
        labelme_data['imageHeight'] = None
        labelme_data['imageWidth'] = None

        return json.dumps(labelme_data, indent=4)

