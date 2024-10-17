import json
import os
import gzip

def write_jsonl(filename, data, append = False):
    """
    Writes an iterable of dictionaries to jsonl
    """
    if append:
        mode = 'ab'
    else:
        mode = 'wb'
    filename = os.path.expanduser(filename)
    if filename.endswith(".gz"):
        with open(filename, mode) as fp:
            with gzip.GzipFile(fileobj=fp, mode='wb') as gzfp:
                for x in data:
                    gzfp.write((json.dumps(x) + "\n").encode('utf-8'))
    else:
        with open(filename, mode) as fp:
            for x in data:
                fp.write((json.dumps(x) + "\n").encode('utf-8'))

def extract_question_answers(question_answer_dir):
    with open(question_answer_dir) as file:
        questions = [line.rstrip() for line in file if line.startswith("Q:")]
    with open(question_answer_dir) as file:
        answers = [line.rstrip() for line in file if line.startswith("A:")]
    return questions, answers