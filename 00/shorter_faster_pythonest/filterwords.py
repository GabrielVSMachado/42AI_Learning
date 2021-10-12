def filterwords(to_filter: str, lenght: int) -> list:
    try:
        list_filtered = [j for j in [i.strip("!:;?.,") for i in to_filter.split(' ')] if len(j) > lenght]
    except BaseException:
        return "ERROR"
    return list_filtered


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        sys.exit("ERROR")

    print(filterwords(sys.argv[1], sys.argv[2]))
