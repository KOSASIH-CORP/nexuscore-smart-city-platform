import hashlib

class RoleBasedAccessControl:
    def __init__(self, roles):
        self.roles = roles
        self.access_control_list = {}

    def add_user(self, user_id, role):
        self.access_control_list[user_id] = role

    def check_access(self, user_id, resource):
        role = self.access_control_list.get(user_id)
        if role:
            if role in self.roles:
                return True
        return False

    def generate_token(self, user_id):
        token = hashlib.sha256(f"{user_id}{self.roles}".encode()).hexdigest()
        return token
