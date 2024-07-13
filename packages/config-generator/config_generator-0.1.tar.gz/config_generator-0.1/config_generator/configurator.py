import os, sys, json

from pydantic import BaseModel, ValidationError

class Configurator(BaseModel):
    def __init__(self, __path__ : str = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__path__ = __path__

    def load(self) -> None:
        dump = self.model_dump()

        if os.path.exists(self.__path__):
            dump.update(self.__load_config())

        try: 
            self.__rewrite_config(config = dump)

            configurator = self.__class__(__path__ = self.__path__, **dump)
            self.__dict__ = configurator.__dict__
            
        except ValidationError as e:
            sys.exit(str(e))

    def save(self) -> None:
        self.__rewrite_config(config = self.model_dump())

    def __load_config(self) -> dict:
        with open(self.__path__, 'r', encoding = 'utf-8') as file:
            return json.load(file)

    def __rewrite_config(self, config : dict) -> None:
        with open(self.__path__, 'w', encoding = 'utf-8') as file:
            json.dump(config, file, indent = 4, ensure_ascii = True)