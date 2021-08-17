#!/bin/bash
set -eux
MODEL=$1
if [ -z ${MODEL} ]; then 
	echo "Usage:  ./generate_tflite.sh <model_name>"; 
	exit;
fi

MODELDIR="/home/harshad/Developer/tflite"
echo "Downloading ${MODEL}..."
wget "http://download.tensorflow.org/models/object_detection/${MODEL}.tar.gz" \
        -O "${MODELDIR}/${MODEL}.tar.gz";
PYTHONPATH="/home/harshad/Developer/tensorflow/models/research"
cd /home/harshad/Developer/tensorflow/models/research;
tar xf "${MODELDIR}/${MODEL}.tar.gz"
python3.6 object_detection/export_tflite_ssd_graph.py \
        --pipeline_config_path=${MODEL}/pipeline.config \
        --trained_checkpoint_prefix=${MODEL}/model.ckpt \
        --output_directory=${MODELDIR}/${MODEL} \
        --add_postprocessing_op=true
cd "${MODELDIR}/${MODEL}"
tflite_convert --graph_def_file=tflite_graph.pbtxt \
        --inference_type=FLOAT \
        --input_arrays=normalized_input_image_tensor \
        --output_arrays='TFLite_Detection_PostProcess',\
            'TFLite_Detection_PostProcess:1',\
            'TFLite_Detection_PostProcess:2',\
            'TFLite_Detection_PostProcess:3' \
        --allow_custom_ops \
        --input_shapes=1,300,300,3 \
        --output_file=${MODEL}.tflite
echo "Done. TF Lite model saved to ${MODELDIR}/${MODEL}/${MODEL}.tflite"
