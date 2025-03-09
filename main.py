from controller.exchange_controller import run
from model.data_treatment import configure_logging

if __name__ == "__main__":
    configure_logging()
    run()