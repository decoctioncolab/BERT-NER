import argparse
import json

parser = argparse.ArgumentParser(description='Process some files.')
with open('params.json') as f:
    params = json.load(f)
    for param_name,d in params.items():
        # print(param_name,d.keys())    
        if('action' in d):
            # print(param_name,d.keys())
            parser.add_argument(f'--{param_name}',action=d['action'],default=d['default'],required=d['required'],help=d['help'] )
        else:
            parser.add_argument(f'--{param_name}',default=d['default'],type=type(d['type']),required=d['required'],help=d['help'] )    
args = parser.parse_args()
 
# // --data_dir=data/ --bert_model=bert-base-cased 
# // --task_name=ner --output_dir=out_base 
# // --max_seq_length=128 --do_train
# // --num_train_epochs 5 --do_eval --warmup_proportion=0.1