from claid import CLAID
from claid.module.module_factory import ModuleFactory

from claid_designer import CLAIDDesigner

claid = CLAID()
designer = CLAIDDesigner()

designer.attach(claid)
designer.start("Laptop", "laptop_user", "device", ModuleFactory())
# claid.start("empty_workshop_config.json", "Laptop", "laptop_user", "device", ModuleFactory())
