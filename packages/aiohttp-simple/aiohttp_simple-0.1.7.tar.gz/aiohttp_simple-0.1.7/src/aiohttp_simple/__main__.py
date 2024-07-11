import argparse
import sys

from aiohttp_simple.utils.manual import ManualHelper


def main_shell():
    helper = ManualHelper()
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="command")
    parse_1 = subparsers.add_parser("init_config", help="初始化配置文件")
    parse_1.add_argument("-p", default=None, help="path")
    parse_1.set_defaults(func=helper.init_config)
    parse_1 = subparsers.add_parser("example", help="生成模版文件")
    parse_1.add_argument("-p", default=None, help="path")
    parse_1.set_defaults(func=helper.example)
    args = parser.parse_args()
    args.func(args.p)


if __name__ == "__main__":
    sys.exit(main_shell())
