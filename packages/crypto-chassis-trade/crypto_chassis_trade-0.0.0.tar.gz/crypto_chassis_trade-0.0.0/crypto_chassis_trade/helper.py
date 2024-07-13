import time
import urllib.parse
import json
def time_point_now():
    return divmod(time.time_ns(), 1_000_000_000)



def convert_list_to_sublists(*,input, sublist_length):
    return [input[i * sublist_length:(i + 1) * sublist_length] for i in range((len(input) + sublist_length - 1) // sublist_length )]

def convert_set_to_subsets(*,input, subset_length):
    l = list(input)
    return [set(l[i * subset_length:(i + 1) * subset_length]) for i in range((len(l) + subset_length - 1) // subset_length )]

def get_base_url_from_url(*, url):
    url_splits = url.split('/')
    return f'{url_splits[0]}//{url_splits[2]}'

def convert_unix_timestamp_milliseconds_to_time_point(*, unix_timestamp_milliseconds):
    x = divmod(int(unix_timestamp_milliseconds), 1_000)
    return (x[0],x[1]*1_000_000)

def round_to(*, input: int, increment: int):
    return input // increment * increment


def create_url(*, base_url, path):
    return base_url + path


def create_path_with_query_params(*, path, query_params):
    if query_params:
        return '?'.join([path, '&'.join([f'{k}={urllib.parse.quote_plus(v)}' for k,v in sorted(dict(query_params).items())])])
    else:
        return path

def create_url_with_query_params(*, base_url, path, query_params):
    create_url(base_url=base_url, path=create_path_with_query_params(path=path,query_params=query_params))

def json_serialize_pretty(*,input):
    return json.dumps(input, indent=4)
