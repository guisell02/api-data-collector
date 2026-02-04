from api_data_collector.collector.clients.api_client import ApiClient
from api_data_collector.collector.services.filters import filter_posts_by_user
from api_data_collector.collector.config.settings import POSTS_ENDPOINT

class DataService:
    """
    Provides business logic to process post data retrieved from the API client.
    """
    def __init__(self,api_client:ApiClient):
        """
            Initializes the service with an API client dependency.

            Args:
            api_client (ApiClient): Client responsible for HTTP communication.
        """
        self.api_client= api_client


    def get_post_titles_by_user(self,user_id:int)->list[str]:
        """
        Retrieve the search titles that correspond to user_id

        Args:
            user_id(int): Client number for find his information

        Returns:
            list[str]: A list contains titles of the user_id 
        """

        posts= self.api_client.get_json(POSTS_ENDPOINT)
        result= filter_posts_by_user(posts,user_id)
        return result



