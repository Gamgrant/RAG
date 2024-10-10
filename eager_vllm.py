from prompts import prompt_without_context_zero_shot, prompt_without_context_few_shot
from utils import write_jsonl, extract_question_answers
from vllm import LLM, SamplingParams
from tqdm import tqdm
import re

def eager_vllm(model, res_dir, qa_dir, num_gpus, temperature, max_tokens, top_p):
    llm = LLM(model, tensor_parallel_size = num_gpus)
    sampling_params = SamplingParams(temperature = temperature, max_tokens = max_tokens, top_p = top_p)

    questions, answers = extract_question_answers(qa_dir)
    assert len(questions) == len(answers)
    res = []
    for question, answer in tqdm(zip(questions, answers)):
        prompt = prompt_without_context_zero_shot(question)
        outputs = llm.generate(prompt, sampling_params=sampling_params, use_tqdm = False)
        response = outputs[0].outputs[0].text
        res.append({'question' : question, 'response' : response, 'answer' : answer})

    write_jsonl(res_dir, res)

if __name__ == '__main__':
    model = "deepseek-ai/deepseek-llm-7b-chat"
    res_dir = './deepseek7B_results.jsonl'
    qa_dir = '/home/rrsood/RAG/question_answers.txt'
    num_gpus = 1
    temperature = 1
    max_tokens = 128
    top_p = 0.95
    
    eager_vllm(model, res_dir, qa_dir, num_gpus, temperature, max_tokens, top_p)
        