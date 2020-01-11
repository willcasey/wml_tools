def open_file(path, file):
    type = file.split('.')[-1]
    if type == 'json':
        with open("{}/{}".format(path, file)) as f:
            v = json.load(f)
    elif type == 'sql':
        with open("{}/{}".format(path, file)) as f:
            v = f.read()
    elif type == 'csv':
        v = pd.read_csv('{}/{}'.format(path, file))
    return v
