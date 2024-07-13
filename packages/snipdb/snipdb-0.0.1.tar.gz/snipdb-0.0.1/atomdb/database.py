import json
import os

class SnipDB:
    def __init__(self, db_path):
        self.db_path = db_path
        if not os.path.exists(db_path):
            with open(db_path, 'w') as f:
                json.dump({}, f)

    def _read_db(self):
        with open(self.db_path, 'r') as f:
            return json.load(f)

    def _write_db(self, data):
        with open(self.db_path, 'w') as f:
            json.dump(data, f, indent=4)

    def insert(self, key, value):
        data = self._read_db()
        data[key] = value
        self._write_db(data)

    def get(self, key):
        data = self._read_db()
        return data.get(key)

    def delete(self, key):
        data = self._read_db()
        if key in data:
            del data[key]
        self._write_db(data)

