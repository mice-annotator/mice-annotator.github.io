import os
import json
import argparse
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--images_path', default = './images/')
    parser.add_argument('--inputs_path', default = './inputs/')
    parser.add_argument('--tokens_path', default = './inputs.txt')
    parser.add_argument('--tasks_per_input', default = 20, type = int)
    args = parser.parse_args()

    if not os.path.exists(args.inputs_path):
        os.makedirs(args.inputs_path)

    image_paths = os.listdir(args.images_path)

    tasks = []
    for image_path in sorted(image_paths):
        image_path = os.path.join(args.images_path, image_path)
        tasks.append({
            'image_path': image_path
        })

    np.random.seed(0)
    np.random.shuffle(tasks)

    inputs = []
    for k, l in enumerate(range(0, len(tasks), args.tasks_per_input)):
        r = min(l + args.tasks_per_input, len(tasks))
        inputs.append(tasks[l:r])

    for k, input in enumerate(inputs):
        input_path = os.path.join(args.inputs_path, '{:08d}.json'.format(k + 1))
        json.dump(input, open(input_path, 'w'))

    input_paths = os.listdir(args.inputs_path)

    with open(args.tokens_path, 'w') as fp:
        print('input', file = fp)
        for input_path in sorted(input_paths):
            input_path = os.path.join(args.inputs_path, input_path)
            print(input_path, file = fp)

