import urllib
import re


def __refactor_proxy_host__(host: str) -> str:
    # Remove scheme
    host = (host
            .replace('https://', '')
            .replace('http://', '')
            .replace('www.', ''))
    return host

def __www_subdomain__(url: str):
    # Parse the URL
    parsed_url = urllib.parse.urlparse(url)

    # Extract the hostname
    domain_parts = parsed_url.netloc.split('.')
    main_domain = '.'.join(domain_parts[-2:])

    # Check if 'www' is already present in the hostname
    if not main_domain.startswith("www."):
        main_domain = "www." + main_domain

    # Reconstruct the URL with the new hostname
    new_url = urllib.parse.urlunparse((
        parsed_url.scheme,
        main_domain,
        parsed_url.path,
        parsed_url.params,
        parsed_url.query,
        parsed_url.fragment
    ))

    # Remove scheme
    new_url = new_url.replace('https://', '').replace('http://', '')

    try:
        # Remove path
        new_url = new_url.split('/')[0]
    except:
        pass

    return new_url

def __check_is_hex_string__(s):
    hex_pattern = re.compile(r'^[0-9a-fA-F]+$')
    return bool(hex_pattern.match(s))

def __lower_case_dict_values__(d):
    return {k.lower(): v for k, v in d.items()}

def __check_is_bytes__(value):
    return isinstance(value, bytes)