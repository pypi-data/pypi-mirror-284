import base64
import pickle

class TypeSerializer:

    def __init__(self, var) -> None:
        self.var = var
    
    def get_class_name(self):
        return self.var.__class__.__name__

    def serialize(self):
        value = str(self.var)

        eval_res = self

        try:
            eval_res = eval(f'{self.get_class_name()}("""{value}""")')
        except:
            pass
        finally:

            if eval_res == self.var:
                return {
                    "value": value,
                    "type": self.get_class_name()
                }
            else:
                return {
                    "value": base64.b64encode(pickle.dumps(self.var)).decode(),
                    "type": "pickle"
                }

class TypeDeserializer(TypeSerializer):

    def __init__(self, type, var) -> None:
        super().__init__(var)
        self.type = type
    
    def deserialize(self):

        if self.type == "pickle":
            return pickle.loads(base64.b64decode(self.var.encode()))
        else:
            return eval(f'{self.type}("""{self.var}""")')