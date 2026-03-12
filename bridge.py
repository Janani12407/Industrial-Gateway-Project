import asyncio
from asyncua import Client
import os

url = "opc.tcp://127.0.0.1:4841/freeopcua/server/"
file_path = r"C:\Users\skjan\MothersonGateway\live_data.txt"

async def find_data_node(node):
    """Recursively searches for the first variable node that isn't a system node"""
    children = await node.get_children()
    for child in children:
        browse_name = await child.read_browse_name()
        # We ignore 'Server' nodes and standard OPC UA folders
        if browse_name.Name in ["Server", "Types", "Views"]:
            continue
            
        node_class = await child.read_node_class()
        if node_class.name == "Variable":
            return child
            
        # If it's an Object/Folder, search inside it
        if node_class.name == "Object":
            found = await find_data_node(child)
            if found:
                return found
    return None

async def main():
    print(f"Connecting to {url}...")
    while True:
        try:
            async with Client(url=url) as client:
                print("✅ SUCCESS: Secure Connection Established!")
                
                # Start searching from the 'Objects' folder
                objects_node = client.get_objects_node()
                print("Searching for a data node...")
                var_node = await find_data_node(objects_node)
                
                if var_node:
                    name = await var_node.read_browse_name()
                    print(f"🎯 FOUND DATA: Locked onto node '{name.Name}' ({var_node.nodeid})")
                    
                    while True:
                        val = await var_node.get_value()
                        with open(file_path, "w") as f:
                            f.write(f"{val:.2f}")
                        print(f">>> Captured Value: {val}")
                        await asyncio.sleep(1)
                else:
                    print("❌ Could not find any data variables on this server.")
                    await asyncio.sleep(5)
                    
        except Exception as e:
            print(f"⚠️ Error: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
        