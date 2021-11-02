import os

class Setup_Path: 

    labels = [
        'freshunripe',
        'freshripe',
        'unripe',
        'ripe',
        'overripe',
        'rotten'
    ]

    def files(self,pretrained_model_name, pretrained_model_url):
        files = {
          "LABELMAP":os.path.join(self.getWorkspaces()['ANNOTATIONS_PATH'], "label_map.pbtxt"),
          'TFRECORD_SCRIPT':os.path.join(self.getWorkspaces()['PREPROCESSING_PATH'], 'generate_tfrecord.py'),
          "PRETRAINED_MODEL_NAME": pretrained_model_name,
          "PRETRAINED_MODEL_URL": pretrained_model_url, 
          "PIPELINE_CONFIG": os.path.join("Tensorflow", "workspace", "my_model_zoo", "pipeline.config")
        }

        return files

    def getWorkspaces(self):
        paths = {
            "ADDONS_PATH":os.path.join("Tensorflow", "addons"),
            "LABEL_IMG_PATH":os.path.join("Tensorflow", "addons", "labeledImage"),
            "TFOD_API_PATH":"Tensorflow",
            "WORKSPACE_PATH":os.path.join("Tensorflow", "workspace"),
            "ANNOTATIONS_PATH":os.path.join("Tensorflow", "workspace", "annotations"),
            "IMAGES_PATH":os.path.join("Tensorflow", "workspace", "images"),
            "TRAINING_IMAGES_PATH":os.path.join("Tensorflow", "workspace", "images", "train"),
            "TESTING_IMAGES_PATH":os.path.join("Tensorflow", "workspace", "images", "test"),
            "EVALUATE_IMAGES_PATH":os.path.join("Tensorflow", "workspace", "images", "eval"),
            "PRETRAINED_MODELS_PATH":os.path.join("Tensorflow", "workspace", "pretrained_models"),
            "PREPROCESSED_IMAGE_PATH":os.path.join("Tensorflow", "addons", "preprocessedImage"),
            "ORIGINAL_IMAGES_PATH":os.path.join("Tensorflow", "addons", "originalImage"),   
            "PREPROCESSING_PATH":os.path.join("Tensorflow", "scripts", "preprocessing"),
            "PROTOS_PATH":os.path.join("Tensorflow", "Google-Protobuf"),
            'CHECKPOINT_PATH': os.path.join("Tensorflow", "workspace", 'my_model_zoo'),
            'TFJS_PATH':os.path.join('Tensorflow', 'workspace', 'my_model_zoo', 'tfjsexport'), 
            'TFLITE_PATH':os.path.join('Tensorflow', 'workspace','my_model_zoo', 'tfliteexport'),
            'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace','my_model_zoo', 'export'), 
        }

        return paths