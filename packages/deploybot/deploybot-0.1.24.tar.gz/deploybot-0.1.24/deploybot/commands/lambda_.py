import argparse
from deploybot.commands.shared import deploy

def lambda_(args):
    """Deploy Lambda services.

    ACTION: Action to perform (deploy).
    SERVICE_NAME: Name of the service to deploy.
    """
    deploy('lambda', args[0], args[1])

def main(args=None):
    if args is None:
        parser = argparse.ArgumentParser(description="Lambda related commands")
        parser.add_argument('action', choices=['deploy'], help='Action to perform')
        parser.add_argument('service_name', help='Name of the service to deploy')
        args = parser.parse_args()

    lambda_([args.action, args.service_name])

if __name__ == "__main__":
    main()
