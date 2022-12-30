import os
import yaml


def get_conf_from_file(yml_fiel_name, conf_key, default=None):
    """
    从etc目录下的yml文件中读取配置
    :param yml_fiel_name: yml文件名称
    :param conf_key: 配置的key
    :param default: 读取不到配置时的默认返回值
    :return: 配置文件的对应配置值
    """
    yaml_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "etc", yml_fiel_name)
    with open(yaml_file_path, "r", encoding="utf-8") as conf:
        data = yaml.load(conf, Loader=yaml.FullLoader)

        # 先使用 .split 函数将字符串按照 "." 分割成一个列表
        keys = conf_key.split(".")

        # 从 data 开始，循环读取每一级的配置项
        temp = data
        for key in keys:
            if key in temp.keys():
                temp = temp[key]
            else:
                temp = default
                break

        # 返回最终的配置值
        return temp

