cd D:\files on D\documenten\privé\studie en verenigingen\Business Analytics and Quantitative Marketing\thesis\cloudcomputing google-drive\gekopieerd van PC\object_detection

ECHO %PIPELINE_CONFIG_PATH%
ECHO %MODEL_DIR%
ECHO %NUM_TRAIN_STEPS%
ECHO %SAMPLE_1_OF_N_EVAL_EXAMPLES%

SET PIPELINE_CONFIG_PATH='Martijn/multitude of possible detectors/model1/pipeline.config'
SET MODEL_DIR='Martijn/multitude of possible detectors/model1/train'
SET NUM_TRAIN_STEPS=50000
SET SAMPLE_1_OF_N_EVAL_EXAMPLES=1

python model_main.py ^
    --pipeline_config_path="Martijn\multitude of possible detectors\model1\pipeline.config" ^
    --model_dir="Martijn\multitude of possible detectors\model1\train" ^
    --num_train_steps=50000 ^
    --sample_1_or_n_eval_examples=1 ^
    --alsologtostderr

or

PIPELINE_CONFIG_PATH='Martijn/multitude of possible detectors/model1/pipeline.config'
MODEL_DIR='Martijn/multitude of possible detectors/model1/train'
NUM_TRAIN_STEPS=50000
SAMPLE_1_OF_N_EVAL_EXAMPLES=1

python model_main.py \
    --pipeline_config_path=PIPELINE_CONFIG_PATH \
    --model_dir=MODEL_DIR \
    --num_train_steps=NUM_TRAIN_STEPS \
    --sample_1_or_n_eval_examples=SAMPLE_1_OF_N_EVAL_EXAMPLES \
    --alsologtostderr
