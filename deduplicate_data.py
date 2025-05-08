import pandas as pd


def consolidate_by_product_title(group):
    consolidate = {}

    group["desc_len"] = group['product_summary'].apply(lambda x: len(str(x)) if pd.notna(x) else 0)
    main_row = group.loc[group['desc_len'].idxmax()]

    for col in group.columns:
        values = group[col].dropna()
        if values.empty:
            consolidate[col] = 'Information not found'
        elif col == 'product_summary':
            consolidate[col] = main_row[col]
        elif col == 'price':
            consolidate[col] = main_row[col]
        elif group[col].dtype == object:
            consolidate[col] = max(values, key=lambda x: len(str(x)))
        else:
            consolidate[col] = values.iloc[0]

    return pd.Series(consolidate)


file_path = "veridion_product_deduplication_challenge.snappy.parquet"

df = pd.read_parquet(file_path)
df = df.drop(columns=['manufacturing_year','page_url'])
df['product_title'] = df['product_title'].str.strip()


duplicates_pd = df[df.duplicated('product_title', keep=False)]

consolidated = duplicates_pd.groupby('product_title').apply(consolidate_by_product_title)
consolidated = consolidated.drop(columns=['desc_len'])
# consolidated.to_excel('output2.xlsx',index=False,engine='openpyxl')

df = df.drop_duplicates(subset='product_title',keep=False)

df = pd.concat([df,consolidated],ignore_index=True)

df = df.sort_values(by=['unspsc','product_title'])
# df.to_excel('output.xlsx',index=False,engine='openpyxl')

