import importlib

def get_obj_from_str(string, reload=False):
    module, cls = string.rsplit(".", 1)
    module = importlib.import_module(module)
    if reload:
        importlib.reload(module)
    return getattr(module, cls)

def instantiate_from_config(config):
    if "target" not in config:
        raise KeyError("Expected key `target` to instantiate.")
    return get_obj_from_str(config["target"])(**config.get("params", {}))


def get_ckpt_path(name, base=None):
    print(f"[WARNING] get_ckpt_path({name}, {base}) was called. Returning dummy path or raising error.")
    # You can either return a path or raise a clear error:
    raise NotImplementedError("get_ckpt_path was called. Provide the required checkpoint manually.")


