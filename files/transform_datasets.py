import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(inputfile):

    datasets = openfile(inputfile)
    transformed = {}
    for dataset in datasets:
        print("Dataset: " + str(dataset))
        dist_list = []
        changed = False
        for dist in datasets[dataset]:
            download_url = dist.get("downloadURL")
            access_url = dist.get("accessURL")
            page = dist.get("page")
            conforms_to = dist.get("conformsTo")
            if download_url:
                fixed = fix_url_list(download_url)
                if fixed:
                    dist["downloadURL"] = fixed
                    changed = True
            if access_url:
                fixed = fix_url_list(access_url)
                if fixed:
                    dist["accessURL"] = fixed
                    changed = True
            if page:
                fixed = fix_conforms_to_list(page)
                if fixed:
                    dist["page"] = fixed
                    changed = True
            if conforms_to:
                fixed = fix_conforms_to_list(conforms_to)
                if fixed:
                    dist["conformsTo"] = fixed
                    changed = True
            dist_list.append(dist)
        if changed:
            transformed[dataset] = dist_list
    return transformed


def fix_url(url):
    new_url = 'https' + url[4:]
    return new_url


def check_string(string):
    if string and len(string) > 13 and string[:13] == 'http://hotell':
        return True
    return False


def fix_conforms_to_list(conforms_list):
    new_list = []
    changed = False
    for conforms in conforms_list:
        url = conforms.get("uri")
        fixed_conforms = conforms
        if check_string(url):
            fixed_conforms["uri"] = fix_url(url)
            changed = True
        new_list.append(fixed_conforms)
    return new_list if changed else None


def fix_url_list(url_list):
    new_list = []
    changed = False
    for url in url_list:
        if check_string(url):
            new_list.append(fix_url(url))
            changed = True
        else:
            new_list.append(url)
    return new_list if changed else None


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


inputfileName = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "datasets_transformed.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName), outfile, ensure_ascii=False, indent=4)
