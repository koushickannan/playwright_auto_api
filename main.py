# main.py
from products.reqres.testdata.token_test_data import create_tenant_admin_token


def main():
    token_request = create_tenant_admin_token()
    print(token_request.json())


if __name__ == "__main__":
    main()
