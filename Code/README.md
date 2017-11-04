# Deployment Classification

## Dependencies

Following python packages are expected:

1. scikit-learn (`pip install scikit-learn`)
2. Weighted-Levenshtein (`pip install weighted-levenshtein`)
3. tqdm (`pip install tqdm`)
4. Numpy
5. cPickle

## Instructions:

1. Collect traces using the scripts in `Deployment`.
2. Run `python classify.py`.
3. Reports will be saved as `model_1_results`, `model_2_results` and `model_3_results`.