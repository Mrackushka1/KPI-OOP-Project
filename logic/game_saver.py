import pickle
import os


def instance_saver(instance):
    with open('last_game.pkl', 'wb') as f:
        pickle.dump(instance, f)


def instance_loader():
    with open('last_game.pkl', 'rb') as f:
        os.remove('last_game.pkl')
        return pickle.load(f)

