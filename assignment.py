import pandas as pd
import numpy as np
df=pd.read_json('domainTags2.json')
df.info()
df.head()


def get_competitors_by_domain(domain_name):
    # Get the rows that match the domainName
    domain_df = df[df['domainName'] == domain_name]
    
    if domain_df.empty:
        # If no companies match the domainName, return an empty list
        return []
    
    # Get the tags for the domain
    domain_tags = domain_df.iloc[0]['tags']
    
    # Find all companies with tags that intersect with the domain tags
    tag_matches = df[df['tags'].apply(lambda x: bool(set(x) & set(domain_tags)))]
    
    # Get the companyNames for the matches
    competitors = list(tag_matches['companyName'].unique())
    
    # Remove the original company name from the list of competitors
    company_name = domain_df.iloc[0]['companyName'][0]
    if company_name in competitors:
        competitors.remove(company_name)
    
    return competitors

competitors = get_competitors_by_domain('embedded')
print(competitors)