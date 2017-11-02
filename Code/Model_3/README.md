# Model 3 - SVMs using Damerau-Levenshtein distance based kernel (single size pkt)

## Instructions

1. Place traces of websites at `../../Datasets/Full Dataset/`.
2. Modify the self-ip prefix in `compute_vectors.py`.
3. Run `python compute_vectors.py`. Dataset will be saved as `dataset`.
4. Run `python train_model.py`. 
5. Avg accuracy after 4-fold cross-validation will be reported and model will be saved as `model_3.pkl`. 