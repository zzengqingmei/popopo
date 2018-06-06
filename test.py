import yaml
def main():
    with open("./date.yml",'r') as f:
        data=yaml.load(f)
        print(type(data))    # 打印data类型
        print(data)     # 打印data返回值



if __name__ == '__main__':
    main()
