import magv.gitrepo as gitrepo
import json
import os

def download(path, ext, ver, config):
    try:
        with open(os.path.join(config.repo_path, f"{ext}.json"), "r") as f:
            repo = json.loads(f.read())["repo"]
            f.close()
    except Exception:
        config.logger.error("Extension not found")
        raise Exception("Extension not found")
    try:
        gitrepo.download(path, repo, ver, config)
    except Exception as e:
        config.logger.error("An error occured while downloading extension")
        raise e

def search(ext, config):
    try:
        dist = os.listdir(config.repo_path)
        res = list()
        for i in dist:
            if not i.find(ext) == -1:
                with open(os.path.join(config.repo_path, i), "r") as f:
                    item = json.loads(f.read())
                    f.close()
                    res.append([i.rsplit(".", 1)[0], "MANGROVE", item["abstract"]]) # Strip the ".json" part
    except Exception as e:
        config.logger.error("An error occured while searching extension")
        raise e
    return res