import unittest
import grpc

# Импортируйте сгенерированные классы gRPC
import example_pb2
import example_pb2_grpc

# Адрес вашего gRPC сервера
SERVER_ADDRESS = 'localhost:50051'

class TestExampleService(unittest.TestCase):

    def setUp(self):
        # Создайте канал gRPC и стаб (stub) для сервиса
        self.channel = grpc.insecure_channel(SERVER_ADDRESS)
        self.stub = example_pb2_grpc.ExampleServiceStub(self.channel)

    def tearDown(self):
        # Закройте канал gRPC (опционально)
        self.channel.close()

    def test_get_user_success(self):
        # 1. Тест успешного получения пользователя
        request = example_pb2.GetUserRequest(user_id=1)
        response = self.stub.GetUser(request)
        self.assertEqual(response.username, "testuser")
        self.assertEqual(response.email, "test@example.com")

    def test_get_user_not_found(self):
        # 2. Тест получения пользователя, которого не существует
        request = example_pb2.GetUserRequest(user_id=999)
        with self.assertRaises(grpc.RpcError) as context:
            self.stub.GetUser(request)
        self.assertEqual(context.exception.code(), grpc.StatusCode.NOT_FOUND)

    def test_create_user_success(self):
        # 3. Тест успешного создания пользователя
        request = example_pb2.CreateUserRequest(username="newuser", email="new@example.com")
        response = self.stub.CreateUser(request)
        self.assertGreater(response.user_id, 0)  # Проверьте, что user_id > 0

    def test_update_user_success(self):
        # 4. Тест успешного обновления пользователя
        request = example_pb2.UpdateUserRequest(user_id=1, new_email="updated@example.com")
        response = self.stub.UpdateUser(request)
        self.assertTrue(response.success)

    def test_update_user_not_found(self):
        # 5. Тест обновления пользователя, которого не существует
        request = example_pb2.UpdateUserRequest(user_id=999, new_email="updated@example.com")
        with self.assertRaises(grpc.RpcError) as context:
            self.stub.UpdateUser(request)
        self.assertEqual(context.exception.code(), grpc.StatusCode.NOT_FOUND)

    def test_delete_user_success(self):
        # 6. Тест успешного удаления пользователя
        request = example_pb2.DeleteUserRequest(user_id=1)
        response = self.stub.DeleteUser(request)
        self.assertTrue(response.success)

    def test_delete_user_not_found(self):
        # 7. Тест удаления пользователя, которого не существует
        request = example_pb2.DeleteUserRequest(user_id=999)
        with self.assertRaises(grpc.RpcError) as context:
            self.stub.DeleteUser(request)
        self.assertEqual(context.exception.code(), grpc.StatusCode.NOT_FOUND)

    def test_list_users_success(self):
        # 8. Тест успешного получения списка пользователей
        request = example_pb2.ListUsersRequest()
        response = self.stub.ListUsers(request)
        self.assertGreater(len(response.users), 0) # Проверьте, что список не пустой
        self.assertEqual(response.users[0].username, "testuser")

    def test_create_user_invalid_data(self):
       # 9. Тест создания пользователя с невалидными данными (например, пустой email)
        request = example_pb2.CreateUserRequest(username="invaliduser", email="")
        with self.assertRaises(grpc.RpcError) as context:
            self.stub.CreateUser(request)
        self.assertEqual(context.exception.code(), grpc.StatusCode.INVALID_ARGUMENT) # Или другая подходящая ошибка

    def test_get_user_id_zero(self):
        # 10. Тест получения пользователя с ID = 0 (граничное значение)
        request = example_pb2.GetUserRequest(user_id=0)
        with self.assertRaises(grpc.RpcError) as context:
            self.stub.GetUser(request)
        self.assertEqual(context.exception.code(), grpc.StatusCode.INVALID_ARGUMENT)

if __name__ == '__main__':
    unittest.main()