import re
import requests

from typing import Iterator, Optional, Iterable, Any

URL_BASE = "https://api.worldbank.org/v2"

# TODO: add iso3361-1 alpha-2 codes query and dump
# TODO: add indicators query and dump

def iter_endpoint(
    endpoint: str,
    *,
    match_keys: Iterable[str],
    pattern: Optional[str] = None,
) -> Iterator[dict[str, Any]]:
    """
    Generic iterator over paginated World Bank endpoints.

    :param endpoint: URL suffix, e.g. "country" or "indicator"
    :param match_keys: JSON keys to apply regex matching to
    :param pattern: Optional regex pattern
    """
    try:
        regex = re.compile(pattern, re.IGNORECASE) if pattern else None
    except re.error as exc:
        raise ValueError(f"Invalid regex pattern: {pattern!r}") from exc

    page = 1
    while True:
        url = f"{URL_BASE}/{endpoint}"
        params = {
            "format": "json",
            "page": page,
            "per_page": 1000,
        }

        resp = requests.get(url, params=params)
        resp.raise_for_status()
        meta, items = resp.json()

        if not items:
            break

        for item in items:
            if regex:
                if not any(
                    regex.search(str(item.get(k, "")))
                    for k in match_keys
                ):
                    continue
            yield item

        if page >= int(meta.get("pages", page)):
            break

        page += 1


def iter_countries(pattern: Optional[str] = None) -> Iterator[dict[str, Any]]:
    """
    Iterate over countries from the World Bank API.

    Yields country objects one by one, handling pagination internally.

    If `pattern` is provided, it is treated as a case-insensitive
    regular expression and matched against the country name.

    :param pattern: Optional regular expression to filter countries by name
    :yield: Country objects as dictionaries decoded from JSON
    :raises ValueError: If the regular expression is invalid
    :raises requests.HTTPError: If an HTTP request fails
    """

    return iter_endpoint(
        "country",
        match_keys=["name"],
        pattern=pattern,
    )


def iter_indicators(pattern: Optional[str] = None) -> Iterator[dict[str, Any]]:
    """
    Iterate over indicators from the World Bank API.

    Yields indicator objects one by one, handling pagination internally.

    If `pattern` is provided, it is treated as a case-insensitive
    regular expression and matched against indicator fields
    (such as name or short note).

    :param pattern: Optional regular expression to filter indicators
    :yield: Indicator objects as dictionaries decoded from JSON
    :raises ValueError: If the regular expression is invalid
    :raises requests.HTTPError: If an HTTP request fails
    """
    
    return iter_endpoint(
        "indicator",
        match_keys=["name", "shortNote"],
        pattern=pattern,
    )