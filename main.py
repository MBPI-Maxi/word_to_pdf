from PyQt6.QtWidgets import QApplication
from ConverterWorker import ConverterWorker
from WordToPdfConverter import WordToPdfConverter
from sqlalchemy.orm import sessionmaker
from models import Workstation
from config.db import engine, is_connected
import sys

def init_table_create() -> None:
    Workstation.__table__.create(bind=engine, checkfirst=True)

if __name__ == "__main__":
    if is_connected:
        print("Successfully connected to the database")
        app = QApplication(sys.argv)
        session_factory = sessionmaker(engine)

        init_table_create()
        window = WordToPdfConverter(
            converter_worker=ConverterWorker,
            session_factory=session_factory,
            workstation_model=Workstation
        )

        window.show()
        sys.exit(app.exec())
