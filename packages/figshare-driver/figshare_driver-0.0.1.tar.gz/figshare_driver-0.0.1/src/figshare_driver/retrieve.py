from typing import List
import requests
import pandas as pd


class FigshareMetrics:
    """
    Class to retrieve metrics for articles from Figshare.
    """

    def __init__(
        self,
        user: str,
        password: str,
        url: str,
        ids: List[int]
    ) -> None:
        self.username = user
        self.password = password
        self.url = url
        self.article_ids = ids

    def get_articles_views(self) -> pd:
        """
        Retrieve views metrics for a list of article IDs.

        Returns:
            pd.DataFrame: DataFrame containing article metrics.
        """
        counter = "views"
        full_url = f"{self.url}month/{counter}/article/"
        return self.get_articles_metrics(counter, full_url)

    def get_article_downloads(self) -> pd:
        """
        Retrieve downloads metrics for a list of article IDs.

        Returns:
            pd.DataFrame: DataFrame containing article metrics.
        """
        counter = "downloads"
        full_url = f"{self.url}month/{counter}/article/"
        return self.get_articles_metrics(counter, full_url)

    def get_article_shares(self):
        """
        Retrieve shares metrics for a list of article IDs.

        Returns:
            pd.DataFrame: DataFrame containing article metrics.
        """
        counter = "shares"
        full_url = f"{self.url}month/{counter}/article/"
        return self.get_articles_metrics(counter, full_url)

    def get_articles_metrics(self, counter: str, url: str) -> pd:
        """
        Download the metrics dynamically for each counter,
        for reference, see Endpoint format:
            https://docs.figshare.com/#stats_breakdown

        Args:
            counter (str): 'views', 'downloads' or 'shares'
            url (str): Url with all the parameters

        Returns:
            pandas frame: Metrics organized by ID and counter
        """
        data = []
        headers = {"Content-Type": "application/json"}

        for article_id in self.article_ids:
            full_url = f"{url}{article_id}"
            response = requests.get(
                full_url, auth=(self.username, self.password), headers=headers
            )
            if response.status_code == 200 and response.json()['breakdown']:
                data.append(
                    {
                        "measure": f"""
                            https://metrics.operas-eu.org/figshare/{counter}/v1
                        """,
                        "Article ID": article_id,
                        "Metrics": response.json(),
                    }
                )
            else:
                print(
                    f"""Failed to fetch article {article_id}.
                    Status code: {response.status_code}"""
                )
        return data


def fetch_report(
    base_url: str,
    username: str,
    password: str,
    article_ids: List
) -> List:
    """
    Fetch the views, downloads and shares by country and artice_id
    """
    figshare_metrics = FigshareMetrics(
        user=username, password=password, url=base_url, ids=article_ids
    )
    # Retrieve article metrics
    results = [
        figshare_metrics.get_articles_views(),
        figshare_metrics.get_article_downloads(),
        figshare_metrics.get_article_shares()
    ]

    return results
