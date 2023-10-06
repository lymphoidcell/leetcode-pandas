import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    author_read_its_own = views[views['author_id'] == views['viewer_id']]
    unique_value = author_read_its_own['author_id'].unique()
    unique_value = sorted(unique_value)

    id = pd.DataFrame({'id': unique_value})

    return id
