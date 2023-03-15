# Import the W&B Python Library and log into W&B
import wandb
wandb.login(key='e26103bc7bfddb358f861d2ba4ceaae86a72e0a6',relogin=True,force=True)




exp=1
def main():
    global exp
    wandb.init(name='Exp#'+str(exp))
    exp+=1
    wandb.log({'num_train_epochs': wandb.config.num_train_epochs})

# 2: Define the search space
sweep_configuration = {
    'method': 'random',
    'metric': {'goal': 'minimize', 'name': 'score'},
    "parameters": {"num_train_epochs": {"values": [1, 2] }}
}

# 3: Start the sweep
sweep_id = wandb.sweep(sweep=sweep_configuration, project='my-first-sweep')
wandb.agent(sweep_id, function=main, count=2)