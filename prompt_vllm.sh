#!/bin/bash
#SBATCH --job-name=rag_prompting
#SBATCH --output=rag_prompting.out
#SBATCH --error=rag_prompting.err
#SBATCH --mem=48G
#SBATCH --nodelist=babel-0-27
#SBATCH --time=15:00:00

MODEL_NAME="meta-llama/Meta-Llama-3-8B-Instruct"
PORT=8070
TEMPERATURE=0.8
TOP_P=0.95
MAX_TOKENS=128
QUESTION_ANSWER_DIR="./question_answers.txt"
OUTPUT_DIR="./rag_prompting_results.jsonl"

python3 prompt_vllm.py \
        --model_name $MODEL_NAME \
        --port $PORT \
        --temperature $TEMPERATURE \
        --top_p $TOP_P \
        --max_tokens $MAX_TOKENS \
        --question_answer_dir $QUESTION_ANSWER_DIR \
        --output_dir $OUTPUT_DIR \