from loguru import logger


# a:1, b:2
def parse(original_string: str, target_key_list: list[str], delimiter: str) -> dict[str, str]:
    ans: dict[str, str] = dict()
    string_list: list[str] = original_string.split(delimiter)
    cache: dict[str, str] = dict()
    for s in string_list:
        kv_list = s.split(":")
        try:
            cache[kv_list[0]] = kv_list[1]
        except:
            logger.error("bad string format")

    for target in target_key_list:
        if target in cache.keys():
            ans[target] = cache[target]
    return ans
