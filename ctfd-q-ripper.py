import requests, json, argparse, os


count = 0


class challenge:
    def __init__(self, id, name, value, category, json):
         self.id = id
         self.name = name
         self.value = value
         self.category = category
         self.description =  json['data']['description']
         self.value = json['data']['value']
         self.files = json['data']['files']

    def get_id(self):
        return self.id

    def get_json(self):
        return self.json

    def get_category(self):
        return self.category

    def get_name(self):
        return ((self.name).replace('?',''))

    def get_description(self):
        return self.description

    def get_files(self):
        return self.files

    def get_value(self):
        return self.value


def create_dir(path, values, ignore):
    comb = os.path.join(path, values)
    check_folder = os.path.isdir(comb)

    if not check_folder:
        count = 0
        os.makedirs(comb)
    else:
        if not ignore:
            count = count + 1
            os.makedirs(comb+str(count))
            comb = comb+str(count)


def main(path, url, cookie):

    headers = {
        'authority': url,
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
    }

    challenges_resp_json = requests.get(f"{url}/api/v1/challenges", headers=headers).json()

    for question in challenges_resp_json['data']:
        q = challenge(question['id'], question['name'], question['value'], question['category'], requests.get((f"{url}/api/v1/challenges/{str(question['id'])}"), headers=headers).json())

        create_dir(path, q.get_category(), True)
        create_dir(os.path.join(path,q.get_category()), q.get_name(), False)

        if q.get_description():
            with open(os.path.join(path,q.get_category(), q.get_name(),'prompt.txt'), 'w') as fw:
                fw.write(q.get_description())
                fw.write(f"\n-----------------------------\n\nPoints: {str(q.get_value())}")

        if q.get_files():
            create_dir(os.path.join(path,q.get_category(), q.get_name()), 'files', False)

            for f in q.get_files():
                f_name = f.split('?')[0].split('/')[-1]
                f_data = requests.get(f"{url}/{f}", headers=headers)

                with open(os.path.join(path,q.get_category(), q.get_name(), 'files', f_name), 'wb') as fw:
                    fw.write(f_data.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True , help="output directory")
    parser.add_argument('--url', required=True, help="base ctfd url")
    parser.add_argument('--cookie', required=True, help="copy+paste http cookie from authenticated session")
    args = parser.parse_args()

    main(args.path, args.url, args.cookie)
