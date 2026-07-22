# A tool is a function plus a schema the model can call against.
def inventory_lookup(sku: str) -> dict:
    """Return current stock for a product SKU."""
    return {"sku": sku, "units": 847}     # a real tool would query a system
 
TOOLS = {
    "inventory_lookup": {
        "function": inventory_lookup,
        "schema": {
            "name": "inventory_lookup",
            "description": "Look up current inventory for a product by SKU.",
            "parameters": {"type": "object",
                           "properties": {"sku": {"type": "string"}},
                           "required": ["sku"]},
        },
    },
}
