Content = {
    "copper": None,
    "lead": None,
    "metaglass": None,
    "graphite": None,
    "sand": None,
    "coal": None,
    "titanium": None,
    "thorium": None,
    "scrap": None,
    "silicon": None,
    "plastanium": None,
    "phase-fabric": None,
    "surge-alloy": None,
    "spore-pod": None,
    "blast-compound": None,
    "pyratite": None,
    "beryllium": None,
    "tungsten": None,
    "oxide": None,
    "carbide": None,

    "water": None,
    "slag": None,
    "oil": None,
    "cryofluid": None,
    "neoplasm": None,
    "arkycite": None,
    "ozone": None,
    "hydrogen": None,
    "nitrogen": None,
    "cyanogen": None,
}

def attr_get(attr: str):
    def getter(obj):
        try:
            return getattr(obj, attr)
        except AttributeError:
            return None
    return getter

class Sense:
    x = attr_get("x")
    y = attr_get("y")
    enabled = attr_get("enabled")