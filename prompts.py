# def prompt_without_context_few_shot(question):
#      prompt_template = """
# Answer the question in one sentence. Like the following examples.

# Here are the examples:

# Question: What state is Pittsburgh located in?
# Answer: Pittsburgh is located in Pennsylvania.

# Question: When was Carnegie Mellon University founded?
# Answer: Carnegie Mellon University was founded in 1900.

# Question: What is the name of Pittsburgh's football team?
# Answer: Pittsburgh Steelers

# Here is my question:

# Question: {}
# """.format(question)
#      return prompt_template

def prompt_without_context_few_shot(question):
     prompt_template = """
Answer my question in one sentence based on the following examples.

Here are the examples:

Question: What state is Pittsburgh located in?
Answer: Pittsburgh is located in Pennsylvania.

Question: When was Carnegie Mellon University founded?
Answer: Carnegie Mellon University was founded in 1900.

Question: What is the name of Pittsburgh's football team?
Answer: Pittsburgh Steelers

Please answer my question:

Question: {}
Answer:
"""
     return prompt_template

def prompt_without_context_zero_shot(question):
     prompt_template = """
Question: {}
Answer:
""".format(question)
     return prompt_template

def prompt_with_context_few_shot(question, context):
     prompt_template_context = """
Answer the question in one sentence based on the context below and the examples.

Here is the context:
{}

Here are the examples:

Question: What state is Pittsburgh located in?
Answer: Pittsburgh is located in Pennsylvania.

Question: When was Carnegie Mellon University founded?
Answer: Carnegie Mellon University was founded in 1900.

Question: What is the name of Pittsburgh's football team?
Answer: Pittsburgh Steelers

Here is my question:

Question: {}
""".format(question, context)
     return prompt_template_context

