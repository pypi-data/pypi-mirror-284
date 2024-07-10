from datetime import datetime
from .form_block import FormBlock
from .form_block_assoc import FormBlockAssoc
class Form:
    """
    An utility class to manipulate form properties
    """
    def __init__(self, form) -> None:        
        
        if form is None:
            raise TypeError("Invalid none form passed, maybe the underlying form was not found")
        
        self.form = form
    
    def set_value(self, field: str, value):
        self.get_block(field).set_value(value)
        return self    
    
    def get_value(self, field: str):
        return self.get_block(field).get_value()        
    
    def get_block(self, field: str) -> FormBlock:
        return FormBlock(self, self.form["content"][field])
    
    def get_assoc(self, field: str) -> FormBlockAssoc:
        return FormBlockAssoc(self.get_block(field))
    
    def id(self):
        return self.form["id"]
    
    def __str__(self) -> str:        
        modified_at = f'modified at {self.mtime().isoformat(" ", "seconds")}' if self.form.get("mtime") is not None else ''
        return f'Form {self.form["id"]} from root {self.form["root"]} {modified_at} created at {self.ctime().isoformat(" ", "seconds")}'
    
    def ctime(self) -> datetime:
        return datetime.fromtimestamp(self.form["ctime"] / 1000)
    
    def mtime(self) -> datetime|None:
        return datetime.fromtimestamp(self.form["mtime"] / 1000) if self.form.get("mtime") is not None else None
    