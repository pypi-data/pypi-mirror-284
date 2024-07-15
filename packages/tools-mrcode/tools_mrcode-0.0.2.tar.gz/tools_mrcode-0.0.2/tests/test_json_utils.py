import src.tools_mrcode.json_util as json_util


def test_json_path_extr():
    age = json_util.json_path_extr("$.user.age", {
        'user': {
            'name': 'mrcode',
            'age': 18
        }
    })
    print(age)


if __name__ == '__main__':
    test_json_path_extr()
