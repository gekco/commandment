from collections.abc import Iterator
from typing import Union, List, Dict
import requests
from requests.auth import AuthBase
from requests_oauthlib import OAuth1
import re
from datetime import timedelta, datetime
from .exceptions import DEPError
from enum import Enum
from email.utils import parsedate  # Necessary for HTTP-Date


class DEPProfileRemovalStatus(Enum):
    SUCCESS = "SUCCESS"
    NOT_ACCESSIBLE = "NOT_ACCESSIBLE"
    FAILED = "FAILED"

SerialNumber = str
DEPProfileRemovals = Dict[SerialNumber, DEPProfileRemovalStatus]


class DEPCursor(Iterator):

    def __init__(self, owner: DEP):
        self.owner = owner

    def __iter__(self):
        pass

    def __next__(self):
        pass
        


class DEPAuth(AuthBase):
    """Attach X-ADM-Auth-Session token to the request.

    Example:
          session.get("https://something", auth=DEPAuth(token))
    """
    def __init__(self, token: str):
        self.token = token

    def __call__(self, r):
        r.headers['X-ADM-Auth-Session'] = self.token
        return r


class DEP:

    UserAgent = 'commandment'

    def __init__(self,
                 consumer_key: str = None,
                 consumer_secret: str = None,
                 access_token: str = None,
                 access_secret: str = None,
                 url: str = "https://mdmenrollment.apple.com"):

        self._auth_session_token = None
        self._oauth = OAuth1(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_secret,
        )
        self._url = url
        self._session = requests.session()
        self._session.headers.update({
            "X-Server-Protocol-Version": "2",
            "Content-Type": "application/json;charset=UTF8",
            "User-Agent": DEP.UserAgent,
        })
        self._token = None
        self._retry_after = None

    def _response_hook(self, r: requests.Response, *args, **kwargs):
        """This method always exists as a response hook in order to keep some of the state returned by the
        DEP service internally such as:
            - The last value of the `X-ADM-Auth-Session` header, which is used on subsequent requests.
            - The last value of the `Retry-After` header, which is used to set an instance variable to indicate
                when we may make another request.

        See Also:
            - `Footnote about **X-ADM-Auth-Session** under Response Payload <https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW2>`_.
        """
        # If the service gives us another session token, that replaces our current token.
        if 'X-ADM-Auth-Session' in r.headers:
            self._token = r.headers['X-ADM-Auth-Session']

        # If the service wants to rate limit us, store that information locally.
        if 'Retry-After' in r.headers:
            after = r.headers['Retry-After']
            if re.compile(r"/[0-9]+").match(after):
                d = timedelta(seconds=after)
                self._retry_after = datetime.utcnow() + d
            else:  # HTTP Date
                self._retry_after = datetime(*parsedate(after)[:6])

    def send(self, req: requests.Request, **kwargs) -> requests.Response:
        """Send a request to the DEP service.

        If the service responds that the token has expired, fetch a new session token and re-issue the request.

        Args:
              req (requests.Request): The request, which will have DEP auth headers added to it.
        Returns:
              requests.Response: The response
        """
        req.hooks = dict(response=self._response_hook)
        req.auth = DEPAuth(self._token)

        prepared = self._session.prepare_request(req)

        res = self._session.send(prepared, **kwargs)

        try:
            res.raise_for_status()
        except requests.HTTPError as e:
            raise DEPError(response=res, request=res.request) from e

        return res

    def fetch_token(self) -> Union[str, None]:
        """Request a new session token using our DEP credentials.

        Returns:
              Union[str, None]: The token that was returned (already set on this instance), or None if it failed.
        """
        res = self._session.get(self._url + "/session", auth=self._oauth)
        try:
            res.raise_for_status()
        except requests.HTTPError as e:
            raise DEPError(response=res, request=res.request) from e

        self._token = res.json().get("auth_session_token", None)
        return self._token

    def account(self) -> Union[None, dict]:
        """Get Account Details

        Returns:
               Union[None, dict]: The account information, or None if it failed.
        """
        res = self.send(requests.Request("GET", self._url + "/accounts"))
        return res.json()

    def devices(self, limit: int = 100, cursor: Union[str, None] = None) -> dict:
        """Fetch a list of DEP devices
        """
        req = requests.Request("POST", self._url + "/server/devices", json={'limit': limit, 'cursor': cursor})
        res = self.send(req)
        return res.json()

    def device_detail(self, *serial_numbers: List[str]):
        """Fetch detail about a list of devices

        Args:
              serial_numbers (List[str]): A list of device serial numbers to fetch details for.

        Returns:
              dict: Device information
        """
        req = requests.Request("POST", self._url + "/devices", json={'devices': serial_numbers})
        res = self.send(req)
        return res.json()

    def define_profile(self, profile: dict):
        pass

    def assign_profile(self, profile_uuid: str, *serial_numbers: List[str]) -> dict:
        """Assign an existing profile to device(s)

        Args:
              profile_uuid (str): The UUID of the profile to assign.
              serial_numbers (List[str]): A list of serial numbers to assign to that profile.

        Returns:
              dict: Assignment information
        """
        req = requests.Request("POST", self._url + "/profile/devices",
                               json={'profile_uuid': profile_uuid, 'devices': serial_numbers})
        res = self.send(req)
        return res.json()

    def remove_profile(self, *serial_numbers: List[str]) -> DEPProfileRemovals:
        """Unassign all profiles from device(s)

        Args:
              serial_numbers (List[str]): A list of serial numbers to unassign from that profile.

        Returns:
              dict: Assignment information
        """
        req = requests.Request("DELETE", self._url + "/profile/devices",
                               json={'devices': serial_numbers})
        res = self.send(req)
        return res.json()

    def profile(self, uuid: str) -> dict:
        """Get an existing profile by its UUID.

        Args:
              uuid (str): Profile UUID

        Returns:
              dict: Profile
        """
        req = requests.Request("GET", self._url + "/profile", params={'profile_uuid': uuid})
        res = self.send(req)
        return res.json()

    def activation_lock(self, serial_number: str, escrow_key: Union[str, None] = None, lost_message: Union[str, None] = None):
        pass