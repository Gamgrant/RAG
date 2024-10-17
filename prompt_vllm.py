from openai import OpenAI
from tqdm import tqdm
from utils import write_jsonl, extract_question_answers
from prompts import prompt_with_context, prompt_without_context
import fire



def prompt_vllm(model_name, questions, answers, contexts, api_base, params):
    api_key = "EMPTY"
    client = OpenAI(
        api_key=api_key,
        base_url=api_base)
    
    responses = []
    for i in tqdm(range(len(questions))):
        question = questions[i]
        context = contexts[i]
        answer = answers[i]
        prompt = prompt_with_context(question, context)
        
        try:
            response = client.completions.create(
                model=model_name,
                prompt=prompt,
                logprobs=False,
                stream=False,
                **params)

            responses.append({"question" : question, "response" : response.choices[0], "answer" : answer})

        except Exception as e:
            print(e)
    
    return responses

def main(model_name, port, temperature, top_p, max_tokens, question_answer_dir, output_dir):
    api_base = "http://localhost:%d/v1" % port
    params = {
        "temperature" : temperature,
        "top_p" : top_p,
        "max_tokens" : max_tokens,
    }

    questions, answers = extract_question_answers(question_answer_dir)
    contexts = ["" for _ in range(len(questions))]

    responses = prompt_vllm(model_name, questions, answers, contexts, api_base, params)

    write_jsonl(output_dir, responses)
    

if __name__ == '__main__':
    fire.Fire(main)

    