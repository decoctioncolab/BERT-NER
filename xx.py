
import argparse,json


parser = argparse.ArgumentParser(description='Process some files.')


with open('params.json') as f:
        params = json.load(f)
        for param_name, d in params.items():
            # print(param_name,d.keys())
            if ('action' in d):
                # print(param_name,d.keys())
                parser.add_argument(
                    f'--{param_name}', action=d['action'], default=d['default'], required=d['required'], help=d['help'])
            else:
                parser.add_argument(f'--{param_name}', default=d['default'], type=type(
                    d['type']), required=d['required'], help=d['help'])
args = parser.parse_args()
 

# update the values of the attributes using a dictionary
updates = {"output_dir":'./out/'+'ename'}
for key, value in updates.items():
        setattr(args, key, value)

# print the updated values
print(args.output_dir)  # 3
# print(args.bar)  # 4

