import pandas as pd
from dotenv import load_dotenv
import os
import base64
import json
import requests
from requests import post, get
from pprint import pprint
import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import ObjectId
import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns
# Sample user-genre interaction data
data = {
    'user_id': ['U1', 'U2', 'U3', 'Pseudo_User'],
    'Pop': [1, 0, 0, 1],
    'Rock': [1, 1, 0, 0],
    'Jazz': [0, 1, 1, 1],
    'Classical': [0, 0, 1, 0],
    'EDM': [0, 1, 0, 0]
}

# Convert to DataFrame
df = pd.DataFrame(data).set_index('user_id')


svd = TruncatedSVD(n_components=min(12, df.shape[1]-1))
svd.fit(df)

plt.figure(figsize=(8, 4))
plt.bar(
    range(1, len(svd.explained_variance_ratio_) + 1),
    svd.explained_variance_ratio_,
    color="#000080"  # Navy blueish purple
)
plt.xlabel('SVD Component')
plt.ylabel('Variance Ratio')
plt.title('Variance per SVD Component')
plt.grid(True)
plt.tight_layout()
plt.show()


# plt.figure(figsize=(8, 5))
# sns.heatmap(df, annot=True, cmap="Blues", cbar=True)
# plt.title("User-Genre Interaction Matrix")
# plt.xlabel("Genre")
# plt.ylabel("User")
# plt.tight_layout()
# plt.show()

# # 5. Genre Recommendation Count (Popularity)
# genre_counts = df.sum().sort_values(ascending=False)
# plt.figure(figsize=(8, 5))
# sns.barplot(x=genre_counts.values, y=genre_counts.index, palette=sns.light_palette('navy',reverse=True))
# plt.title("Genre Popularity Based on User Preferences")
# plt.xlabel("Number of Users")
# plt.ylabel("Genre")
# plt.tight_layout()
# plt.show()
