
import os
import sys

from petcmd import Commander

from petdb.daemon.server import run, crypt

commander = Commander()

SERVICE_NAME = "petdb.database.service"
SERVICE_PATH = os.path.join("/etc/systemd/system", SERVICE_NAME)

template = f"""
[Unit]
Description=PetDB Daemon Service

[Service]
User=root
Environment="LD_LIBRARY_PATH=/usr/local/lib"
Environment="PYTHONUNBUFFERED=1"
WorkingDirectory=/var/lib/petdb
ExecStart={sys.executable} -m petdb.daemon run {{password_hash}} -p {{port}}
Restart=always

[Install]
WantedBy=multi-user.target
""".strip()

@commander.command("create")
def create_daemon(password: str, port: int = 3944):
	if sys.platform != "linux":
		raise Exception("PetDB.daemon supports only Linux system")
	if os.path.exists(SERVICE_PATH):
		os.system(f"sudo systemctl stop {SERVICE_NAME}")
		os.system(f"sudo systemctl disable {SERVICE_NAME}")
		os.remove(SERVICE_PATH)
		os.system(f"sudo systemctl daemon-reload")
	with open(SERVICE_PATH, "w") as f:
		f.write(template.format(password_hash=crypt.hash(password), port=port))
	os.system(f"sudo systemctl daemon-reload")
	os.system(f"sudo systemctl enable {SERVICE_NAME}")
	os.system(f"sudo systemctl start {SERVICE_NAME}")

@commander.command("run")
def run_daemon(password_hash: str, port: int):
	run(password_hash=password_hash, port=port)

if __name__ == "__main__":
	commander.process()
