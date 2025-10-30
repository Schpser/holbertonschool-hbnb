from app.models.user import User
from app.persistence.data_manager import DataManager

class HBnBFacade:
    def __init__(self):
        self.data_manager = DataManager()
        self.user_repo = InMemoryRepository()
        self.PEPPER = "exemple_2_Pepper'extra789long#"

    def create_user(self, user_data):
        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            is_admin=user_data.get('is_admin', False)
        )

        user.hash_password(user_data['password'], self.PEPPER)
        self.data_manager.save(user)
        return user

    def get_user(self, user_id):
        return self.data_manager.get(user_id, 'User')

    def get_all_users(self):
        return self.data_manager.get_all('User')

    def get_user_by_email(self, email):
        users = self.data_manager.get_all('User')
        for user in users:
            if user.email == email:
                return user
        return None

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            return None

        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        if 'email' in user_data:
            user.email = user_data['email']
        if 'password' in user_data:
            user.hash_password(user_data['password'], self.PEPPER)
        
        self.data_manager.save(user)
        return user

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            self.data_manager.delete(user_id, 'User')
            return True
        return False

# Instantiate the facade
facade = HBnBFacade()