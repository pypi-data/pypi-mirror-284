from pandas import util
import numpy as np
import pandas as pd

n_rows = 100000
n_classes = 500
df = pd.DataFrame(
    {
        "A_numeric": np.random.rand(n_rows),
        "B_numeric": np.random.rand(n_rows),
        "C_categorical": np.random.randint(n_classes, size=n_rows),
        "D_categorical": np.random.randint(n_classes, size=n_rows),
    }
)


from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from chunkdot import CosineSimilarityTopK

numeric_features = ["A_numeric", "B_numeric"]
numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])

categorical_features = ["C_categorical", "D_categorical"]
categorical_transformer = Pipeline(steps=[("encoder", OneHotEncoder())])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

cos_sim = CosineSimilarityTopK(top_k=50)

pipe = Pipeline(steps=[("preprocessor", preprocessor), ("cos_sim", cos_sim)])
pipe.fit_transform(df)
