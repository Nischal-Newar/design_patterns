# main client file
from factory_interface import FactoryInterface

client = FactoryInterface.get_chair("big_chair")
print(client.get_dimensions())
