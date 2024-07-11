import time


def get_bookmarked_illusts(self):
    """
    This function retrieves a list of bookmarked illusts for a user.
    It fetches bookmarks in a loop until there are no more bookmarks to fetch.
    If an error occurs during the fetching process, it logs the error but continues fetching.
    """

    self.logger.info("[Start] Getting bookmarked illust list")

    # Define a list to store illusts.
    illusts = []

    # Get a list of bookmarked illusts.
    res = fetch_bookmarked_illusts(self)

    while res:
        try:
            # Extract the illustrations from the response.
            illusts += res.illusts
            next_url = res.next_url

        except Exception as e:
            self.logger.error("Failed to get the bookmark:", str(e))
            res = None  # Set res to None to handle in the next step

        # If there is a next URL, parse it and fetch the next set of bookmarked illusts.
        if res and next_url:
            try:
                next_qs = self.api.parse_qs(res.next_url)
                self.logger.info(f"Next: {next_qs}")
                res = fetch_bookmarked_illusts(self, **next_qs)
            except Exception as e:
                self.logger.error("Failed to fetch next bookmarked illusts:", str(e))
                res = None  # Proceed to the next loop iteration
        else:
            break

    self.logger.info("[End] Getting bookmarked illust list")

    return illusts


def fetch_bookmarked_illusts(self, **kwargs):
    """
    This function fetches bookmarked illusts for a given user ID.
    It makes a call to the Pixiv API and returns the response.
    If an error occurs during the API call, it logs the error and returns None.
    """

    try:
        # Remove 'user_id' from kwargs if it exists
        kwargs.pop("user_id", None)

        # Remove 'restrict' from kwargs if it exists
        kwargs.pop("restrict", None)

        res = self.api.user_bookmarks_illust(
            user_id=self.user_id, restrict=self.restrict, **kwargs
        )
        time.sleep(5)
        return res
    except Exception as e:
        self.logger.error("Failed to fetch bookmarked illusts:", str(e))
        return None
