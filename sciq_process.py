import json
import os
import random

from special_tokens import tokens_set


def convert_to_text(json_path_dir: str) -> None:
    samples = []
    with open(os.path.join(os.getcwd(), json_path_dir, 'test.json')) as content:
        json_sciq = json.loads(content.read())
 
    for item in json_sciq:
        for i in range(1, 4):
            sample_string = ' '.join([
                tokens_set['support_token'],
                item['support'],
                tokens_set['question_token'],
                item['question'],
                tokens_set['key_token'],
                item['correct_answer'],
                tokens_set['distractor_token'],
                item[f'distractor{i}'],
                '<|endoftext|>',
            ])

            samples.append(sample_string.strip())

    random.shuffle(samples)

    with open(os.path.join(os.getcwd(), json_path_dir, 'test.txt'), 'w') as f:
        f.write('\n'.join(samples))

convert_to_text('sciq')