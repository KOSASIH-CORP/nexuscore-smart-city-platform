import sqlite3

class DeviceRegistry:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def register_device(self, device_id, device_type, device_ip):
        self.cursor.execute("INSERT INTO devices (device_id, device_type, device_ip) VALUES (?,?,?)",
                            (device_id, device_type, device_ip))
        self.conn.commit()

    def get_device(self, device_id):
        self.cursor.execute("SELECT * FROM devices WHERE device_id =?", (device_id,))
        return self.cursor.fetchone()
