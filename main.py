import argparse

from asts2vectors import asts2vectors
from sparse_transform import sparse_transform
from collect_statistic import collect_statistic
from normalize import normalize

parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with ASTs')
parser.add_argument('--output_folder', '-o', nargs=1, type=str,
                    help='output folder with files, which will contain ast_features and feature values as JSON')
parser.add_argument('--ast2vec_path', nargs=1, type=str, help='path to ast2vec repo')
parser.add_argument('--sparse_format', default='matrix', choices=['matrix', 'map'])
parser.add_argument('--all_features_file', nargs=1, type=str,
                    help='path to all_features file (in JSON) generated by asts2vectors stage')
parser.add_argument('-n', nargs='*', default=[1, 2, 3], help='n for collect n-grams statistic')
parser.add_argument('--stage', '-s', choices=['asts2vectors', 'sparse_transformation', 'normalize', 'collect_statistic'])
args = parser.parse_args()

input_folder = args.input_folder[0]
output_folder = args.output_folder[0]
stage = args.stage

if stage == 'asts2vectors':
    ast2vec_path = args.ast2vec_path[0]
    asts2vectors(input_folder, output_folder, ast2vec_path)
elif stage == 'sparse_transformation':
    sparse_format = args.sparse_format[0]
    all_features_file = args.all_features_file[0]
    sparse_transform(input_folder, output_folder, all_features_file, sparse_format)
elif stage == 'normalize':
    all_features_file = args.all_features_file[0]
    normalize(input_folder, output_folder, all_features_file)
elif stage == 'collect_statistic':
    all_features_file = args.all_features_file[0]
    n = args.n
    collect_statistic(output_folder, all_features_file, n)
