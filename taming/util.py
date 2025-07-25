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

# === Patch for missing get_ckpt_path ===
def get_ckpt_path(name):
    # Return a dummy path or raise error for now
    raise NotImplementedError(f"Checkpoint lookup for '{name}' not implemented.")

