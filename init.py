from composio import Composio, Action
from decouple import config

client = Composio(config("composio_api_key")) 

integration = client.get_integration(config("integration_id"))

connected_account = integration.initiate_connection(entity_id = None)

print("Complete the auth flow, link: ", connected_account.redirectUrl)


connected_account = connected_account.wait_until_active(timeout=60)

about_user = connected_account.execute_action(action_name=Action.GITHUB_GET_ABOUT_ME, params={})
github_repos = connected_account.execute_action(action_name=Action.GITHUB_LIST_GITHUB_REPOS, params={})

print(about_user, github_repos)