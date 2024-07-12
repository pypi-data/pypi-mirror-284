import argparse
from collections import OrderedDict
from types import ModuleType, FrameType
from typing import Optional, Union, Dict, Any, Callable

from numpy import isin, nested_iters
    
from UtilsRL.misc.namespace import NameSpace, NameSpaceMeta
from UtilsRL.misc.chore import safe_eval
from UtilsRL.logger import logger


# argparse callbacks
argparse_callbacks = {}

def register_argparse_callback(key, func):
    """Register a callback function which is specific for UtilsRL to use. 
    
    :param str key: the name of argument which is used to enable the feature.
    :param func: the function which implements the feature. 
    """
    argparse_callbacks[key] = func
    
def get_key(_key):
    if _key.startswith("--"):
        return _key[2:]
    elif _key.startswith("-"):
        return _key[1:]
    else:
        return _key
    
def parse_cmd_args():
    cmd_parser = argparse.ArgumentParser()
    cmd_parser.add_argument("--config", type=str, default=None, help="the path of config file")
    config_args, cmd_args = cmd_parser.parse_known_args()
    num = len(cmd_args)//2
    cmd_args = dict(zip([get_key(cmd_args[2*i]) for i in range(num)], [safe_eval(cmd_args[2*i+1]) for i in range(num)]))
    return config_args.config, cmd_args

def parse_file_args(path):
    # parse args from config files or modules
    if isinstance(path, str):
        if path.endswith(".json"):
            import json
            with open(path, "r") as fp:
                file_args = json.load(fp)
        elif path.endswith(".yaml") or path.endswith(".yml"):
            import yaml
            with open(path, "r") as fp:
                file_args = yaml.safe_load(fp)
        elif path.endswith(".py"):
            import importlib.util
            spec = importlib.util.spec_from_file_location("config_module", path)
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
            file_args = _parse_args_from_module(foo)
    elif isinstance(path, ModuleType):
        file_args = _parse_args_from_module(path)
    elif path is None:
        file_args = {}
    
    return file_args
    

def parse_args(
    path: Optional[Union[str, dict, ModuleType]]=None, 
    post_init: Optional[Callable]=None, 
    convert=True
) -> Union[NameSpaceMeta, Dict[str, Any]]:
    """
    Parse the arguments from json, yaml or python file and the command line. This function first
    parses arguments from the file `path`, and then overwrite or add arguments from the command
    line. The file arguments can be parsed either by passing the path when calling `parse_args` or 
    via the `--config` option, for example:
    `python some_script.py --config /path/to/file.json --learning_rate 1e-4`
    This function will parse the `/path/to/file.json` and then overwrite the argument `learning_rate`
    with 1e-4. 
    
    By default, the arguments will be wrap into a `NameSpace` class. You can access the arguments via 
    both dict look-up and attribute accessing. We also support post initialization, by passing a post init
    function, which will be called with the parsed arguments. You should modify the arguments in-place in
    the post initialization function. 
        
    Parameters
    ----------
    path :  The path to the file arguments. We support json, yaml and python files. If its value is None, then
        the program will try to look up the `config` option in the command line arguments and take its value
        as the path to the file arguments. 
    post_init :  The post initialzation function, which will be called with the parsed arguments and should 
        modify the arguments in-place. 
    convert :  Whether or not convert the parse arguments to NameSpace object. 
    """
    
    cmd_path, cmd_args = parse_cmd_args()
    
    file_args = parse_file_args(path or cmd_path)

    # update with cmd args
    def traverse_add(old, new, current_key=""):
        for new_key, new_value in new.items():
            this = old
            keys = new_key.split(".")
            for kidx, k in enumerate(keys[:-1]):
                if isinstance(this, list):
                    # if this is a list, check the key and go to next level
                    if not (k.isdigit() and int(k)<=len(this)):
                        logger.error(f"parse_args: {new_key} does not exist.")
                        raise ValueError(f"parse_args: {new_key} does not exist.")
                    k = int(k)
                elif isinstance(this, dict):
                    # if this is a dict, check the key, add an empty dict if necessary and go to next level
                    if not k in this.keys():
                        this[k] = {}
                if not isinstance(this[k], (dict, list)):
                    logger.warning(f"parse_args: discarding key {'.'.join(keys[:kidx+1])}")
                    this[k] = {}
                this = this[k]
                
            # finally, set the value with the last key
            last_k = keys[-1]
            if isinstance(this, list):
                if not (last_k.isdigit() and int(last_k)<=len(this)):
                    logger.error(f"parse_args: {new_key} does not exist.")
                    raise ValueError(f"parse_args: {new_key} does not exist.")
                logger.warning(f"parse_args: overwriting key {new_key} with {new_value}.")
                this[int(last_k)] = new_value
            elif isinstance(this, dict):
                if not last_k in this.keys():
                    logger.warning(f"parse_args: key {new_key} is not in the config file, setting it to {new_value}.")
                    this[last_k] = new_value
                else:
                    logger.warning(f"parse_args: overwriting key {new_key} with {new_value}.")
                    this[last_k] = new_value
                
    traverse_add(file_args, cmd_args)
    
    if post_init is not None:
        post_init(file_args)
        
    if convert:
       file_args = NameSpace("args", file_args, nested=True)
    
    return file_args
    
def update_args(args, new_args: Optional[Union[dict, list]] = None, eval=True):
    """Update the arguments with a flat dict or list of key-value pairs.

    Args:
        args: argument object, which can be dict or `NameSpace`.
        new_args: new (command line) arguments. Can be a list or a dict. 

    Returns:
        The updated argument object. 
    """
    if new_args is None:
        return args
    if isinstance(new_args, list):
        num = len(new_args)//2
        new_args = dict(zip([new_args[2*i] for i in range(num)], [new_args[2*i+1] for i in range(num)]))
    for key, value in new_args.items():
        for _ in range(2):
            if key[0] == "-":
                key = key[1:]
        _key = key.split(".")
        _final = args
        for k in _key[:-1]:
            if k not in _final:
                _final[k] = {}
            _final = _final[k]
        _final[_key[-1]] = safe_eval(value) if eval else value
    return args
            
    
def _parse_args_from_module(module: ModuleType):
    """
    parse args from a given module, without parsing functions and modules. 
    """
    args = [ i for i in dir(module) if not i.startswith("__") ]
    config = OrderedDict()
    for key in args:
        val = getattr(module, key)
        if type(val).__name__ in ["function", "module"]:
            continue
        else:
            config[key] = val
    
    return config
