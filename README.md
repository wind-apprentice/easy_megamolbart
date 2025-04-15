basic command to run megamolbart container:

docker run --rm -it --gpus all \
  -v ~/easy_megamolbart/zinc_example_data:/workspace/zinc_example_data \
  -v ~/easy_megamolbart/scripts:/workspace/scripts \
  -v ~/easy_megamolbart/results:/workspace/results \
  nvcr.io/nvidia/clara/megamolbart_v0.2:0.2.3 bash




how to preprocess data?

how to evaluate data using pretrained megamolbart?

python /opt/nvidia/nemo_chem/examples/chem/megamolbart_eval.py \
    --model_file /tmp/models/MegaMolBART_0_2_0.nemo \
    --prompt "CCO" \
    --tokens_to_generate 50



how to evaluate

important paths:
    model path: 
    