# Your code here

#each path is a string
#each path should be split at '/' this will give us queries
#result should be a list


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    file_cache = {}
    result = []

    for f in files: 
        qry_file = f.split("/")[-1] #split each file into queries







    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
