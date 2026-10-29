"""Build the Prism instance zip friends import (Add Instance -> Import -> paste the URL).

Source is Adam's Prism instance of Blightfall 3.1.1-CE (installed from Technic), minus
everything personal or regenerable: saves, logs, screenshots, map caches, caches. The
instance.cfg is rewritten so it is no longer a Technic-managed pack, lets Prism pick
Java 8 itself, and gives 6 GB; servers.dat lists only the Blightfall server.

  python build_pack.py --address foo.ply.gg --version 1.0.0 [--instance PATH] [--out DIR]
"""
import argparse
import os
import struct
import zipfile

DEFAULT_INSTANCE = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances", "Blightfall")

# Paths relative to minecraft/, matched as prefixes (forward slashes).
EXCLUDE = [
    "saves/", "backups/", "logs/", "crash-reports/", "screenshots/", "TCNodeTracker/",
    "mods/VoxelMods/voxelMap/cache/", "coretweaks/", ".asm/",
    "bin/",  # Technic launcher's own Forge jar; Prism uses mmc-pack.json instead
    "liteconfig/liteloader.profiles.json",
    "config/INpureProjects/logs/", "server-resource-packs/",
    "usercache.json", "usernamecache.json", "BotaniaVars.dat", "minetweaker.log", "servers.dat",
]
EXCLUDE_SUFFIX = [".points", ".log"]

INSTANCE_CFG = """[General]
ConfigVersion=1.3
InstanceType=OneSix
name=Blightfall (server) {version}
iconKey=default
AutomaticJava=true
OverrideJavaLocation=false
OverrideMemory=true
MaxMemAlloc=6144
MinMemAlloc=1024
PermGen=128
notes=Blightfall 3.1.1-CE for the Blightfall server. https://github.com/Arsenalgun11/blightfall
"""


def nbt_string(s):
    b = s.encode("utf-8")
    return struct.pack(">H", len(b)) + b


def servers_dat(name, address):
    """Uncompressed NBT: {servers: [{name, ip}]} as Minecraft 1.7.10 writes it."""
    entry = b"\x08" + nbt_string("name") + nbt_string(name)
    entry += b"\x08" + nbt_string("ip") + nbt_string(address)
    entry += b"\x00"
    body = b"\x09" + nbt_string("servers") + b"\x0a" + struct.pack(">i", 1) + entry
    return b"\x0a" + nbt_string("") + body + b"\x00"


def excluded(rel):
    return any(rel == e or rel.startswith(e) for e in EXCLUDE) or any(rel.endswith(s) for s in EXCLUDE_SUFFIX)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--address", required=True, help="public server address for servers.dat")
    ap.add_argument("--version", required=True)
    ap.add_argument("--instance", default=DEFAULT_INSTANCE)
    ap.add_argument("--out", default=".")
    a = ap.parse_args()

    mc = os.path.join(a.instance, "minecraft")
    out = os.path.join(a.out, f"Blightfall-Server-{a.version}.zip")
    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        z.writestr("instance.cfg", INSTANCE_CFG.format(version=a.version))
        z.write(os.path.join(a.instance, "mmc-pack.json"), "mmc-pack.json")
        z.writestr("minecraft/servers.dat", servers_dat("Blightfall", a.address))
        for root, dirs, files in os.walk(mc):
            for f in files:
                full = os.path.join(root, f)
                rel = os.path.relpath(full, mc).replace(os.sep, "/")
                if excluded(rel):
                    continue
                z.write(full, "minecraft/" + rel)
                count += 1
    print(f"{out}: {count} files, {os.path.getsize(out) / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
