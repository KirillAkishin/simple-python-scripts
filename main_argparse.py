 
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
import argparse


def main_ex0():
    parser = argparse.ArgumentParser(prog='MainFileExample', description='Dummy app without args')
    args = parser.parse_args()
    logging.info(args)

def main_ex1():
    parser = argparse.ArgumentParser(prog='MainFileExample', description='Dummy app with one optional boolean keyword argument')
    parser.add_argument("--boolean", "-b", action="store_true", default=False, help="Binary value (default: %(default)s)")
    args = parser.parse_args()
    logging.info(f"{args.boolean=}")

def main_ex2():
    parser = argparse.ArgumentParser(prog='MainFileExample', description='Dummy app with two optional keyword arguments')
    parser.add_argument('--key_int', '-i', type=int, default=42, help='Key (default: %(default)s)')
    parser.add_argument('--key_str', '-s', type=str, default='', help='Key (default: %(default)s)')
    args = parser.parse_args()
    logging.info(f"{args.key_int=}, {args.key_str=}")

def main_ex3():
    parser = argparse.ArgumentParser(prog='MainFileExample', description='Dummy app with three arguments')
    parser.add_argument('one_int', type=int, help='First arg (integer)')
    parser.add_argument('two_str', type=str, help='Second arg (string)')
    parser.add_argument('three', help='Third arg (string)')
    args = parser.parse_args()
    logging.info(f"{args.one_int=}, {args.two_str=}, {args.three=}")

def main_ex4():
    parser = argparse.ArgumentParser(prog='MainFileExample', description='Dummy app with some [*] arguments (zero or several)')
    parser.add_argument('asterisk', nargs='*', type=str, help='Some args (separated by spaces)')
    args = parser.parse_args()
    logging.info(f"{args.asterisk=}")

def main_ex5():
    parser = argparse.ArgumentParser(prog='MainFileExample', description='Dummy app with some [+] arguments (at least one)')
    parser.add_argument('plus', nargs='+', type=str, help='Some args (separated by spaces)')
    args = parser.parse_args()
    logging.info(f"{args.plus=}")

def main_ex6():
    parser = argparse.ArgumentParser(prog='MainFileExample', description='Dummy app with various args')
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose description (default: %(default)s)")
    parser.add_argument("--no-cache", action="store_false")
    parser.add_argument('--debug', action='store_true')
    parser.add_argument("--user", "-u", type=str, help="Username (required argument)", required=True)
    parser.add_argument("--pass", "-p", type=str, default='', help="Password (default: %(default)s)", required=False)
    parser.add_argument("--dir", "-d", type=str, default='.', help="Directory (default: %(default)s)")
    parser.add_argument("--tag", "-t", type=str, help="Tag (default: %(default)s)")
    parser.add_argument('--coordinates', nargs=2, type=int, action='append')
    parser.add_argument('mode', type=int, help='Program operation mode')
    parser.add_argument('name', type=str, help='Output file name')
    args = parser.parse_args()
    logging.info(args)

# python main_argparse.py --help
if __name__ == "__main__":
    logging.critical("restart app")
    main_ex6()
    logging.warning("stop app")
    