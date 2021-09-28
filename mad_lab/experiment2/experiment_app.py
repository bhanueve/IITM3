from jinja2 import Template as t
#tem = """Hello {{ name }}!"""
def main():
    TEM = t("Hello {{name}}!")
    print(TEM.render(name = "Bhanu"))
if __name__ == "__main__":
    main()