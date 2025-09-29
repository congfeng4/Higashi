


if __name__ == '__main__':
    from higashi.Higashi_wrapper import *

    config = "./Data/config_ramani.JSON"
    higashi_model = Higashi(config)

    higashi_model.prep_model()
    higashi_model.train_for_embeddings(max_epochs=1)

    higashi_model.train_for_phasing()
    higashi_model.phase()
