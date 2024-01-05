from services.user_flow_service import UserflowService

userflow_service = UserflowService()


def start_cafeteria():
    userflow_service.start_cafeteria_flow()


if __name__ == '__main__':
    start_cafeteria()
