from agent.controller import AgentController
from tools.terminal import run_command
from logger_util import get_logger

# Color definitions
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

logger = get_logger(__name__)

controller = AgentController()

while True:

    user = input(f"\n{BLUE}You >> {RESET}")
    logger.info(f"\nYou >> {user}")

    if user.lower() in ["exit", "quit"]:
        break
    
    result = controller.process(user)


    if result.action == "answer":
        print(f"\n{GREEN}Chottu >> {RESET}{result.response}")
        logger.info(f"\nChottu >> {result.response}")

    elif result.action == "command":

        
        print(f"\n{RED}Chottu wants to run: {RESET}{result.command} ; {result.reason}")
        logger.info(f"\nChottu wants to run: {result.command} ; {result.reason}")

        confirm = input("\nExecute? (y/n):")
        logger.info(f"\nExecute? (y/n): {confirm}")

        if confirm.lower() == "y":

            output = run_command(result.command)

     
            print(f"\n{GREEN}Chottu >> {RESET}{output['stdout']}")
            logger.info(f"\nChottu >> {output['stdout']}")

            if output["stderr"]:
                print(f"\n{GREEN}Chottu Error: {RESET}{output['stderr']}")  
                logger.info(f"\nChottu Error: {output['stderr']}")