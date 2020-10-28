import argparse
from modules import Read_folder
from modules import apis
from modules import ex_job_description
from modules import gathering_cleaning

def argument_parser():
    parser = argparse.ArgumentParser(description='Job position and api key..')
    parser.add_argument("-p", "--path", type = str, help='specify the company and Job position...', required=True)
    parser.add_argument("-k", "--key", type=str, help='specify API key...', required=True)
    args = parser.parse_args()

    return args


def main():
    print('hi')

if __name__ == '__main__':
    arguments = argument_parser()
    print(arguments.path)
    print(arguments.key)