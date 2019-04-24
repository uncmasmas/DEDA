import json
import requests
import pandas as pd

def get_expectations_dataset():
    """
    Function to download expectations dataset.
    """

    with open('../datasets/2017-2c-introalgo-2c-2017.json', 'r+') as json_file:
            json_data = json.load(json_file)

    train_df = pd.io.json.json_normalize(json_data)
    expectations_lst = []
    base_url = 'https://bibliotheca-api.mumuki.io/guides/'

    slug_names = train_df['guide.slug'].drop_duplicates()
    for slug_name in slug_names:
        print('Extracting  {}'.format(str(slug_name)))
        resp = requests.get(base_url + str(slug_name)).json()
        expectations_lst.append(resp)

    with open('../datasets/expectations.json', 'w+') as fp:
        json.dump(expectations_lst, fp)
        print('Expectations extracted')


def calculate_distribution_percentage(df, column_name, exercise):
    """
    df: Dataframe with submissions
    column_name: column with status

    Function to obtain distribution of submissions status
    return metrics and amount of submissions
    """
    total_amount_submissions = df.shape[0]
    submissions_grouped = df.groupby([column_name]).size()
    metrics = {}
    metrics = submissions_grouped / total_amount_submissions
    metrics['exercise'] = str(exercise)
    metrics['submission_amount'] = total_amount_submissions
    return metrics


def weighted_mean(df, columns_to_mean, amount):
    """
    df: Dataframe with submissions
    columns_to_mean: columns to consider to be divided
    amount: pounded

    return add the weighted mean of status submission
    in the dataframe
    """
    df_mean = (df[columns_to_mean].astype(float).multiply(df[amount], axis="index")).sum()/(df[amount]).sum()
    df_mean['exercise'] = 'Weighted Mean'
    df_mean['submission_amount'] = df['submission_amount'].sum()
    df.loc[len(df)+1] = df_mean
    return df


def clean_submissions(submissions_df, to_train=False):
    """
    submissions_df: Dataframe with submissions
    to_train: indicate if dataframe will be use for training

    Function to cleaning dataset
    """
    submissions_df = submissions_df[~(submissions_df['status'] == 'aborted')]
    submissions_df = submissions_df[~(submissions_df['status'] == 'pending')]
    submissions_df = submissions_df[~(submissions_df['status'] == 'running')]
    submissions_df = submissions_df[~(submissions_df['status'] == 'manual_evaluation_pending')]
    
    if to_train:
            submissions_df = submissions_df[submissions_df['content'] != ""]
            submissions_df = submissions_df[~submissions_df['content'].isnull()]
    return submissions_df
