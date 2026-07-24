from agent.controller import AgentController
from tools.terminal import run_command

# Color definitions
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


controller = AgentController()

while True:

    user = input(f"\n{BLUE}You >> {RESET}")

    if user.lower() in ["exit", "quit"]:
        break

    result = controller.process(user)

    if result.action == "answer":
        print(f"\n{GREEN}Chottu >> {RESET}{result.response}")

    elif result.action == "command":

        print(f"\n{RED}Chottu wants to run: {RESET}{result.command} ; {result.reason}")

        confirm = input("\nExecute? (y/n):")

        if confirm.lower() == "y":

            output = run_command(result.command)

            print(f"\n{GREEN}Chottu >> {RESET}{output['stdout']}")

            if output["stderr"]:
                print(f"\n{GREEN}Chottu Error: {RESET}{output['stderr']}")  